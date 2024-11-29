#  problem 1 -even number in a new list(append)- condition
list = [2,7,21,56,72,99,82,64,22]
new_list =[] # take A new empty list for even no.
for i in list:
    if i%2==0: # if we want to get the remainder as 0 then we will use % otherwise we use / 
        print(i)
        new_list.append(i)
print(new_list)