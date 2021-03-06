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


def handler(signum, frame):
    print('\nServer terminated')
    exit(1)


logger = logging.getLogger()

if args.output:
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s '
                                  '\n--------------------------------------------------------')

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)

    logger.addHandler(stdout_handler)
elif args.file_output:
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('\n--------------------------------------------------------\n'
                                  '%(asctime)s | %(levelname)s | %(message)s')

    file_handler = logging.FileHandler(args.file_output)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

signal.signal(signal.SIGINT, handler)

if args.server:
    try:
        if args.tcp and args.udp:
            print('Simultaneous use of tcp and udp is not allowed')
        elif args.tcp or (not args.tcp and not args.udp):
            server(args.host, args.port, 'tcp')
        elif args.udp:
            server(args.host, args.port, 'udp')
    except Exception as Argument:
        logger.exception('Something happened with server')
else:
    try:
        if args.tcp and args.udp:
            print('Simultaneous use of tcp and udp is not allowed')
        elif args.tcp or (not args.tcp and not args.udp):
            client(args.host, args.port, 'tcp')
        elif args.udp:
            client(args.host, args.port, 'udp')
    except Exception as Argument:
        logger.exception('Something happened with client')
