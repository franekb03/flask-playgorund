import os
import subprocess

import click

from app import app


@app.cli.group()
def translate():
    """Translation and localization commands."""
    pass


@translate.command()
@click.argument('lang')
def init(lang):
    """Initialize a new language."""
    _run(['pybabel', 'extract', '-F', 'babel.cfg', '-k', '_l',
          '-o', 'messages.pot', '.'], 'extract command failed')
    _run(['pybabel', 'init', '-i', 'messages.pot',
          '-d', 'app/translations', '-l', lang], 'init command failed')
    os.remove('messages.pot')


@translate.command()
def update():
    """Update all languages."""
    _run(['pybabel', 'extract', '-F', 'babel.cfg', '-k', '_l',
          '-o', 'messages.pot', '.'], 'extract command failed')
    _run(['pybabel', 'update', '-i', 'messages.pot',
          '-d', 'app/translations'], 'update command failed')
    os.remove('messages.pot')


@translate.command()
def compile():
    """Compile all languages."""
    _run(['pybabel', 'compile', '-d', 'app/translations'],
         'compile command failed')


def _run(args, message):
    if subprocess.call(args):
        raise RuntimeError(message)