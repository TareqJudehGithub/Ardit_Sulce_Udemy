monday_temp = [9.1, 8.8, 7.5]

monday_temp.append(8.4)

# insert(index, value)
monday_temp.insert(0, 10)

print(monday_temp)

print(monday_temp.index(10))

monday_temp.pop()
print(monday_temp)


# list indexing
# returns 2nd item till the rest
print(monday_temp[1:])

# return the 3rd and the 4th items only
print(monday_temp[2:4])

# negative indexing:
# get the last item
print(monday_temp[-1])

# get the last 2 items
print(monday_temp[-2:])

monday_temp.append('monday')
print(monday_temp)

# extract 'day' from monday_temp list
print(monday_temp[-1][-3:])

