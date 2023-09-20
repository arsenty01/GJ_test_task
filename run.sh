#!/bin/sh
pip install -r /usr/src/myapp/requirements.txt
export PYTHONPATH=/usr/src/myapp/
pytest /usr/src/myapp/tests