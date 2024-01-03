password = input()

has_valid_length = False
has_valid_case = False
has_upper_case = False
has_digit = False
has_special_characters = False

if(len(password)>=13)and(len(password)<=16):

    has_valid_length = True

    for i in password:

        if(i.islower()):
            has_lower_case = True

            if(i.isupper()):
                has_upper_case = True

                if(i.isdigit()):
                    has_digit = True

                    if(i=="@" or i=="$" or i=="#" or i =="^" or i=="&" or i=="*" ):
                        has_special_characters = True

if (has_valid_length==True and has_lower_case ==True and has_upper_case == True and has_digits == True and has_special_characters == True):
    print("Valid Password")
else:
        print("Invalid Password")                        