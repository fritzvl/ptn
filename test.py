data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []


#while data_list:
#    minimum = data_list[0]  # arbitrary number in list
#    for x in data_list:
#        if x < minimum:
#            minimum = x
#    new_list.append(minimum)
#    data_list.remove(minimum)
#print new_list


def sort2(list):
    for index in range(1,len(list)):
        value = list[index]
        i = index-1
        while i>=0:
            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i -= 1
            else:
                break

sort2(data_list)
print data_list
