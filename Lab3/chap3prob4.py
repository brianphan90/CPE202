def sort_pair(lst,counter = 0):
    if counter == len(lst) - 1:         #tests for odd list
        last = lst[-1]
        ex_lst.append(last)
        return(f_lst + ex_lst)
    if counter == len(lst):             #tests for even list    
        return(f_lst)
    first = lst[counter]
    second = lst[counter +1]
    

    f_lst.append(second)
    f_lst.append(first)
    return f_lst + sort_pair(lst, counter+2)
    
#lst = [1,2,3,4,5,6]
lst=[2,4,6,8,9]
ex_lst=[]
f_lst = []
sort_pair(lst)


    