WAF-Brain - the clever and efficient Firewall for the Web
=========================================================

.. image:: https://img.shields.io/pypi/v/waf-brain
   :target: https://pypi.org/project/waf-brain/

.. image:: https://img.shields.io/github/issues/BBVA/waf-brain
   :target: https://github.com/BBVA/waf-brain/issues

.. image:: https://img.shields.io/pypi/l/waf-brain
   :target: https://github.com/BBVA/waf-brain/blob/master/LICENSE

.. image:: https://img.shields.io/pypi/pyversions/waf-brain
   :target: https://www.python.org/downloads/release/python-360/

.. image:: https://raw.githubusercontent.com/BBVA/waf-brain/master/docs/waf-brain-logo-250px.png
   :scale: 50%
   :align: center


What's WAF-Brain
================

This project was born to try to create a WAF (Web Application Firewall) with the **Machine-Learning-Deep Learning Way**.

WAF-Brain detect attacks by using Deep Learning Networks. It checks each parameter of each HTTP Request by the network. The Neural Network resolved if a specific parameter content is dangerous or not. If it consider that parameter is dangerous, then WAF-Brain will block the request.

.. note::

    **Currently** the project only includes models for **SQL Injection Attacks**, but you can use your custom machine-learning model.

About the the research
======================

You can find the complete document about the research process at `RESEARCH.md <https://github.com/BBVA/waf-brain/blob/master/research/RESEARCH.md>`_

Install
=======

.. code-block:: console

    $ pip install waf-brain

Usage
=====

Demo App
--------

We have developed a demo App, that you can find at `demo app <https://github.com/BBVA/waf-brain/tree/master/demo_app>`_.

In summary, it exposes an **end-point** at **/{tail}** that accept a random parameter in **tail**.

For launching the App.

.. code-block:: console

    $ pip install aiohttp
    $ python app.py
    ======== Running on http://127.0.0.1:5000 ========
    (Press CTRL+C to quit)

Consume the App with curl is so easy:

.. code-block:: console

    $ curl -v /my-tail
    OK

**We we'll use this app to check the WAF**

Launching WAF
-------------

The application that we want to protect listen at **127.0.0.1:5000**. Then:

**With the default model**

.. code-block:: console

    $ waf_brain -A 127.0.0.1:5000 -l 0.0.0.0
    ======== Running on http://127.0.0.1:8000 ========
    (Press CTRL+C to quit)

**custom model**

.. code-block:: console

    $ waf_brain -l 0.0.0.0 -A 127.0.0.1:5000 -M custom_model.h5
    ======== Running on http://127.0.0.1:8000 ========
    (Press CTRL+C to quit)

**Testing mode**

For launch a server in **test mode** with our model on **localhost**, and collect partial results, launch this command

.. code-block:: console

    $ waf_brain -T --dump-file logs.txt -l 0.0.0.0 -A 127.0.0.1:5000
    ======== Running on http://127.0.0.1:8000 ========
    (Press CTRL+C to quit)

Benchmarking
------------

You have multiples kind of benchmarking, by a hacking tool (like *sqlmap*) or using our `WAF-Benchmark <https://github.com/BBVA/waf-benchmark>`_.

In summary, in our test, we found that with WAF-Brain you can detect more attacks, in long payloads, than ModSecurity.

Other Options
=============

CLI is self-explained you can use **-h** command to display all the options:

.. code-block:: console

    $ waf-brain -h
    usage: waf-brain [-h] [-v] [--backend-timeout BACKEND_TIMEOUT]
                     [-A PROTECTED_URL] [-l LISTEN] [-p PORT] [-b BACKLOG]
                     [--blocking-mode] [--blocking-threshold BLOCKING_THRESHOLD]
                     [-M MODEL] [-T] [--dump-file DUMP_FILE] [-a]

    WAF-brain: the clever and efficient Firewall for the Web

    optional arguments:
      -h, --help            show this help message and exit
      -v                    log level

    Server Options:
      --backend-timeout BACKEND_TIMEOUT
                            timeout to connect to the backend
      -A PROTECTED_URL, --protected-url PROTECTED_URL
                            address service to protect with the WAF
      -l LISTEN, --listen LISTEN
                            listen address. Default: 127.0.0.1
      -p PORT, --port PORT  listen port for service. Default: 8000
      -b BACKLOG, --backlog BACKLOG
                            maximum concurrent connections

    WAF Behavior:
      --blocking-mode       enables active blocking of dangerous request
      --blocking-threshold BLOCKING_THRESHOLD
                            if the dangerous levels is upper this number, and
                            blocking mode is enabled, WAF will block a request
      -M MODEL, --model MODEL
                            model used for WAF

    Enable testing mode:
      -T, --enable-testing  enable testing mode
      --dump-file DUMP_FILE
                            dump file to track each request
      -a, --access-log      enable access log for each request


Authors
=======

*Waf-Brain* is being developed by `BBVA-Labs Security team members <https://bbvalabs.gitbook.io/oss/bbva_labs_security>`_

*Waf-Brain* is Open Source Software and available under the `Apache 2
license <https://raw.githubusercontent.com/BBVA/kapow/master/LICENSE>`_

Contributions
-------------

Contributions are of course welcome.  See
`CONTRIBUTING <https://raw.githubusercontent.com/BBVA/kapow/blob/master/CONTRIBUTING.rst>`_
or skim existing tickets to see where you could help out.


Acknowledgments
===============

Logo image was `Designed by Freepik <http://www.freepik.com>`_