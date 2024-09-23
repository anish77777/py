#make condition
is_male = True

if is_male:
    print("u are a male")

is_male = False
if is_male:
    print("u are a male")
else:
    print("u are not a male")



is_male = True
is_tall=True

if is_male or is_tall:
     print("u are a male or tallor bath")
else:
    print("you neither male nor tall")
    
is_male = False
is_tall= False
if is_male and is_tall:#and both
     print("u are a male or tallor bath")
elif not(is_male) and not(is_tall):
    print("u are not male and not tall")
else:
    print("you neither male nor tall")
    