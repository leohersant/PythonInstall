#!/bin/bash

#CREATE VIRTUAL ENVIRONMENT
virtualenv -p python3 env/ 
#ACTIVATE THE ENVIRONMENT
source env/bin/activate
#INSTALL FLASK INSIDE THE ENVIRONMENT
pip install flask
