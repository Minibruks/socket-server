from server import server
from client import client
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--server', action='store_true')
args = parser.parse_args()

if args.server:
    server()
else:
    client()
