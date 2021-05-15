####################
###### CLASS #######
####################
class Machine:
  def __init__(self, nom, ip,cpu,ram,hdd,os):
    self.nom= nom
    self.ip = ip
    self.cpu= cpu
    self.ram= ram
    self.hdd= hdd
    self.os = os

####################################################
#########       CRUD     ###########################
####################################################
    
def readAll():
    with open('machines.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t hostname={row[0]}, ip={row[1]}, nombre CPU={row[2]}, RAM={row[3]}, HardDisk={row[4]}, OS={row[5]} ')
                line_count += 1
    print(f'Processed {line_count} lines.')
    return line_count


def readAllv2():
    
    with open('machines.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        str_machine =""
        for row in csv_reader:
            #if line_count != 0:
            m1 = Machine(row[0],row[1],row[2],row[3],row[4],row[5])
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
                print(f'\t hostname={row[0]}, ip={row[1]}, nombre CPU={row[2]}, RAM={row[3]}, HardDisk={row[4]}, OS={row[5]} ')
                m1 = Machine(row[0],row[1],row[2],row[3],row[4],row[5])
                print('the row found is '+strReturn)
                line_count += 1
    if line_count == 0:
        print ("Hostname NOT FOUND")      
    return m1


def create(machine):
    with open('machines.txt', mode='a',newline='') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer.writerow([machine.nom, machine.ip, machine.cpu,machine.ram,machine.hdd,machine.os])
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

"""

#################################
######## test unitair ###########
#################################
class TestStringMethods(unittest.TestCase):

    def test_readAll(self):

        file = open("machines.txt","r")
        Counter = 0
        # Reading from file
        Content = file.read()
        CoList = Content.split("\n")
        
        for i in CoList:
            if i:
                Counter += 1
        file.close()
        self.assertEqual(readAll(), Counter)
        

if __name__ == '__main__':
    unittest.main()
    
"""


#############################
########### API #############
#############################
app = Flask(__name__)

@app.route("/machine",methods=["GET"])
def getAllAPI():
  return readAllv2()

@app.route("/machine/<hostname>", methods=["GET"])
def getByIdAPI(hostname):
    print('hostname ======' +hostname)
    m1 =readByName(hostname)
    return json.dumps(m1.__dict__)

@app.route('/machine/addorupdate', methods=['POST'])
def createAPI():
   data = request.get_json()
   nom= data.get('nom', '')
   ip= data.get('ip', '')
   cpu= data.get('cpu', '')
   ram= data.get('ram', '')
   hdd= data.get('hdd', '')
   os= data.get('os', '')
   m1 = Machine(nom,ip,cpu,ram,hdd,os)
   createOrUpdate(m1)
   return "Creation de l'hote "+nom+" est enregistrer avec succée !!"

@app.route('/machine/del/<host>', methods=['DELETE'])
def deleteApi(host):
  delete(host)
  return "le host "+host+" est supprimer avec succée !!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')


"""
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
    readByName(hostname)
elif action=="2":
    print("Saisir les information de la machine a ajouter")
    hostname = input("Saisir nom du hote:")
    ip = input("Saisir l'adresse IP du hote:")
    cpu = input("Saisir le nombre de CPU du hote:")
    ram = input("Saisir la taille RAM du hote:")
    hdd = input("Saisir la taille disque dur du hote:")
    os = input("Saisir l'OS du hote:")
    machine = Machine(hostname, cpu,ip,ram,hdd,os)
    createOrUpdate(machine)

    
elif action=="3":
    hostname = input("Merci de saisir le hostname a supprimer:")
    delete(hostname)
else:
    print("Saisir les information de la machine a modifier, s'il n'existe pas il va êtres créer")
    hostname = input("Saisir nom du hote:")
    readByName(hostname)
    print("****")
    ip = input("Saisir l'adresse IP du hote:")
    cpu = input("Saisir le nombre de CPU du hote:")
    ram = input("Saisir la taille RAM du hote:")
    hdd = input("Saisir la taille disque dur du hote:")
    os = input("Saisir l'OS du hote:")
    machine = Machine(hostname, cpu,ip,ram,hdd,os)
    createOrUpdate(machine)
"""
####### tester CRUD #######
#m1 = Machine("host1", "ababababa","8","256","500","Ubuntu")
#createOrUpdate(m1)
#create(m1)
#delete("host2")
#find("host2")


