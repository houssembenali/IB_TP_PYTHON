#!/usr/bin/env bash

sudo apt update

##jouter les hostnames
echo 192.168.0.14 jenkins >> /etc/hosts
echo 192.168.0.24 gradle >> /etc/hosts
echo 192.168.0.44 nexus >> /etc/hosts

sudo apt install -y openjdk-11-jdk 
sudo apt install -y unzip

## Récupération de la dernière version


VERSION=7.0
wget https://services.gradle.org/distributions/gradle-${VERSION}-bin.zip -P /tmp

unzip -d /opt/gradle /tmp/gradle-${VERSION}-bin.zip

# Faire pointer le lien vers la dernière version de gradle

ln -s /opt/gradle/gradle-${VERSION} /opt/gradle/latest

# Ajout de gradle au PATH

touch /etc/profile.d/gradle.sh

echo "export PATH=/opt/gradle/latest/bin:${PATH}" > /etc/profile.d/gradle.sh

chmod +x /etc/profile.d/gradle.sh

source /etc/profile.d/gradle.sh

## Ajout de PHP pour l'exemple : 

sudo apt install php php-mbstring php-dom