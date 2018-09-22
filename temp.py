a=[i for i in range(10)]
b=[i for i in "abcdefgh"]

a=map(lambda x:"aaaa" if x==1 else x,a)

print(list(a))