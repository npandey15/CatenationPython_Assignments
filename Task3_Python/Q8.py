Dict1={1:10,2:20}
Dict2={3:30, 4:40}
for d in (Dict1,Dict2): Dict2.update(d)
print(Dict2)