import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo",
    help="Echo the input to standard output.", type=int)
args = parser.parse_args()
print(args.echo)