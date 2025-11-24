#task 1
lis = [4, 65, 23, 545, 645, 1 ,26, 1233]
print(lis)
currmax = 0
for i in lis:
    for x in lis:
       if i < x:
          currmax = x
       else:
          continue
print(currmax)

#task 2
#======================#

#task 3
tuples = [(1, 10), (2, 20), (1, 5)]
result = {}
for key, value in tuples:
        if key in result:
            result[key] += value
        else:
            result[key] = value
print(result)