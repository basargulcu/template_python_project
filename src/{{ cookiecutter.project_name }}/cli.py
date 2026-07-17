import click
import {{ cookiecutter.project_name }}.main as project_main

@click.group()
def cli():
    pass

@cli.command(name="test")
def _test():
    """dummy cli command."""
    project_main.main()
    

def main():
    cli()
