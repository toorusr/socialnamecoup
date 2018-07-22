import requests as req
import sys
from itertools import product
from tqdm import tqdm

chars = "abcdefghijklmnopqrstuvwxyz1234567890"
variants = [a+b+c for a,b,c in product(chars, repeat=3)]
free = []
class All:
    def __init__(self, service):
        if service == "i":
            self.instagram()
        elif service == "gh":
            self.github()
        else:
            print("[D] Service id wrong")

    def custom(c, start):
        new = []
        if c:
            isstart = 0
            for i in variants:
                if i == start:
                    isstart = 1
                else: 
                    pass
                if isstart:
                    new.append(i)
        else:
            new = variants

        return new



    def instagram(self):
        for i in tqdm(variants):
            rsp = req.get("https://instagram.com/{}".format(i))
            if rsp == "<Response [200]>":
                # print("\r\t\t\t\033[1m\033[92m%s\tFREE\033[0m" % i)
                free.append(i)
                with open('instagram.3char.dump', 'a') as freedump:
                    freedump.write("FRE:" + i + "\n")
            else:
                # print("\t\t\t\033[91m%s\tTAKEN\033[0m" % i)
                with open('instagram.3char.dump', 'a') as freedump:
                    freedump.write("TAK:" + i + "\n")

    def github(self):
        for i in tqdm(variants):
            rsp = req.get("https://github.com/{}".format(i))
            if rsp == "<Response [200]>":
                # print("\r\t\t\t\033[1m\033[92m%s\tFREE\033[0m" % i)
                free.append(i)
                with open('github.3char.dump', 'a') as freedump:
                    freedump.write("FRE:" + i + "\n")
            else:
                # print("\t\t\t\033[91m%s\tTAKEN\033[0m" % i)
                with open('github.3char.dump', 'a') as freedump:
                    freedump.write("TAK:" + i + "\n")

print(All.custom(1, "wp1"))
try:
    argv2 = sys.argv[1]
    if argv2 == "instagram" or "i" or "insta":
        All("i")
    elif argv2 == "github" or "gh" or "git":
        All("gh")
    else:
        print("Missing service to check")
except IndexError:
    print("Missing service to check")
