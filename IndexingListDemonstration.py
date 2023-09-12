# Attemtping to slice from point A to the end of a list.
number = [0,1,1,2,3,5,8,13,21,34]
# Technically the last element is #9, but since it's an exclusive featured we add 9+1.
print('number[7:10]',number[7:10])
# another form of indexing the last element in a slice is to leave the second element empty:
print('number[7:]',number[7:])
# The lesson here is that there are multiple ways of slicing a string or list that may be more appropriate or convenient for the project's globals

# It is also possible to determine a slice range with a determined increment or "step"
print(number[0:10:2])

# From the beginning to the end, every fourth list member:
print(number[::4])

# A negative element means that the increment will be counted backwards:
print(number[::-2])
print(number[10:0:-2])
# When counting backwards, make sure that there are indeed elements to be counted from the starting point.

print(number[5:-1:2])