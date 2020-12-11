#Creating a dictionary from a list of tuples

'''
Creating a list of tuples which we name "users"
'''

users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234"),
]

'''
we are transcribing the data from users into a dictionaries. The first is a username mapping which will take the
username as the key which will map to it's corresponding tuple. The key of each of the key:value pairs will consist of 
the [1]st element of each tuple in the list of users. In this case this refers to the names "Bob","Rolf","Jose" etc.
The value will then consist of the tuple associated with the key. If we print username mapping we are returned this newly
created dictionary of k:v pairs with name:associated tuple. This dictionary called "username_mapping" can be used like a
normal dictionary
'''

username_mapping = {user[1]: user for user in users}
userid_mapping = {user[0]: user for user in users}

print(username_mapping)

print(username_mapping["Bob"])
