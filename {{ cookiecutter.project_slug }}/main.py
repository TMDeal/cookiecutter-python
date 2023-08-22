#!/usr/bin/env python3

import os
import random

from {{ cookiecutter.module_name }}.debug import start_debugger

ENV: str | None = os.environ.get("ENV")

if ENV == "dev":
    start_debugger()

num: int = 0
rando: int = random.randint(0, 10)
rando2: int = random.randint(0, 10)

num += rando
num += rando2

print("What is the number?")
print(num)
