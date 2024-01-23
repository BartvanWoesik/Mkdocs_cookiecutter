# Mkdocs Template

This template can be used to create a new project or implement mkdocs documentation in existing projects.

The template can be used by running the following command

```shell
$ cookiecutter https://github.com/BartvanWoesik/Mkdocs_cookiecutter.git
```

The following information will be asked:
    - is_existing_project: specifiy if the project already exists or not.
    - project_name: Name of the project.

If the project already exists only the documentation related files will be created based on the given project name. Otherwise a whole basic project structure will be created including the setup fo;r the mkdocs.