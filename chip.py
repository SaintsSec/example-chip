#!/bin/python3
import subprocess
from typing import List
from navi_shell import tr, get_ai_name, llm_chat, get_user
from navi import get_ip_address, get_hostname, get_parameters, get_command_path


command = "Example_Chip"
use = "A simple chip for testing."
aliases = ['--exchip']

navi = None

def append_text(self, text="Hello world!"):
    self.text_edit.append(text)

def set_navi_instance(self,navi_instance):
    global navi
    navi = navi_instance

def run(arguments=None):
    set_navi_instance()
    append_text()