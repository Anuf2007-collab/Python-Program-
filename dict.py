d={}
print(d)
d["employee no."]=123
print(d)
d["employee name"]="abc"
print(d)
print(d["employee no."])
print(d["employee name"])
for key in d:
    print(key)
for value in d.values():
    print(value)
for key,values in d.items():
    print(key,values)               
d.pop("employee no.")
print(d)
d.popitem()
print(d)
