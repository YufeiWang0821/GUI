#!/usr/bin/env python3

import os

import paramiko

# exec_command(cmd)
# 文件传输
class connect_ssh:

    def __init__(self):
        jumpbox_host_ip = "222.20.98.67"  # 跳板机
        ssh_user = "wangyufei"
        ssh_key_filename = 'C:/Users/JJ/.ssh/id_rsa'
        target_host_ip = '192.168.33.2'  # 目的服务器
        print(ssh_key_filename)

        print("connecting to the jump host")
        # 创建一个实例化
        jumpbox_ssh = paramiko.SSHClient()
        # 自动添加策略，保存远端主机的主机名和密钥信息，如果不添加，那么不在本地knows_hosts文件中记录的主机将无法连接，默认拒接
        jumpbox_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接跳板机
        jumpbox_ssh.connect(hostname=jumpbox_host_ip,port=5088, username=ssh_user, key_filename=ssh_key_filename)
        print("\n** connected jumpbox! **")

        print("\nopening a tunnel for connecting router host")
        # 创建一个中间连接的通道
        jumpbox_transport = jumpbox_ssh.get_transport()
        src_addr = (jumpbox_host_ip, 5088)
        dest_addr = (target_host_ip, 5011)
        jumpbox_channel = jumpbox_transport.open_channel(kind="direct-tcpip", dest_addr=dest_addr, src_addr=src_addr, )
        print("\n** opened a tunnel! **")

        print("\nconnecting a router host")
        # 去连接远端服务器
        target_ssh = paramiko.SSHClient()
        target_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        target_ssh.connect(hostname=target_host_ip,port=5011, username=ssh_user, key_filename=ssh_key_filename,
                              sock=jumpbox_channel)
        print("\n** connected to the destination host! **")
		# 创建一个SFTP客户端通道
        trans = target_ssh.get_transport()
        sftp = paramiko.SFTPClient.from_transport(trans)
        print(sftp)

        self.target_ssh = target_ssh
        self.sftp = sftp
    
    def execute(self, cmd):    
        stdin, stdout, stderr = self.target_ssh.exec_command(cmd)
        print(stdout.read())
        return stdout.read()
  

    def close(self, cmd):    
        self.target_ssh.close()
        self.jumpbox_ssh.close()
        self.sftp.close()
        print("Closed!")


if __name__ == '__main__':
    server = connect_ssh()
    #server.execute("pwd\n")
    
    print("done")

