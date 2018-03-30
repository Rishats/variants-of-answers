import itertools

lst = [1, 2, 3, 4]
combs = []

for i in xrange(1, len(lst)+1):
    els = [list(x) for x in itertools.combinations(lst, i)]
    combs.extend(els)

print combs