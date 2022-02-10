# How to Hack a Password in Python?

You can find tutorial [here]().

- crack simple (my password) password and wordlist of 20 words
- create list of passwords with usernames as a dictinary cvs and crack them using wordlist and single hash (Top12Thousand-probable-v2.txt) lists
- create rainbow table with different hash functions as cvs (Top29Million-probable-v2.txt)
- create postgress database locally, create 2 tables with passwords and rainbow table (Top109Million-probable-v2.txt)



https://workshops.hackclub.com/passwordcracker/
https://github.com/berzerk0/Probable-Wordlists












- wordlist
- compare hashing algorithms
- get wordlist and database with passwords (postgress)
- run postgress in container


When viewing a file on GitHub.com, you usually see the version at the current head of a branch. For example:
https://docs.github.com/en/repositories/working-with-files/using-files/getting-permanent-links-to-files

try to use rainbow tables
- https://en.wikipedia.org/wiki/Rainbow_table

- https://www.techslang.com/definition/what-is-a-rainbow-table-attack/
Rainbow table attacks succeed when the hackers match the hash functions used to protect the passwords.


Hashing Algorithmshttps://www.sciencedirect.com/topics/computer-science/hashing-algorithm
Hashing algorithms are just as abundant as encryption algorithms, but there are a few that are used more often than others. Some common hashing algorithms include MD5, SHA-1, SHA-2, NTLM, and LANMAN.

Why use bcrypt
https://stackoverflow.com/questions/9594125/salt-and-hash-a-password-in-python

Password Hashing: Scrypt, Bcrypt and ARGON2
https://medium.com/analytics-vidhya/password-hashing-pbkdf2-scrypt-bcrypt-and-argon2-e25aaf41598e

https://pypi.org/project/argon2-cffi/
https://www.password-hashing.net
Argon2 won the Password Hashing Competition and argon2-cffi is the simplest way to use it in Python and PyPy:

Passwords should ideally use specialised hashing functions like Argon2, BCrypt or PBKDF2, they are modified to prevent Rainbow Table attacks.

These days, more and more systems use proper password storage algorithms such as Bcrypt, Scrypt or Argon2. See: How to securely [store] passwords? Those algorithms are no longer "vulnerable" to rainbow tables: since each hash is unique, even if the passwords are equal, rainbow tables no longer work.

That's why rainbow tables are unpopular today. Even if something modern like Argon2 is not used, developers nowadays usually know that they should at least use a salt. That is already enough to make a rainbow table useless.