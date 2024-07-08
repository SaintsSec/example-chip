#!/bin/python3
import subprocess
from typing import List


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