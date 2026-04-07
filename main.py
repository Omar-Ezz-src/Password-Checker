import requests

def CheckPasswordStrength(password):
    points = 0
    if len(password) >= 12: 
        points += 1

    hasLower = any(i.islower() for i in password)
    hasUpper = any(i.isupper() for i in password)
    if hasLower and hasUpper: 
        points += 1

    if any(i.isdigit() for i in password):
        points += 1 

    specialChars = " ~!@#$%^&*()_+/*-}{|:',.><?/. " + ' " '
    if any(i in specialChars for i in password):
        points += 1

    url = "https://raw.githubusercontent.com/R3DHULK/python-for-ethical-hacking/refs/heads/main/rockyou.txt"
    found_in_list = False
    
    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    if password == line.decode('latin-1').strip():
                        found_in_list = True
                        break
    except:
        pass

    if not found_in_list:
        points += 1
    
    return points

while (True):   
    password = input("\nEnter a password : ")
    score = CheckPasswordStrength(password)
    print(str(score) + " / 5")
    if score >= 5:
        print("good password")
    elif score >= 3:
        print("medium password")
    else:
        print("weak password")