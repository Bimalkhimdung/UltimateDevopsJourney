
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