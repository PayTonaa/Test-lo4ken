# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife", "knife", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}



utensils.update(dishes) # dodaje wszystkie elementy z setu dishes do utensils
utensils.add("napkin")
utensils.remove("fork")
# utensils.clear()

print(utensils.difference(dishes))  # wyswietla to czego nie ma w drugim
print(utensils.intersection(dishes)) # wyświetla to co jest w obu


dinner_table = utensils.union(dishes) # łączy podane sety


# for x in dinner_table:
#     print(x)

