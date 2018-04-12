FROM tensorflow/tensorflow:nightly-py3

RUN pip install -U pip

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

