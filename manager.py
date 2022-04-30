from server import server
from client import client
import argparse
import logging
import sys
import signal

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--server', action='store_true')
parser.add_argument('host')
parser.add_argument('port')
parser.add_argument('-t', '--tcp', action='store_true')
parser.add_argument('-u', '--udp', action='store_true')
parser.add_argument('-o', '--output', action='store_true')
parser.add_argument('-f', '--file_output')
args = parser.parse_args()

if args.output:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)

    logger.addHandler(stdout_handler)
elif args.file_output:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

    file_handler = logging.FileHandler(args.file_output)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

if args.server:
    try:
        if args.tcp and args.udp:
            print('bad')
        elif args.tcp:
            server(args.host, args.port, 'tcp')
        else:
            server(args.host, args.port, 'udp')
    except Exception as Argument:
        logger.exception('Something happened with server')
else:
    try:
        if args.tcp and args.udp:
            print('bad')
        elif args.tcp:
            client(args.host, args.port, 'tcp')
        else:
            client(args.host, args.port, 'udp')
    except Exception as Argument:
        logger.exception('Something happened with client')
