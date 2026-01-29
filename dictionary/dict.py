dict_types={"sid" : "Bihar", "manoj" : "haryana", "ashok" : "Mp", "dev" : "odisha", "soumo" : "kolkata"}
 dict_types
#{'sid': 'Bihar', 'manoj': 'haryana', 'ashok': 'Mp', 'dev': 'odisha', 'soumo': 'kolkata'}

 dict_types["sid"]    # Accessing value using key "sid". 
'Bihar'

dict_types.get("manoj") # Accessing value using get() method for key "manoj"
'haryana'

dict_types.get("rahul", "Not Found") # Accessing non-existing key with default value
'Not Found'

dict_types["ashok"] = "Madhya Pradesh" # Updating value for key "ashok"
 dict_types
{'sid': 'Bihar', 'manoj': 'haryana', 'ashok': 'Madhya Pradesh', 'dev': 'odisha', 'soumo': 'kolkata'}

for val in dict_types :
...     print(val) # Iterating through dictionary keys and printing key names

sid
manoj
ashok
dev
soumo

for val in dict_types.values() :
...     print(val) # Iterating through dictionary values and printing them

Bihar
haryana
Madhya Pradesh
odisha
kolkata

for key, value in dict_types.items() :  # items() method to get key-value pairs
...     print(f"Key: {key}, Value: {value}") # Iterating through key-value pairs and printing them

Key: sid, Value: Bihar
Key: manoj, Value: haryana
Key: ashok, Value: Madhya Pradesh
Key: dev, Value: odisha
Key: soumo, Value: kolkata

if "dev" in dict_types : # Checking if key "dev" exists in the dictionary
...     print("Key 'dev' found in dictionary")

Key 'dev' found in dictionary

del dict_types["soumo"] # Deleting key "soumo" from the dictionary
 dict_types
{'sid': 'Bihar', 'manoj': 'haryana', 'ashok': 'Madhya Pradesh', 'dev': 'odisha'}    

print(len(dict_types)) # Getting the number of key-value pairs in the dictionary
4   # 4 key-value pairs remain after deletion

dict_types.pop("manoj") # Removing key "manoj" and returning its value
'haryana'
 dict_types
{'sid': 'Bihar', 'ashok': 'Madhya Pradesh', 'dev': 'odisha'}

dict_types.popitem() # Removing and returning the last inserted key-value pair
('dev', 'odisha')
 dict_types
{'sid': 'Bihar', 'ashok': 'Madhya Pradesh'}

newDict=dict_types.copy() # Creating a shallow copy of the dictionary
 newDict
{'sid': 'Bihar', 'ashok': 'Madhya Pradesh'}

dict_types.clear() # Clearing all items from the original dictionary
 dict_types
{}

knowledge ={
    "sid" : {"Python", "Java", "C++"},
    "manoj" : ["HTML", "CSS", "JS"],
    "ashok" : ["Django", "Flask"]
}

 knowledge
{'sid': {'C++', 'Java', 'Python'}, 'manoj': ['HTML', 'CSS', 'JS'], 'ashok': ['Django', 'Flask']}

 knowledge["sid"] # Accessing set of programming languages for key "sid"
{'C++', 'Java', 'Python'}

 knowledge["manoj"][1] # Accessing second item in the list for key "manoj"
'CSS'

 knowledge["ashok"].append("FastAPI") # Adding "FastAPI" to the list for key "ashok"
 knowledge
{'sid': {'C++', 'Java', 'Python'}, 'manoj': ['HTML', 'CSS', 'JS'], 'ashok': ['Django', 'Flask', 'FastAPI']} 

 knowledge["sid"].add("Ruby") # Adding "Ruby" to the set for key "sid"
 knowledge
{'sid': {'C++', 'Java', 'Python', 'Ruby'}, 'manoj': ['HTML', 'CSS', 'JS'], 'ashok': ['Django', 'Flask', 'FastAPI']}

 knowledge["sid"].remove("Java") # Removing "Java" from the set for key "sid"
 knowledge
{'sid': {'C++', 'Python', 'Ruby'}, 'manoj': ['HTML', 'CSS', 'JS'], 'ashok': ['Django', 'Flask', 'FastAPI']} 

 knowledge.keys() # Getting all keys in the dictionary
dict_keys(['sid', 'manoj', 'ashok'])

 knowledge.values() # Getting all values in the dictionary
dict_values([{'C++', 'Python', 'Ruby'}, ['HTML', 'CSS', 'JS'], ['Django', 'Flask', 'FastAPI']])

 knowledge.items() # Getting all key-value pairs in the dictionary
dict_items([('sid', {'C++', 'Python', 'Ruby'}), ('manoj', ['HTML', 'CSS', 'JS']), ('ashok', ['Django', 'Flask', 'FastAPI'])])

squared_numbers = {x: x**2 for x in range(1, 6)} # Dictionary comprehension to create a dictionary of numbers and their squares
 squared_numbers
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

keys_list = list(squared_numbers.keys()) # Converting dictionary keys to a list
 keys_list
[1, 2, 3, 4, 5]

values_list = list(squared_numbers.values()) # Converting dictionary values to a list
 values_list
[1, 4, 9, 16, 25]

items_list = list(squared_numbers.items()) # Converting dictionary items to a list of tuples
 items_list
[(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

keys=["java", "c++", "python"]

default_value="programming language"

dict_from_keys = dict.fromkeys(keys, default_value) # Creating a dictionary from a list of keys with a default value
 dict_from_keys
{'java': 'programming language', 'c++': 'programming language', 'python': 'programming language'}

dict_from_keys=dict.fromkeys(keys,keys) # Creating a dictionary from a list of keys with None as default value
 dict_from_keys
{'java': ['java', 'c++', 'python'], 'c++': ['java', 'c++', 'python'], 'python': ['java', 'c++', 'python']}  

tuple_types=("sid", "manoj", "ashok")

tuple_types[-1] # Accessing last element of the tuple
'ashok'

tuple_types.index("manoj") # Finding index of element "manoj"
1

tuple_types.count("sid") # Counting occurrences of element "sid"
1

tuple_types[1 : ]  # Slicing the tuple from index 1 to the end
('manoj', 'ashok')

len(tuple_types) # Getting the length of the tuple
3

tuple_types + ("dev", "soumo") # Concatenating two tuples
('sid', 'manoj', 'ashok', 'dev', 'soumo')

tuple_types[1]= "rahul" # Trying to modify an element of the tuple (will raise an error)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment


if "manoj" in tuple_types : # Checking if "manoj" exists in the tuple
...     print("manoj is present in the tuple")
manoj is present in the tuple

tuple_types.count("dev") # Counting occurrences of element "dev"
0

(SID, MANOJ, ASHOK) = tuple_types # Unpacking the tuple into variables
 SID
'sid'

 MANOJ   
'manoj'

type(tuple_types) # Checking the type of tuple_types
<class 'tuple'>

score=input("enter value :")   # we can take input as string
enter value :85
  score
'85'

score  / 2   # This will raise an error since score is a string
Traceback (most recent call last):


newScore = int(score)  # Converting string input to integer
 newScore
85

  newScore / 2  # Now we can perform arithmetic operations  
42.5









