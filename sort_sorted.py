list1 =[10,5,3,60]
list1.sort(key= abs, reverse=True)
print(list1)

list1 =[10,5,3,60]
list1.sort(reverse=True)
print(list1)

list1 =[10,5,3,60]
list1.sort(key= abs)
print(list1)


list3=[75,8,10,15]
list2 = sorted(list3, reverse=True)
print(list2) # only the altered list value changes 
print(list3) # original list remains unaffected

lst= [(5,4),(3,2),(8,1),(9,10)]
lst.sort(key= lambda f: f[1], reverse = True) # on the basis of 2nd element i.e., 1st index
lst4 = sorted(lst, key= lambda c: c[0], reverse = True) # ont he basis of 1st element i.e., 0th index
print(lst)
print(lst4)
