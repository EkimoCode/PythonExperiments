things = ['z', 'b', 'c','a', 'd']
print(things)
print(things[1])
print(things[-1])
# order alphabetically
things.sort()
print(things)

half =  things[0:int(len(things)/2)]
print(half)

print("numbers!")
things[4]=1
print(things)
print(1 in things)
print("k" in things)

newThing = ['Big', 'Yellow', 'Truck']
size, color, name = newThing
print(size)
print(color)
print(name) 