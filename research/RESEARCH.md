# RESEARCH

This project is composed for a Deep Learning Model with Recurrent Neural Networks, with the objective of make easy the development of this part,
this directory contains this elements:

- **NOTEBOOKS**: For reply and create the model.[Go to Notebooks](https://github.com/BBVA/waf-brain/blob/master/research/notebooks/NOTEBOOKS.md)

- **GENERATED MODELS**: You can use differents models previosly generated.[Go to Models](https://github.com/BBVA/waf-brain/blob/master/research/models/MODELS.md)

## You can contribute with this project
You can create new models and upload to our models directory, also you can test with [waf-benchmark](https://github.com/BBVA/waf-benchmark).

![alt](http://kirklandweblog.typepad.com/.a/6a00d83451975769e201b8d290befa970c-800wi)

## Thanks to the rooted mail list.
That helped us attacking our honeypots.  [**Here**](https://github.com/BBVA/waf-brain/blob/master/research/rooted/wafbrain_output.txt) are the promised results:
- The first parameter is the percentage of sql injection attack.
- The second parameter is the time to process this payload.
- The third parameter is the payload.
- The last parameter is the weight inside the network, the first element is the loss weight and the second is a binary element, if the network match this element.
    This is important for explicability, because you can detect patterns of attacks.


## FINAL RESULTS

### MODSECURITY

These are our results with waf-benchmark and [this model](https://github.com/BBVA/waf-brain/blob/master/waf_brain/models/model_feat-5_botneck-101_v2.h5)

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

Waf-brain is based on **Deep Learning**.

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

