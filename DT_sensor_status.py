#!/usr/bin/env python3
import time

from DtAPI import DtAPI
# Dict with API tokens and server address. should look like:
# authparams={'server': 'https://darktrace.example.com', 'private': 'xxxxxxxxxxx', 'public':'yyyyyyyyyyyyy'}
import apitoken

# Number of days' data to collect
SINCE_DAYS = 7

#utility function
def prettyPrintDevice(device):
    buffer = ""
    if 'hostname' in device:
        buffer += device['hostname']

    if 'ip' in device:
        if len(buffer) > 0:
            buffer += ' - '
        buffer += device['ip']

    if 'macaddress' in device:
        if len(buffer) > 0:
            buffer += ' - '
        buffer += device['macaddress']

    if 'vendor' in device:
        if len(buffer) > 0:
            buffer += ' - '
        buffer += device['vendor']

    return buffer


api = DtAPI(apitoken.authparams['server'], apitoken.authparams['public'], apitoken.authparams['private'])
try:
    status = api.getStatus(includeProbes=False)
    print('Version: ' + status['version'])

except Exception as e:
    print(str(e))

