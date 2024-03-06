name=input('Hello, what is your name?: ')
name= name.capitalize()
first= name[0]
if name == 'Matthew':
    print('Hey you have the same name as the person who coded me, Matthew and the start of your name is M!')
elif first == 'M':
    print('hello there '+name+ ', the first letter of your name is '+first+'! Thats the same Letter as my creator')
else:
    print('hello there '+name+ ', the first letter of your name is '+first+'!')
