import os
import output_generator
import instruction_generator
import json

def genLlamaDataFormat(output_data, instructionlist):
    llamaDataList = []
    for instruction in instructionlist:
        llamaData = {}
        llamaData['instruction'] = instruction
        llamaData['input'] = ""
        llamaData['output'] = json.dumps(output_data)
        
        llamaDataList.append(llamaData);

    return llamaDataList

if __name__ == '__main__':
    llama_data = []
    for i in range(100):
        output_data = output_generator.genOutput()
        instructionList = instruction_generator.genInstructionList(output_data)
        llama_data.extend(genLlamaDataFormat(output_data, instructionList))

        # print(instructionList)

    # print(output_data)

    jsonString = json.dumps(llama_data)
    with open("sample.json", "w") as outfile:
        outfile.write(jsonString)
    
    # print(llama_data)
    print(len(llama_data))
    
    