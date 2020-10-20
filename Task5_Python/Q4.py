print('Enter correct username and password to continue')
count=0
password="Consultadd123"
username="N_pandey"

while password!='Consultadd123' and username!='N_pandey' and count<4:
    username=input('Enter username: ') 
    password=input('Enter password: ')

    if password=='Consultadd123' and username=='N_pandey':
     print('Access granted')

    else:
        print('Access denied. Try again.')
        count-=1