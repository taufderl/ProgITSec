import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-H', dest='tgtHost', type=str, \
    help='specify target host', required=True)
parser.add_argument('-p', dest='tgtPort', type=int, \
    help='specify target port', required=True)
args = parser.parse_args()