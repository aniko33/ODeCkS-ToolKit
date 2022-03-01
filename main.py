import time
import os
import getpass
import colorama
from colorama import Fore, Back,Style
colorama.init(autoreset=True)
def main():
    os.system('clear')
time.sleep(0.10)
print('''
    [1] Scanning
    [2] Exploitation
    [3] OSINT
    [4] Information gathering
    [77] Install tools
    [55] Config
    [99] Exit''')
select=input(Fore.LIGHTYELLOW_EX+'Select > ')
if select=='1':
    scanner()
elif select=='2':
    exploite()
elif select=='3':
    osint()
elif select=='4':
    ig()
elif select=='99':
    quitmain()
elif select=='77':
    upgrade()
elif select=='55':
    config()
def phoneinfoga():
    os.system('clear')
    phonenumber=input(Fore.LIGHTYELLOW_EX+'Phone number > ')
    os.system('cd tools && ./phoneinfoga scan -n '+phonenumber)
def slock():
    os.system('clear')
    print(Fore.LIGHTMAGENTA_EX+'''
                                             _,aggdd888bbgg,,_
                                    ,ad88888YYYYYYYYYYY8888ba,
                                 ,d888P""'              ``""Y88b,
                               ,d888"'                       "Y888,
                              d88P'                            `Y88b,
                            ,d88'                                `Y88,
                           ,888'                                  `Y88,
                          ,d88'                                    `Y8b,
                          d88'                                      `88I
                         ,88P                                        I88
                         I88I                                        I88
                         I88I                                        I8I
                         `888,                                       d8I
                          `888,                                     d88'
                           `888,                                   d8PI
                           ,dP"8b,                               ,8P'd'
                         ,dP'   "Yb,                          _,d8" P'
                       ,dP' ,db,  "Yb,_                    ,ad8P" ,P'
                     ,dP' ,d8888b,  `"Yba,,__        __,ad88P"  ,d"
                   ,dP' ,d88888888b,    "88Y8888888888PP""   _,d"
                 ,dP' ,d888888888888P  ,d"8              _,gd"'
               ,dP' ,d888888888888P' ,d" ,8bbaagggggaaddP""'
             ,dP' ,d888888888888P' ,d" ,d"'
           ,dP' ,d888888888888P' ,d" ,d"
         ,dP' ,d888888888888P' ,d" ,d"     
       ,dP' ,d888888888888P' ,d" ,d"      
     ,dP' ,d888888888888P' ,d" ,d"
   ,dP' ,d888888888888P' ,d" ,d"
 ,dP' ,d888888888888P' ,d" ,d"
dP'  d888888888888P' ,d" ,d"
8"Ya, `888888888P' ,d" ,d"
8  "Ya, `88888P' ,d" ,d"
8a,  "Ya, `8P' ,d" ,d"
 "Ya,  "Ya,  ,d" ,d"
   "Ya,  "Y8P" ,d"
     "Ya,  8 ,d"
       "Ya,8d"
         "YP
    ''')
    target=input(Fore.LIGHTYELLOW_EX+ 'Username > ')
    os.system('cd sherlock/sherlock && python3 sherlock.py '+target)
def whois():
    os.system('clear')
    target=input(Fore.LIGHTYELLOW_EX+'Domain or IP > ')
    os.system('whois '+target)
def ig():
    os.system('clear')
    print('''
    
                           !
                       |
                       |    |~/
                       |   _|~
         .============.|  (_|   |~/
       .-;____________;|.      _|~
       | [_________I__] |     (_|
       |  """"" (_) (_) |
       | .=====..=====. |
       | |:::::||:::::| |
       | '=====''=====' |
       '----------------'

    
    ''')
    print('''
    [1] Whois
    [2] Sherlock''')
    select=input(Fore.LIGHTYELLOW_EX+'Select > ')
    if select=='1':
        whois()
    elif select=='2':
        slock()
def scanner():
    os.system('clear')
    print(Fore.WHITE+'''
     .    '                   .  "   '
            .  .  .                 '      '
    "`       .   .
                                     '     '
  .    '      _______________
          ==c(___(o(______(_()
                  \=\
                   )=\
                  //|\\
                 //|| \\
                // ||  \\
               //  ||   \\
              //         \\
    ''')
    print('''
    [1] Nmap
    [99] Back
    ''')
    scanner=input(Fore.LIGHTYELLOW_EX+'Select > ')
    if scanner=='1':
        nmap()
    elif scanner=='2':
        main()
def nmap():
    os.system('clear')
    print(Fore.GREEN+"""
  _  _   __  __     _     ___ 
 | \| | |  \/  |   /_\   | _ |
 | .` | | |\/| |  / _ \  |  _|
 |_|\_| |_|  |_| /_/ \_\ |_|  
                              """)
    print('''
    [1] Classic
    [2] Detect OS
    [3] Custom
    [4] Vuln script
    [99] Back''')
    type=input('Type: ')
    if type=='1':
        IP=input('IP or Domain: ')
        os.system('nmap -sV '+IP)
    elif type=='2':
        IP=input('IP or Domain: ')
        os.system('nmap -O '+IP) 
    elif type=='3':
        print('exaple: nmap -sV www.google.com')
        com=input('Insert Nmap command: ')
        os.system(com)
    elif type=='4':
        IP=input('IP or Domain: ')
        os.system('nmap -sV -O -script vuln '+IP)
    elif type=='99':
        scanner()
def msfbuider():
    os.system('clear')
    print(Fore.CYAN+'''
          °*°°°.                .°*°°°          
                 °°°°°°°°°°°°°°                 
         °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°         
      ° °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°° °      
      ° °°°oOOOOO*°°°°°°°°°°°°oOOOOO*°°° °      
      ° °°°o@@@@@@Oo°°°°°°°°o#@@@@@@*°°° °      
      ° °°°o####@@@@#o*°°*O#@@@@####*°°° °      
      ° °°°o@#@@##@@@@#OO@@@@@##@@#@*°°° °      
      ° °°°o@##@o*O#@@@@@@@@#o°O@##@*°°° °      
      ° °°°o@##@o°°°o#####O*°°°O@##@*°°° °      
      ° °°°o@##@o°°°°o@#@#°°°°°O@##@*°°° °      
      ° °°°o###@o°°°°o####*°°°°O@##@*°°° °      
      ° °°°o@##@o°°°°o@@@@*°°°°O@##@*°°° °      
       o°°°°#@##o°°°°*oooo°°°°°O##@O°°°°o       
       ° °°°*O@@o°°°°°°°°°°°°°°O@#o°°°° o       
        o  °°°*#o°°°°°°°°°°°°°°OO*°°°           
         °  o°°°*°°°°°°°°°°°°°°°°°°  oo         
           *   °°°°°°°°°°°°°°°°°°   °           
             *°  °°°°°°°°°°°°°°  ..             
               °°   °°°°°°°°   °°               
                  .*   °°   ..                  
                    o°.  °°o   
    ''')
    os.system('python tools/msfbuider.py')
def upgrade():
    os.system('clear')
    print('INSTALL TOOLS')
    print('''
    FIRST NECESSITY TOOL
    
    [00] Nano
    [01] Sudo
    [02] Python
    [03] Git
    [04] Curl''')
    print('''
    [1] Nmap
    [2] Metasploit
    [3] Osintgram
    [4] Phoneinfoga
    [5] Sherlock
    [6] Whois''')
    install=input(Fore.LIGHTYELLOW_EX+"Select > ")
    if install=='1':
        os.system('sudo apt install nmap && sudo pacman -S nmap')
    elif install=='6':
        os.system('sudo apt install whois && sudo pacman -S whois')
    elif install=='5':
        os.system('git clone https://github.com/sherlock-project/sherlock.git && cd sherlock/sherlock && python3 -m pip install -r requirements.txt')
    elif install=='2':
        os.system('''curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall && \
      rm msfinstall''')
    elif install=='3':
        os.system('git clone https://github.com/Datalux/Osintgram.git ')
        os.system('cd Osintgram && pip install -r requirements.txt && pip3 install -r requirements.txt')
        os.system('clear')
        print('enter your username and password to use the Instagram account (necessary to use the tool)')
        print('info: https://github.com/Datalux/Osintgram')
        input(Fore.BLUE+'Press Enter to continue')
        os.system('nano Osintgram/config/credentials.ini')
    elif install=='00':
        os.system('sudo apt install nano && sudo pacman -S nano')
    elif install=='01':
        os.system('apt install sudo && pacman -S sudo')
    elif install=='02':
        os.system('sudo apt install python python3 python2 python-pip python3-pip python-is-python3 && sudo pacman -S python python3 python2 python-pip python3-pip python-is-python3')
    elif install=='03':
        os.system('sudo apt install git && sudo pacman -S git')
    elif install=='04':
        os.system('sudo apt install curl && sudo pacman -S curl')
def osint():
    os.system('clear')
    print(Fore.YELLOW+'''
 
                                  
                              ██████░░░░░░░░░░░░░░░░██████                              
                            ██░░░░░░                ░░░░░░██          
                          ██░░                            ░░██                      
                        ██░░                                ░░██                        
                        ██    ██████                ██████    ██                        
                        ██  ░░░░░░░░████        ████░░░░░░░░  ██                        
                        ██          ░░████    ████░░          ██                        
                        ██            ░░░░    ░░░░            ██                        
                        ██░░  ░░██████░░░░    ░░░░██████░░  ░░██                        
                        ██░░░░██████████░░    ░░██████████░░░░██                        
                        ██░░  ░░░░░░░░  ░░    ░░  ░░░░░░░░  ░░██                        
                        ██              ░░    ░░              ██                        
                        ██  ░░░░░░      ░░    ░░      ░░░░░░  ██                        
                        ██  ░░░░░░    ░░        ░░    ░░░░░░  ██                        
                        ██░░          ░░        ░░          ░░██                        
                        ██░░░░██        ██░░░░██        ██░░░░██                        
                        ██░░  ██████░░████████████░░██████  ░░██                        
                        ██  ░░  ██████████    ██████████  ░░  ██                        
                          ██  ░░░░    ░░░░░░░░░░░░    ░░░░  ██                          
                          ██      ░░                ░░      ██                          
                            ██  ░░  ░░░░░░████░░░░░░  ░░  ██                            
                            ██░░  ░░      ████      ░░  ░░██                            
                              ██░░      ░░████░░      ░░██                              
                                ██░░    ░░████░░    ░░██                                
                                  ██░░░░  ████  ░░░░██                                  
                                    ████░░████░░████                                    
                                        ████████                                        

    [1] Osintgram
    [2] Phoneinfoga''')
    select=input(Fore.LIGHTYELLOW_EX+'Select > ')
    if select=='1':
        target=input(Fore.LIGHTYELLOW_EX+'Target > ')
        os.system('cd Osintgram && python3 main.py '+target )
    elif select=='2':
        phoneinfoga()
def config():
    os.system('clear')
    print('''CONFIG SETTINGS
    
    [1] Sudo
    [2] Osintgram''')
    select=input(Fore.LIGHTYELLOW_EX+'Select > ')
    if select=='1':
        print('How to do it: https://www.linuxfordevices.com/tutorials/linux/adding-users-to-sudoers')
        input(Fore.BLU+'Press Enter to continue')
        os.system('su && nano /etc/sudoers')
    elif select=='2':
        print('info: https://github.com/Datalux/Osintgram/blob/master/README.md#installation')
        input(Fore.BLU+'Press Enter to continue')
        os.system('nano Osintgram/config/credentials.ini')
def exploite():
    os.system('clear')
    print(Fore.LIGHTRED_EX+'''                 _
               /\)
              /\/
             /\/
           _/L/
          (/\_)
          /%/  
         /%/  
        /%/
       /%/
      /%/
     /%/
    /%/
   /%/
  /%/
 /%/ 
/,' 
"''')
    print('''
    [1] MSFVenom buider
    [99] Back''')
    select=input(Fore.LIGHTYELLOW_EX+'Select > ')
    if select=='1':
        msfbuider()
    elif select=='2':
        main()
def checkroot():
    os.system('clear')
    if os.geteuid()!=0:
        print(Fore.RED + 'You are not root user')
        quit()
def quitmain():
    os.system('clear')
    print(Fore.RED+'bye!')
checkroot()
os.system('clear')
print(Fore.WHITE+'''
                                         ╓╥╖
                                      ╓@▄██▀`  ,,
                                  ,g▄██▀`  ,╥▄██▀`
                              ,g▄██▀`  ,╓▄██▀▀  ,╓@██▀
                           ╓@███▀   ╓g▄██▀`  ╓g▄██▀`  ╓@█L
                             "╙▀█████▀`  ,g▄██▀"  ,g▄████L
                           @╥╖,  ╙▀███▄███▀▀  ,g▄████  ▒]L
                           `╙▀██▄╖   ╙▀██▄▄▄▄███▀ ╙░█  ║]L
                           ,   `╙▀██▄╖   ╙▀▀▀▀▀▓  ]░▓  ║]L
                           ╨▒██▄,  "╙▀██▄, ,,║▄█  ]░▓  ║]L
                              ╙▀███▄,  ╙▀▀███▀"  ,á▄█  ║]L
                           ║@▄╖,  ╙▀██▄▄,    ,╓▄██▀"  ,▒▄L
                            `╙▀██▄╖   ╙▀██████▀▀   ╓@███▀
                                `╙▀██▄,   ╙"`  ╓g▄██▀`
                                    ╙╙▀██▄,╓g▄██▀`
                                        ╙▀▀█▀''')
time.sleep(0.10)
print('''
    [1] Scanning
    [2] Exploitation
    [3] OSINT
    [4] Information gathering
    [77] Install tools
    [55] Config
    [99] Exit''')
select=input(Fore.LIGHTYELLOW_EX+'Select > ')
if select=='1':
    scanner()
elif select=='2':
    exploite()
elif select=='3':
    osint()
elif select=='4':
    ig()
elif select=='99':
    quitmain()
elif select=='77':
    upgrade()
elif select=='55':
    config()
else:
    time.sleep(1.6)
    print(Fore.RED+'Error')
    main()
