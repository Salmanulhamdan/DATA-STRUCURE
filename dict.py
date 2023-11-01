dict1 = {"NFLX": 4950, "TREX": 2400, "FIZZ": 1800, "XPO": 1700}
dict2 = {x: v for (x, v) in dict1.items() if v > 2000}
print(dict2)
