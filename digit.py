user_input = input()
digit = 0
letters = 0

for i in user_input:

    if i.isdigit():
        digit=digit+1

    elif i.isalpha():

        letters=letters+1
        

print("The input string", user_input,"has",letters,"letters and", digit,"digits.")        

