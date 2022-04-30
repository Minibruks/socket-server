from server import server
from client import client
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--server', action='store_true')
parser.add_argument('host')
parser.add_argument('port')
parser.add_argument('-t', '--tcp', action='store_true')
parser.add_argument('-u', '--udp', action='store_true')
args = parser.parse_args()

if args.server:
    if args.tcp and args.udp:
        print('bad')
    elif args.tcp:
        server(args.host, args.port, 'tcp')
    else:
        server(args.host, args.port, 'udp')
else:
    if args.tcp and args.udp:
        print('bad')
    elif args.tcp:
        client(args.host, args.port, 'tcp')
    else:
        client(args.host, args.port, 'udp')
