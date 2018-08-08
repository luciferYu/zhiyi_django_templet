#!/data/exec/python/bin/python3
# -*- coding:utf-8 -*-
# auth Yuzhiyi
import paramiko
import os
import logging

logger = logging.getLogger(__name__)


class LinuxShell(object):
    def __init__(self, host_ip, username='root', ssh_key='id_rsa'):  # 指定 用户名 和 登录的 ssh key
        '''设置主机连接'''
        self.host_ip = host_ip
        self.username = username
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # print(self.host_ip,self.username)
        paramiko.util.log_to_file('/data/log/mydjango/ssh.log')
        self.ssh = paramiko.SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.privatekey = os.path.join(self.BASE_DIR, 'sshkey', ssh_key)  # 指定key的位置
        self.key = paramiko.RSAKey.from_private_key_file(self.privatekey)
        self.result_code = None

    def __del__(self):
        self.ssh.close()

    def __str__(self):
        return str(self.host_ip, self.username)

    def conn(self):
        self.ssh.connect(hostname=self.host_ip, username=self.username, pkey=self.key, timeout=5)

    def run_cmd(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd, get_pty=True)
        if not stderr.read():
            self.result_code = 'ok'
            # print(stdout.read().decode('utf-8'))
            return stdout.read().decode('utf-8').strip()
        else:
            # todo add log
            self.result_code = 'failed'
            return stderr.read().decode('utf-8').strip()


if __name__ == '__main__':
    kshell = LinuxShell('127.0.0.1')
    kshell.conn()
    result = kshell.run_cmd('uptime')
    print(result, kshell.result_code)
