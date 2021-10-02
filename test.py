import requests
import json
import sys

#- 
# Qureying IP's blacklist.de does not require an API token.
blde_url = 'http://api.blocklist.de/api.php'
blde_params = {'ip': sys.argv[1], 'start': 1}
blde_response = requests.get(blde_url, blde_params)

print( blde_url )
print( blde_response.text )



