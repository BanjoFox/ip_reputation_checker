#- 
# This is a basic IP reputation checker using AbuseIPDB.  May add others in the future.
# For AbuseIPDB use the CHECK Endpoint query:
# Source: https://docs.abuseipdb.com/#check-endpoint
#

#!/usr/bin/env python3

import argparse
import requests
import json
import sys

#-
# Import API keys from file
# -- why doesn't this work?

from api_keys import abuseipdb_token

#-
# Argument parser :D
# Source: https://www.golinuxcloud.com/python-argparse/#What_is_command_line_argument
#
parser = argparse.ArgumentParser()
parser.add_argument('-H', '--host',
                    dest='host',
                    help='Provide target host IP.',
                    type=str
                    )
parser.add_argument('-c', '--cidr',
                    dest='cidr',
                    help='Provide target CIDR address.',
                    type=str
                    )
parser.add_argument('-f', '--file',
                    dest='file',
                    help='Path to input file.',
                    type=str
                    )
parser.add_argument('-o', '--output',
                    dest='output',
                    help='Path to output file.',
                    type=str
                    )                    
parser.add_argument('-q', '--quiet',
                    action='store_true',
                    dest='quiet',
                    help='Suppress Output'
                    )
parser.add_argument('-v', '--verbose',
                    action='store_true',
                    help='Verbose Output'
                    )                    

args = parser.parse_args()

#-
# Open the API keystore file
#
keyFile = open('api_keys', 'r')
apiKey = keyFile.readline().rstrip()

#-
# Define the AbuseIPDB api-endpoint
#
aipdb_url = 'https://api.abuseipdb.com/api/v2/check'

querystring = {
    'ipAddress': {args.host},
    'maxAgeInDays': '90'
}

headers = {
    'Accept': 'application/json',
    'Key': '6b38c2371777268042b8129c34461b0ec2d987af160006a43c8d1104a77d7c7aec38571599d4383b'
}

#-
# Query the AbuseIPDB API
response = requests.request(method='GET', url=aipdb_url, headers=headers, params=querystring)

#-
# Formatted output
decodedResponse = json.loads(response.text)
json_out = json.dumps(decodedResponse, sort_keys=True, indent=4)

print( json_out )

#- 
# Qureying IP's blacklist.de does not require an API token.
blde_url = 'http://api.blocklist.de/api.php'
blde_params = {'ip': args.host, 'start': 1}
blde_response = requests.get(blde_url, blde_params)

print( blde_response.text )
