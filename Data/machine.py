####################
###### CLASS #######
####################
class Machine:
  def __init__(self, nom,ip,cpu,ram,hdd_nb,hdd_size,os):
    self.nom= nom
    self.ip = ip
    self.cpu= cpu
    self.ram= ram
    self.hdd_nb= hdd_nb
    self.hdd_size= hdd_size
    self.os = os
   
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
#                print(f'\t hostname={row[0]},nombre CPU={row[1]},ip={row[2]},RAM={row[3]},HardDisk={row[4]},OS={row[5]} ')
# test KS insertion du nb de disque et affichage en GO
                print(f'\t hostname={row[0]},nombre CPU={row[1]},ip={row[2]},RAM={row[3]},NB_Disk={row[4]},Taille_Disk={row[5]}Go,OS={row[6]} ')
                m1 = Machine(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                print('the row found is '+strReturn)
                line_count += 1

    if line_count == 0:
        print ("Hostname NOT FOUND")        
    return m1

def create(machine):
    with open('machines.txt', mode='a',newline='') as new_host:
            machine_add = csv.writer(new_host, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            machine_add.writerow([machine.nom,machine.cpu,machine.ip,machine.ram,machine.hdd_nb,machine.hdd_size,machine.os])
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
                  print ('existe dans la colon N°'+str(line_count))
                  line_found = line_count
    print ('ligne trouver :'+str(line_found))
    return line_found

def delete(host):
    a_file = open("machines.txt", "r")
    lines = a_file.readlines()
    a_file.close()
    #supprimer ligne
    del lines[find(host)]
    #réecrir fichier apres suppression ligne
    new_file = open("machines.txt", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()
    return ''

