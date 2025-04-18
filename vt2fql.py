import click
import vt
from config import *

from vt_client import (
    get_file_report,
    get_ip_report,
    get_domain_report,
    get_url_report
)

from extractor import (
    extract_file_fields,
    extract_ip_fields,
    extract_domain_fields,
    extract_url_fields
)


@click.command()
@click.option("--hash", help= "File Hash (SHA256, SHA1, MD5)")
@click.option("--ip", help= "IP Address")
@click.option("--domain", help= "domain")
@click.option("--url", help= "url")

def main(hash, ip, domain, url):
    
    client = vt.Client(VT_API_KEY)
    if not any([hash, ip, domain, url]):
        click.echo("❌ Please provide one of: --hash, --ip, --domain, or --url", err=True)

        return
    
    if hash:
        click.echo(f"🔍 Searching for file hash: {hash}")
        report = get_file_report(hash)
        print(extract_file_fields(report))
        
    
    elif ip:
        click.echo(f"🔍 Searching for ip: {ip}")
        report = get_ip_report(ip)
        extract_ip_fields(report)
        
        
    elif domain:
        click.echo(f"🔍 Searching for domain: {domain}")
        report = get_domain_report(domain)
        extracted = extract_domain_fields(report)
        
    elif url:
        click.echo(f"🔍 Searching for URL: {url}")
        report = get_url_report(url)
        extracted = extract_url_fields(report)

    


if __name__ == "__main__":
    main()
