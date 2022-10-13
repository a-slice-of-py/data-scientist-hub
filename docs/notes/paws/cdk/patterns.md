---
tags:
  - ITA
---

# Custom L3 Constructs (Patterns)

## Esigenza

Nell'utilizzo avanzato di [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html), si realizza prima o poi l'esigenza di centralizzare alcune logiche e risorse in maniera da poterle riutilizzare in maniera rapida, riducendo il codice boilerplate.
Anche se una prima analisi potrebbe suggerire che la soluzione sia l'implementazione di una "casalinga" [factory](https://en.wikipedia.org/wiki/Factory_method_pattern) - pythonica sì, ma non conforme alle best practices di CDK - la risposta probabilmente più corretta potrebbe riguardare l'implementazione di un costrutto L3, [descritto come](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html#constructs_lib):

> designed to help you complete common tasks in AWS, often involving multiple kinds of resources.

## Implementazione

Per cercare di aderire il più possibile alla _CDK-way_ nella gestione dei costrutti, è utile ispirarsi al sorgente di patterns built-in, come ad esempio [LambdaRestApi](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_apigateway/LambdaRestApi.html). Prendere ispirazione non sempre è un'attività lineare, visto che a forza di scavare under the hood prima o poi ci si scontra con la traduzione operata da [jsii](https://github.com/aws/jsii), ma le best practices che è possibile estrapolare si possono ridurre a:

1. il costrutto L3 che si vuole implementare deve estendere la classe `Construct`, es. `class MyConstruct(Construct)`
2. la configurazione del costrutto avviene tramite `kwargs`, passati esplicitamente nell'`__init__` della classe
3. le logiche di gestione e validazione della configurazione di un costrutto vanno separate dalla classe che implementa il costrutto stesso, in una  classe ad hoc che ne eredita il nome con il suffix _Props_, es. `class MyConstructProps`
4. la classe che gestisce la configurazione si occupa di validare gli input ricevuti e settarli come [managed attributes](https://realpython.com/python-property/) via `@property`
5. dopo aver wrappato le configurazioni nella classe deputata, esse vengono bindate alla classe che definisce il costrutto, che viene anche "triggerata" (a deploy-time) tramite un metodo `create`

Nel seguito un paio di utils comode per validare i parametri di configurazione e bindarli ad un costrutto.

=== "Validate"

    ```python
    from typing import Any, Tuple


    def _check_type(property: str,
                    value: object,
                    expected_types: Tuple[Any],
                    skip_if_missing: bool = True
                    ) -> None:
        if skip_if_missing and value is None:
            return
        else:
            if hasattr(expected_types[0], '__jsii_type__'):
                _expected_types = list(
                    map(lambda x: getattr(x, '__jsii_type__'), expected_types))
                if (not hasattr(value, '__jsii_type__')) or (getattr(value, '__jsii_type__') not in _expected_types):
                    _type = getattr(value, '__jsii_type__') if hasattr(
                        value, '__jsii_type__') else type(value)
                    raise TypeError(
                        f"Property '{property}' must be in {_expected_types}, received a {_type}.")
            else:
                if not isinstance(value, expected_types):
                    raise TypeError(
                        f"Property '{property}' must be in {expected_types}, received a {type(value)}.")
    ```

=== "Register"

    ```python
    def _register(props: object, obj: object) -> None:
        for attr in props._values:
            setattr(obj, attr, getattr(props, attr))
    ```

!!! warning

    Una scelta apparentemente naturale per organizzare i costrutti nella codebase potrebbe essere di inserirli in un folder `/constructs`, come nella seguente alberatura:

    ```
    /infra
        /constructs
            __init__.py
            my_construct.py
        /stacks
            __init__.py
            my_stack.py
        app.py
        cdk.json
    /src
        ...
    ```

    Con una configurazione come quella sopra, purtroppo, a deploy-time ci si scontra con l'errore `ModuleNotFoundError: No module named 'constructs._jsii'`. A fare chiarezza ci pensa [questa issue](https://github.com/aws/aws-cdk/issues/19301#issuecomment-1064644589): essenzialmente, nel folder in cui si esegue `cdk deploy` non può esserci un folder con nome "constructs".

## Utilizzo

Una volta creato il costrutto, si può utilizzare esattamente come gli altri costrutti L1, L2 e L3 nativi, ovvero istanziandolo in uno stack fornendogli quindi uno scope (il `self` dello stack stesso), un id e gli eventuali parametri di configurazione.

## Takeaway

L'esperienza di refactoring di parti di codice CDK utilizzate spesso in costrutti L3 è decisamente consigliabile: è senz'altro time-consuming (per lo meno la prima volta) e rischia di sembrare fine a se stessa, ma oltre che educativa consegna al termine un codice di più facile manutenzione e, soprattutto, riutilizzabile![^1].

Trasformare in costrutti gli snippets che vengono continuamente riciclati da un progetto all'altro permette di standardizzare le best practices del proprio lavoro, ed effettuare il design di una applicazione CDK per costrutti anzichè per stack permette inoltre di aderire ad un'altra best practice di CDK, ovvero:

> composition is preferred over inheritance when developing AWS CDK constructs.[^2]

[^1]: Essenzialmente perchè "sganciato" da logiche puntuali di un dato stack.
[^2]: Come indicato [qui](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html#constructs_composition) e [qui](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html#constructs_author).
