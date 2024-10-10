
numbers=[]
size=0
for i in range(120115,120200+1):
    numbers.append(i)
    size+=1
temp_start=0
for i in range(len(numbers)):
    if numbers[0]%numbers[i]==0:
        temp_start+=1
index=0
max=numbers[0]
for i in range(len(numbers)):
    temp=0
    for k in range(0, numbers[i]+1):
        if numbers[i]%numbers[k]==0:
            temp+=1
    if temp>temp_start:
        temp_start=temp
        max=numbers[i]
        index=i
print('Index: ', index, 'Number: ', max)

