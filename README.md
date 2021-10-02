# ip_reputation_checker
A simple Python script to check IP reputations against the following tools:
- AbuseIPDB | [https://www.abuseipdb.com/](https://www.abuseipdb.com/)
- Blocklist.de | [https://www.blocklist.de/](https://www.blocklist.de/)

### Usage
[OSX/*nix] - Run the script from a user terminal <br />
`[prompt] python3 reputation_checker.py -H [ip_address]`

### Help
These features are NOT implemented yet:
- -c, --cidr # May not work for all blacklists/reputation sources!
- -f, --file # What type(s)/formats do we need to support?
- -o, --output # Output to JSON, CSV, others?
- -q, --quiet # Send output to a default log?
- -v, --verbose # Probably not required, it was part of tutorial ;)

```
usage: reputation_checker.py [-h] [-H HOST] [-c CIDR] [-q] [-v]

# How do we make one of these REQUIRED?
  -H HOST, --host HOST  Provide target host IP.
  -c CIDR, --cidr CIDR  Provide target CIDR address.
  -f, --file            File to read addresses from
  
optional arguments:
  -h, --help            show this help message and exit
  -q, --quiet           Suppress Output
  -v, --verbose         Verbose Output
  -o, --output          Output filename
```

### TODO
- Create loop/handler for multiple IP addresses
- Add Greynoise API functionality
- Cleanup blocklist.de output

### Optional
- Command line options to run against specific lists
- Consider re-defining each reputation source as a function()