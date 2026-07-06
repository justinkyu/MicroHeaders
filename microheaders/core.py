import requests

def show(host):

    print()
    print("MicroHeaders")
    print("="*40)

    if not host.startswith("http"):
        host="https://"+host

    r=requests.get(host,timeout=5)

    for k,v in r.headers.items():
        print(f"{k}: {v}")
