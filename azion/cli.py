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
def domain_group():
    pass

@domain_group.command("domain-list")
@click.option('--id', type=int)
def domain_list(id):
    if id is not None:
        domain = client.get_domain(id)
        print(domain)
    else:
        for domain in client.domains():
            print(domain)


@click.group()
def edge_function_group():
    pass

@edge_function_group.command("edge-function-list")
@click.option('--id', type=int)
def edge_function_list(id):
    if id is not None:
        edge_function = client.get_edge_function(id)
        print(edge_function)
    else:
        for edge_function in client.edge_functions():
            print(edge_function)


@edge_function_group.command("edge-function-info")
@click.option('--id', type=int, required=True)
def edge_function_info(id):
    edge_function = client.get_edge_function(id)
    pprint(vars(edge_function))


cli = click.CommandCollection(sources=[domain_group, edge_function_group])

if __name__ == '__main__':
    cli()

