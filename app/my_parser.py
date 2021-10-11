import requests
import xml.etree.ElementTree as ET
import geocoder


url = 'http://isc.sans.edu/api/intelfeed/'

headers = {
    'User-Agent': 'srkraynick@gmail.com'
}


def get_response(header):
    response = requests.get(url, header)
    tree = ET.fromstring(response.content)

    #intelfeed
    for x in tree.findall('ip'):
        item = x.find('ip').text
        price = x.find('description').text
        g = geocoder.ip(item)
        print(g.location)
       # print(g.response)
       # print(g.current_result)
        #print(item, price)
