from flask import Flask, jsonify,request
import crudmachine
#from flask_apscheduler import APScheduler
#############################
########### API #############
#############################
app = Flask(__name__)

@app.route("/machine",methods=["GET"])
def getAllAPI():
  return crudmachine.readAllv2()

@app.route("/machine/<hostname>", methods=["GET"])
def getByIdAPI(hostname):
    print('hostname ======' +hostname)
    m1 =crudmachine.readByName(hostname)
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
   m1 = crudmachine.Machine(nom,ip,cpu,ram,hdd,os)
   crudmachine.createOrUpdate(m1)
   return "Creation de l'hote "+nom+" est enregistrer avec succée !!"

@app.route('/machine/del/<host>', methods=['DELETE'])
def deleteApi(host):
  crudmachine.delete(host)
  return "le host "+host+" est supprimer avec succée !!"

def hi():
  print ("app launched...")
  if __name__ == "__main__":
    app.run(host='0.0.0.0')
  #scheduler = APScheduler()
  #scheduler.init_app(app)
  #scheduler.start()
  #app.run(host='0.0.0.0')
    
hi()
