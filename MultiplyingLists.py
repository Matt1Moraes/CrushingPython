# Basic multiplication makes the list repeat itself (duh)
my_list = [1, 5]
print(my_list*4)

endings = ['st','nd','rd']+['th']*17+['st','nd','rd']+['th']*7+['st']

# Empty lists. It is possible to assign placeholder in a list for future modification based on user's inputs:
temps = [None]*10
temps[2] = 90
temps[3] = 80
temps[4] = 70
print(temps)
print(temps[4])

#None tells python that a place in a list is being held by actually no value, which means that in eventual calculations involving members of said list, it'll know to skip "None" assignments.

total = temps[2]+temps[3]+temps[4]
average = total/3.0
print('Average:',average)