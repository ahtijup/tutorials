import hashlib
from urllib.request import urlopen


def get_wordlist(url):
    try:
        with urlopen(url) as f:
            wordlist = f.read().decode('utf-8').splitlines()
            return wordlist
    except Exception as e:
        return f'failed to get wordlist: {e}'


def hash(password):
    result = hashlib.sha256(password.encode())
    return result.hexdigest()


def bruteforce(wordlist, password):
    password_hash = hash(password)
    for guess_password in wordlist:
        if hash(guess_password) == password_hash:
            return guess_password


if __name__ == '__main__':
    WORDLIST_URL = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/2df55facf06c7742f2038a8f6607ea9071596128/Real-Passwords/Top12Thousand-probable-v2.txt'
    MY_PASSWORD = 'password123'

    wordlist = get_wordlist(WORDLIST_URL)
    print(f'wordlist contains {len(wordlist)} items')
    print(wordlist)

    password = bruteforce(wordlist, MY_PASSWORD)
    if password is not None:
        print('your password is:', password)
    else:
        print('your password is not in the wordlist')
