import paramiko

host_name = '10.122.23.135'
u_name ='smell'
p_word = '8Aug19'
port_no = 22

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host_name, username=u_name, password=p_word, port=port_no)
except paramiko.AuthenticationException:
    print("Authentication failed, please verify your credentials")


## Create FTP object to copy file from local to remote and remote to local
ftp = ssh.open_sftp()

## Copy file from remote machine to local machine
rsrc = '/home/smellamp/srikumar.py'
ldst = r'C:\Users\smellamp\Desktop\DU_TELEF\srikumar.py'

ftp.get(rsrc, ldst)

## Copy file from local machine to remote machine
lsrc = r'C:\Users\smellamp\Desktop\DU_TELEF\sss.txt'
rdst = '/home/smellamp/sss.txt'

ftp.put(lsrc, rdst)

# close ftp and ssh connections
ftp.close()
ssh.close()