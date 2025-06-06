import numpy as np 

# define the data type 
# [("feild_name", "data_type")]
dtype = [("name", "U10"), ("age", "i4")]
# create data
data = [("abc", 29), ("pqr", 32), ("mno", 24)]
structured_data = np.array(data, dtype=dtype)

# accessing the name
print(structured_data["name"])
print(structured_data["age"])

# structured data for 3d array 
dtype3d = [("length", "i4"), ("width", "i4"), ("height", "f4")]
data3d = [(10, 10, 10.0), (3, 4, 2.9), (10, 11, 23.23)]
structured_data3d = np.array(data3d, dtype=dtype3d)

# accessing data
print(structured_data3d["height"])
print(structured_data3d["length"])
# accessing multiple fields 
print(structured_data3d[["length", "width", "height"]])

# boolean indexing 
searched = structured_data3d["width"] > 5
print(structured_data3d[searched])