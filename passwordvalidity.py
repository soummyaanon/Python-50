password = input()

has_valid_length = False
has_lower_case = False  # Added this variable
has_upper_case = False
has_digit = False
has_special_characters = False

if 13 <= len(password) <= 16:
    has_valid_length = True

    for i in password:
        if i.islower():
            has_lower_case = True
        elif i.isupper():
            has_upper_case = True
        elif i.isdigit():
            has_digit = True
        elif i in ["@", "$", "#", "^", "&", "*"]:
            has_special_characters = True

if has_valid_length and has_lower_case and has_upper_case and has_digit and has_special_characters:
    print("Valid Password")
else:
    print("Invalid Password")
