i=1
while i<=10:
    i+=1
    if i%2==0:
        print(i)


for i in range(0,10,2):
    print(i)


i=2
while i<=20:
    print(i)
    i+=2  

for ele in range(100,50,-1):
    print(ele)  

#List 

eids=[101,102,103,104]
#index 0   1   2   3
print(eids[0])  #Output 101
print(eids[1])  #Output 102
print(eids[2])  #Output 103
print(eids[3])  #Output 104

#for reverse
reversed_eids=eids[::-1]
print(reversed_eids)

