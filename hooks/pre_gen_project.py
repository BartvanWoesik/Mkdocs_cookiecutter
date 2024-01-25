
import re
import sys


def description():
    '''Print description for cookiecutter.'''

    print("""
    Creating Mkdocs template in current project with name {{ cookiecutter.project_slug}}.
    """)

def check_project_slug():
    """ 
    Check if the project name is a valid name for python packages.
    """

    MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

    module_name = '{{ cookiecutter.project_slug}}'

    if not re.match(MODULE_REGEX, module_name):
        print('ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead' % module_name)

        #Exit to cancel project
        sys.exit(1)

check_project_slug()
description()