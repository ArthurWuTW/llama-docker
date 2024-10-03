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
    
    output_data = output_generator.genOutput()
    instructionList = instruction_generator.genInstructionList(output_data)
    llama_data.extend(genLlamaDataFormat(output_data, instructionList))
    
    # print(output_data)
    print(llama_data)

    
    