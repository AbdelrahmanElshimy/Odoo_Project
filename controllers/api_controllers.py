import xmlrpc.client

url = 'http://localhost:8069'
db = 'db12'
username = 'admin'
password = 'admin'

# Create an XML-RPC client to connect to the Odoo instance
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
print("details...", version)

# Authenticate and retrieve the user's UID (user ID)
uid = common.authenticate(db, username, password, {})

# models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
partners_ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['customer', '=', True]]] , {'offset': 10, 'limit': 10})
print("partners...", partners_ids)


partners_rec = models.execute_kw(db, uid, password, 'res.partner', 'read', [partners_ids], {'fields':['id', 'name']})
print("partners_rec...", partners_rec)

new_contact = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "odoo test", 'mobile': "1234", 'website': "test"}])
print ("Newly created ID is", new_contact)