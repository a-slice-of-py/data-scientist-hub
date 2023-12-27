---
date: 2021-12-21
authors:
  - silvio
categories:
  - Guides
---

# AWS Chalice

[AWS Chalice](https://github.com/aws/chalice) is a microframework for writing serverless apps in Python.

<!-- more -->

## Comparison with SAM

The following table provides a mapping between AWS SAM and AWS Chalice commands:

<table>
<thead>
<tr class="header">
<th><p>Chalice</p></th>
<th><p>Main options</p></th>
<th><p>Notes</p></th>
<th><p>SAM equivalent</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code>chalice new-project </code><project_name></p></td>
<td></td>
<td><p>initialize an "hello world" sample project at the <i>dev</i> stage</p></td>
<td><p><code>sam init --name </code><project_name></p></td>
</tr>
<tr class="even">
<td><p><code>chalice deploy</code></p></td>
<td><p><code>--no-autogen-policy</code> to avoid auto policy generation, requires a source policy file <code>.chalice/policy-</code><stage_name><code>.json</code><br />
<code>--stage </code><stage_name> to set a different deployment stage (<i>dev</i> by default)</p></td>
<td><p>Chalice automatically builds apps, storing the build results in <code>.chalice/deployments/</code></p></td>
<td><p><code>sam build &amp;&amp; sam deploy</code></p></td>
</tr>
<tr class="odd">
<td><p><code>chalice local</code></p></td>
<td><p><code>--port=XXXX</code> to redirect local hosting on a specific port</p></td>
<td><p>locally run the app (by default on port 8000)</p></td>
<td><p>partially covered by <code>sam local invoke</code></p></td>
</tr>
<tr class="even">
<td><p><code>chalice invoke --name </code><lambda_name></p></td>
<td></td>
<td><p>invoke a Lambda function</p></td>
<td><p>partially covered by <code>sam local invoke</code></p></td>
</tr>
<tr class="odd">
<td><p><code>chalice gen-policy</code></p></td>
<td></td>
<td><p>redirect to stdout the auto-generated AWS policy for the defined app (useful as a starting template for <code>.chalice/policy-</code><stage_name><code>.json</code>)</p></td>
<td></td>
</tr>
<tr class="even">
<td><p><code>chalice delete</code></p></td>
<td></td>
<td><p>delete the deployed app</p></td>
<td></td>
</tr>
</tbody>
</table>

The following sample is the Chalice implementation equivalent of SAM project discussed [here](sam.md#w-custom-local-module).

``` python
chalice-app/
│
├── .chalice/
│   ├── deployed/
│   │   └── <stage_name>.json
│   ├── deployments/
│   ├── policy-<stage_name>.json
│   └── config.json
│
├── chalicelib/
│   ├── __init__.py
│   └── custom_script.py
│
├── app.py
│
└── requirements.txt
```

where `app.py` contains (possibly) all the Lambda handlers, each one decorated with `@app.lambda_function(name='my_lambda_name')`, needed to let Chalice treat them as [pure Lambda functions](https://chalice.readthedocs.io/en/latest/topics/purelambda.html).
