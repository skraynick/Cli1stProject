import click

from app import requestcallvalues, my_parser


@click.group()
def main():
    pass


@main.command()
@click.option(
    '--name', '-n',
    help='Your name or a friend\'s name',
)
def hello(name):
    click.echo(f'Hello {name}')


@main.command()
@click.option(
    '--file', '-f',
    help='File to parse.',
)
def parse(file):
    click.echo(f'File name: {file}')


@main.command()
@click.option(
    '--thing', '-t',
    help='Headers, like user agent from dshield.. ex, \'User-Agent\': \'example@gmail.com\'',
)
def headers(thing):

    requestcallvalues.requestCallValues.headers = thing
    print(requestcallvalues.requestCallValues.headers)
    my_parser.get_response(requestcallvalues.requestCallValues.headers)


@main.command()
@click.option(
    '--ip', '-i',
    help='IP you would like to know location.',
)
def geolocate(ip):
    click.echo(f'Location: {ip}')
    print(my_parser.find_location(ip))
