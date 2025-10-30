import click

@click.command()
@click.option('--name', default='World', help='Nom de la personne à saluer')
def hello(name):
    click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    hello()
