import vt
from config import *

client = vt.Client(VT_API_KEY)

def get_file_report(hash):
    return client.get_object(f"/files/{hash}").to_dict()  # Report is a Dictionary

def get_ip_report(ip):
    return client.get_object(f"/ip_addresses/{ip}").to_dict()  # Report is a Dictionary

def get_domain_report(domain):
    return client.get_object(f"/domains/{domain}").to_dict()  # Report is a Dictionary

def get_url_report(url):
    return client.get_object(f"/urls/{url}").to_dict()  # Report is a Dictionary



    
