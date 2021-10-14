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
    my_parser.get_response(requestcallvalues.requestCallValues.headers)


@main.command()
@click.option(
    '--ip', '-i',
    help='IP you would like to know location.',
)
def geolocate(ip):
    click.echo(f'Location: {ip}')
    print(my_parser.find_location(ip))


@main.command()
@click.option(
    '--header', '-h',
    help='Headers, like user agent from dshield.. ex, \'User-Agent\': \'example@gmail.com\'',
)
@click.option(
    '--ip', '-i',
    help='IP target',
)
def ipi(header, ip):
    requestcallvalues.requestCallValues.headers = header
    my_parser.find_ip_information(ip, requestcallvalues.requestCallValues.headers)


@main.command()
@click.option(
    '--header', '-h',
    help='Header...user agent from dshield.. ex, \'User-Agent\': \'example@gmail.com\''
)
def topips(header):
    requestcallvalues.requestCallValues.headers = header
    my_parser.top_ips(header)
