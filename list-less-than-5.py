################ List Less Than Ten ############

myList = [1,2,3,4,5,6,7,8]
def Processing(lists):
    for i in lists:
        if i <= 5:
            print("%s less than 5" % i)
        else:
            print("%s more than 5" % i) 

answer = Processing(myList)

