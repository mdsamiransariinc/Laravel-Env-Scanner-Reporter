import urllib3
import os.path
import requests
from os import path
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Random headers of a browser is used , You can also replace it with your user-agent
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Language': 'en-US,en;q=0.5',
           'Accept-Encoding': 'gzip, deflate'}


class Bot:

    def envScanner(self, url):

        def dotenv(url, plainurl):

            # uriPATH conist the most frequetly used extensions , their are alot of more extension , you can add here or replace with your own
            uriPATH = ['/', 'local/', 'admin/', 'dev/', 'api/', 'stag/', 'platform/', 'staging/', 'development/', 'localhost/', 'test/', 'production/', 'developer/', 'public/', 'app/', 'core/', 'data/', 'api1/', 'api2/', 'api3/', 'API/', 'apiv1/', 'apiv2/', 'apiv3/', 'apps/', 'git/', 'laravel/', 'sites/', 'web/', 'v1/api/', 'v2/api/', 'v3/api/', 'site/', 'admin/', 'administrator/', 'backend/', 'portal/',
                       'office/', 'application/', 'laravel2/', 'laravel1/', 'default/', 'public/laravel/', 'laravel/public/', 'st/', 'blog/', 'blogs/', 'admins/', 'Admin/', 'ADMIN/', 'ADMINISTRATOR/', 'Administrator/', 'Site/', 'Public/', 'Staging/', 'Stag/', 'Production/', 'prod/', 'Prod/', 'Local/', 'Development/', 'Backend/', 'Api/', 'Api1/', 'APIV1/', 'Platform/', 'Laravel/', 'Web/', 'Core/', 'App/']

            for PATHS in uriPATH:
                keys = ['MAIL_HOST=', 'APP_ENV=']
                # Sending request to site /.env to see if it vulnerable or not , if yes please fix it or contact and inform the owner
                r = requests.get(f'{url}{PATHS}.env', verify=False,
                                 timeout=10, allow_redirects=False)
                print(
                    f'\033[33;1m[SCANNING ENV] \033[34;1m: \033[37;1m{r.url}\033[0m')
                if r.status_code == 200:
                    if any(key in r.text for key in keys):
                        # bug found please fix it
                        print(
                            f'\033[32;1m[ENV BUG FOUND ON SITE < FIX THE DEBUG ON SITE] \033[34: \033[37{r.url}\033[0m')
                    else:
                        print(
                            "\033[32;1mENV MODE OFF ON SITE < YOUR SITE IS SECURED :) ")

        def Debugenv(url, plainurl):
            try:
                ID = ['<td>APP_DEBUG</td>', '<td>APP_ENV</td>']
                data = {'debug': 'true'}
                # Sending Post request to site using debug mode to see if it vulnerable or not , if yes please fix it or contact and inform the owner
                r = requests.post(
                    url, data=data, allow_redirects=False, verify=False, timeout=10)
                print(
                    f'\033[32;1m[SCANNING DEBUG] \033[34m: \033[37m{r.url}\033[0m')
                if any(Identifier in r.text for Identifier in ID):
                    # bug found please fix it
                    print(
                        f'\033[32;1[DEBUG BUG FOUND ON SITE < TURN OFF THE DEBUG ON SITE] \033[34m: \033[37m{r.url}\033[0m')
                else:
                    print(
                        "\033[32;1mDEBUG MODE OFF ON SITE < YOUR SITE IS SECURED :) ")
            except:
                pass

        # This function is used to check if the website url/ip exists or if it is up and functioning well
        def checkStatus(url):
            url = str(url)
            if "http://" in url:
                url = url.replace("http://", '')
            if "https://" in url:
                url = url.replace("https://", '')
            try:
                r = requests.get(
                    f'http://{url}/', allow_redirects=False, timeout=10, verify=False, headers=headers)

                if r.status_code == 200:
                    Debugenv(r.url.strip('/'), url)
                    dotenv(r.url.strip('/'), url)
                if r.status_code == 301:
                    r = requests.get(
                        f'{r.headers["Location"]}', verify=False, timeout=10, allow_redirects=False, headers=headers)
                    if r.status_code == 200:
                        Debugenv(r.url.strip('/'), url)
                        dotenv(r.url.strip('/'), url)
                    else:
                        r = requests.get(
                            f'http://www.{url}/', verify=False, timeout=10, allow_redirects=False, headers=headers)
                        if r.status_code == 200:
                            Debugenv(r.url.strip('/'), url)
                            dotenv(r.url.strip('/'), url)
                        else:
                            r = requests.get(
                                f'https://www.{url}/', verify=False, timeout=10, allow_redirects=False, headers=headers)
                            if r.status_code == 200:
                                Debugenv(r.url.strip('/'), url)
                                dotenv(r.url.strip('/'), url)
                            else:
                                Debugenv(f'https://{url}', url)
                                dotenv(f'https://{url}', url)
                if r.status_code == 302:
                    try:
                        r = requests.get(
                            r.headers['Location'], verify=False, timeout=10, allow_redirects=False, headers=headers)
                        if r.status_code == 200:
                            dotenv(r.url.strip('/'), url)
                            Debugenv(r.url.strip('/'), url)
                        if r.status_code == 302:
                            url = r.headers['Location']
                            r = requests.get(url.replace(
                                'www.', ''), verify=False, timeout=10, allow_redirects=False, headers=headers)
                            if r.status_code == 200:
                                dotenv(r.url.strip('/'), url)
                                Debugenv(r.url.strip('/'), url)
                            else:
                                r = requests.get(url.replace(
                                    '://', '://www.'), verify=False, timeout=10, allow_redirects=False, headers=headers)
                                if r.status_code == 200:
                                    dotenv(r.url.strip('/'), url)
                                    Debugenv(r.url.strip('/'), url)
                                else:
                                    dotenv(f'http://{url}', url)
                                    Debugenv(f'http://{url}', url)
                    except:
                        print(
                            "\033[31;1m[!] \033[37mConnection timeout to the site, Please contact the owner.\033[0m")
            except Exception as e:
                pass

        checkStatus(url)


# Main module
if __name__ == '__main__':
    bot = Bot()

    os.system('cls')
    print("""\033[34m


         ██▓███   ██▀███  ▓█████ ▓█████▄  ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
        ▓██░  ██▒▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
        ▓██░ ██▓▒▓██ ░▄█ ▒▒███   ░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
        ▒██▄█▓▒ ▒▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
        ▒██▒ ░  ░░██▓ ▒██▒░▒████▒░▒████▓  ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
        ▒▓▒░ ░  ░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
        ░▒ ░       ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
        ░░         ░░   ░    ░    ░ ░  ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
                    ░        ░  ░   ░          ░  ░            ░ ░     ░     
                                  ░                                          

                https://github.com/mdsamiransariinc
\t\t\033[33mCoded by \033[32mMD samir - a.k.a Predator
        """)
    print(
        "\033[31m1 \033[33m- \033[37mLaravel env Vulnerability scanner / report")
    print("\033[31m2 \033[33m- \033[37mMore Tools coming soon ... ")
    print("\033[31m3 \033[33m- \033[37mExit")
    print("\n\n")
    inp = int(input("\033[34mSelect :\033[32m "))
    if inp == 1:
        url = input(
            "\033[34mEnter your website url/ip to check vulnerability and fix it :\033[32m ")
        check = Bot()
        result = check.envScanner(str(url))
    elif inp == 8:
        exit()
    else:
        print("\033[31mSorry Command unrecognized by me")
