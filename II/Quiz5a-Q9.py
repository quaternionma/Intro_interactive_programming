my_list = [0, 1]
for i in range(40):    
    sum_last = my_list[i] + my_list[i+1]
    my_list.append(sum_last)
print my_list

        