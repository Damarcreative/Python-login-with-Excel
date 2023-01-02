import openpyxl

# Opens the Excel file used as the database
wb = openpyxl.load_workbook('database.xlsx')

# Opens a sheet in an Excel file
sheet = wb['Sheet1']

def login():
  # Request input username and password from the user
  username = input('Enter username: ')
  password = input('Enter password: ')

  # Check each row in the Excel sheet
  for row in sheet.rows:
    # If the username and password entered by the user match those in the Excel sheet
    if row[2].value == username and row[3].value == password:
      print('Login successful!')
      return
  
  # If no rows match, then login failed
  print('Incorrect username or password!')

def signup():
  # Request input of name, email, username, and password from the user
  name = input('Enter a name: ')
  email = input('Enter e-maill: ')
  username = input('Enter username: ')
  password = input('Enter password: ')

  # Adding a new row in the Excel sheet with data entered by the user
  sheet.append([name, email, username, password])

  # Save changes in the Excel file
  wb.save('database.xlsx')
  print('Sign up successful!')

# Performs a loop to request input from the user until the user chooses to exit
while True:
  print('1. Login')
  print('2. Sign up')
  print('3. Log out')
  pilihan = input('Select a menu: ')
  
  if pilihan == '1':
    login()
  elif pilihan == '2':
    signup()
  elif pilihan == '3':
    break
  else:
    print('Invalid choice!')
