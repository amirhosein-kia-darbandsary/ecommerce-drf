#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from drfEcommerce.settings.base import DEBUG

def main():
    "Set the env_path"
    if DEBUG:
        env_path = "local"
    else:
        env_path = "production"
        
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'drfEcommerce.settings.{env_path}')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
