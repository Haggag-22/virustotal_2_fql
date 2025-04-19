# VirusTotal_2_FQL

`vt2fql` is a command-line tool that extracts Indicators of Compromise (IOCs) from VirusTotal and converts them into CrowdStrike Falcon Query Language (FQL) detection queries. These can be used directly in Falcon Next Gen SIEM for detection and hunting.

---

## Supported Platforms

This tool is currently built and tested to run on **Linux/macOS terminals**.  
Support for Windows PowerShell will be added in a future update.

---

## Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/Haggag-22/virustotal_2_fql.git

# 2. Navigate into the project directory
cd virustotal_2_fql

# 3. Run the setup command to install dependencies
python vt2fql.py --setup

# 4. Open the .env file in the root folder and paste your VirusTotal API key
#
#    VT_API_KEY=your_virustotal_api_key_here
#
#    (You can get a free API key at https://www.virustotal.com)

# 5. Run the tool with one of the following options:
python vt2fql.py --hash <sha256>
python vt2fql.py --ip <ip_address>
python vt2fql.py --domain <domain_name>
python vt2fql.py --url <url>

# 6. (Optional) Use --explain to see what fields were used
python vt2fql.py --hash <sha256> --explain

# 7. (Optional) Use --help to see all available options
python vt2fql.py --help
