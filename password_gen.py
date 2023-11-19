import random
import string
lower=string.ascii_uppercase
upper=string.ascii_lowercase
digits=string.digits
pass_len=int(input("enter the length of the password: "))
com=int(input('''enter the complexity of the password
1 for normal
2 for hard
'''))

if com == 1:  # normal
    pwd=[]
    pwd.extend(list(lower))
    pwd.extend(list(upper))
    pass_key=''.join([random.choice(pwd) for i in range(pass_len)])

    print(pass_key)


if com == 2:  # hard
    pwd=[]
    pwd.extend(list(lower))
    pwd.extend(list(upper))
    pwd.extend(list(digits))
    pass_key=''.join([random.choice(pwd) for i in range(pass_len)])

    print(pass_key)
    



