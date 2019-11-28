WAF-Brain - the clever and efficient Firewall for the Web
=========================================================

.. image:: https://raw.githubusercontent.com/BBVA/waf-brain/master/docs/waf-brain-logo-250px.png
   :scale: 50%
   :align: center

.. image:: https://img.shields.io/pypi/v/waf-brain
   :target: https://pypi.org/project/waf-brain/
.. image:: https://img.shields.io/github/issues/BBVA/waf-brain
   :target: https://github.com/BBVA/waf-brain/issues
.. image:: https://img.shields.io/pypi/pyversions/waf-brain
.. image:: https://img.shields.io/pypi/l/waf-brain
   :target: https://github.com/BBVA/waf-brain/blob/master/LICENSE


What's WAF-Brain
================

This project was born to try to create a WAF (Web Application Firewall) with the **Machine-Learning-Deep Learning Way**.

**Currently** the project only includes models for **SQL Injection Attacks**, but you can use your custom machine-learning model.

Install
=======

.. code-block:: console

    $ pip install waf-brain

Usage
=====

1. Launch the waf server and the application server
---------------------------------------------------

`This is a example repo for launch modsecurity server with express server <https://github.com/theonemule/docker-waf>`

2. Launch waf-benchmark over the waf server address
---------------------------------------------------

You have multiples kind of benchmarking

- For launch a server in **test mode** with our model on **localhost**, and collect partial results, launch this command

.. code-block:: console

    $ waf_brain -T --dump-file logs.txt -l 0.0.0.0

- Use **custom model**

.. code-block:: console

    $ waf_brain -T --dump-file logs.txt -l 0.0.0.0 -M custom_model.h5

.. note::

    Default port of server is **8000**

About the the research
======================

You can find the complete document about the research process at `RESEARCH.md <https://github.com/BBVA/waf-brain/blob/master/research/RESEARCH.md>`_

Other Options
=============

CLI is self-explained, you can use **-h** command to display all the options:

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