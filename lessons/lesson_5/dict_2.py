from collections import defaultdict, Counter, OrderedDict

grouped = defaultdict(list)
for word in ["apple", "banana", "apricot", "cherry"]:
    grouped[word[0]].append(word)

print(grouped)

counts = Counter("abracadabra")
print(counts)
print(counts.most_common(2))

c1 = Counter(a=3, b=1)
c2 = Counter(a=2, b=2)

print(c1 + c2)

my_od = OrderedDict().fromkeys('abcde')
print(my_od)
my_od.move_to_end("b")
print(my_od)

my_od.move_to_end("b", last=False)
print(my_od)
