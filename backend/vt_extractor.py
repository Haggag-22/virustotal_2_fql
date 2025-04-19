import vt

def extract_file_fields(report):
    attributes = report.get("attributes", {})
    iocs = {}

    if attributes.get("sha256"):
        iocs["sha256"] = attributes["sha256"]
    if attributes.get("sha1"):
        iocs["sha1"] = attributes["sha1"]
    if attributes.get("md5"):
        iocs["md5"] = attributes["md5"]
    if attributes.get("pe_info", {}).get("imphash"):
        iocs["imphash"] = attributes["pe_info"]["imphash"]
    if attributes.get("type_description"):
        iocs["file_type"] = attributes["type_description"]
    if attributes.get("names"):
        iocs["file_name"] = attributes["names"]
    
    dlls = [
        lib.get("library_name")
        for lib in attributes.get("pe_info", {}).get("import_list", [])
        if lib.get("library_name")
    ]
    if dlls:
        iocs["dll"] = dlls

    if attributes.get("tags"):
        iocs["tag"] = attributes["tags"]

    return iocs


def extract_ip_fields(report):
    attributes = report.get("attributes", {})
    iocs = {}

    if report.get("id"):
        iocs["ip"] = report["id"]
    if attributes.get("asn"):
        iocs["asn"] = attributes["asn"]
    if attributes.get("as_owner"):
        iocs["as_owner"] = attributes["as_owner"]
    if attributes.get("country"):
        iocs["country"] = attributes["country"]
    if attributes.get("network"):
        iocs["network"] = attributes["network"]
    if attributes.get("regional_internet_registry"):
        iocs["rir"] = attributes["regional_internet_registry"]
    if attributes.get("tags"):
        iocs["tag"] = attributes["tags"]

    return iocs


def extract_domain_fields(report):
    attributes = report.get("attributes", {})
    iocs = {}

    if report.get("id"):
        iocs["domain"] = report["id"]
    resolved_ips = [
        record.get("value")
        for record in attributes.get("last_dns_records", [])
        if record.get("type") == "A" and record.get("value")
    ]
    if resolved_ips:
        iocs["resolved_ips"] = resolved_ips
    if attributes.get("tags"):
        iocs["tag"] = attributes["tags"]
    if attributes.get("categories"):
        iocs["category"] = attributes["categories"]
    if attributes.get("registrar"):
        iocs["registrar"] = attributes["registrar"]

    return iocs


def extract_url_fields(report):
    attributes = report.get("attributes", {})
    iocs = {}

    if attributes.get("url"):
        iocs["url"] = attributes["url"]
    if attributes.get("host"):
        iocs["host"] = attributes["host"]
    if attributes.get("last_http_response_content_sha256"):
        iocs["sha256"] = attributes["last_http_response_content_sha256"]
    if attributes.get("last_http_response_code"):
        iocs["status_code"] = attributes["last_http_response_code"]
    if attributes.get("tags"):
        iocs["tag"] = attributes["tags"]
    if attributes.get("categories"):
        iocs["category"] = attributes["categories"]

    return iocs
