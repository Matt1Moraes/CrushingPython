# Slicing Demonstration Video

tag = 'Pater Noster'
print(tag[9])

# Now, let's say I want to extract the word "Pater" only. That's what slicing is for. Remeber, the closing element of a slice is NON INCLUSIVE; meaning it won't be a part of the call.
print(tag[0:5])

# A slice can also be assigned to a variable:
Pater_slice = tag[0:5]
print(Pater_slice)
    
    