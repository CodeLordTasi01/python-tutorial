list1=[]
leap_list=[]
notleap_list=[]
size=int(input("entre years no"))
for i in range(size):
    ele=int(input("enter year"))
    list1.append(ele)
    if ele%4==0 and ele%400!=0 and ele%100==0:
        leap_list.append(ele)
    else:
        notleap_list.append(ele)
print("original list",list1)
print("leap year list",leap_list)
print("not leap  list",notleap_list)
