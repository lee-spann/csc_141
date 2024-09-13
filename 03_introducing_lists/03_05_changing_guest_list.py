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
