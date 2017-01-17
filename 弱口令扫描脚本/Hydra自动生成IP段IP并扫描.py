#coding=utf-8  
#Hydra自动生成IP段IP并扫描
import os,re
def Hydra():
    protocol=raw_input("enter a kind of protocol:")
    password=raw_input("请输入密码，空为默认路径（当前目录下password文件）")
    username=raw_input("请输入用户名，空为默认路径（当前目录下users文件）")
    if len(protocol)==0:
        protocol=" asterisk"
    if len(password)==0:
        password=" -P password"
    if len(username)==0:
        username=" -L users" 
    cmd="hydra -M ip"+username+password+' '+protocol+" -t 20 "+" -o report"
    if len((os.popen("whereis hydra")).read())<=8:
    	version=(os.popen("cat /etc/issue")).read()
    	if len(re.findall("Debian|Ubuntu|Xandros|Linspire",version))!=0:
    		os.system("apt-get install hydra")
    		print len(re.findall("Debian|Ubuntu|Xandros|Linspire",version))
    	elif len(re.findall("Fedora|CentOS|Red Hat|Enterprise|Linux|OpenSUSE|Mandriva|PCLinuxOS",version))!=0:
    		os.system("yum install hydra")
    	else :
    		print "*********Unkown Linux System,please install hydra by yourself********"
    		exit(1)
    else :
    	os.system(cmd)
    	print "scan has finished ,report has been created"

def creatRanIP(case):
	if case==0:
		strIP=""
		for i in range(193,255):
			for j in range(0,255):
				for k in range(0,255):
					for l in range(1,255):
						strIP=strIP+str(i)+'.'+str(j)+'.'+str(k)+'.'+str(l)+'\n'
		fp=open("ip",'w')
		fp.write(strIP)
		fp.close()
	if case==2:
		strtemp=raw_input("input the first two Byte of IP:")
		strIP=""
		for k in range(0,255):
			for l in range(1,255):
				strIP=strIP+strtemp+'.'+str(k)+'.'+str(l)+'\n'
		fp=open("ip",'w')
		fp.write(strIP)
		fp.close()
	if case==1:
		strtemp=raw_input("input the first Byte of IP:")
	        strIP=""
		for j in range(0,255):
		    for k in range(0,255):
			for l in range(1,255):
			    strIP=strIP+strtemp+'.'+str(j)+'.'+str(k)+'.'+str(l)+'\n'
		fp=open("ip",'w')
		fp.write(strIP)
		fp.close()
	if case==3:
                strIP=""
		strtemp=raw_input("input the first three Byte of IP:")
		for l in range(1,255):
                    strIP=strIP+strtemp+'.'+str(l)+'\n'
		fp=open("ip",'w')
		fp.write(strIP)
		fp.close()
	if case==4:
		RanIPstr=raw_input("please enter the IP:")
		fp=open("ip",'w')
		fp.write(RanIPstr)
		fp.close()

if os.geteuid() != 0:
    print "This program must be run as root. Aborting."
    exit(1)
'''
case=raw_input("enter the size of IP:")
case=int(case)
while not (case>=0 and case<=4):
	case=raw_input("Input error,please try again:")
	case=int(case)
creatRanIP(case)
'''
Hydra()
