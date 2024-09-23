lucky_numbers = [4,5,10,6,7,8,46,78,93]
friends=["keven","henry","salman","sharukh","keven"]
friends.append("creed")
friends.insert(1,"kauli")
friends.remove("salman")#friends.clear remove all element from list
friends.extend(lucky_numbers)
friends.pop()
print(friends)
print(friends.index("keven"))
print(friends.count("keven"))
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)