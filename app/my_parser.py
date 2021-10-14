import requests
import xml.etree.ElementTree as ET
import geocoder
import nmap


url = 'http://isc.sans.edu/api/intelfeed/'


def get_response(header):
    response = requests.get(url, header)
    tree = ET.fromstring(response.content)

    #intelfeed
    for x in tree.findall('ip'):
        item = x.find('ip').text
        price = x.find('description').text

       # print(g.response)
       # print(g.current_result)
        #print(item, price)


def find_location(ip):
    #g = geocoder.ip('199.175.213.12')
    #print(g.headers)
    nm = nmap.PortScanner()
    print(nm.scan(hosts=ip))


def find_ip_information(ip, header):
    link_addr = 'https://www.dshield.org/api/ip/'
    response = requests.get(link_addr + ip, header)
    print(response.content)
    #print(link_addr + ip)
