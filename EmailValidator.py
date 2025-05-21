from email_validator import validate_email, EmailNotValidError

def is_valid_email(email):
    if email:
        try:
            validate_email(email)
            return True
        except EmailNotValidError:
            return False


email = input("Enter email-id : ")

if is_valid_email(email):
    print("Email-id is Valid :-",email)
else:
    print("Email-id is Not Valid :-",email)