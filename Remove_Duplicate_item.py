######## Remove duplicate items in the Python list

def RemoveNum(Mylist1,Mylist2):
    Twolist = Mylist1 + Mylist2
    
    final_list = []

    for num in Twolist:
        if num not in final_list:
            final_list.append(num)

    return sorted(final_list)
     

list1 = [2, 4, 10, 20, 5, 2, 20, 4]
list2 = [2,2,3,4,5,6,10,20 ,4, 10, 20, 5, 2, 20, 4]

print(RemoveNum(list1,list2))