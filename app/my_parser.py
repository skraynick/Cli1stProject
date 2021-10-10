import requests





url = 'http://isc.sans.edu/api/ip/70.91.145.10/'

headers = {
    'User-Agent': 'srkraynick@gmail.com'
}


def get_response(header):
    response = requests.get(url, header)
    print(response.text)
