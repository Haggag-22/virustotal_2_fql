import vt
from vt_client import *


def extract_file_fields(report):
    attributes= report.get("attributes",{})
    
    sha256 = attributes.get("sha256")
    sha1 = attributes.get("sha1")
    md5 = attributes.get("md5")
    imphash = attributes.get("pe_info", {}).get("imphash")
    file_names = attributes.get("names", []) ## Executable Names List
    dll = [
    lib.get("library_name")
    for lib in attributes.get("pe_info", {}).get("import_list", [])
    if lib.get("library_name") is not None ] ## DLLs Used List
    file_type = attributes.get("type_description")
    tags = attributes.get("tags", []) # Tags List
    
    client.close()

def extract_ip_fields(report):
    attributes = report.get("attributes", {})

    ip = report.get("id")  
    country = attributes.get("country")
    asn = attributes.get("asn")
    as_owner = attributes.get("as_owner")
    network = attributes.get("network")
    rir = attributes.get("regional_internet_registry")
    tags = attributes.get("tags", [])
    reputation = attributes.get("reputation")
    total_votes = attributes.get("total_votes")
    last_analysis_stats = attributes.get("last_analysis_stats", {})
    last_analysis_date = attributes.get("last_analysis_date")
    
    client.close()
    
def extract_domain_fields(report):
    attributes = report.get("attributes", {})
    
    domain = report.get("id")
    resolved_ips = [record.get("value") for record in attributes.get("last_dns_records", [])]
    malicious_votes = attributes.get("last_analysis_stats", {}).get("malicious", 0)
    tags = attributes.get("tags", [])
    reputation = attributes.get("reputation")
    registrar = attributes.get("registrar")
    last_analysis_date = attributes.get("last_analysis_date")
    categories = attributes.get("categories", {})
    
    client.close()
    
def extract_url_fields(report):
    pass
    
    
    
    
    
    
    
    
    
    
    

