import os
import json

# read json files
medicine_net_arr = []
path = os.getcwd() + '/MedicineNet_orthopedics/'

for filename in os.listdir(path):
    with open(path + filename, 'r') as reader:
        jf = json.loads(reader.read())
        # medicine_net_arr += jf
        for key in jf:
            obj = {}
            obj['disease'] = key
            obj['symptom'] = jf[key]
            medicine_net_arr.append(obj)

print('Number of diseases : ' + str(len(medicine_net_arr)))

# output dataset
filename = 'dataset/MedicineNet_orthopedics_dataset.json'
dataset = medicine_net_arr
fo = open(filename, 'w')
encodedjson = json.dumps(dataset)
print('Output: ' + filename)
fo.write(encodedjson)
fo.close()

# collect symptoms
medicine_net_symptom_list = []
for obj in medicine_net_arr:
    medicine_net_symptom_list += obj['symptom']

print('Number of symptom (before remove repeat) : ' + str(len(medicine_net_symptom_list)))

medicine_net_symptom_list = list(set(medicine_net_symptom_list))
print('Number of symptom (after remove repeat) : ' + str(len(medicine_net_symptom_list)))

# output symptom list
filename = 'dataset/medicine_net_symptom_list.json'
dataset = medicine_net_symptom_list
fo = open(filename, 'w')
encodedjson = json.dumps(dataset)
print('Output: ' + filename)
fo.write(encodedjson)
fo.close()
