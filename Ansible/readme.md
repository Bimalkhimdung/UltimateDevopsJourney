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