obj_list = ['person', 'bicycle', 'car', 'motorcycle', 'traffic light', 'bus', 'truck', 'sports ball', 'kite', 'bottle', 'toilet', 'tv', 'bird', 'cat', 'dog', 'microwave', 'sink', 'refrigerator', 'book', 'palette', 'rock', 'bollard', 'hat', 'grating', 'stroller', 'fence', 'raised spot', 'forklift', 'tent', 'mat', 'manhole', 'cup', 'firewood', 'boxes', 'PE tank', 'vacuum', 'tree', 'hanger', 'door', 'parking bump', 'pillar', 'rubber cone', 'air cleaner', 'frame', 'standing light', 'power strip', 'roll mat', 'container', 'deck', 'trashcan', 'stairs', 'guitar', 'mannequin', 'basketball stands', 'goalpost', 'arbor', 'mirror', 'balloon sign', 'trash heap', 'curtain', 'electricity control panel', 'tripod', 'tissue box', 'outdoor unit of air conditioner', 'kerb', 'rainwater pipe', 'bike rack', 'traffic signs', 'momument', 'booth', 'faucet', 'sculpture', 'window', 'fan', 'guardrail', 'telegraph pole', 'pothole', 'wheelchair', 'parasol', 'bowl', 'table', 'vase', 'bag', 'fire extinguisher', 'fire hydrant', 'stone', 'banner', 'cart', 'PE barrier', 'entry barrier', 'sign', 'chair', 'desk', 'bed', 'shelf', 'streetlight']

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

new_list = ["tuck -> truck",
"sculp -> sculpture",
"arbo -> arbor",
"pe barrier -> PE barrier",
"sculpt -> sculpture",
"trashcon ->trashcan",
"talbe -> table",
"bycicle -> bicycle",
"flowerbed -> flower bed",
"stone barrier -> stone",
"desk -> table",
"seat -> chair",
"umbrella -> parasol",
"potted plant -> vase",
"flat bench -> chair",
"backpack -> bag",
"phone booth -> booth",
"net pole -> net post",
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

notin_list = []

print("=================merge_list===================")
merge_list = [x.split("->")[-1].lstrip() for x in merge_list]
for merge_element in merge_list:
    if merge_element in obj_list:
        print("merge_list 포함",merge_element)
    else:
        print("merge_list 미포함",merge_element)
        notin_list.append(merge_element)

print("=================new_list===================")
new_list = [x.split("->")[-1].lstrip() for x in new_list]
for new_element in new_list:
    if new_element in obj_list:
        print("new_list 포함",new_element)
    else:
        print("new_list 미포함",new_element)
        notin_list.append("new_list의 "+new_element)

print(notin_list)





