#!bin/bash

#Author @Bimal Rai , raibimal.com.np



set -x



#installing Jenkins 

sudo apt update
#installing Java 
sudp apt install openjdk-11-jre

java --version

#jenkins installing
curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
  
sudo apt-get update
echo " Installing Jenkins "
sudo apt-get install jenkins

echo " Installing jenkins password "

sudo cat /var/lib/jenkins/secrets/initialAdminPassword

jenkins --version

