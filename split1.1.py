import machine
import csv
import json
#from flask import Flask, jsonify,request
#convert to JSON string
#jsonStr = json.dumps(laptop1.__dict__)

#########################
#### INTERACTIVE ########
#########################

print ("Ce program permet de gérer les hosts")
print ("FORMAT : nom, ip, cpu, ram, nb hdd,taille hdd, os")
print ("Tapez votre choix")
print ("1:afficher , 2:ajouter , 3:supprimer, 4:modifier")
action = input("")

if action == "1":
    hostname = input("Merci de saisir le hostname a afficher:")
    machine.readByName(hostname)
elif action=="2":
    print("Saisir les information de la machine a ajouter")
    hostname = input("Saisir nom du hote:")
    ip = input("Saisir l'adresse IP du hote:")
    cpu = input("Saisir le nombre de CPU du hote:")
    ram = input("Saisir la taille RAM du hote(en Mo):")
    hdd_nb = input("Saisir le nb de disque dur du hote:")
    hdd_size = input("Saisir la taille disque dur du hote (en Go):")
    os = input("Saisir l'OS du hote:")
    machine = Machine(hostname,cpu,ip,ram,hdd_nb,hdd_size,os)
    createOrUpdate(machine)

elif action=="3":
    hostname = input("Merci de saisir le hostname a supprimer:")
    machine.delete(hostname)
else:
    print("Saisir les information de la machine a modifier, s'il n'existe pas il va êtres créer")
    hostname = input("Saisir nom du hote:")
    readByName(hostname)
    print("****")
    ip = input("Saisir l'adresse IP du hote:")
    cpu = input("Saisir le nombre de CPU du hote:")
    ram = input("Saisir la taille RAM du hote:")
    hdd_nb = input("Saisir le nb de disque dur du hote:")
    hdd_size = input("Saisir la taille des disques du hote:")
    os = input("Saisir l'OS du hote:")
    machine = Machine(hostname,cpu,ip,ram,hdd_nb,hdd_size,os)
    createOrUpdate(machine)
