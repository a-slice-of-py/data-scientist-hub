---
date: 2023-11-30
authors:
  - silvio
categories:
  - TIL
tags:
  - ITA
  - SQL
---

# Presto/Trino, unix timestamp, window functions e daylight saving time

Se si usano window functions (es. `LAG`) per calcolare delta tra timestamp Unix, il risultato "ignora" eventuali switch di ora legale/solare (correttamente, dato che un timestamp Unix conta esclusivamente il tempo che scorre).

<!-- more -->

Non è stato immediato trovare una soluzione che tenesse conto dello switch e che, quindi, aggiungesse/sottraesse l'ora di delta, e anche `DATE_DIFF` non ha aiutato.

Una soluzione manuale è però possibile tramite la utils [`TIMEZONE_HOUR`](https://prestodb.io/docs/current/functions/datetime.html#convenience-extraction-functions), che restituisce il delta rispetto a UTC, quindi 1 o 2 ore a seconda del periodo dell'anno.

!!! example
    ```sql
    SELECT 
      TIMEZONE_HOUR(unix_timestamp) - LAG(TIMEZONE_HOUR(unix_timestamp), 1, 0) OVER (
        PARTITION BY partition_key
        ORDER BY unix_timestamp
      )
    FROM my_table
    ```
