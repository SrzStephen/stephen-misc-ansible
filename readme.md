# Ansible
![travis ci badge](https://travis-ci.com/SrzStephen/stephen-misc-ansible.svg?branch=master)

This repo is basically just somewhere for me to throw ansible playbooks and scripts that I've made.

I'm expecting this to expand as I start automating some of the things I find myself doing.

Each of these scripts should be considered WIP and not prod ready -> I generally get them to the point where I'm happy 
with them but have made no attempt to deal with errors/environments that I don't control.

## Provides
### install_cuda_10.1
``` 
ansible-playbook playbooks/install_cuda_10.1.yml
```
Installing Tensorflow + CUDA + CUDANN on linux can be [a pain](https://www.youtube.com/watch?v=_36yNWw_07g).

This playbook automates the installation of this, since at the time 
[my usual favourite way of installing cuda](https://support.system76.com/articles/cuda/) wasn't playing nice with my 
system.

Expects hosts to be defined in your inventory with a group```cuda_ml```, eg:
```yml
cuda_ml:
  hosts:
    my_cool_host:
      ansible_host: 192.168.0.x
```
Playbook was tested on Ubuntu Server 20.04 with a Nvidia 2070 GPU and will install everything needed for 
```tensorflow==2.3.0``` and validate that you install works properly with the GPU.

### Setup
Nvidia does not provide the CUDNN libraries in an easy distribute way. You will need to download them from 
[Nvidias Developer Program](https://developer.nvidia.com/rdp/cudnn-download).

You will need to get the following files and move them to /roles/static/
```
libcudnn7-dev_7.6.5.32-1+cuda10.1_amd64.deb
libcudnn7_7.6.5.32-1+cuda10.1_amd64.deb
cudnn-10.1-linux-x64-v7.6.5.32.tgz
```


#### Improvements:
Ways that this can be improved:
1. Split out some of the things (filepaths etc) into vars similar to 
[this](https://github.com/djx339/ansible-role-cudnn/blob/master/vars/main.yml) to allow version combinations.
2. register installation actions and use that to figure out the restart
3. Use variables everywhere I've defined static things.

#### Things I learnt making this
1. Ansible doesn't run ~/.bashrc or ~/.profile so it doesn't get any environment variables you've exported there.
2. /etc/profile can't deal with bash variables, and breaking PATH means you have to refer to things by their full path
 to try to fix it eg ```/bin/sudo /bin/vi /etc/environment```.
3. Ansibles [unarchive](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/unarchive_module.html) 
makes copying directories to the remote host unnecessary.


