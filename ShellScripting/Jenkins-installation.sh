#!bin/bash

#Author @Bimal_Rai
#Please Cheackout my website  [ raibimal.com.np ]

sudo apt update

#Installing Java

echo " installing Java "

sudo apt install openjdk-11-jre

java --version

curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
  
echo "Installing jenkins..."
sudo apt-get install jenkins
 jenkins --version
