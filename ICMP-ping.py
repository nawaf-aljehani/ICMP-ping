import subprocess

host = "172.217.18."                                    #put full ip host

for num in range(197,204):                              #if you know the host delet this line
    new_host = host + str(num)                          #if you know the host delet this line

result = subprocess.call(['ping','-c','2',new_host])    #if you know the host change new_host to host
if result == 0:
    print(f"the host {new_host} is running")
else:
    print(f"the host {new_host} is not running")
