#!/usr/bin/env python3

import os

from {{ cookiecutter.module_name }}.debug import start_debugger

ENV: str | None = os.environ.get("ENV")

if ENV == "dev":
    start_debugger()
