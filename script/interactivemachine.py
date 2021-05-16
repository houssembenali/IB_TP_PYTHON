import crudmachine
import objectsmachine

#########################
#### INTERACTIVE ########
#########################

print ("Ce program permet de gérer les hosts")
print ("FORMAT : nom, ip, cpu, ram, hdd, os")
print ("Tapez votre choix")
print ("1:afficher , 2:ajouter , 3:supprimer, 4:modifier")
action = input("")

if action == "1":
    hostname = input("Merci de saisir le hostname a afficher:")
    crudmachine.readByName(hostname)
elif action=="2":
    print("Saisir les information de la machine a ajouter")
    hostname = input("Saisir nom du hote:")
    ip = input("Saisir l'adresse IP du hote:")
    cpu = input("Saisir le nombre de CPU du hote:")
    ram = input("Saisir la taille RAM du hote:")
    hdd = input("Saisir la taille disque dur du hote:")
    os = input("Saisir l'OS du hote:")
    machine = objectsmachine.Machine(hostname, cpu,ip,ram,hdd,os)
    crudmachine.createOrUpdate(machine)

    
elif action=="3":
    hostname = input("Merci de saisir le hostname a supprimer:")
    crudmachine.delete(hostname)
else:
    print("Saisir les information de la machine a modifier, s'il n'existe pas il va êtres créer")
    hostname = input("Saisir nom du hote:")
    crudmachine.readByName(hostname)
    print("****")
    ip = input("Saisir l'adresse IP du hote:")
    cpu = input("Saisir le nombre de CPU du hote:")
    ram = input("Saisir la taille RAM du hote:")
    hdd = input("Saisir la taille disque dur du hote:")
    os = input("Saisir l'OS du hote:")
    machine = objectsmachine.Machine(hostname, cpu,ip,ram,hdd,os)
    crudmachine.createOrUpdate(machine)