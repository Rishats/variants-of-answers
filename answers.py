import itertools

lst = ['E', 'O', 'И', 'Б']
combs = []

for i in range(1, len(lst)+1):
    els = [list(x) for x in itertools.combinations(lst, i)]
    combs.extend(els)

print (combs)