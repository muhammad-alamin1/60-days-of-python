this_dic = {
    "brand": "Tesla",
    "Model": "AMT244",
    "year" : 1970,
    "colors": ["red", "white", "blue"]
}

# nested dictionary
child_details = {
    "child_one" :{
        "name" : "Muhammad",
        "dob"  : 2006
    },
    "child_two" :{
        "name" : "Tamim",
        "dob"  : 2008
    },
    "child_three" :{
        "name" : "Abdulla",
        "dob"  : 2010
    }
}

try:
    # copy dictionary
    _copy_dic = this_dic.copy()
    _copy_dic1 = dict(this_dic)
    
    second_child_dob = child_details["child_two"]["dob"]
    # print(second_child_dob)
    
    for x, obj in child_details.items():
        for y in obj:
            print(y + " : ", obj[y])
        
    print(child_details.get("child_one").get("name"))
except KeyError as err:
    print("Exception Caught: ", err)