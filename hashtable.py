# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.table = [[] for _ in range(size)]
#
#     def hash_(self, key):
#         return hash(key) % self.size
#
#     def insert(self, key, value):
#         index = self.hash_(key)
#         for item in self.table[index]:
#             if item[0] == key:
#                 item[1] = value
#                 return
#         self.table[index].append([key, value])
#
#     def get(self, key):
#         idx = self.hash_(key)
#         for item in self.table[idx]:
#             if item[0] == key:
#                 return item[0],item[1]
#         raise KeyError(key)
#     def table(self):
#         print(self.table)
# dict=HashTable(5)
# dict.hash_("name")
# dict.insert("name","hamdan")
# print(dict.get("name"))
#
# dict.hash_("name")
# dict.insert("name","sree")
# print(dict.get("name"))
#
#
#
def hashkey(string1):
    hashvalue = 0
    for char in string1:
        hashvalue += ord(char)
    return hashvalue % 100


print(hashkey('A'))
