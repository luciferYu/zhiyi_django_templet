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
- ansible-playbook -i hosts common.yml 
- ansible-playbook -i hosts py-server.yml 
- ansible-playbook -i hosts  toa.yml
- vim /boot/grub/grub.conf  
  default=0 #modify this to 2.6.32  
  timeout=5  
  splashimage=(hd0,0)/grub/splash.xpm.gz  
  hiddenmenu  
  title CentOS (2.6.32)  
        root (hd0,0)  
        kernel /vmlinuz-2.6.32 ro root=UUID=eda6c32f-5659-43e2-be25-5f0dff7542c7 rd_NO_LUKS rd_NO_LVM LANG=en_US.UTF-8 rd_NO_MD SYSFONT=latarcyrheb-sun16 crashkernel=auto  KEYBOARDTYPE=pc KEYTABLE=us rd_NO_DM rhgb quiet  
        initrd /initramfs-2.6.32.img  
  title CentOS 6 (2.6.32-754.el6.x86_64)  
        root (hd0,0)  
        kernel /vmlinuz-2.6.32-754.el6.x86_64 ro root=UUID=eda6c32f-5659-43e2-be25-5f0dff7542c7 rd_NO_LUKS rd_NO_LVM LANG=en_US.UTF-8 rd_NO_MD SYSFONT=latarcyrheb-sun16 crashkernel=auto  KEYBOARDTYPE=pc KEYTABLE=us rd_NO_DM rhgb quiet  
        initrd /initramfs-2.6.32-754.el6.x86_64.img  
- reboot  
- ansible-playbook -i hosts ngx-server.yml --extra-vars 'ngx_version=nginx_1.10.1'  



#django
- pip install -r requirements.txt
