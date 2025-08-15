import getpass
import hashlib   
import requests  
import re        

def check_strength(password):
    """
    Evaluates password against multiple strength criteria.
    Returns: (score, list_of_messages)
    """
    criteria = {
        "length": len(password) >= 12,  
        "lowercase": re.search(r'[a-z]', password) is not None,  
        "uppercase": re.search(r'[A-Z]', password) is not None,  
        "digit": re.search(r'[0-9]', password) is not None,      
        "special": re.search(r'[^A-Za-z0-9\s]', password) is not None  
    }

    score = sum(criteria.values())

    messages = []

    if not criteria["length"]:
        messages.append("Too short (minimum 12 characters).")
    if not criteria["lowercase"]:
        messages.append("Add at least one lowercase letter.")
    if not criteria["uppercase"]:
        messages.append("Add at least one uppercase letter.")
    if not criteria["digit"]:
        messages.append("Add at least one number.")
    if not criteria["special"]:
        messages.append("Add at least one special character.")

    return score, messages  

def check_breach(password):

    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    res = requests.get(url)

    if res.status_code != 200:
        res = requests.get(url)

    hashes = (line.split(':') for line in res.text.splitlines())

    for hash_suffix, count in hashes:
        if hash_suffix == suffix:
            return True, f"This password has been seen {count} times in breaches so is not safe to use."

    return False, "This password is strong and it was not found in any  known breach."

if __name__ == "__main__":
    try:
        while True:
            password = getpass.getpass(("\nEnter password to check: ").strip())
            score, feedback = check_strength(password)
            for msg in feedback:
                print(msg)
            if score < 5:
                print("Please try again with a stronger password.")
                continue
 
            if score == 5:
                breached, breach_msg = check_breach(password)
                print(breach_msg)

            choice = input("\nDo you want to check another password? (y/n): ").lower()
            if choice != 'y':
                print("🔒 Session ended.")
                break
    except KeyboardInterrupt:
        print("\n[!] Program interrupted by the user.")
