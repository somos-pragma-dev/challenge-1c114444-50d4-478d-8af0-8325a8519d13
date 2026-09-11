#!/usr/bin/env python
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

try:
    from django.core.management import execute_from_command_line
except ImportError as e:
    raise ImportError(
        'No Django installation found. Please ensure Django is installed and available on your PYTHONPATH environment variable. Did you forget to activate a virtual environment?'
    ) from e

execute_from_command_line(sys.argv)