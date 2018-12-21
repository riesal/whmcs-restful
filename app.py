from flask import Flask, request, jsonify, json
from pywhmcs7 import invoke
import logging as log
import os

app = Flask(__name__)
app.config.from_object(__name__)

# cloud foundry ibm bluemix virtual port
port = int(os.getenv('VCAP_APP_PORT', 8080))

app.config.update(dict(
    WHMCS_URL = "https://your-website.com/includes/api.php",
    API_USER = "apiuser",
    API_PASS = "apipassword",
    ACCESS_KEY = "apiaccess",
    RESPONSE_TYPE = "json" # do not change. just JSON supported.
))
application = app

@app.route("/")
def hello():
    return "Welcome to your-website.com"

@app.route("/invoice/", methods=["GET"])
def invoices():
    return i("getinvoices", {})

@app.route("/ticket/", methods=["GET"])
def tickets():
    return i("gettickets", {})

@app.route("/domainregister/", methods=["GET"])
def domain_register():
    return i("domainregister", {})

@app.route("/domaingetlockingstatus/", methods=["GET"])
def domain_getlocking_status():
    return i("domaingetlockingstatus", {})

@app.route("/domaingetnameservers/", methods=["GET"])
def domain_getnameservers():
    return i("domaingetnameservers", {})

@app.route("/domaingetwhoisinfo/", methods=["GET"])
def domain_getwhoisinfo():
    return i("domaingetwhoisinfo", {})

@app.route("/domainrelease/", methods=["GET"])
def domain_release():
    return i("domainrelease", {})

@app.route("/domainrenew/", methods=["GET"])
def domain_renew():
    return i("domainrenew", {})

@app.route("/domainrequestepp/", methods=["GET"])
def domain_requestepp():
    return i("domainrequestepp", {})

@app.route("/domaintoggleidprotect/", methods=["GET"])
def domain_toggleidprotect():
    return i("domaintoggleidprotect", {})

@app.route("/domaintransfer/", methods=["GET"])
def domain_transfer():
    return i("domaintransfer", {})

@app.route("/domainupdatelockingstatus/", methods=["GET"])
def domain_updatelocking_status():
    return i("domainupdatelockingstatus", {})

@app.route("/domainupdatenameservers/", methods=["GET"])
def domain_updatenameservers():
    return i("domainupdatenameservers", {})

@app.route("/domainupdatewhoisinfo/", methods=["GET"])
def domain_updatewhoisinfo():
    return i("domainupdatewhoisinfo", {})

@app.route("/domainwhois/", methods=["GET"])
def domain_whois():
    return i("domainwhois", {})

@app.route("/domainwhois/<string:domain>/", methods=["GET"])
def domainwhois(domain):
    return i("DomainWhois", {'domain': domain, 'stats':True})

@app.route("/encryptpassword/", methods=["GET"])
def encrypt_password():
    return i("encryptpassword", {})

@app.route("/endtasktimer/", methods=["GET"])
def endtasktimer():
    return i("endtasktimer", {})

@app.route("/fraudorder/", methods=["GET"])
def fraudorder():
    return i("fraudorder", {})

@app.route("/geninvoices/", methods=["GET"])
def generate_invoices():
    return i("geninvoices", {})

@app.route("/getactivitylog/", methods=["GET"])
def get_activitylog():
    return i("getactivitylog", {})

@app.route("/getadmindetails/", methods=["GET"])
def get_admindetails():
    return i("getadmindetails", {})

@app.route("/getaffiliate/", methods=["GET"])
def get_affiliate():
    return i("getaffiliate", {})

@app.route("/order/",methods=["GET"])
def order_list():
    return i("getorder", {})

@app.route("/stats/", methods=["GET"])
def stats_list():
    return i("getstats", {})

@app.route("/product/", methods=["GET"])
def products():
    return i("GetProducts", {'productid': 1})

@app.route("/product/pid/<int:pid>/", methods=["GET"])
def productpid(pid):
    return i("GetProducts", {'pid': pid, 'stats': True})

@app.route("/product/gid/<int:gid>/", methods=["GET"])
def productgid(gid):
    return i("GetProducts", {'gid': gid})

@app.route("/client/", methods=["GET"])
def clients():
    return i("getclients", {})

@app.route("/client/<int:clientid>/",
           methods=["GET", "POST", "PUT", "DELETE", "HEAD"])
def client(clientid):
    if request.method == 'GET':
        app.logger.debug("ClientId: %d" % clientid)
        return i("getclientsdetails", {'clientid': clientid, 'stats': True})
    elif request.method == 'POST':
        app.logger.debug(request.form)
        data_dict = {}
        for data in request.form.items():
            data_dict.update({data[0]: data[1]})
        return i("addclient", data_dict)
    elif request.method == 'PUT':
        app.logger.debug(request.form)
        data_dict = {'clientid': clientid}
        for data in request.form.items():
            data_dict.update({data[0]: data[1]})
        return i("updateclient", data_dict)
    elif request.method == 'DELETE':
        app.logger.debug("ClientId: %d" % clientid)
        return i("deleteclient", {'clientid': clientid})

def i(action, params):
    return jsonify(json.loads(invoke(app.config["WHMCS_URL"],
                              app.config["API_USER"],
                              app.config["API_PASS"],
                              app.config["ACCESS_KEY"],
                              action,
                              app.config["RESPONSE_TYPE"],
                              params)[1]))


def main():
    app.run(host='0.0.0.0',port=port,debug=True)

if __name__ == "__main__":
    main()
