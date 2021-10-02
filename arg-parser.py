#!/usr/bin/env python3

import argparse
import sys

#-
# Argument parser :D
# Source: https://www.golinuxcloud.com/python-argparse/#What_is_command_line_argument
#

parser = argparse.ArgumentParser()
requiredArg = parser.add_argument_group('required')

parser.add_argument('-H', '--host',
                    help='Provide target host IP.',
                    default=True,
                    type=str
                    )
parser.add_argument('-c', '--cidr',
                    nargs='+',
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

querystring = {
    'ipAddress': {args.host},
    'maxAgeInDays': '90'
}

print(f'The host is "{querystring}"')