#!/usr/loca/bin/python
from __future__ import print_function
import yagmail
import psutil

def get_os_configure():
    cpu_count=psutil.cpu_count()
    mem_size=psutil.virtual_memory().total
    disk_mount_info=[mount[0:2] for mount in  [ mountpoint for mountpoint in psutil.disk_partitions()]]
    disk_percent={}
    for point in disk_mount_info:
        disk_percent[str(point[1])]=psutil.disk_usage(str(point[1]))

    
    network_info={net:str(psutil.net_if_addrs()[net][0]).split(',')[1:3]  for net in psutil.net_if_addrs().keys()}
    with open('/tmp/contents.txt','w') as f:
        print('cpu_count is:{0},mem_size is:{1},disk_mount_info is:{2},disk_percent is:{3},netowork_info is:{4}'.format(cpu_count,mem_size,disk_mount_info,disk_percent,network_info),file=f)

def send_mail():
    get_os_configure()
    yag=yagmail.SMTP(user='601290552@qq.com',password='leoxu8703@123',host='smtp.qq.com',port='25') 
    yag.send(to='xujing020@deppon.com',subject="your os configure information",contents="this is your os congiure",attachments='/tmp/contents.txt')



if __name__=="__main__": 
   send_mail() 
   
