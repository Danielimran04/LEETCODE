roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

user_input=input("Please enter romans number to convert:").upper()#IV

number=0

n=len(user_input)#2


for i in range(n):
    current_value=roman_map[user_input[i]]#1 and 5
    
    if i+1<n and roman_map[user_input[i+1]]>current_value:
        number=number-current_value
    else:
        number=number+current_value


print(number)



