test_dict = {'Codingal' : 7, 'is' : 7, 'best' : 7, 'for' : 7, 'coding' : 7}

print("The original dictionary : " + str(test_dict))

K = 7

res = 0

for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

print("Frequency of K is :" + str(res))