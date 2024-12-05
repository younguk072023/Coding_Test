

#1 csv파일 연동과 데이터베이스

f=open("재고.csv","r")
text=f.read()
f.close()

item_list=text.strip().split("\n")
item_dict={}

for i in item_list:
    name,count=i.strip().split(",")
    count=int(count)
    item_dict[name]=count

item=input("재고를 확인하려는 물건의 이름을 입력하세요: ")

if item in item_dict:
    print(f"{item}의 재고는{item_dict[item]}개 입니다.")
else:
    print(f"재고에 {item}는 없습니다!")

    


#2,3 csv파일 연동과 데이터베이스 관리모드

s=open("재고.csv","r")
text2=s.read()
s.close()

items_dict={}                           #딕셔너리와 for문은 while문 밖에있어야됨

items_list=text2.strip().split("\n")
    
for j in item_list:
    names,counts=j.strip().split(",")
    counts=int(counts)
    items_dict[names]=counts


while True:
    num=int(input("옵션->조회(1)추가(2)없는 물건 추가(3)종료(3): "))

    if num==1:
        check=input("확인하려는 물건의 이름을 입력하세요: ")
        if check in items_dict:
            print(f"{check}의 재고는 {items_dict[check]}개 입니다.")

    elif num==2:
        plus_item,plus_counts=input("추가하려는 물건의 이름과 수를 입력하세요: ").split()
        plus_counts=int(plus_counts)

        if plus_item in items_dict:
            if plus_counts<0:
                print(f"재고가 음수가 될 수 없습니다. 현재 {plus_item}의 재고는 {items_dict[plus_item]}")
            else:
                
                original_count=items_dict[plus_item]    #items_dict[plus_item]의 키값을 original_count에 넣어줌

                counts=plus_counts+original_count
                items_dict[plus_item]=counts


                print(f"{plus_item}의 재고가 {original_count}->{items_dict[plus_item]}개로 바뀌었습니다.")
              

    elif num==3:
        extra_item,extra_counts=input("추가하려는 물건의 이름과 수를 입력하세요: ").split()
        extra_counts=int(extra_counts)

        if extra_item not in items_dict:
            items_dict[extra_item]=extra_counts
            print(f"{extra_item}가 추가되었습니다. 재고는 {items_dict[extra_item]}개 입니다.")
        else:
            print("이미 존재합니다!")



    elif num==4:
        print("출력 없음, 프로그램 종료")
        break



