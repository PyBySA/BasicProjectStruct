import json


def compare_json_objects(obj1, obj2, exclude_keys):
    # Remove excluded keys from each object
    obj1_filtered = {key: obj1[key] for key in obj1 if key not in exclude_keys}
    obj2_filtered = {key: obj2[key] for key in obj2 if key not in exclude_keys}

    # Compare filtered objects
    return obj1_filtered == obj2_filtered



def compair_by_json(db_json, api_response_json):
    # Sample list of JSON data
    json_list1 = db_json

    json_list2 = api_response_json

    # List of keys to exclude from comparison
    exclude_keys = ["modifiedby", "modifiedat", "createdat", "createdby"]

    # Separate into duplicate and unique lists
    duplicate_json_list = []
    unique_json_list1 = []
    unique_json_list2 = []

    for obj1 in json_list1:
        found_duplicate = False
        for obj2 in json_list2:
            if compare_json_objects(obj1, obj2, exclude_keys):
                duplicate_json_list.append(obj1)
                found_duplicate = True
                break
        if not found_duplicate:
            unique_json_list1.append(obj1)


    for obj2 in json_list2:
        found_duplicate = False
        for obj1 in json_list1:
            if compare_json_objects(obj1, obj2, exclude_keys):
                found_duplicate = True
                break
        if not found_duplicate:
            unique_json_list2.append(obj2)

            # print("Duplicate JSON List:",json.dumps(duplicate_json_list))
            # print("Unique JSON List 1:", json.dumps(unique_json_list1))
            # print("Unique JSON List 2:", json.dumps(unique_json_list2))
    # if unique_json_list1:
    #     for idx,x in enumerate(unique_json_list2):
    #         if x in unique_json_list1:
    #             unique_json_list2.pop(idx)



    return duplicate_json_list, unique_json_list1, unique_json_list2

