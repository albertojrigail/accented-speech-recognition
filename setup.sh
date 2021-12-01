#!/bin/bash
# Install Dependencies.
pip3 install matplotlib
pip3 install --upgrade google-cloud-speech
pip3 install jiwer
pip3 install boto3
pip3 install --upgrade deepspeech
pip3 install pydub

# Set up development environment (required for Mozilla Deep Speech).
virtualenv -p python3 $HOME/tmp/deepspeech-venv/
source $HOME/tmp/deepspeech-venv/bin/activate