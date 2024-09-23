#access with a key value defination
monthConversions = {
     "jan" :"january",
     "feb":"february",
     "Apr":"April",
 }

print(monthConversions["jan"])
print(monthConversions.get("Luv","not a valid key"))#we can put number as a key
