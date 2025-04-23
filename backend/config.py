import os
import vt
from dotenv import load_dotenv

load_dotenv()
VT_API_KEY = os.getenv("VT_API_KEY")

client = vt.Client(VT_API_KEY)

def get_file_report(client,file_hash):
    return client.get_object(f"/files/{file_hash}").to_dict()

def get_ip_report(client,ip):
    return client.get_object(f"/ip_addresses/{ip}").to_dict()

def get_domain_report(client,domain):
    return client.get_object(f"/domains/{domain}").to_dict()

def get_url_report(client, url):
    return client.get_object(f"/urls/{url}").to_dict()