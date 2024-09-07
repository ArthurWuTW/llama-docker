import json
import uuid

REQ_PATTERN = '/edi/getDevice?SN='
ATTRIBUTE_LIST = ['Display', 'Keyboard', 'Housing', 'CPU', 'Fan', 'RAM', 'Disk', 'Touchpad', 'Battery', 'THEMAL', 'Motherboard', 'CASE']
PART_LIST = ['DEVICE', 'SAMPLE']
PART_NR_LIST_PREFIX = ['QWE', 'WER', 'VFS', 'ERE', 'GGG', 'VDS', 'QWE', 'QQQ', 'GFD', 'IOP']



def generateDataDict(serialNr):
    data = {}
    
    data['SerialNumber'] = serialNr
    data['PartNumber'] = generatePartNr()
    data['Attributes'] = []
    for attr in ATTRIBUTE_LIST:
        attr_data = {}
        attr_data['ComponentPart'] = attr
        attr_data['SerialNumber'] = generateRandomWord(12)
        attr_data['REGION'] = 'TW'
        attr_data['FORMAT'] = 'UTF8'
        data['Attributes'].append(attr_data)
        
    data['PART'] = []    
    for part in PART_LIST:
        part_data = {}
        part_data['Part'] = part
        part_data['NS'] = generateRandomWord(12)
        data['PART'].append(part_data)
    
    return data


def generateRandomWord(num):
    randomString = uuid.uuid4().hex.upper()
    return randomString[:num]
    
def generatePartNr():
    randomString = uuid.uuid4().hex.upper()
    return randomString[:3] + '-' + randomString[4:9]

def getLlamaDataFormat(responseBody, serialNr):
    llamaData = {}
    llamaData['instruction'] = REQ_PATTERN + serialNr
    llamaData['input'] = ""
    llamaData['output'] = json.dumps(responseBody)
    return llamaData


if __name__ == "__main__":
    generate_data = []
    for i in range(1000):
        serialNr = generateRandomWord(12)
        responseBody = generateDataDict(serialNr)
        generate_data.append(getLlamaDataFormat(responseBody, serialNr))
    generate_data = generate_data + generate_data
    jsonString = json.dumps(generate_data)
    with open("sample.json", "w") as outfile:
        outfile.write(jsonString)

    # # Create a nested dictionary
    # person = {
    #     "name": "John Doe",
    #     "age": 30,
    #     "address": {
    #         "street": "123 Main St",
    #         "city": "Anytown",
    #         "state": "CA"
    #     }
    # }

    # # Convert person dictionary to JSON
    # json_string = json.dumps(person)  
    # print(json_string)
    # data = {"instruction": json_string}
    # print(data)
    # data_string = json.dumps(data) 
    # print(data_string)

