 #imports the PasswordHash class from the pwdlib library.
from pwdlib import PasswordHash

 #creates a PasswordHash object using the recommended password-hashing algorithm
password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(
    password: str,
    hashed_password: str
) -> bool:    #true or false
    return password_hash.verify(
        password,
        hashed_password
    )