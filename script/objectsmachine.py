####################
###### CLASS #######
####################

class Machine:
  def __init__(self, nom, ip,cpu,ram,hdd,os):
    self.nom= nom
    self.ip = ip
    self.cpu= cpu
    self.ram= ram
    # nbr disque a ajouter ##TODO
    self.hdd= hdd
    self.os = os