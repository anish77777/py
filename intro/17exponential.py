def raise_topower(base_num,pow_num):
    result = 1
    for index in range(pow_num):
        result = result* base_num
    return result    

print(raise_topower(3,2))