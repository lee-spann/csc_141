#list of flavors
flavors=['vanilla','chocolate','caramel','spicy','mint','strawberry','bbq']

#del function
del flavors[-1]
print(flavors)

#append function
flavors.append('bbq')
print(flavors)

#pop function
work=flavors.pop(2)
print(flavors)
print(work)

#insert function
flavors.insert(1,work)
print(flavors)

#sorted
print(sorted(flavors))
print(flavors)

#sorted reverse
print(sorted(flavors,reverse=True))
print(flavors)

#reverse
flavors.reverse()
print(flavors)
flavors.reverse()
print(flavors)

#sort
flavors.sort()
print(flavors) 

#sort reverse
flavors.sort(reverse=True)
print(flavors)