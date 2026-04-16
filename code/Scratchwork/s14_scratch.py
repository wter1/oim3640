# #Open Claw AI



# s = "test"

# print(s in "t")

# lst = ["Bello", "Aorld"]

# print(sorted(lst))

# print(lst)

# print(lst.sort())

# print(lst)


# a = [1,2,3]
# b = a
# b.append(a)


### Dictionary
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
for eng in eng2sp:
    print(eng)

for eng in eng2sp:
    sp = eng2sp[eng]
    if sp == "dos":
        print(eng)
#The above is convoluted so you could just make a new sp2eng dictionary


for k in eng2sp.keys():
    print(k)


for v in eng2sp.values():
    print(v)

for k, v in eng2sp.items():
    print(k, v)

print(max(eng2sp.values()))