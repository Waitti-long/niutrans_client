from argparse import ArgumentParser
import sys


def init():
    parser = ArgumentParser()
    parser.add_argument("-z", action="store_true", help="chinese to english")
    parser.add_argument("--apikey", help="temporarily specify the apikey")
    parser.add_argument("-f", help="specify origin language")
    parser.add_argument("-t", help="specify dist language")
    parser.add_argument("--auto", action="store_true", help="auto choose origin language")
    parser.add_argument("--list", action="store_true", help="list all supported language")
    parser.add_argument("--show", action="store_true", help="show from language and to language")
    parser.add_argument("-p", action="store_true", help="accept pipe data")
    pipe = "-p" in sys.argv
    if not pipe:
        parser.add_argument("src_text", help="src_text")
    args = parser.parse_args()
    if pipe:
        args.src_text = sys.stdin.read()
    return args
