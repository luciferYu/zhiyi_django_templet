# 建立一个django的模板

- 操作系统版本
[root@localhost ~]# cat /etc/*release*
CentOS release 6.10 (Final)


- 安装epel ansible git
yum -y install epel-release libselinux-python  git zlib*
yum -y install ansible
//yum -y install mock
//useradd -s /sbin/nologin mockbuild

[root@localhost ~]# ansible --version
ansible 2.5.5
[root@localhost ~]# git version
git version 1.7.1

- mkdir -p /data/web
- mkdir -p /data/exec
- cd /data/web/
- git clone https://github.com/luciferYu/zhiyi_django_templet.git
- ssh-keygen -t rsa 
- cp ~/.ssh/id_rsa.pub ~/.ssh/authorized_keys
