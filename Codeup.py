data = input()
result = int(data[0])   #첫 번쨰 값

for i in range(1,data):
    num = int(data[i])

    if result<=1 or num<=1:
        result+=1
    else:
        result*=num

print(result)