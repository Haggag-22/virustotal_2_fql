import click
import vt
import subprocess
import sys
from backend.config import *
from backend.vt_extractor import *
from backend.generator import *

@click.command(help="""
vt2fql - Generate FQL detection queries from VirusTotal IOCs.

Examples:
  python vt2fql.py --hash <sha256>
  python vt2fql.py --ip <ip_address>
""")

@click.option("--hash", help="File Hash (SHA256, SHA1, or MD5)")
@click.option("--ip", help="IP Address to investigate")
@click.option("--domain", help="Domain to investigate")
@click.option("--url", help="URL to investigate")
@click.option("--explain", is_flag=True, help="Show used fields in the FQL query")


def main(hash, ip, domain, url, explain):

    click.echo(click.style("\n🔍 Falcon Query Generator from VirusTotal\n", fg="cyan", bold=True))

    if not any([hash, ip, domain, url]):
        click.echo(click.style("❌ Please provide one of: --hash, --ip, --domain, or --url\n", fg="red", bold=True), err=True)
        return

    with vt.Client(VT_API_KEY) as client:

        ioc_inputs = {
            "hash": (hash, get_file_report, extract_file_fields),
            "ip": (ip, get_ip_report, extract_ip_fields),
            "domain": (domain, get_domain_report, extract_domain_fields),
            "url": (url, get_url_report, extract_url_fields),
        }

        for label, (value, report_func, extract_func) in ioc_inputs.items():
            if value:
                click.echo(click.style(f"✔ Analyzing {label}: ", fg="green") + click.style(value, fg="yellow"))
                report = report_func(client,value)
                iocs = extract_func(report)
                query = FQLGenerator(iocs)

                click.echo(click.style("\n🎯 Generated FQL Query:\n", fg="blue", bold=True))
                click.echo(click.style(query.generate() + "\n", fg="white", bold=True))

                if explain:
                    click.echo(click.style("🧠 Fields used in the query:", fg="magenta", bold=True))
                    query.explain()




