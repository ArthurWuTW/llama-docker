#!/usr/bin/env bash
git clone https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip3.12 install -r requirement.txt
pip3.12 install -e ".[torch,metrics]"

