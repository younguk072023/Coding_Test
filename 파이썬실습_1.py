

#1 튜플 이용

num_1,name_1=input("학번과 이름을 입력하세요: ").split()
num_1=int(num_1)
total=(num_1,name_1)
print(total)




#2 튜플을 활용한 데이터베이스

all=[]

while True:
    num_2=int(input("옵션->추가(1)조회(2)종료(3) : "))

    if num_2==1:
        number,name_2=input("학번과 이름을 입력하세요: ").split()
        number=int(number)
        all.append((number,name_2))
        print(all)
    
    elif num_2==2:
        number=int(input("학번을 입력하세요 : "))
        
        for i in all:
            if number==i[0]:
                print(f"{number}학번의 이름은 '{i[1]}'입니다.")
    
    elif num_2==3:
        print("출력 없음, 프로그램 종료")
        break




#3 딕셔너리를 활용한 데이터베이스

All={} 

while True:
    num_3=int(input("옵션->추가(1)조회(2)삭제(3)종료(4)"))

    if num_3==1:
        number_3,name_3=input("학번과 이름을 입력하세요: ").split()
        number_3=int(number_3)
        All[number_3]=name_3
        print(All)
    
    elif num_3==2:
        number_3=int(input("학번을 입력하세요: "))
        
        if number_3 in All:
            print(f"{number_3}학번의 이름은 '{All[number_3]}'입니다.")

    elif num_3==3:
        number_3=int(input("학번을 입력하세요: "))

        if number_3 in All:
            del All[number_3]
        print(All)

    elif num_3==4:
        print("출력 없음, 프로그램 종료")
        break
