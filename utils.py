import os
import requests
import socket
import json

def carregar_json(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao carregar JSON {caminho_arquivo}: {e}")
        return None

def main_banner(): #<------- Main Banner
    
    print(rf"""{B}
{B}        ____________        {O}                                        
{B}       /\  ________ \       {O}        ____ _       _           _  {B} ____  _   _  ____
{B}      /  \ \______/\ \      {O}       / ___| | ___ | |__   __ _| | {B}|  _ \| \ | |/ ___|
{B}     / /\ \ \  / /\ \ \     {O}      | |  _| |/ _ \| '_ \ / _` | | {B}| | | |  \| |\___ \                                
{B}    / / /\ \ \/ / /\ \ \    {O}      | |_| | | (_) | |_) | (_| | | {B}| |_| | |\  | ___) |          
{B}   / / /__\_\/ / /__\_\ \   {O}       \____|_|\___/|_.__/ \__,_|_| {B}|____/|_| \_||____/             
{B}  / /_/_______/ /________\  {O}          {H}   ____                  _                           _            
{B}  \ \ \______ \ \______  /  {O}          {H}  | __ )  ___ _ __   ___| |__   _ __ ___   __ _ _ __| | __    
{B}   \ \ \  / /\ \ \  / / /   {O}          {H}  |  _ \ / _ | '_ \ / __| '_ \ | '_ ` _ \ / _` | '__| |/ /
{B}    \ \ \/ / /\ \ \/ / /    {O}          {H}  | |_) |  __| | | | (__| | | || | | | | | (_| | |  |   <      
{B}     \ \/ / /__\_\/ / /     {O}          {H}  |____/ \___|_| |_|\___|_| |_||_| |_| |_|\__,_|_|  |_|\_\   
{B}      \  / /______\/ /      {O}                                                  
{B}       \/___________/       {O}                                                 Created By {B}Christopher Rissardi
                               {O}                                                        
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

def data_information(): #<-------- Get usar information
    url = "https://ipwho.is/"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get("success", False):
            print(f"""Your Informations:                                            

[{B}+{O}] IP Address: {data['ip']} | {data['type']}
[{B}+{O}] City: {data['city']}
[{B}+{O}] Region: {data['region']} ({data['region_code']})   
[{B}+{O}] Country: {data['country']} ({data['country_code']})                                      
[{B}+{O}] Continent: {data['continent']} ({data['continent_code']})                                                                     
[{B}+{O}] ISP: {data['connection']['isp']}
[{B}+{O}] Org: {data['connection']['org']}
[{B}+{O}] Domain: {data['connection']['domain']}
[{B}+{O}] ASN: {data['connection']['asn']}
                                                    Welcome {B}{get_username()}{O}.            
                                                Your local IP is: {B}{get_local_ip()}{O}  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

            # Retorna os dados para uso no script principal
            return data
        else:
            print("Error getting external IP information. Check an API.")
            return None
    
    except Exception as e:
        print(f"Error connecting to API: {e}")
        return None

def get_local_ip(): #<----------Get Local Host
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))
        ip_local = s.getsockname()[0]
    except Exception:
        ip_local = 'Unavailable'
    finally:
        s.close()
    return ip_local

dados_usuario = data_information()  # <---> Information of IP Address on information.py

def get_username(): #<--------- Get username
    return os.getlogin()

def information():
    print(f"\n\nRoot Servers Available - Info")
    print("Here is the tab dedicated to information about Root-Servers spread all over the world")
    print(f"""
Root Server (A) - {B}Verisign{O} | a.root-servers.net
          
[{B}+{O}] Status: success
[{B}+{O}] IP: 198.41.0.4
[{B}+{O}] City: Lakeside (TX)
[{B}+{O}] Region: Texas
[{B}+{O}] Country: United States
[{B}+{O}] Continent: North America (TX)
[{B}+{O}] Latitude: 32.8223
[{B}+{O}] Longitude: -97.4934
[{B}+{O}] ISP: VeriSign Inc.
[{B}+{O}] Org: VeriSign Infrastructure & Operations
[{B}+{O}] AS: AS25485 VeriSign Inc.
[{B}+{O}] ASNAME: VERISIGN-AS
[{B}+{O}] IP Proxy: Unknown
[{B}+{O}] Reverse IP: a.root-servers.net
[{B}+{O}] ZIP Code Of State: 76135
[{B}+{O}] IP Hosting: Unknown
[{B}+{O}] Currency: USD
[{B}+{O}] Time Zone: America/Chicago

Root Servers (B) - {B}University of Southern California{O} | b.root-servers.net
          
[{B}+{O}] Status: success
[{B}+{O}] IP: 170.247.170.2
[{B}+{O}] City: Miami (FL)
[{B}+{O}] Region: Florida
[{B}+{O}] Country: United States
[{B}+{O}] Continent: North America (FL)
[{B}+{O}] Latitude: 25.7617
[{B}+{O}] Longitude: -80.1918
[{B}+{O}] ISP: LACNIC - Latin American and Caribbean
[{B}+{O}] Org: B-Root OPS
[{B}+{O}] AS: AS394353 B.Root-Server-OPS
[{B}+{O}] ASNAME: BROOT-AS
[{B}+{O}] IP Proxy: Unknown
[{B}+{O}] Reverse IP: b.root-servers.net
[{B}+{O}] ZIP Code Of State: 33102
[{B}+{O}] IP Hosting: Unknown
[{B}+{O}] Currency: USD
[{B}+{O}] Time Zone: America/New_York

Root Server (C) - {B}Cogent Communications{O} | c.root-servers.net
          
[{B}+{O}] Status: success
[{B}+{O}] IP: 192.33.4.12
[{B}+{O}] City: New York (NY)
[{B}+{O}] Region: New York
[{B}+{O}] Country: United States
[{B}+{O}] Continent: North America (NY)
[{B}+{O}] Latitude: 40.7128
[{B}+{O}] Longitude: -74.006
[{B}+{O}] ISP: Cogent Communications
[{B}+{O}] Org: Cogent communications - IPENG
[{B}+{O}] AS: AS2149 Cogent Communications
[{B}+{O}] ASNAME: COGENT-2149
[{B}+{O}] IP Proxy: Unknown
[{B}+{O}] Reverse IP: c.root-servers.net
[{B}+{O}] ZIP Code Of State: 10123
[{B}+{O}] IP Hosting: Unknown
[{B}+{O}] Currency: USD
[{B}+{O}] Time Zone: America/New_York

Root Server (D) - {B}University of Maryland{O} | d.root-servers.net
          
[{B}+{O}] Status: success
[{B}+{O}] IP: 199.7.91.13
[{B}+{O}] City: College Park (MD)
[{B}+{O}] Region: Maryland
[{B}+{O}] Country: United States
[{B}+{O}] Continent: North America (MD)
[{B}+{O}] Latitude: 38.9827
[{B}+{O}] Longitude: -76.9474
[{B}+{O}] ISP: University of Maryland
[{B}+{O}] Org: University of Maryland
[{B}+{O}] AS: AS10886 University of Maryland
[{B}+{O}] ASNAME: MAX-GIGAPOP
[{B}+{O}] IP Proxy: Unknown
[{B}+{O}] Reverse IP: d.root-servers.net
[{B}+{O}] ZIP Code Of State: 20742
[{B}+{O}] IP Hosting: Unknown
[{B}+{O}] Currency: USD
[{B}+{O}] Time Zone: America/New_York
          
Root Server (E) - {B}NASA{O} | e.root-servers.net
          
[{B}+{O}] Status: success
[{B}+{O}] IP: 192.203.230.10
[{B}+{O}] City: Birmingham (AL)
[{B}+{O}] Region: Alabama
[{B}+{O}] Country: United States
[{B}+{O}] Continent: North America (AL)
[{B}+{O}] Latitude: 33.5186
[{B}+{O}] Longitude: -86.8104
[{B}+{O}] ISP: National Aeronautics and Space Administration
[{B}+{O}] Org: National Aeronautics and Space Administration
[{B}+{O}] AS: AS21556 National Aeronautics and Space Administration
[{B}+{O}] ASNAME: NARC-EROOT
[{B}+{O}] IP Proxy: Unknown
[{B}+{O}] Reverse IP: e.root-servers.net
[{B}+{O}] ZIP Code Of State: 35201
[{B}+{O}] IP Hosting: Unknown
[{B}+{O}] Currency: USD
[{B}+{O}] Time Zone: America/Chicago
          
Root Server (F) - {B}Internet Systems Consortium ISC{O} | f.root-servers.net
          
[{B}+{O}] Status: success
[{B}+{O}] IP: 192.5.5.241
[{B}+{O}] City: Newmarket (NH)
[{B}+{O}] Region: New Hampshire
[{B}+{O}] Country: United States
[{B}+{O}] Continent: North America (NH)
[{B}+{O}] Latitude: 43.0789
[{B}+{O}] Longitude: -70.9368
[{B}+{O}] ISP: Internet Systems Consortium, Inc.
[{B}+{O}] Org: Internet Systems Consortium, Inc.
[{B}+{O}] AS: AS3557 Internet Systems Consortium, Inc.
[{B}+{O}] ASNAME: ISC-AS
[{B}+{O}] IP Proxy: Unknown
[{B}+{O}] Reverse IP: f.root-servers.net
[{B}+{O}] ZIP Code Of State: 03857
[{B}+{O}] IP Hosting: Unknown
[{B}+{O}] Currency: USD
[{B}+{O}] Time Zone: America/New_York

Root Server (G) - {B}Defense Information Systems Agency{O} | g.root-servers.net
          
[{B}+{O}] Status: success
[{B}+{O}] IP: 192.112.36.4
[{B}+{O}] City: Columbus (OH)
[{B}+{O}] Region: Ohio
[{B}+{O}] Country: United States
[{B}+{O}] Continent: North America (OH)
[{B}+{O}] Latitude: 39.9819
[{B}+{O}] Longitude: -82.9048
[{B}+{O}] ISP: DoD Network Information Center
[{B}+{O}] Org: DoD Network Information Center
[{B}+{O}] AS: AS5927 DoD Network Information Center
[{B}+{O}] ASNAME: DNIC-ASBLK-05800-06055
[{B}+{O}] IP Proxy: Unknown
[{B}+{O}] Reverse IP: G.ROOT-SERVERS.NET
[{B}+{O}] ZIP Code Of State: 43218
[{B}+{O}] IP Hosting: Unknown
[{B}+{O}] Currency: USD
[{B}+{O}] Time Zone: America/New_York
          
Root Server (H) - {B}US Army (Research Lab){O} | h.root-servers.net
          
[{B}+{O}] Status: success
[{B}+{O}] IP: 198.97.190.53
[{B}+{O}] City: Miami (FL)
[{B}+{O}] Region: Florida
[{B}+{O}] Country: United States
[{B}+{O}] Continent: North America (FL)
[{B}+{O}] Latitude: 25.7617
[{B}+{O}] Longitude: -80.1918
[{B}+{O}] ISP: GOC
[{B}+{O}] Org: USAISC
[{B}+{O}] AS: AS1508 Headquarters, USAISC
[{B}+{O}] ASNAME: DNIC-AS-01508
[{B}+{O}] IP Proxy: Unknown
[{B}+{O}] Reverse IP: h.root-servers.net
[{B}+{O}] ZIP Code Of State: 33102
[{B}+{O}] IP Hosting: Unknown
[{B}+{O}] Currency: USD
[{B}+{O}] Time Zone: America/New_York
          
Root Server (I) - {B}Netnod{O} | i.root-servers.net
          
[{B}+{O}] Status: success
[{B}+{O}] IP: 192.36.148.17
[{B}+{O}] City: Stockholm (AB)
[{B}+{O}] Region: Stockholm County
[{B}+{O}] Country: Sweden
[{B}+{O}] Continent: Europe (AB)
[{B}+{O}] Latitude: 59.3293
[{B}+{O}] Longitude: 18.0686
[{B}+{O}] ISP: reserved DNS root name server i.root-servers.net
[{B}+{O}] Org: Unknown
[{B}+{O}] AS: AS29216 Netnod AB
[{B}+{O}] ASNAME: I-ROOT
[{B}+{O}] IP Proxy: Unknown
[{B}+{O}] Reverse IP: i.root-servers.net
[{B}+{O}] ZIP Code Of State: 104 25
[{B}+{O}] IP Hosting: Unknown
[{B}+{O}] Currency: SEK
[{B}+{O}] Time Zone: Europe/Stockholm

Root Server (J) - {B}Verisign{O} | j.root-servers.net
   
[{B}+{O}] Status: success
[{B}+{O}] IP: 192.58.128.30
[{B}+{O}] City: Reston (VA)
[{B}+{O}] Region: Virginia
[{B}+{O}] Country: United States
[{B}+{O}] Continent: North America (VA)
[{B}+{O}] Latitude: 38.9567
[{B}+{O}] Longitude: -77.3623
[{B}+{O}] ISP: VeriSign Global Registry Services
[{B}+{O}] Org: VeriSign Global Registry Services
[{B}+{O}] AS: AS20431 VeriSign Global Registry Services
[{B}+{O}] ASNAME: VGRS-AC19
[{B}+{O}] IP Proxy: Unknown
[{B}+{O}] Reverse IP: j.root-servers.net
[{B}+{O}] ZIP Code Of State: 20190
[{B}+{O}] IP Hosting: Unknown
[{B}+{O}] Currency: USD
[{B}+{O}] Time Zone: America/New_York         

Root Server (K) - {B}RIPE NCC{O} | k.root-servers.net

[{B}+{O}] Status: success
[{B}+{O}] IP: 193.0.14.129
[{B}+{O}] City: Amsterdam (NH)
[{B}+{O}] Region: North Holland
[{B}+{O}] Country: The Netherlands
[{B}+{O}] Continent: Europe (NH)
[{B}+{O}] Latitude: 52.3777
[{B}+{O}] Longitude: 4.9022
[{B}+{O}] ISP: K-ROOT Service Network
[{B}+{O}] Org: Unknown
[{B}+{O}] AS: AS25152 Reseaux IP Europeens Network Coordination Centre (RIPE NCC)
[{B}+{O}] ASNAME: K-ROOT-SERVER
[{B}+{O}] IP Proxy: Unknown
[{B}+{O}] Reverse IP: k.root-servers.net
[{B}+{O}] ZIP Code Of State: 1016
[{B}+{O}] IP Hosting: Unknown
[{B}+{O}] Currency: EUR
[{B}+{O}] Time Zone: Europe/Amsterdam

Root Server (L) - {B}ICANN{O} | l.root-servers.net

[{B}+{O}] Status: success
[{B}+{O}] IP: 199.7.83.42
[{B}+{O}] City: Los Angeles (CA)
[{B}+{O}] Region: California
[{B}+{O}] Country: United States
[{B}+{O}] Continent: North America (CA)
[{B}+{O}] Latitude: 33.9829
[{B}+{O}] Longitude: -118.405
[{B}+{O}] ISP: ICANN
[{B}+{O}] Org: ICANN
[{B}+{O}] AS: AS20144 ICANN
[{B}+{O}] ASNAME: IMRS
[{B}+{O}] IP Proxy: Unknown
[{B}+{O}] Reverse IP: l.root-servers.net
[{B}+{O}] ZIP Code Of State: 90045
[{B}+{O}] IP Hosting: Unknown
[{B}+{O}] Currency: USD
[{B}+{O}] Time Zone: America/Los_Angeles         

Root Server (M) - {B}WIDE Project{O} | m.root-servers.net

[{B}+{O}] Status: success
[{B}+{O}] IP: 202.12.27.33
[{B}+{O}] City: Fujisawa (14)
[{B}+{O}] Region: Kanagawa
[{B}+{O}] Country: Japan
[{B}+{O}] Continent: Asia (14)
[{B}+{O}] Latitude: 35.3882
[{B}+{O}] Longitude: 139.428
[{B}+{O}] ISP: WIDE Project
[{B}+{O}] Org: WIDE
[{B}+{O}] AS: AS7500 WIDE Project
[{B}+{O}] ASNAME: M-ROOT-DNS
[{B}+{O}] IP Proxy: Unknown
[{B}+{O}] Reverse IP: m.root-servers.net
[{B}+{O}] ZIP Code Of State: 251-8533
[{B}+{O}] IP Hosting: Unknown
[{B}+{O}] Currency: JPY
[{B}+{O}] Time Zone: Asia/Tokyo


[{B}!{O}] More information at: https://root-servers.org/

""")






# >>=============================================<<
# ||A = "\033[0;30m" # Black/Preto               ||
B = "\033[0;31m" # Red/Vermelho                  ||
# ||C = "\033[0;32m" # Green/Verde               ||
# ||D = "\033[0;33m" # Brown/Marrom              ||
# ||E = "\033[0;34m" # Blue/Azul                 ||
# ||F = "\033[0;35m" # Purple/Roxo               ||
# ||G = "\033[0;36m" # Cyan/Ciano                ||
H = "\033[1;30m" # Black 2/Preto 2               ||
# ||I = "\033[1;31m" # Light Red/Vermelho Claro  || 
# ||J = "\033[1;32m" # Light Green/Verde Claro   ||  <-------- Colors
# ||K = "\033[1;33m" # Light Yellow/Amarelo Claro||
# ||L = "\033[1;34m" # Light Blue/Azul Claro     ||
# ||M = "\033[1;35m" # Light Purple/Roxo Claro   ||
# ||N = "\033[1;36m" # Light Cyan/Ciano Claro    ||
O = "\033[1;37m" # White                         ||
# ||P = "\033[4;30m" # Underline/Sublinhado      ||
# ||Q = "\033[5;30m" # Blinking/Piscando         ||
# ||R = "\033[7;30m" # Inverted/Invertido la ele ||
# ||S = "\033[8;30m" # Concealed/Encolhido       ||
# >>=============================================<<

