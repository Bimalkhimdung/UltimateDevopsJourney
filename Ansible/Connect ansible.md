
## How you can connect two servers with the help of ansible

1. Lunch two EC2 instances one is the main server and another one is the target server and store the new key pairs in a local directory.
![luching to instances](/Ansible/image/create_Instances.png)

2. Connect both servers from your terminal with command
    - ***ssh -i { Location of key pair } ubuntu@pulic ip address***
    ![connceting from terminal](/Ansible/image/1.png)
    ![connected in both terminal ](/Ansible/image/connceted%20in%20both.png)
    
    > ***in case of permission is denied then use***
    > 
    - ***chmod 600 { location of key pair }***
    - ***ssh -i { location of keypair } ubuntu@public ip address***

3. Generate key in both servers with command
    - ***ssh-keygen***
    ![generate key](/Ansible/image/8%20keygen.png)

4. check for the generated key with the command
    - ***ls /home/ubuntu/.ssh/***
    ![check key](/Ansible/image/9.check%20key%20gen.png)

5. Open the Public of the main server with the command
    - *********cat /home/ubuntu/.ssh/id_rsa.pub*********
    ![open key](/Ansible/image/10%20pulic%20key.png)

6. Copy the public key of the main server to authorize key of the target server.
    - ***vim /home/ubuntu/.ssh/authorize_keys***
    ***Enter esc+ i  for insert and esc + shift : wq !  for save and exit***
    ![copy key](/Ansible/image/12%20vim%20open.png)

7. ssh target server through main server
- ***ssh private ip add.***
![ssh target server](/Ansible/image/13%20ssh%20to%20target.png)