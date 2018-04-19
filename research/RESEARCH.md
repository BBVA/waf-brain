# RESEARCH

This project is composed for a Deep Learning Model with Recurrent Neural Networks, with the objective of make easy the development of this part,
this directory contains this elements:

- **NOTEBOOKS**: For reply and create the model.[Go to Notebooks](Link to Notebooks)

- **GENERATED MODELS**: You can use differents models previosly generated.[Go to Models](Link to Generated Models)

## You can contribute with this project
You can create new models and upload to our models directory, also you can test with [waf-benchmark](http://).

![alt](http://kirklandweblog.typepad.com/.a/6a00d83451975769e201b8d290befa970c-800wi)

These are our results with waf-benchmark and [this model]()

### MODSECURITY

Modsecurity is based on **regular expressions**.

| Tool name                 | Attacks blocked | Success attacks |
|---------------------------|-----------------|-----------------|
| sqlmap                    | 20586           | 1876            |
| OWASP ZAP                 | 47952           | 9700            |

| Payloads                  | False Positives | Passed          |
|---------------------------|-----------------|-----------------|
| Darkweb 2017 Top 10000    | 0               | 20000           |
| Family Names USA Top 1000 | 0               | 2000            |
| Female Names USA Top 1000 | 0               | 2000            |
| Male Names USATop 1000    | 0               | 2000            |
| Names                     | 0               | 20326           |


### WAF BRAIN

| Tool name                 | Attacks blocked | Success attacks |
|---------------------------|-----------------|-----------------|
| sqlmap                    | 21626           | 832             |
| OWASP ZAP                 | 49048           | 8206            |

| Payloads                  | False Positives | Passed          |
|---------------------------|-----------------|-----------------|
| Darkweb 2017 Top 10000    | 36              | 19872           |
| Family Names USA Top 1000 | 0               | 2000            |
| Female Names USA Top 1000 | 0               | 2000            |
| Male Names USATop 1000    | 0               | 2000            |
| Names                     | 4               | 20322           |

