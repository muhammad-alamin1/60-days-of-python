this_dic = {
    "brand": "Tesla",
    "Model": "AMT244",
    "year" : 1970,
    "colors": ["red", "white", "blue"]
}
person = dict(name = "Muhammad", age = 23, country = "Bangladesh")

li = [this_dic, person]
x = person.get("name")
person["name"] = "Al-Amin"
dic_tup = person.items()

if "name" in li[1]:
    pass

this_dic.update({"Model":"PIXEL 79"})
this_dic["country"] = "USA"

print(this_dic)
this_dic.pop("country")
this_dic.popitem()

for x in this_dic.items():
    print(x)