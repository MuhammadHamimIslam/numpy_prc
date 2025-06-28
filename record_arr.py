import numpy as np

# creating record array from structured array 
struct_arr = np.array([
    ("Abc", 29),
    ("Pqr", 35),
    ("Xyz", 31)
], dtype=[("name", "U10"), ("age", "i4")])

# need to copy the array 
rec_arr = struct_arr.view(np.recarray)
print(rec_arr)

# accessing fields 
print(rec_arr.name) # returns all name
print(rec_arr.age) # returns all age

# directly creating record array 
record_arr = np.rec.array([
        ("Abc", 29),
        ("Pqr", 35),
        ("Xyz", 31)
    ],dtype=[("name", "U10"), ("age", "i4")])

print(record_arr)

# accessing multiple fields
print(record_arr[["name", "age"]])

# modifying a field 
indices = record_arr["name"] == "Abc"
record_arr[indices]["age"] = 39 # modifying age for Abc
print(record_arr)
