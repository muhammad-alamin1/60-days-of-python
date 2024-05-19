# a sets is a collection which is unordered, unchangeable, & unindexed
# Sets do not allow duplicate values
# True & 1 consider the same values

this_sets = {"apple", "watermelon", "banana", "apple"}
thisset = set(("apple", "banana", "cherry", True, 1, 2))

print(type(this_sets))

for x in this_sets:
    if x == "watermelon":
        # print(x)
        pass

# add an item to a set
this_sets.add("orange")
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc
tropical = ["pineapple", "mango", "papaya"]
this_sets.update(tropical)

# to remove item in a set, use remove() or discard() method
try:
    this_sets.remove("apple")
    this_sets.discard("pineapple")
    thisset.clear()
except Exception as er:
    print(er)
else:
    """ 
    print(this_sets)
    print(thisset)
    """
    pass
finally:
    pass

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = {"apple", 1, "banana", 0, "cherry"}
set4 = {False, "google", "microsoft", "apple", True}

# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates

new_set = this_sets.union(thisset)
intersection_set = set1.intersection(set2)
intersection_set1 = set3.intersection(set4)
set1.intersection_update(set2)
dif = this_sets.difference(thisset)
_sym_dif = set1.symmetric_difference(set2)

print(set1, set2)
print(intersection_set1)
print(dif)
print(_sym_dif)