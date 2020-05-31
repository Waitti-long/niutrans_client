from requests import post
import sys, json
import os

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


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("need 3 params")
    else:
        args = sys.argv[1:]
        from_lan = ""
        to_lan = ""
        if args[0] == "-z":
            from_lan = "zh"
            to_lan = "en"
        else:
            from_lan = "en"
            to_lan = "zh"
        apikey = read_api_key()
        if apikey is None:
            print("cant't find apikey.txt")
        else:
            r = post(address,
                     data={"from": from_lan, "to": to_lan, "apikey": apikey, "src_text": args[1]})
            print(json.loads(r.text)["tgt_text"])
