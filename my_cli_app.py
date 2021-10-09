import click


@click.command()
@click.option(
    '--name', '-n',
    help='your API key for the OpenWeatherMap API',
)
def hello(name):
    click.echo(f'Hello {name}')

