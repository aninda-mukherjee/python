lucky_numbers = [2,4,5,2,4,6,3]
friends = ["Kevin", "Jim", "Oscar", "Jon"]

friends.sort()
print(friends)

lucky_numbers.reverse()
print(lucky_numbers)

friends.extend(lucky_numbers)
print(friends)

friends.append("Appended")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends2 = friends.copy()

friends.remove("Kelly")
print(friends)

print(friends.index("Jim"))



friends.pop()
print(friends)

friends.clear()
print(friends)

print(friends2)


