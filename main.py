import csv
import json
import ipaddress
import os
#from flask import Flask, jsonify,request
#convert to JSON string
#jsonStr = json.dumps(laptop1.__dict__)

####################
###### CLASS #######
####################

class Machine:
  def __init__(self, nom,cpu,ip,ram,ops):
    self.nom= nom
    self.cpu= cpu
    self.ip = ip
    self.ram= ram
    self.ops = ops
   
# Changement de la variable os par ops (operating system) car conflit avec class os
# Pb de compatibilité version python
	#print("Column names are",", ".join(row))
    #print(f'Column names are {", ".join(row)}')

class Hdd:
    hdd_nb = 1
    hdd_size = 1

    def __init__(self,hdd_nb, hdd_size):
       self.hdd_nb = hdd_nb
       self.hdd_nb = hdd_size


def readAllv2():
 
    with open('machines.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        str_machine =""
        for row in csv_reader:
            #if line_count != 0:
            m1 = Machine(row[0],row[1],row[2],row[3],row[4])
            str_machine =  str_machine + json.dumps(m1.__dict__)
            line_count += 1
    return str_machine


def readByName(hostname):
    with open('machines.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        strReturn=""
        for row in csv_reader:
            if row[0] == hostname:
#               print(f'\t hostname={row[0]}  nombre CPU={row[1]}  ip={row[2]}  Ram={row[3]}Mo  NB_Disk={row[4]}  Taille_Disk={row[5]}Go  OS={getOsById(row[6])}')
                print(f'\t hostname={row[0]}  nombre CPU={row[1]}  ip={row[2]}  Ram={row[3]}Mo  OS={getOsById(row[4])}')
#               # Lecture des HDD
                ListHddByHost(hostname)      
#               print(f'\t hostname={row[0]}  nombre CPU={row[1]}  ip={row[2]}  Ram={row[3]}Mo  NB_Disk={row[4]} OS={getOsById(row[6])}')
#                m1 = Machine(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
#                print('the row found is '+strReturn)
                line_count += 1
#               Ajouter l'echec de la recherche d'hote
#               si host non trouver, relancer le menu 1
#                return True 

    if line_count == 0:
#        print ("Hostname NOT FOUND")
        return True
    return True

def create(machine):
    with open('machines.csv', mode='a',newline='') as new_host:
            machine_add = csv.writer(new_host, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            machine_add.writerow([machine.nom,machine.cpu,machine.ip,machine.ram,machine.ops])
            #addHddByName(machine.nom)
            addHddByName(hostname)

    #addHddByName(machine)
    
    return ''
    
def createOrUpdate(machine):
    if find(machine.nom) >= 0:
        delete(machine.nom)
    create(machine)
    addHddByName(hostname)
#addHddByName(hostname)
    return ''

def find(hostname):
    with open('machines.csv', 'rt') as f:
         reader = csv.reader(f, delimiter=',')
         line_count = -1
         line_found = -1
         for row in reader:
                line_count +=1
                if hostname == row[0]: # if the username shall be on column 3 (-> index 2)
#                  print ('existe dans la colon N°'+str(line_count))
                  line_found = line_count
#    print ('ligne trouver :'+str(line_found))
    return line_found

def delete(hostname):
    a_file = open("machines.csv", "r")
    lines = a_file.readlines()
    #print (lines)
    a_file.close()
    #supprimer ligne
    # Ajouter la ligne a supprimer
    print ("Le Host suivant sera supprime/modifie")
    readByName(hostname)
    # print suppression de [find(host)]
    deleteHddByName(hostname) 
    del lines[find(hostname)]
    new_file = open("machines.csv", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()
    return ''

def deleteHddByNameV2(hostname):
    hd_file = open("hdd.csv", "r")
    lines = hd_file.readlines()
    #a_file.close()
    print ("Les HDD suivants seront supprimes")
    ListHddByHost(hostname)
    # print suppression de [find(host)]

    for row in reader:
        if hostname != row['id']:
            writer.writerow(row) ; # write all non-matching rows
        else:
            print("Avatar Record Deleted") # nothing to write

    new_file.close()
    return ''
def deleteHddByName(hostname):
    hd_file = open("hdd.csv", "r")
    lines = hd_file.readlines()
    #print (lines)
    hd_file.close()
    #supprimer ligne
    # Ajouter la ligne a supprimer
    print ("suppression des HDD")
    # print suppression de [find(host)]
    del lines[find(hostname)]
    new_file = open("hdd.csv", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()
    return ''

def addHddByName(hostname):
#    hd_file = open("hdd.csv", "r")
#    lines = hd_file.readlines()
    #a_file.close()
    List_Machine_HDD = [hostname]
    #print (List_Machine_HDD)

    count = 1
    more_disk = True
    while more_disk == True :
        boucle = (count)
        print("disque numero : %s" %(boucle))      
        #print("HDD numero " %(count))
        # Si entreé egal vide fin liste HD a saisir
        hdd_size = input("Saisir la taille du disque dur(en Go):")    
        print ("Entrée Vide pour finir la saisie des HDD :")
        print (type(hdd_size))
        print (hdd_size)
        
        if (hdd_size == '' or hdd_size ==0 or hdd_size =='0'):
            print ("dans la boucle fin hdd ?")
            print (hdd_size)
            print ("Alors on sort ?")
            more_disk = False
            print ("alors ? More disk a saisir ?")
            print (more_disk)
        
        elif (int(hdd_size) > 1) : 
#            List_Machine_HDD.append(hdd_size)
#            print (line)
             List_Machine_HDD.append(hdd_size)

    # Faire un liste LigneHDD = Hostname,<TailleHD>,+ajouter element HD N
    # Supprimer les caracteres en trop dans la liste les " et ' 
        count += 1
    # sortie de la boucle de creation de HDD

    print ("la nouvelle ligne dans HDD.csv")
    print (List_Machine_HDD)
    
    with open('hdd.csv', mode='a',newline='') as new_host_hdd:
    #        hdd_add = csv.writer(new_host_hdd, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            hdd_add = csv.writer(new_host_hdd, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            hdd_add.writerow(List_Machine_HDD)
       
    
def addHddByName2(hostname):
    hd_file = open("hdd.csv", "r")
    lines = hd_file.readlines()
    print ("Ajout de HDD a un hostname")
    ListHddByHost(hostname)
#
#   Faire la procedure d'ajout
#

def getOsById(id):
    OS_Libel = ""

    with open('OS_version.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if int(row[0]) == int(id):
                OS_Libel = row[1]+" "+row[2]
    if len(OS_Libel) == 0:
        OS_Libel = "OS Non Disponible"    
    return OS_Libel


class OPS_version:
      def __init__(self, id,ops,version):
        self.id= id
        self.ops= ops
        self.version = version

def readOS():
        #file = open('OS_Version.txt')
        #lines = file.readlines()
        #print (file)
        with open("OS_Version.txt", "r") as file:
            print(file.read()) 
            file.close()

def readLineOS(ops):
        #file = open('OS_Version.txt')
        #lines = file.readlines()
        #print (file)
        with open("OS_Version.txt", "r") as file:
            line=file.readlines()[ops]
            print(line) 
            file.close()
   
def ListHddByHost(hostname):
            with open("hdd.csv", 'r') as csv_file2:
                csv_reader2 = csv.reader(csv_file2, delimiter=',')
                for row2 in csv_reader2 :
#                   Equivalant a if hostname in row2:
                    if row2[0] == hostname:
            #                print (('{:<15}  {:<15}  {:<20}'.row2))
                          
                            print(("Liste des HDD de la machine"))
 #                           print(('{:<8} {:<10}(Go){:<15}(Go){:<20}(Go)'.format(*row2)))
                            print('         {:<8}(Go){:<8}(Go){:<8}(Go){:<8}'.format(*row2))
                            print ("")
                            print ("\n") 
                	#print({row2[0]} {row2[1]}Go')
                return True

#########################
#### INTERACTIVE ########
#########################
hdd_nb = int(1)
#addHddByName(machine,hdd_nb)
while True :
        
    print ("Ce program permet de gérer les hosts")
    print ("FORMAT : nom, cpu, ip, ram, hdd, os/version")
    print (" ")
    print ("Tapez votre choix")
    print ("1:Consulter , 2:ajouter , 3:supprimer, 4:modifier 5:Lister ")
    action = input("")

    if action == "1":
        #        os.system('cls')
        # print ("\n" * 100) pour foctionnement Universel 
        hostname = True
        while not(hostname == "") :
            hostname = input("Merci de saisir le hostname a afficher [Entrer vide pour revenir au menu]:")
            search = bool(readByName(hostname))
            #readByName(hostname)
            #ListHddByHost(hostname)
            # PREVOIR UNE SORTIE de la boucle Consulter
    elif action=="2":
        #        os.system('cls')
        # print ("\n" * 100) pour foctionnement Universel 
        print("Saisir les information de la machine a ajouter")
        hostname = input("Saisir nom du hote:")
    #  TEST la validite IP   
    #   Boucle try exept pour validation de l'adresse IP
        while True:
            try:
                ip = input("Saisir l'adresse IP du hote:")
                ipaddress.ip_address(ip)
    #             x = int(input("Please enter a number: "))
                break
            except ValueError:
                print("Oops! Adresse IP Invalide. Merci de saisir une IP Valide ")

        #cpu = input("Saisir le nombre de CPU du hote:")
        #ram = input("Saisir la taille RAM du hote(en Mo):")
        cpu = int(4)
        ram = int(4096)
        hdd_nb = int(3)
        print (hdd_nb)
        #hdd_size = int(input("Saisir la taille disque dur du hote (en Go):"))
        hdd_size =int(1000)
        #print("Saisir lOS et la version de la machine a ajouter choix de 1 a 25")
        # AFFICHER LE CONTENU DU FICHIER OS_version.txt
        # Choisir l OS et la Version 
        readOS()
        #ops = input("Saisir la version OS :")
        ops = int(15)
        # convertir la valeur OS/version 1-25 en champs caracteres OS et Version
        # prendre la ligne saisie (1-25)
        # enregistrer le 7eme champs (OPS) avec les champs 2 et 3 de OS_Version
        #print (ops)
        ops = int(ops)
        print (ops)
        print (type(ops))
        
        machine = Machine(hostname,cpu,ip,ram,ops)
        createOrUpdate(machine)

    elif action=="3":
        #        os.system('cls')
        hostname = input("Merci de saisir le hostname a supprimer:")
        delete(hostname)
    elif action=="4":
        #        os.system('cls')  # on windows
        print("Saisir les information de la machine a modifier, s'il n'existe pas il va êtres créer")
        hostname = input("Saisir nom du hote:")
        print("****")
        cpu = input("Saisir le nombre de CPU du hote:")
        
    #   Boucle try exept pour validation de l'adresse IP
        while True:
            try:   
                ip = input("Saisir l'adresse IP du hote:")
                ipaddress.ip_address(ip)

    #             x = int(input("Please enter a number: "))
                break
            except ValueError:
                print("Oops! Adresse IP Invalide. ")
        ram = input("Saisir la taille RAM du hote:")
        readOS()
        ops = input("Saisir l'OS du hote:")
        # convertir la valeur OS/version 1-25 en champs caracteres OS et Version
        # prendre la ligne saisie (1-25)
        # enregistrer le 7eme champs (OPS) avec les champs 2 et 3 de OS_Version
        readLineOS(int(ops))
        
        # supprimer hdd_nb et hdd_size dansla creation machine
        machine = Machine(hostname,cpu,ip,ram,ops)
        createOrUpdate(machine)
        
    elif action=="5":
        print ("")
        print ("\n") 
 
        with open('machines.csv') as csv_file:
            print("Liste de tout les Hosts :")
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            str_machine =""
            for row in csv_reader:
            #   print (', '.join(row))        
            #   print('         {:<8}(Go){:<8}(Go){:<8}(Go){:<8} OS={getOsById(row[4])}'.format(*row))
            #   print(f'\t hostname={row[0]} nombre CPU={row[1]}  ip={row[2]}  Ram={row[3]}Mo  OS={getOsById(row[4])}')
                print(f'\t hostname={row[0]}  nb CPU={row[1]}  ip={row[2]}  Ram={row[3]}Mo  OS={getOsById(row[4])}')
                        
            print("****")
