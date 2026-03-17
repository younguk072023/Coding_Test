T=int(input())

all_list=[]

for i in range(T):
    N=int(input())

    number_list=input().split()

    A=[]

    for i in number_list:
        i=int(i)
        A.append(i)
    
    all_list.append(A)

print(all_list)