import click
import subprocess
import os
import json
import shutil

taint_content = {
    {
  "sources": [
    {
      "name": "CustomUserControlled",
      "comment": "use to annotate user input"
    }
  ],

  "sinks": [
    {
      "name": "CodeExecution",
      "comment": "use to annotate execution of python code"
    }
  ],

  "features": [],

  "rules": [
    {
      "name": "Possible RCE:",
      "code": 5001,
      "sources": [ "CustomUserControlled" ],
      "sinks": [ "CodeExecution" ],
      "message_format": "User specified data may reach a code execution sink"
    }
  ]
}
}

model_content = """
django.http.request.HttpRequest.GET: TaintSource[CustomUserControlled] = ...
def eval(__source: TaintSink[CodeExecution], __globals, __locals): ...
"""

stubs_content = """
from django.http import HttpRequest, HttpResponse
def operate_on_twos(request: HttpRequest) -> HttpResponse: ...
"""

@click.group()
def PysaCoolCli():
    pass

@PysaCoolCli.command()
@click.option("--config-path", default=".", show_default=True, type=click.Path())
def init(config_path):
    """
    Initializes the project folder with .pysa and taint.config files
    """
    click.echo("Initializing...")
    os.system("pyre init")
    pyre_config = None
    with open('.pyre_configuration', 'r') as fp:
        pyre_config = json.load(fp)
        pyre_config["search_path"] = os.path.join(config_path, "stubs")
        pyre_config["taint_models_path"] = config_path
    if os.path.isfile('.pyre_configuration'):
        os.remove('.pyre_configuration')
    with open('.pyre_configuration', "w") as fp:
        fp.write(json.dumps(pyre_config))
    if not os.path.isdir(config_path):
        os.mkdir(config_path)
    stubs_path = os.path.join(config_path, "stubs")
    if os.path.isdir(stubs_path):
        shutil.rmtree(stubs_path)
    os.mkdir(stubs_path)
    os.mkdir(os.path.join(stubs_path, "PysaCoolCli"))
    click.echo("Created stubs directory...")
    model_path = os.path.join(config_path, "models.pysa")
    with open(model_path, 'w') as fp:
        fp.write(model_content)
    click.echo("Created models.pysa file...")
    taint_config_path = os.path.join(config_path, 'taint.config')
    with open(taint_config_path, 'w') as fp:
        content = json.dumps(taint_content, indent=2)
        fp.write(content)
    click.echo("Create taint.config file...")
    click.echo(f"Configuration files generated at '{config_path}'")

@PysaCoolCli.command()
def analyze():
    os.system("pyre analyze")