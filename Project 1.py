# is a comment function
# ctrl c reset

def playgame():
  print('''
  Here is what I can do for you:
  
  + for addition
  - for subtraction
  * for multiplication
  / for division
  ''')

  choice = input('What do you want to do? (Pick from + - * /) ')

  if choice != '+' or '-' or '*' or '/'
    print('That is not supported!')
 
  num1 = input('1st Number: ')
  num1 = int(num1)

  num2 = input('2nd Number: ')
  num2 = int(num2)

  if choice == '+':
    print(f'{num1} + {num2} = {num1 + num2}')

  elif choice == '-': #elif is else if
    print(f'{num1} - {num2} = {num1 - num2}')
    
  elif choice == '*': 
    print(f'{num1} * {num2} = {num1 * num2}')
    
  elif choice == '/': 
    print(f'{num1} / {num2} = {num1 / num2}')

  else:
    print('That is not supported!')


print('Hello player')
print()

print('Disclaimer: This game is not suitable for certain ages')

#P5js: let age = something
#python: age = something
#or
print()

yn1 = ''
while yn1 != 'Yes':
  age = input('Please verify your age in numerals to continue: ')
  print()
  print(f'So you are {age} years old?')
  yn1 = input('Are you sure? (Yes/No) ')
  

age = int(age)

if age < 13 and yn1 == 'Yes':
  print('You are not old enough bro.') 

if age >= 13 and age <= 20 and yn1 == 'Yes':
  print('Ok fine, just be cautious...')
  playgame()
  

if age > 20 and age <= 80 and yn1 == 'Yes':
  print('Ok, have fun!')
  playgame()

if age > 80:
  print('Hell nah you are too old')

