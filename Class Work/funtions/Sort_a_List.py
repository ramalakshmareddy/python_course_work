def bubble_sort():
    list_input=list(map(int,input("enter the numbers :").split()))
    legnth=len(list_input)
    for i in range(legnth):
        for j in range(1,legnth-i-1):
            if(list_input[j]>list_input[j+1]):
                list_input[j],list_input[j+1]=list_input[j+1],list_input[j]
    print(list_input)
bubble_sort()                