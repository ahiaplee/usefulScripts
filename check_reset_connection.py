""" Script to create batch file with commands to cut and convert music compilations into individual mp3s
"""

from subprocess import Popen, PIPE
import os
import time

def getFullCommand(connectionSpeedStr : str):
    router_login_addr = "youradminlogin@yourRouteIp"
    router_pw = "yourRoutePassword"
    cmd = f'"ethctl eth4 media-type {connectionSpeedStr}"'
    # print(f"plink -batch {router_login_addr} -pw {router_pw} {cmd}")
    return f"plink -batch {router_login_addr} -pw {router_pw} {cmd}"

def checkAndResetConnection():
    fast_speed = "1000FD"
    slow_speed = "100FD" #if you somehow want to make your connection bad lmao

    p0 = Popen(getFullCommand(""), stdout=PIPE, stderr=None, shell=True)
    printout =  p0.communicate()[0].decode("utf-8")
    if ("Link is Up at Speed: 1G" not in printout):
        print("Connection is bad, resetting...")
        p0 = Popen(getFullCommand(fast_speed))
        time.sleep(2.5) # requires some delay to query correctly
        p1 = Popen(getFullCommand(""))
        stdout, stderr = p1.communicate()
    else:
        print("Connection is ok \n", printout)

def queryNICSpeed(printQueryResults : bool):
    cmd = "wmic nic where netEnabled=true get name,speed"
    p0 = Popen(cmd, stdout=PIPE, stderr=None, shell=True)
    printout =  p0.communicate()[0].decode("utf-8")
    if printQueryResults:
        print(printout)
    # print(printout.split())
    speed = int(printout.split()[-1])
    # print(speed)
    if speed != 1000000000:
        #  print("connection bad")
         return False
    else:
        #  print("Connection is fine")
         return True
    
if __name__ == "__main__":
    print("Monitoring speed")
    queryNICSpeed(True)
    while(True):
        if not queryNICSpeed(False):
            print("connection bad!!!")
            # checkAndResetConnection()

        time.sleep(2.5)
