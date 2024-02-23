import json
with open("C:/Users/ASUS/Desktop/python projects/pythonUni/lab4/jsonpython/sample-data.json", "r") as my_file:
    jsonstring = my_file.read()
data = json.loads(jsonstring)
interfaces = data.get('imdata', [])
print("Interface status")
print("="*80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" *50, "-"*20, "-" * 8, "-" * 6)

for i in interfaces:
    phys = i.get('l1PhysIf', {})
    at = phys.get('attributes', {})
    dn = at.get('dn', '')
    descr = at.get('descr', '')
    speed = at.get('speed', 'inherit')
    mtu = at.get('mtu', '')
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, descr, speed, mtu))
    
    
       