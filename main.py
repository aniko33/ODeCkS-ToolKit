
import time
import os
import getpass
import colorama
from colorama import Fore, Back,Style
colorama.init(autoreset=True)
def phoneinfoga():
    os.system('clear')
    phonenumber=input('Phome number: ')
    os.system('cd tools && ./phoneinfoga scan -n '+phonenumber)
def slock():
    os.system('clear')
    target=input('Username: ')
    os.system('cd sherlock/sherlock && python3 sherlock.py '+target)
def whois():
    os.system('clear')
    target=input('Domain or IP: ')
    os.system('whois '+target)
def ig():
    os.system('clear')
    print('''
    [1] Whois
    [2] Sherlock''')
    select=input('Select: ')
    if select=='1':
        whois()
def scanner():
    os.system('clear')
    print('''
    [1] Nmap
    ''')
    scanner=input('Select: ')
    if scanner=='1':
        nmap()
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
    [4] Vuln script''')
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
    install=input("Select: ")
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
        print('wait...')
        time.sleep(5)
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

        #o°    #Oo****°°*°°°*****oO#    °o#         
       oo   #o**°°°°°°.°. °°°°°.°°°°°**o#   oo       
     *#  Oo*°°°°*°o°°o.**.oo°°oo*°°o.°°°°*oO  #*     
    o  Oo*°°°.*°*°**°°°.......°°°°°°oo°.°.°*oO  o    
  °@ oo*. .°o*°*..... °°*ooOo. ......*°°**°°.°oo @°  
 #  o*..°..°°°. .......°.*###o ........°*°.....*o  # 
##.o* °****°.......  ..°o#####°............*oo..*o.##
o o°.***o........ .**.°o##o*oOO° .   .......o°°*.°o o
 o* ***°........**oOOo**ooo**ooo*o***.......°****.*o 
°o.°*°°°....... *@@@@@@@@@#@@@@@@@@@* ...... *°*°°.o°
** °***........ *########@°###@#####* ........°**° **
o* **°°........ *@#@##oO*o.**OoO#@#@* ........***° *o
** *°**°....... *####Oo.... ..*oO###* ........*..o.*o
°o.°*.**....... *#OOo*°. .   .°*oOO#* ........°**°.o°
 o* °°°. ...... *@@@#Oo°°....°oO#@@@* ..........° *o 
o o° ...** .... °#####O#o#.Oo#O#####° .... *oo*. *o o
##.o* °OOO*. .. °@@@@@@@@@*#@@@@@@@@° .. .*oOO° *o.##
 #  o*.°oOOo°....*O#######@#######O*. ..*oOoo..*o  # 
  °@ oo°.°*oOo*°.  .......*......   .°*ooo*°.°oo @°  
    o  Oo°°°*ooOoo*°°..... ....°°*ooooo*°°°°oO  o    
     *#  #o*°°°°*oooOOoOoooooOOooOo**°°°°*o#  #*     
       oo   #o**°°°°°°********°°°°°°°**o#   oo       
         #o°    #Oo***°°°°°°°°****oO#    °o#  


    [1] Osintgram
    [2] Phoneinfoga''')
    select=input('Select: ')
    if select=='1':
        target=input('Target: ')
        os.system('cd Osintgram && python3 main.py '+target)
    elif select=='2':
        phoneinfoga()
def config():
    os.system('clear')
    print('''CONFIG SETTINGS
    
    [1] Sudo
    [2] Osintgram''')
    select=input('Select: ')
    if select=='1':
        print('How to do it: https://www.linuxfordevices.com/tutorials/linux/adding-users-to-sudoers')
        time.sleep(5)
        print('wait...')
        os.system('su && nano /etc/sudoers')
    elif select=='2':
        time.sleep(5)
        print('info: https://github.com/Datalux/Osintgram/blob/master/README.md#installation')
        print('wait...')
def exploite():
    os.system('clear')
    print('''
    

    
    ''')
    print('''
    [1] MSFVenom buider''')
    select=input('Select: ')
    if select=='1':
        msfbuider()
def checkroot():
    os.system('clear')
    if os.geteuid()!=0:
        print(Fore.RED + 'You are not root user')
        quit()
def quitmain():
    os.system('clear')
    print(Fore.RED+'bye!')
checkroot()
print('''
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
    [55] config
    [99] Exit''')
select=input('Select: ')
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
