# Print the first letter of the following string

school = "McHenry County College"

print school[0]


# print the length of the school string

print len(school)

# Use a while loop to print each character (including spaces) in the school variable

count = 0
while count < len(school):
    letter = school[count]
    print letter
    count += 1

# Slice school into three variables, print the variables

first = school[:7]
second = school[8:14]
third = school[15:]

print first
print second
print third

# use a while statement to search for the letter "e" in the contents of the school variable
# print the index of every location with the letter "e"
# rembember, you should not use the same variable twice in the same
# so if you used the variable index, use something else

def find(word, letter):
    i = 0
    while i < len(school):
        if school[i] == letter:
            return i
        i = i + 1
    return -1

find(school, 'e')

# Write the code to count the number of times the letter y appears in the school variable
# print the total


count = 0
for letter in school:
    if letter == 'y':
        count = count + 1
print count


# create a variable named college and store the upper case version of the variable school in it
college = school.upper()
print college

# check to see if Count is in the school variable



# check to see if count is in the school variable

