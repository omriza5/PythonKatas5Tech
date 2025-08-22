import socket


def is_valid_email(email: str):
    """
    Validates if an email address is properly formatted.
    
    Basic email validation rules:
    - Must contain exactly one @ symbol DONE
    - Must have a local part before @ (1-64 characters)
    - Must have a domain part after @ (1-253 characters)
    - Domain must be REAL (hint: check it in python by os.gethostbyname()) DONE
    - Local part can contain letters, numbers, and some special chars: . _ % + - DONE
    - Must not start or end with special characters DONE
    
    You must use regex pattern matching
    
    Args:
        email: The email string to validate
        
    Returns:
        True if the email is valid, False otherwise
    """
    EMAIL_MIN_LENGTH = 5
    MAX_LOCAL_PART = 64
    MAX_DOMAIN_PART = 253
    
    if len(email) < EMAIL_MIN_LENGTH:
        return False
    if not contains_single_at_sign(email):
        return False
    if email_starts_or_ends_with_special_char(email):
        return False
    
    sign_index = email.index("@")
    email_local_part = email[:sign_index]
    email_domain_part = email[sign_index + 1:]
    
    if len(email_local_part) > MAX_LOCAL_PART:
        return False
    
    if len(email_domain_part) > MAX_DOMAIN_PART:
        return False
    
    if not is_real_domain(email_domain_part):
        return False
    
    return True

def contains_single_at_sign(email):
    AT_SIGN = '@'
    counter = 0
    
    for letter in email:
        if letter == AT_SIGN:
            counter += 1
    
    return counter == 1

def email_starts_or_ends_with_special_char(email):
    special_chars = ["." ,"_" ,"%" ,"+" ,"-"]
    
    email_first_char = email[0]
    email_last_char = email[len(email) -1]
    
    if email_first_char in special_chars or email_last_char in special_chars:
        return True
    
    return False

def is_real_domain(domain):
    try:
        socket.gethostbyname(domain)
        return True
    except Exception as e:
        return False
    
    
if __name__ == "__main__":
    test_emails = [
        "user@cnn.com",           # Valid
        "john.doe@cnn.com",     # Valid
        "admin+test@cnn.com",        # Valid
        "user_name@cnn.com",  # Valid
        "user@@domain",           # Invalid 
        "",                           # Invalid - empty
        "user@domain..com",           # Invalid - double dot
    ]
    
    for email in test_emails:
        result = is_valid_email(email)
        print(f"'{email}' is valid: {result}") 