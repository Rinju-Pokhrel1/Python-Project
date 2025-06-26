import re  # for searching

def check_strong_password(password):
    strength = 0
    
    if len(password) >= 8:
        if re.search('[a-z]', password):
            strength += 1
        if re.search('[A-Z]', password):
            strength += 1
        if re.search('[0-9]', password):
            strength += 1
        if re.search('[@#$%+=!]', password):
            strength += 1
        strength += 1  # for length ≥ 8
    return strength

def main():
    password = input("Enter your password: ")
    strength = check_strong_password(password)

    if strength == 5:
        print("Wow! Very strong password")
    elif strength == 4:
        print("Strong password")
    elif strength == 3:
        print("Medium password")
    elif strength == 2:
        print("Weak password")
    else:
        print("Oops! Very Weak password")

if __name__ == '__main__':
    main()
