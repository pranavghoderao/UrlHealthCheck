import paramiko
import os
import requests

class util():

    def connect(self,ip,uname):
        p= paramiko.SSHClient()
        p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #ip= "192.168.147.10"
        #uname= "vagrant"
        try:
            p.connect(ip,port=22,username=uname,key_filename='C:\\Users\\pghoderao\\Downloads\\key\\private_key_open_ssh')
        except:
            print("[!] Cannot connect to the SSH Server")
            exit()

        return p

    def checkTomcat(self,p):
        print("inside Tomcat..")
        #cmd = "ps -ef | grep salt-minion | grep -v 'grep salt-minion' "
        cmd = "ps -ef | grep tomcat | grep -v 'grep tomcat' "
        try:
            stdin,stdout,stderr=p.exec_command(cmd)
            op=stdout.readlines()
            op=" ".join(op)
            print(op)
            if not op:
                result = "UP"
            else:
                result = "DOWN"
        except Exception as e:
            result = "Something wrong happend"

        return result
    
    def status(self,u):
        url = u
        r = requests.get(url,verify=False)
        code = r.status_code
        print(code)
        if code == 200 :
            status ='UP'
        else :
            status ='Down'

        return status
