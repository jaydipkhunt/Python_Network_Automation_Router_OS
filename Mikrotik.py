import paramiko
import datetime
user = 'admin'
secret = 'admin'
port = 22
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
# define variables
time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
infilepath = "C:\\Users\\jaydi\\Desktop\\Python\\Cisco\\"
outfilepath = "C:\\Users\\jaydi\\Desktop\\Python\\Cisco\\"
devicelist = "device-list1.txt"
 
# open device file
input_file = open( infilepath + devicelist, "r")
iplist = input_file.readlines()
input_file.close()
 
# loop through device list and execute commands
for ip in iplist:
    ipaddr = ip.strip()
    ssh.connect(hostname=ipaddr, username=user, password=secret, port=port)
    stdin, stdout, stderr = ssh.exec_command('export')
    list = stdout.readlines()
    outfile = open(outfilepath + ipaddr + "_" + time_now, "w")
    for char in list:
        outfile.write(char)
    ssh.close()
    outfile.close()