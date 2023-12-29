import random as r
import string as st

chars = st.ascii_letters + st.digits + st.punctuation

while True:
    try:
        length = int(input('\nHow many characters would you like (Minimum 15 recommend)? >>> '))
        for _ in range(length):       
            print(r.choice(chars), end='')      
                                                
    except ValueError:
        print('Enter a number!')


'''

Notes for self (or others if learning Pyhton):

'for _ in range(length):' '_' means whatever. It is an 'idc'. range is using what was determined from length
'.choice' will select a random character from the chars variable
'end=' will determine what to end the function with
'st.ascii_letters + st.digits + st.punctuation' are ascii letters | numbers | symbols

'''     
