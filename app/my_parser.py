import requests
import xml.dom.minidom
import xml.etree.ElementTree as ET
import feedparser


url = 'http://isc.sans.edu/api/intelfeed/'

headers = {
    'User-Agent': 'srkraynick@gmail.com'
}


def get_response(header):
    response = requests.get(url, header)
    tree = ET.fromstring(response.content)

    #print(response.content)
    #intelfeed

    for x in tree.findall('ip'):
        item = x.find('ip').text
        price = x.find('description').text
        print(item, price)
    print(tree.tag)
