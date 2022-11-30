    
def password_validation(password):  
    # if password != password2 :
    #     messages.error(request , 'Пароль не совпадает')
    if len(password) < 8:
        return False
    if '!' not in password and '@' not in password and '$' not in password:
        return False
    return True


