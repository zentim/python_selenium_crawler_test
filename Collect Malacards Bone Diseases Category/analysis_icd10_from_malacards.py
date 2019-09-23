import os
import json

# read json files
malacards_arr = []
path = os.getcwd() + '/Collect Malacards Bone Diseases Category/malacards_bone_diseases_category/'
for filename in os.listdir(path):

    with open(path + filename, 'r') as reader:
        jf = json.loads(reader.read())
        malacards_arr += jf

# filter has ICD10's malacard
malacards_has_ICD10_arr = list(filter(lambda obj: len(obj['ICD10']) != 0, malacards_arr))

print(len(malacards_has_ICD10_arr))

# # output json
# filename = "malacards_has_ICD10.json"
# fo = open(filename, "w")
# encodedjson = json.dumps(malacards_has_ICD10_arr)
# print('Output: ' + filename)
# fo.write(encodedjson)
# fo.close()

# collect ICD10
ICD10_list = []
ICD10_list_XXX = []
for obj in malacards_has_ICD10_arr:
    ICD10_list += obj['ICD10']
    # ICD10_list += map(lambda x: x[:3], obj['ICD10'])

print(len(ICD10_list))

# remove repeat ICD code
ICD10_list = list(set(ICD10_list))
ICD10_list.sort()
print(ICD10_list)
print(len(ICD10_list))
