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

print("\nNumber of diseases with ICD10 code: " + str(len(malacards_has_ICD10_arr)))


##############################################

# collect symptom one hot encoding list
symptom_one_hot_encoding_list = []
dataset = malacards_has_ICD10_arr[:5]
for obj in dataset:
    symptom_one_hot_encoding_list += obj['sign_or_symptoms']
    symptom_one_hot_encoding_list += obj['HOP_symptoms']

print('Before remove repeat symptom: ' + str(len(symptom_one_hot_encoding_list)))
symptom_one_hot_encoding_list = list(set(symptom_one_hot_encoding_list))  # remove repeat symptom
print('After remove repeat symptom: ' + str(len(symptom_one_hot_encoding_list)))
print(symptom_one_hot_encoding_list)

for obj in dataset:
    let obj_one_hot_list = []
    for symptom in symptom_one_hot_encoding_list:
        if ()



# ###############################################

# # # output json
# # filename = "malacards_has_ICD10.json"
# # fo = open(filename, "w")
# # encodedjson = json.dumps(malacards_has_ICD10_arr)
# # print('Output: ' + filename)
# # fo.write(encodedjson)
# # fo.close()

# # collect ICD10 (XXX.XX)
# ICD10_list = []
# for obj in malacards_has_ICD10_arr:
#     ICD10_list += obj['ICD10'] # ICD10 code's fomat is XXX.XX

# print("\nNumber of ICD10 code : " + str(len(ICD10_list)))

# # remove repeat ICD code
# ICD10_list = list(set(ICD10_list))
# ICD10_list.sort()
# # print(ICD10_list)
# print("\nNumber of no repeat ICD10 code (XXX.XX) : " + str(len(ICD10_list)))


# # collect ICD10 (XXX)
# ICD10_list = []
# for obj in malacards_has_ICD10_arr:
#     ICD10_list += map(lambda x: x[:3], obj['ICD10']) # ICD10 code's fomat is XXX

# # print("\nNumber of ICD10 code : " + str(len(ICD10_list)) + "\n")

# # remove repeat ICD code
# ICD10_list = list(set(ICD10_list))
# ICD10_list.sort()
# print("\nNumber of no repeat ICD10 code (XXX) : " + str(len(ICD10_list)))
# print(ICD10_list)