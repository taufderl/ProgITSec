def bubblesort(a):
    for j in range(len(a) - 1):
        for i in range(len(a) - j - 1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a
 
a = [9,3,0,6,2,1,8,7,4,5]
print("Unsortiert: ", a)
 
result = bubblesort(a)	
print("Sortiert  : ", result)