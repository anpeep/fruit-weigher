#!/usr/bin/env python
<<<<<<< HEAD
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fruitweigher.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        try:
            import django
        except ImportError:
            raise
        raise ImportError(
            "Could not import Django. Are you sure it is installed and "
=======
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fruitweigher.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
>>>>>>> 09d8a70f6f1503353eae641fd0e18058403d135c
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
<<<<<<< HEAD
=======


if __name__ == '__main__':
    main()
>>>>>>> 09d8a70f6f1503353eae641fd0e18058403d135c
