#### Randomize Organizational Items into Group
#### Example:
#### randomizeToGroup.py -u myuser -p mypassword -query -num 10 -portal https://esri.maps.arcgis.com -group a23455GROUPID334323434 

import argparse
import sys

from agoTools.admin import Admin

def _raw_input(prompt=None, stream=None, input=None):
    # A raw_input() replacement that doesn't save the string in the
    # GNU readline history.
    if not stream:
        stream = sys.stderr
    if not input:
        input = sys.stdin
    prompt = str(prompt)
    if prompt:
        stream.write(prompt)
        stream.flush()
    # NOTE: The Python C API calls flockfile() (and unlock) during readline.
    line = input.readline()
    if not line:
        raise EOFError
    if line[-1] == '\n':
        line = line[:-1]
    return line

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-p', '--password')
parser.add_argument('-portal', '--portal')
parser.add_argument('-group', '--group')
parser.add_argument('-query', '--query')
parser.add_argument('-num', '--num')

args = parser.parse_args()

if args.user == None:
    args.user = _raw_input("Username:")

if args.portal == None:
    args.portal = _raw_input("Portal: ")

if args.group == None:
    args.group = _raw_input("Group ID: ")

args.portal = str(args.portal).replace("http://","https://")

agoAdmin = Admin(args.user,args.portal,args.password)

agoAdmin.randomizeToGroup(args.query,args.num,args.group)


