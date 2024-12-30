from utils import main_banner
import os

os.system('cls' if os.name == 'nt' else 'clear')

B = "\033[0;31m"  # Vermelho
O = "\033[1;37m"  # Branco
H = "\033[1;30m"  # Preto 2

def credits_info():
    main_banner()
    print(f"""
    {B}My GitHub:{O} https://github.com/christopherrissardi     
    {B}ASCII Art:{O} https://www.asciiart.eu
    {B}DNS data:{O} https://public-dns.info
    {B}IP Lookup API:{O} http://ip-api.com
    {B}Get Information User API:{O} https://ipwhois.io/documentation
    {B}Whois Lookup:{O} https://pypi.org/project/python-whois/
        
    Thank you very much for using the tool! I hope it can contribute in some way to your goals
    of finding the best DNS server for your home/work/company or whatever! :)
    """)

