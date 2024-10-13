lst_lst = [[1, 2, 4], [3, 5, 6, -1, 7], [1, 9]]

# LIST COMPREHENSION #

flatlist = [elem for sublst in lst_lst for elem in sublst if elem >= 0]
print(flatlist)