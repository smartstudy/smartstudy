#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if not os.path.isfile(os.path.join("smartstudy", "settings", "local.py")):
        print "[Error] No such file : 'smartstudy/settings.local.py"
        sys.exit()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smartstudy.settings.local")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
