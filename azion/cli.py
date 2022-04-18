import azion.api
import click
import os
import sys
from pprint import pprint

AZION_USERNAME = os.getenv('AZION_USERNAME')
AZION_PASSWORD = os.getenv('AZION_PASSWORD')
AZION_API_TOKEN = os.getenv('AZION_API_TOKEN')

if AZION_API_TOKEN:
    client = azion.api.Client(token=AZION_API_TOKEN)
elif AZION_USERNAME and AZION_PASSWORD:
    client = azion.api.Client(
        username=AZION_USERNAME,
        password=AZION_PASSWORD
    )
else:
    sys.tracebacklimit = 0
    raise ValueError("AZION_API_TOKEN or (AZION_USERNAME and AZION_PASSWORD) must be provided")

@click.group()
def edge_application_group():
    pass

@click.option('--debug', is_flag=True, help="Debug the api requests.")
@edge_application_group.command("edge-application-list")
def edge_application_list(debug):
    client.debugIfEnabled(debug)
    for edge_application in client.edge_applications():
        print(edge_application)

@click.option('--debug', is_flag=True, help="Debug the api requests.")
@edge_application_group.command("edge-application-info")
@click.option('--id', type=int, required=True)
def edge_application_info(debug, id):
    client.debugIfEnabled(debug)
    edge_application = client.get_edge_application(id)
    pprint(vars(edge_application))

##############################################################################

@click.group()
def origin_group():
    pass

@click.option('--debug', is_flag=True, help="Debug the api requests.")
@click.option('--edge-application-id', type=int, required=True)
@origin_group.command("origin-list")
def origin_list(debug, edge_application_id):
    client.debugIfEnabled(debug)
    for origin in client.get_edge_application_origins(edge_application_id):
        print(origin)

@click.option('--debug', is_flag=True, help="Debug the api requests.")
@origin_group.command("origin-info")
@click.option('--edge-application-id', type=int, required=True)
@click.option('--origin-key', required=True)
def origin_info(debug, edge_application_id, origin_key):
    client.debugIfEnabled(debug)
    origin = client.get_edge_application_origin(edge_application_id, origin_key)
    pprint(vars(origin))

##############################################################################

@click.group()
def domain_group():
    pass

@click.option('--debug', is_flag=True, help="Debug the api requests.")
@domain_group.command("domain-list")
def domain_list(debug):
    client.debugIfEnabled(debug)
    for domain in client.domains():
        print(domain)

@click.option('--debug', is_flag=True, help="Debug the api requests.")
@domain_group.command("domain-info")
@click.option('--id', type=int, required=True)
def domain_info(debug, id):
    client.debugIfEnabled(debug)
    domain = client.get_domain(id)
    pprint(vars(domain))

##############################################################################

@click.group()
def edge_function_group():
    pass

@click.option('--debug', is_flag=True, help="Debug the api requests.")
@edge_function_group.command("edge-function-list")
def edge_function_list(debug):
    client.debugIfEnabled(debug)
    for edge_function in client.edge_functions():
        print(edge_function)


@click.option('--debug', is_flag=True, help="Debug the api requests.")
@edge_function_group.command("edge-function-info")
@click.option('--id', type=int, required=True)
def edge_function_info(debug, id):
    client.debugIfEnabled(debug)
    edge_function = client.get_edge_function(id)
    pprint(vars(edge_function))

##############################################################################

command_sources = [
    domain_group,
    edge_function_group,
    edge_application_group,
    origin_group
]

cli = click.CommandCollection(sources=command_sources)

if __name__ == '__main__':
    cli()

