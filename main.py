from colorama import init, Fore, Back, Style
import subprocess
import os
import requests
import pyautogui
import webbrowser
import platform
from flask import Flask, make_response
import sys
import time

app = Flask(__name__)

init()
    
def check_for_id_rsa_pub():
    file_path = os.path.expanduser(r"~/.ssh/id_rsa.pub")
    if os.path.exists(file_path):
        return True
    else:
        return False
    
def main():
    print(Fore.YELLOW + '''
╔╦═╦══════╦╦══╦╦══╦╦══════╦╦╦╦═══╗
║║╚╬═╦═╦═╦╣╠╦═╣╚╗╔╣╠╦═╗╔══╬╬╣╠╦═╗║
║╠╗║╠╣╠╬╝╠╗╔╣╠╣║║╚╗╔╣║║╠╗╚╣╠╗╔╣╩╣║
║╚═╩═╩╝╚═╝╚═╩═╩╩╝─╚═╩═╝╚══╩╝╚═╩═╝║
╚════════════════════════════════╝
╔╦═╦═══╦╦════════════╦╦════╗
║║░╩╦═╦╣╠╦═╗╔╦╦═╦═╦══╬╬═╦═╗║
║║░░║╩╬╗╔╬╝║║║║╩╣╠╬╗╚╣║║║║║║
║╚══╩═╝╚═╩═╝╚═╩═╩╝╚══╩╩═╩╩╝║
╚══════════════════════════╝    made by fander-company
------------------------------------------------------------
    ''')
    if check_for_id_rsa_pub == True:
        pass
    else:
        if platform.system() == "Windows":
            print(Fore.RED + "[!] STARTING PUBLIC SSH KEY GENERATION, DO NOT INTERFERE WITH THE PROCEDURE TO AVOID MALFUNCTIONS!")
            subprocess.Popen('cmd.exe')
            time.sleep(5)
            realbro = os.path.expanduser(r"~/.ssh/")
            pyautogui.typewrite(f"cd {realbro}")
            pyautogui.press("enter")
            pyautogui.typewrite("ssh-keygen")
            pyautogui.press("enter")
            pyautogui.typewrite("id_rsa")
            pyautogui.press("enter")
            pyautogui.press("enter")
        else:
            print('Your system does not support SSH procedures, redirect to manual setup...')
            webbrowser.open('https://github.com/fandercompany/scratch-to-site/tree/main')
            sys.exit()
    
    idscr = input('Link to ur scratch project: ')
    idsite = input('Subdom name: ')
    
    subprocess.Popen('cmd.exe')
    pyautogui.typewrite(f"ssh -o ServerAliveInterval=60 -R {idsite}:80:localhost:5000 serveo.net")
    pyautogui.press("enter")
    
    
    @app.route("/")
    def index():
        html_code = f'<iframe src="{idscr}" allowtransparency="true" frameborder="0" scrolling="no" allowfullscreen></iframe>'
        response = make_response(html_code)
        response.headers['Content-Type'] = 'text/html'
        return response
    
    app.run(port='5000')
    
if __name__ == "__main__":
    main()
