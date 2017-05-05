#!/usr/local/bin/python
import socket
from pexpect import pxssh
import  paramiko
import time
from threading import Thread

def write_passwd(host,username,password,port):
    log_file='/tmp/password.txt'
    with open(log_file,'a') as file:
        file.write('host:%s,username:%s,password:%s,port:%s\n'%(host,username,password,port))

def write_log(host,username,curren_pwd,new_pwd):
    log_file='/tmp/changepasswd.log'
    with open(log_file,'a') as file:
        file.write('host:%s,username:%s,current_password:%s,new_password:%s\n'%(host,username,curren_pwd,new_pwd))


def trypassword(host,port,username,pwd_dict):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    global new_pwd
    for pwd in pwd_dict:
        try:
            client.connect(host,port,username=username, password=pwd)  
            write_passwd(host,username,pwd,port)  
            print "ip: %s using port: %s is login success,password is %s" % (host,port,pwd)   
            print(changepassword(host,username,client,pwd,new_pwd))
            break
        except Exception,e:
            print "host: %s login has no pass" %(host)
            print (e)



def getpassword(host,port,username,pwd_dict):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    result=sk.connect_ex((host,14816))
    print result
    if not result:
        trypassword(host,14816,username,pwd_dict)
    elif (result == 11):
        noconnect.write("host:%s is not connect\n" % (host))
        print  "host:%s is not connect" % (host)
    else:
        trypassword(host,22,username,pwd_dict)     

def changepassword(host,username,client,curren_pwd,new_pwd):
    print('begin change password')
    interact=client.invoke_shell()

    interact.send('passwd'+'\n')
    time.sleep(1)
    print (interact.recv(65535))
    interact.send(curren_pwd+'\n')
    time.sleep(1)
    print (interact.recv(65535))
    interact.send(new_pwd+'\n')
    time.sleep(1)
    print (interact.recv(65535))
    interact.send(new_pwd+'\n')
    time.sleep(1)
    result=interact.recv(65535).split('\r\n')[-2]
    print (result)
    if result=='passwd: all authentication tokens updated successfully.':
        write_log(host,username,curren_pwd,new_pwd)
        print('change password is successful')
    interact.shutdown(2)


def run_thread(func,many_thread,args):
    threads=[]
    for i in range(many_thread):
        thread=Thread(target=func,args=args)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join() 

if __name__ == '__main__':
    username='oracle'
    port=14816
    client = paramiko.SSHClient()  
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
    #client.connect('192.168.8.248', 22, username='root', password='password', timeout=4)  
    start=time.time()
    with open('/tmp/hosts.txt') as hosts,open('/tmp/notconnect.txt','a') as noconnect:
        threads=[]
        for host in hosts:
            host=host.strip('\n\r')
            print "begin to get password from host:%s" %(host)
            #run_thread(getpassword,,args=(host,port,username,pwd_dict))
            #getpassword(host,port,username,pwd_dict)
            thread=Thread(target=getpassword,args=(host,port,username,pwd_dict))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
    client.close()
    end=time.time()
    print('Finished change password is %.3f seconds'%(end - start))
