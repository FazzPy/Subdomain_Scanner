import requests
import sys

SUB_LIST = open("wordlist.txt").read()

SUBDOMAINS = SUB_LIST.splitlines()

for sub in SUBDOMAINS:
    
    # ARGV SCANNER

    sub_domain = f"http://{sub}.{sys.argv[1]}"

    print(sub_domain)

    # WORDLIST SCANNER

    try:
        requests.get(sub_domain)
    except requests.ConnectionError:        
        pass
    else:
        print("Found : ", sub_domain)
        OUTPUT = open("output.txt", "a")
        OUTPUT.write(sub_domain+" ")
