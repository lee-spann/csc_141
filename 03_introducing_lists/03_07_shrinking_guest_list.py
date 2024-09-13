guestlist = ['beyonce', 'travis scott', 'shai gilgeous-alexander', 'leonardo da vinci']

name = guestlist[0].title()
print(f"{name}, your invited to come to dinner.")

name = guestlist[1].title()
print(f"{name}, your invited to come to dinner.")

name = guestlist[2].title()
print(f"{name}, your invited to come to dinner.")

name = guestlist[3].title()
print(f"{name}, your invited to come to dinner.")


name = guestlist[3].title()
print(f"Sorry {name}, cannot make it to the dinner.")
#Da Vinci cant make dinner, we'll invite someone else

del(guestlist[3])
guestlist.insert(1, 'lil wayne')

name = guestlist[0].title()
print(f"{name}, your invited to come to dinner.")

name = guestlist[1].title()
print(f"{name}, your invited to come to dinner.")

name = guestlist[2].title()
print(f"{name}, your invited to come to dinner.")

name = guestlist[3].title()
print(f"{name}, your invited to come to dinner.")

#We've found a bigger table
print("We've found a bigger table")

guestlist.insert(0, 'mike tyson')
guestlist.insert(3, 'kanye west')
guestlist.append('lebron james')

name = guestlist[0].title()
print(f"{name}, your invited to come to dinner.")

name = guestlist[1].title()
print(f"{name}, your invited to come to dinner.")

name = guestlist[2].title()
print(f"{name}, your invited to come to dinner.")

name = guestlist[3].title()
print(f"{name}, your invited to come to dinner.")

name = guestlist[4].title()
print(f"{name}, your invited to come to dinner.")

name = guestlist[5].title()
print(f"{name}, your invited to come to dinner.")

name = guestlist[6].title()
print(f"{name}, your invited to come to dinner.")

#The table wont arrive on time, we can only fit 2 people now.
print("The table wont arrive on time, we can only fit 2 people now.")

name = guestlist.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guestlist.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guestlist.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guestlist.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guestlist.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

# There should be two people left.
name = guestlist[0].title()
print(f"{name}, please come to dinner.")

name = guestlist[1].title()
print(f"{name}, please come to dinner.")

# Empty the list
del(guestlist[0])
del(guestlist[0])

# Empty
print(guestlist)