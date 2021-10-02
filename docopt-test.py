#!/usr/bin/env python3

import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument('-H', '--host',
                    nargs='+',
                    dest='host',
                    help='Provide target host IP.',
                    type=str
                    )
parser.add_argument('-c', '--cidr',
                    dest='cidr',
                    help='Provide target CIDR address.',
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

"""Manage logfiles
Usage:
    managelog.py [options] process -- <logfile>...
    managelog.py [options] upload -- <logfile>...
    managelog.py [options] process upload -- <logfile>...
    managelog.py -h
Options:
    -V, --verbose      Be verbose
    -U, --user <user>  Username
    -P, --pswd <pswd>  Password
Manage log file by processing and/or uploading it.
If upload requires authentication, you shall specify <user> and <password>
"""
if __name__ == "__main__":
    from docopt import docopt
    args = docopt(__doc__)
    print( args )
