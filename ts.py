from requests import post
import json
import os
from argparse_init import init
from data import lans, err_msg

address = "http://free.niutrans.com/NiuTransServer/translation"


def read_api_key():
    if os.access("apikey.txt", os.R_OK):
        f = open("apikey.txt")
    elif os.access("/usr/bin/apikey.txt", os.R_OK):
        f = open("/usr/bin/apikey.txt")
    else:
        f = None
    if f is None:
        return None
    apikey = f.readline()
    f.close()
    return apikey


def check():
    apikey = read_api_key()
    if apikey is None:
        raise FileNotFoundError("Cant't find apikey.txt")
    return apikey


def run(apikey):
    args = init()
    from_lan = "auto"
    to_lan = "zh"
    if args.apikey:
        apikey = args.apikey
    if args.z:
        from_lan = "zh"
        to_lan = "en"
    if args.f:
        from_lan = args.f
    if args.t:
        to_lan = args.t
    if args.auto:
        from_lan = "auto"
    if args.list:
        for li in lans:
            print("%s\t%s\t%s\t" % (li[0], li[1], li[2]))
    r = post(address,
             data={"from": from_lan, "to": to_lan, "apikey": apikey, "src_text": args.src_text})
    js = json.loads(r.text)
    if "error_msg" in js:
        raise IOError(js["error_msg"])
    if args.show:
        print(r.text, end="")
    else:
        print(js["tgt_text"], end="")


if __name__ == '__main__':
    apikey = check()
    run(apikey)
