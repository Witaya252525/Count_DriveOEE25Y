#create list of fruits
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
fruits.append('fig')
fruits.append('grape')  
print(fruits)
# replace arrey that contain "ch" with " witaya"
fruits[2] = 'witaya'
print(fruits)





for fruit in fruits:
    # Check if the fruit is  start with char 'a' or 'A'
    if fruit.startswith('a') or fruit.startswith('A'):
        print(fruit, "starts with 'a' or 'A'")
    else:
        print(fruit, "does not start with 'a' or 'A'")

# Check if the fruit is contain with rr or 'RR'
for fruit in fruits:
    if 'rr' in fruit or 'RR' in fruit:
        print(fruit, "contains 'rr' or 'RR'")
    else:
        print(fruit, "does not contain 'rr' or 'RR'")   
