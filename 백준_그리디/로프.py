N = int(input())

weight = []

for i in range(N):
    weight.append(int(input()))

weight.sort()
max_weight = 0

a = len(weight)

for i in range(a):
    current_weight = weight[i]*(N-i)

    if current_weight>max_weight:
        max_weight = current_weight

print(max_weight)


