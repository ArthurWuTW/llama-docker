import json

API_NAME = 'ACCESSORIES'

def genSerialNumber(jsonString):
    data = json.loads(jsonString)
    serialNr = data['SerialNumber'] 
    return "SN=" + serialNr

def genProject(jsonString):
    data = json.loads(jsonString)
    project = data['Project'] 
    return "Project=" + project

def genLastAssemblyAttributeList(jsonString):
    
    instructionlist = []

    data = json.loads(jsonString)
    collection = list(filter(lambda p: p['LastAssembly'] == 'LAST_ASSEMBLY', data['componentCollection']))
    # print(collection)
    for assembly in collection[0]['Assemblylist']:
        attribute = assembly['Attribute']
        value = assembly['Value']

        instructionlist.append('LastAssembly Assemblylist add Attrubute="' + attribute 
        + '" Value="' + value + '"')
    
    return instructionlist

def genLastAssemblyComponenetList(jsonString):
    instructionlist = []
    data = json.loads(jsonString)
    collection = list(filter(lambda p: p['LastAssembly'] == 'LAST_ASSEMBLY', data['componentCollection']))
    # print(collection)
    for component in collection[0]['ComponentList']:
        componentLoc = component['componentLoc']
        componentPart = component['componentPart']
        componentNumber = component['componentNumber']

        instructionlist.append('LastAssembly ComponentList add componentLoc="' + componentLoc 
        + '" componentPart="' + componentPart + '"' + ' componentNumber="' + componentNumber + '"')
    
    return instructionlist

def genAsas(jsonString):
    instructionlist = []
    data = json.loads(jsonString)
    collection = list(filter(lambda p: p['LastAssembly'] == 'LAST_ASSEMBLY', data['componentCollection']))
    for assembly in collection[0]['Asas']:
        attribute = assembly['Attribute']
        value = assembly['Value']

        instructionlist.append('LastAssembly Asas add Attrubute="' + attribute 
        + '" Value="' + value + '"')
    
    return instructionlist


def genInstructionList(data):
    jsonString = json.dumps(data)
    serialNumberInstruction = genSerialNumber(jsonString)
    projectInstruction = genProject(jsonString)
    candidateInstructions = []
    candidateInstructions.extend(genLastAssemblyAttributeList(jsonString))
    candidateInstructions.extend(genLastAssemblyComponenetList(jsonString))
    candidateInstructions.extend(genAsas(jsonString))
    

    # print(serialNumberInstruction)
    # print(candidateInstructions)
    
    instructions = []
    for candidate in candidateInstructions:
        instructions.append(
            'ApiName '+API_NAME+': '+serialNumberInstruction+', '
            + projectInstruction + ', '
            +candidate
        )
    

    return instructions