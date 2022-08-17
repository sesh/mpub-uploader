import requests
import sys
from urllib.parse import urlencode

def parse_args(args):
    result = {
        a.split("=")[0]: int(a.split("=")[1])
        if "=" in a and a.split("=")[1].isnumeric()
        else a.split("=")[1]
        if "=" in a
        else True
        for a in args
        if "--" in a
    }
    result["[]"] = [a for a in args if not a.startswith('--')]
    return result


def usage():
    print("usage")


def upload(fn, url, token):
    files = {"file": open(fn, 'rb')}
    response = requests.post(url, files=files, headers={
        "Authorization": f"Bearer {token}"
    })

    print(response.headers['Location'])


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    mediapub_url = args.get("--url")
    mediapub_token = args.get("--token")
    filename = args["[]"][0]

    if mediapub_url and mediapub_token and filename:
        upload(filename, mediapub_url, mediapub_token)
    else:
        token = login()
