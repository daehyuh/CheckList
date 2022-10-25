obj_list = ['person', 'bicycle', 'car', 'motorcycle', 'traffic light', 'bus', 'truck', 'sports ball', 'kite', 'bottle', 'toilet', 'tv', 'bird', 'cat', 'dog', 'microwave', 'sink', 'refrigerator', 'book', 'palette', 'rock', 'bollard', 'hat', 'grating', 'stroller', 'fence', 'raised spot', 'forklift', 'tent', 'mat', 'manhole', 'cup', 'firewood', 'boxes', 'PE tank', 'vacuum', 'tree', 'hanger', 'door', 'parking bump', 'pillar', 'rubber cone', 'air cleaner', 'frame', 'standing light', 'power strip', 'roll mat', 'container', 'deck', 'trashcan', 'stairs', 'guitar', 'mannequin', 'basketball stands', 'goalpost', 'arbor', 'mirror', 'balloon sign', 'trash heap', 'curtain', 'electricity control panel', 'tripod', 'tissue box', 'outdoor unit of air conditioner', 'kerb', 'rainwater pipe', 'bike rack', 'traffic signs', 'momument', 'booth', 'faucet', 'sculpture', 'window', 'fan', 'guardrail', 'telegraph pole', 'pothole', 'wheelchair', 'parasol', 'bowl', 'table', 'vase', 'bag', 'fire extinguisher', 'fire hydrant', 'stone', 'banner', 'cart', 'PE barrier', 'entry barrier', 'sign', 'chair', 'desk', 'bed', 'shelf', 'streetlight']

re_merge_list = []
re_new_list = []

merge_list = ["stop sign -> sign",
"bench -> chair",
"backpack -> bag",
"umbrella -> parasol",
"handbag -> bag",
"suitcase -> bag",
"couch -> bed",
"potted plant -> vase",
"dining table -> table",
"handcart -> cart",
"window seat -> chair",
"bookshelf -> shelf",
"plastic bag -> bag",
"fire truck -> truck",
"busstop sign -> sign",
"cart rack -> cart",
"hand cart -> cart",
"stone flat bench -> stone",
"stone handrail -> stone"]

merge_A = [x.split("->")[-1].lstrip() for x in merge_list]
merge_B = [x.split("->")[0].rstrip() for x in merge_list]

print(merge_A)
print(merge_B)

for idx in range(len(merge_A)):
    re_merge_list.append(merge_B[idx]+" -> "+merge_A[idx])
    if merge_A[idx] == merge_B[idx]:
        print(merge_A[idx], merge_B[idx])

new_list = ["tuck -> truck",
"sculp -> sculpture",
"arbo -> arbor",
"pe barrier -> PE barrier",
"sculpt -> sculpture",
"trashcon ->trashcan",
"talbe -> table",
"bycicle -> bicycle",
"stone barrier -> stone",
"desk -> table",
"seat -> chair",
"umbrella -> parasol",
"potted plant -> vase",
"flat bench -> chair",
"backpack -> bag",
"phone booth -> booth",
"hand cart -> cart",
"handcart -> cart",
"cart rack -> cart",
"stone flat bench -> stone",
"stop sign -> sign",
"suitcase -> bag",
"window seat -> chair",
"couch -> bed",
"plastic bag -> bag",
"handbag -> bag",
"shopping bag -> bag"]

new_A = [x.split("->")[-1].lstrip() for x in new_list]
new_B = [x.split("->")[0].rstrip() for x in new_list]

print(new_A)
print(new_B)

for idx in range(len(new_A)):
    re_new_list.append(new_B[idx] + " -> " + new_A[idx])
    if new_A[idx] == new_B[idx]:
        print(new_A[idx], new_B[idx])


print(re_new_list)
print(re_merge_list)

re_new_list.extend(re_merge_list)

print(re_new_list)


str = """['tuck -> truck', 'sculp -> sculpture', 'arbo -> arbor', 'pe barrier -> PE barrier', 'sculpt -> sculpture', 'trashcon -> trashcan', 'talbe -> table', 'bycicle -> bicycle', 'stone barrier -> stone', 'desk -> table', 'seat -> chair', 'umbrella -> parasol', 'potted plant -> vase', 'flat bench -> chair', 'backpack -> bag', 'phone booth -> booth', 'hand cart -> cart', 'handcart -> cart', 'cart rack -> cart', 'stone flat bench -> stone', 'stop sign -> sign', 'suitcase -> bag', 'window seat -> chair', 'couch -> bed', 'plastic bag -> bag', 'handbag -> bag', 'shopping bag -> bag', 'stop sign -> sign', 'bench -> chair', 'backpack -> bag', 'umbrella -> parasol', 'handbag -> bag', 'suitcase -> bag', 'couch -> bed', 'potted plant -> vase', 'dining table -> table', 'handcart -> cart', 'window seat -> chair', 'bookshelf -> shelf', 'plastic bag -> bag', 'fire truck -> truck', 'busstop sign -> sign', 'cart rack -> cart', 'hand cart -> cart', 'stone flat bench -> stone', 'stone handrail -> stone']
"""
#
print(str.replace(",","\n"))