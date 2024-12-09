#!/bin/bash

set -e

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


python3 plot_ampl_dist_fft.py $1