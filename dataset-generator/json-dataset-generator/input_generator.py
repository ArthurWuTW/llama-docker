import datetime
import random
import json
import uuid

model_list = ['GIBSON', 'FENDER', 'IBANEZ', 'CORT', 'MUSICMAN', 
    'FREEDOM', 'IMPULSE', 'SAVIOR', 'AKATSUKI', 'STRIKE', 'LEGEND', 
    'JUSTICE', 'BONJOVI', 'GREENDAY', 'SUM41', 'ACDC']

component_list = ['Display', 'Keyboard', 'Housing', 'CPU', 'Fan', 'RAM', 'Disk', 'Touchpad', 'Battery', 'THEMAL', 'Motherboard', 'CASE']
attribute_list = ['DAY', 'YEAR', 'MONTH', 'HOUR', 'VERSION', 'DATE']
asas_list = ['play', 'Key', 'Restart', 'Start']
another_componet_list = ['u1221', 'u1255', 'u7777', 'u8799', 'u9999', 'u1045', 'u6944']
ship_component_list = ['LASTASSEMBLY', 'UUU']

attribute_value_string_size_list = [2, 4, 8, 10]

def genRandomWord(num):
    randomString = uuid.uuid4().hex.upper()
    return randomString[:num]

def genTimeString():
    return datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

def genOutput():
    data = {}
    data['SerialNumber'] = genRandomWord(12)
    data['EventTime'] = genTimeString()
    data['ActionId'] = genRandomWord(8)
    data['Identifier'] = genRandomWord(7)
    data['Process'] = genRandomWord(6)
    data['Order'] = genRandomWord(10)
    model = random.choice(model_list)
    data['Project'] = model
    data['Product'] = model
    data['WorkDate'] = genTimeString()
    data['LifeCycle'] = genRandomWord(2)
    data['componentCollection'] = genComponenetCollection()

    return data

def genComponenetCollection():
    collection = []
    collection.append(genLastAssemblyCollection())
    collection.append(genAnotherCollection())
    collection.append(genShip())
    return collection

def genShip():
    collection = {}
    collection['LastAssembly'] = 'SHIP'
    collection['PartNr'] = generatePartNr()
    collection['SerialNumber'] = genRandomWord(12)
    collection['Assemblylist'] = genLastAssemblyList()
    collection['ComponentList'] = genComponentList(ship_component_list)
    collection['Asas'] = None

    return collection

def genAnotherCollection():
    collection = {}
    collection['LastAssembly'] = 'ANOTHER'
    collection['PartNr'] = generatePartNr()
    collection['SerialNumber'] = genRandomWord(12)
    collection['Assemblylist'] = genLastAssemblyList()
    collection['ComponentList'] = genComponentList(another_componet_list)
    collection['Asas'] = None
    
    return collection

def genLastAssemblyCollection():
    lastAssembly = {}
    lastAssembly['LastAssembly'] = 'LAST_ASSEMBLY'
    lastAssembly['PartNr'] = generatePartNr()
    lastAssembly['SerialNumber'] = genRandomWord(12)
    lastAssembly['Assemblylist'] = genLastAssemblyList()
    lastAssembly['ComponentList'] = genComponentList(component_list)
    lastAssembly['Asas'] = genAsas()

    return lastAssembly


def genAsas():
    asaslist = []
    for asas in asas_list:
        asas_data = {}
        asas_data['Attribute'] = asas
        asas_data['Value'] = genRandomWord(random.choice(attribute_value_string_size_list))
        asaslist.append(asas_data)
    
    return asaslist


def genLastAssemblyList():
    assemblyList = []
    for attr in component_list:
        attr_data = {}
        attr_data['Attribute'] = attr
        attr_data['Value'] = genRandomWord(random.choice(attribute_value_string_size_list))
        assemblyList.append(attr_data)
    
    return assemblyList

def genComponentList(components):
    componentList = []
    for component in components:
        com_data = {}
        com_data['componentLoc'] = component
        com_data['componentPart'] = generatePartNr()
        com_data['componentNumber'] = genRandomWord(23)
        com_data['venderPart'] = None
        com_data['useState'] = genRandomWord(3)
        com_data['writeOnly'] = False
        com_data['isDEE'] = False
        
        componentList.append(com_data)
    
    return componentList

def generatePartNr():
    randomString = uuid.uuid4().hex.upper()
    return randomString[:3] + '-' + randomString[4:9]




def hello():
    print("333")