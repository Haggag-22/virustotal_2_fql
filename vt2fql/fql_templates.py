FQL_TEMPLATE = {
    # Hashes
    "sha256": 'file.sha256:"{value}"',
    "sha1": 'file.sha1:"{value}"',
    "md5": 'file.md5:"{value}"',
    "imphash": 'file.imphash:"{value}"',

    # Executable / DLL
    "dll": 'module.name:"{value}"',
    "file_name": 'file.name:"{value}"',
    "file_type": 'file.type:"{value}"',

    # Network
    "ip": 'network.remote_ipv4:"{value}"',
    "asn": 'network.asn:"{value}"',
    "as_owner": 'network.as_owner:"{value}"',
    "cidr": 'network.cidr_block:"{value}"',

    # Domain
    "domain": 'dnsRequest.domain:"{value}"',
    "registrar": 'dns.domain.registrar:"{value}"',

    # URL
    "url": 'http.request.url:"{value}"',
    "host": 'http.request.hostname:"{value}"',
    "final_url": 'http.request.final_url:"{value}"',
    "status_code": 'http.response.status_code:{value}',

    # Enrichment / Metadata
    "tag": 'metadata.tags:"{value}"',
    "category": 'metadata.categories:"{value}"',
    "country": 'geoip.country_name:"{value}"',
}
