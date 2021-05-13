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
  def __init__(self, nom,cpu,ip,ram,hdd_nb,hdd_size,ops):
    self.nom= nom
    self.cpu= cpu
    self.ip = ip
    self.ram= ram
    self.hdd_nb= hdd_nb
    self.hdd_size= hdd_size
    self.ops = ops
   
# Changement de la variable os par ops (operating system) car conflit avec class os
# Pb de compatibilité version python
# Houssem - peux tu regarder les lignes print(f') ce n'est plus compatible depuis python 3.5 
# ligne 26 et 50  
# Because f in front of strings (f-strings) are only for versions above python 3.5
	#print("Column names are",", ".join(row))
    #print(f'Column names are {", ".join(row)}')

def readAllv2():
    
    with open('machines.txt') as csv_file:
#        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        str_machine =""
        for row in csv_reader:
            #if line_count != 0:
            m1 = Machine(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            str_machine =  str_machine + json.dumps(m1.__dict__)
            line_count += 1
    return str_machine


def readByName(hostname):
    with open('machines.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        strReturn=""
        for row in csv_reader:
            if row[0] == hostname:
#                print(f'\t hostname={row[0]},nombre CPU={row[1]},ip={row[2]},RAM={row[3]},NB_Disk={row[4]},Taille_Disk={row[5]}Go,OS={row[6]} ')
                print(f'\t hostname={row[0]}  nombre CPU={row[1]}  ip={row[2]}  Ram={row[3]}Mo  NB_Disk={row[4]}  Taille_Disk={row[5]}Go  OS={getOsById(row[6])}')
#                m1 = Machine(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
#                print('the row found is '+strReturn)
                line_count += 1
#               Ajouter l'echec de la recherche d'hote
#               si host non trouver, relancer le menu 1
                return True 

    if line_count == 0:
#        print ("Hostname NOT FOUND")
        return True
    return True

def create(machine):
    with open('machines.txt', mode='a',newline='') as new_host:
            machine_add = csv.writer(new_host, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            machine_add.writerow([machine.nom,machine.cpu,machine.ip,machine.ram,machine.hdd_nb,machine.hdd_size,machine.ops])
    return ''
    
def createOrUpdate(machine):
    if find(machine.nom) >= 0:
        delete(machine.nom)
    create(machine)
    return ''

def find(host):
    with open('machines.txt', 'rt') as f:
         reader = csv.reader(f, delimiter=',')
         line_count = -1
         line_found = -1
         for row in reader:
                line_count +=1
                if host == row[0]: # if the username shall be on column 3 (-> index 2)
#                  print ('existe dans la colon N°'+str(line_count))
                  line_found = line_count
#    print ('ligne trouver :'+str(line_found))
    return line_found

def delete(host):
    a_file = open("machines.txt", "r")
    lines = a_file.readlines()
    #print (lines)
    a_file.close()
    
    #supprimer ligne
    # Ajouter la ligne a supprimer
    print ("Le Host suivant sera supprime/modifie")
    readByName(host)
    # print suppression de [find(host)] 
    del lines[find(host)]
    #ajouter un test si le host n'exite pas
    #réecrir fichier apres suppression ligne
    new_file = open("machines.txt", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()
    return ''

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

def doublon(host):
# fonction extraction premiere valuer du fichier machine (hostname)
# Lit la première ligne du fichier (entête de colonnes)
# pour avancer jusqu'à la ligne 2
#    datafile.readline()
    datafile = open('machines.txt', 'r')
    
    while True:
        # Lecture d'une nouvelle ligne dans le fichier
    #    with open('machines.txt') as csv_file:
        line = datafile.readline()
    # Si la ligne est vide, la fin du fichier a été atteinte
        if line == '':
            break
    # Extraction des cellules de la ligne courante
        value = line.split(',')
      # Affichage de la cellule dans la 3ème colonne 
# Comparaision de la valeur lu en 1er colonne avec la nouvelle valeur host
# si existe alors doublon
        exist=(value[0])
        if exist == host:
            return -1
        else : 
            return 0
    datafile.close()


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
   
#########################
#### INTERACTIVE ########
#########################
while True :
        
    print ("Ce program permet de gérer les hosts")
    print ("FORMAT : nom, cpu, ip, ram, hdd, os/version")
    print (" ")
    print ("Tapez votre choix")
    print ("1:afficher , 2:ajouter , 3:supprimer, 4:modifier")
    action = input("")

    if action == "1":
        #        os.system('cls')
        # print ("\n" * 100) pour foctionnement Universel 
        search = False
        while search == False :
           hostname = input("Merci de saisir le hostname a afficher:")
           search = bool(readByName(hostname))
           print ("resultat de la recheche")
           print (search) 
    elif action=="2":
        #        os.system('cls')
        # print ("\n" * 100) pour foctionnement Universel 
        print("Saisir les information de la machine a ajouter")
        hostname = input("Saisir nom du hote:")
    #    TEst doublon() a faire
    #    ip = input("Saisir l'adresse IP du hote:")
    # TEST la validite IP   
    #   Boucle try exept pour validation de l'adresse IP
        while True:
            try:
                ip = input("Saisir l'adresse IP du hote:")
                ipaddress.ip_address(ip)
    #             x = int(input("Please enter a number: "))
                break
            except ValueError:
                print("Oops! Adresse IP Invalide. Merci de saisir une IP Valide ")

        cpu = input("Saisir le nombre de CPU du hote:")
        ram = input("Saisir la taille RAM du hote(en Mo):")
        hdd_nb = input("Saisir le nb de disque dur du hote:")
        hdd_size = input("Saisir la taille disque dur du hote (en Go):")
        print("Saisir lOS et la version de la machine a ajouter choix de 1 a 25")
        # AFFICHER LE CONTENU DU FICHIER OS_version.txt
        # Choisir l OS et la Version 
        readOS()
        ops = input("Saisir la version OS :")
        # convertir la valeur OS/version 1-25 en champs caracteres OS et Version
        # prendre la ligne saisie (1-25)
        # enregistrer le 7eme champs (OPS) avec les champs 2 et 3 de OS_Version
        #print (ops)
        ops = int(ops)
        #print (type(ops))
        #ops_=readLineOS(ops)
    #    ops_=readLineOS(ops)[-2]
    #    ops_= ops+readLineOS(ops)[-1]
            
        machine = Machine(hostname,cpu,ip,ram,hdd_nb,hdd_size,ops)
        createOrUpdate(machine)

    elif action=="3":
        #        os.system('cls')
        hostname = input("Merci de saisir le hostname a supprimer:")
        delete(hostname)
    elif action=="4":
        #        os.system('cls')  # on windows
        print("Saisir les information de la machine a modifier, s'il n'existe pas il va êtres créer")
        hostname = input("Saisir nom du hote:")
        #       readByName(hostname)
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
        hdd_nb = input("Saisir le nb de disque dur du hote:")
        hdd_size = input("Saisir la taille des disques du hote:")
        readOS()
        ops = input("Saisir l'OS du hote:")
        # convertir la valeur OS/version 1-25 en champs caracteres OS et Version
        # prendre la ligne saisie (1-25)
        # enregistrer le 7eme champs (OPS) avec les champs 2 et 3 de OS_Version
        readLineOS(int(ops))
        
        machine = Machine(hostname,cpu,ip,ram,hdd_nb,hdd_size,ops)
        createOrUpdate(machine)