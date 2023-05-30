## Introduction to Ansible

Ansible is an open-source automation tool used for configuration management, application deployment, and task automation. It uses a simple YAML syntax to describe and execute tasks, making it easy to learn and use.

## Advantages of Ansible

- Simple to learn and use
- Agentless architecture, so no need to install software on managed hosts
- Uses YAML syntax which is easy to read and write
- Supports a wide range of operating systems and cloud providers
- Can be used for configuration management, application deployment, and task automation

## Ansible Architecture

Ansible uses a client-server architecture, where the server is called the control node and the clients are called managed nodes. The control node manages the managed nodes using SSH or WinRM, depending on the operating system.

## Ansible Modules

Ansible modules are pre-built scripts that Ansible uses to execute tasks on managed nodes. There are hundreds of modules available for various tasks, including file management, package management, user management, and more.

## Ansible Playbooks

Ansible playbooks are YAML files that describe a set of tasks to be executed on managed nodes. Playbooks make it easy to automate complex tasks and orchestrate multiple modules.

## Ansible Roles

Ansible roles are collections of tasks, files, templates, and variables that can be reused across multiple playbooks. Roles make it easy to organize and maintain complex infrastructure.

## Ansible Inventory

Ansible inventory is a file that lists the managed nodes and groups them based on various criteria, such as operating system, function, or location.

## 

## Ansible vs Other Configuration Management Tools

Ansible is often compared to other configuration management tools such as Puppet and Chef. The main difference is that Ansible uses a push-based model, while Puppet and Chef use a pull-based model. This makes Ansible simpler to set up and use, but may not be suitable for all use cases.

# How to install Ansible in aws server

- ***sudo apt update***
- ***sudo apt install ansible***

## How you can connect two servers with the help of ansible

1. Lunch two EC2 instances one is the main server and another one is the target server and store the new key pairs in a local directory.

2. Connect both servers from your terminal with command
    - ***ssh -i { Location of key pair } ubuntu@pulic ip address***
    
    > *in case of permission is denied then use*
    > 
    - ***chmod 600 { location of key pair }***
    - ***ssh -i { location of keypair } ubuntu@public ip address***

3. Generate key in both servers with command
    - ***ssh-keygen***

4. check for the generated key with the command
    - ***ls /home/ubuntu/.ssh/***

5. Open the Public of the main server with the command
    - *********cat /home/ubuntu/.ssh/id_rsa.pub*********
6. Copy the public key of the main server to authorize key of the target server.
    - ***vim /home/ubuntu/.ssh/authorize_keys***
    ***Enter esc+ i  for insert and esc + shift : wq !  for save and exit***

7. ssh target server through main server
- ***ssh private ip add.***