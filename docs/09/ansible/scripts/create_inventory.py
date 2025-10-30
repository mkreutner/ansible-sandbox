import click
import os
import yaml


def scan(ip: str, begin_with: str | None):
    response = os.popen("arp -a | awk '{print $1, $2}' | awk -F'[() ]' '{print $1, $3}' | grep '^[^?\ ]'").read()
    print(response)


@click.command()
@click.option('--target', default='192.168.1.0/24', help='Target IP or range')
@click.option('--inventory', default='inventory.yaml', help='Inventory name output file')
@click.option('--begin_with', default=None, help='Name of hosts begining with pattern')
def create_inventory(target, inventory, begin_with):
    msg: str = f": Create inventory {inventory} with all hosts whose name begin with {begin_with} :"
    line: str = "+" + "-" * (len(msg) - 2) + "+"
    click.echo(line)
    click.echo(msg)
    click.echo(line)
    if begin_with != None:
        click.echo(f"> Filtered by begining of hosts name: {begin_with}")
    else:
        click.echo(f"> Not Filtered")

    scan(target, begin_with)

if __name__ == '__main__':
    create_inventory()
