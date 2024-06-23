import random

s_char= "!$%^&*()-_=+"
combination = ['qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop',
                'asd', 'sdf', 'dfg', 'fgh', 'ghj', 'hjk', 'jkl', 'zxc', 
                'xcv', 'cvb', 'vbn', 'bnm']


def check_p():     
    p = input("Enter Password: ")
    score = len(p)

    if  8 <= len(p) <= 24:
        upper = any(i.isupper() for i in p)
        lower = any(i.islower() for i in p)
        digit = any(i.isdigit() for i in p)
        special = any(i in s_char for i in p)

        if upper:
            score += 5
        else:
            print("Password must contain at least one uppercase letter.")

        if lower:
            score += 5
        else:
            print("Password must contain at least one lowercase letter.")

        if digit:
            score += 5
        else:
            print("Password must contain at least one digit.")
            
        if special:
            score += 5    
        else:
            print("Password must contain at least one special character from  ! $ % ^ & * () - _ + =  " )

        if upper and lower and digit and special:
            score += 10 

        if p.isalpha():
            score -= 5
        elif p.isdigit():
            score -= 5
            
        for i in combination:
            if p.lower().count(i):
                score -= 5   
        
    else:
        score -= score
        print("Enter a password between 8 to 24 characters.")

    if score >= 25:
        print("\nStrong Password")
    elif 25 > score >=10:
        print("\nMedium Password")
    elif 10 > score >=0 :
        print("\nWeak Pasword")

    return score   


def generate_p():
    l = random.randint(8, 12)

    key = ''
    
    password = chr(random.randint(65,90)) + chr(random.randint(97,122)) + chr(random.randint(48,57)) + random.choice(s_char)

    for i in range(l):
        key =key + random.choice(password)

    score = len(key)

    upper = any(i.isupper() for i in key)
    lower = any(i.islower() for i in key)
    digit = any(i.isdigit() for i in key)
    special = any(i in s_char for i in key)

    if upper:
        score += 5
    else:
            print("\nPassword doesn't contain uppercase letter.")

    if lower:
        score += 5
    else:
        print("\nPassword doesn't contain lowercase letter.")

    if digit:
        score += 5
    else:
        print("\nPassword doesn't contain  digit.")
            
    if special:
        score += 5    
    else:
        print("\nPassword doesn't contain special character from  ! $ % ^ & * () - _ + =  " )

    if upper and lower and digit and special:
        score += 10 

    if key.isalpha():
        score -= 5
    elif key.isdigit():
        score -= 5
            
    for i in combination:
        if key.lower().count(i):
            score -= 5
            
    if score >= 40:
        print("Strong Password")
    elif 40 > score >=24:
        print("Medium Password")
    elif 24 > score >= 0 :
        print("Weak Pasword")

    return key,score


while True: 
    option= input("\nSelect options below:\n 1.Check Password\n 2.Generate Password\n 3.Quit \nEnter your Choice 1,2,3 : ")

    if option == "1":
        score = check_p()
        print("score :",score)

    elif option == "2":
        key,score = generate_p()
        print("Password :",key)
        print("score :",score)

    elif option == "3":
        print("\nYou have chosen to quit the program.")
        break
    
    else:
        print("Invalid Option ")






