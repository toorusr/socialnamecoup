import requests as req
import sys

try:
    argv2 = sys.argv[2]
    if argv2 == "instagram" or "i" or "insta":
        argv = sys.argv[1]
        rsp = req.get("https://instagram.com/{}".format(argv))
    elif argv2 == "github" or "gh" or "git":
        argv = sys.argv[1]
        rsp = req.get("https://github.com/{}".format(argv))
    else:
        print("Please give an existing service you want to check.")

    if str(rsp) == "<Response [200]>":
        print("exists;")
    else:
        print("free;")
except IndexError:
    print("Please give an existing service you want to check.")
