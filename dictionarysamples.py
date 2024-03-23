sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                
                "physics": {"key":"item"
                            ,},
                "history": 80
                
            }
        }
    }
}

# print(sampleDict["class"]["student"]["marks"])

def dictionar(d):
    if isinstance(d, dict):
        for key , info in d.items():
            print(key,"::",info)
            if key=="history":
                return info
            else:
                result=dictionar(info)
                # print(result)
                if result is not None:
                    return result
    

# def find_history_value(d):
#     if isinstance(d, dict):
#         for key, value in d.items():
#             if key == "history":
#                 return value
#             else:
#                 # If the value is another dictionary, recurse
#                 result = find_history_value(value)
#                 if result is not None:
#                     return result
#     # If we reach here, it means we haven't found "history" in this path
#     return None


a=dictionar(sampleDict)
print(a)


employees = ['Kelly', 'Emma','sss']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)


ex="hellllhoweareyou"

dic={}
for i in range(len(ex)):
   
    if ex[i] in dic:
        dic[ex[i]]+=1
    else:
        dic[ex[i]]=1

h=next(key for key,value in dic.items() if value == max(dic.values()))
print(h)



