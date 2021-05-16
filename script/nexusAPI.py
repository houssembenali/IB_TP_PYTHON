

import requests




res = requests.get('http://192.168.1.144:8081/service/rest/v1/assets?repository=nexus-tpp')

print ("Voici la liste des version de l'application Gestion Park Informatique existante sur Nexus :")
print res