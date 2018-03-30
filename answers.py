from itertools import permutations
answers = ['Answer1','Answer2','Answer3','Answer4','Answer5']
counter = 0
for x in permutations(answers):
    print(list(x))
    counter += 1
print ("Number of ways: " + str(counter))