import random

def generator_password():
    mayus = ['A','B','C','D','E','F','G','H','I','J','K','L',
    'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    minus = ['a','b','c','d','e','f','g','h','i','j','k','l',
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    simbols = ['!','¿','¡','?','$','@','&','ç']
    numbers = []
    password = []
    for i in range(15):
        aleatory_number = random.randint(1,100)
        numbers.append(str(aleatory_number))
    
    character = mayus + minus + simbols + numbers

    for i in range(10):
        character_random = random.choice(character)
        password.append(character_random)

    password = "".join(password)
    return password


def run():
    password = generator_password()
    print("Your new password is: " + password)


if __name__ == "__main__":
    run()