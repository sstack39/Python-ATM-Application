#input pin valid
#check value of pin variable
Balance = 473
error = 0
while error<5:
  pin = int(input('Enter your pin: '))
  #give appropriate statement
  if pin == 1001:
    print('Thank you, one moment')
    #menu 
    while True:
      option = int(input('Enter 1 to withdraw, Enter 2 to deposit, Enter 3 to Check Balance, Enter 4 to Exit Account '))
      if option == 1:
        amount = float(input('Enter amount you would like to withdraw '))
        if amount.is_integer():
          if amount <= Balance - 23: 
            Balance = (Balance - amount)
            print('New Balance after withdrawal is $', Balance)
          else:
            print('Insufficient Funds Available')            
        else:
          print('Please enter a valid whole number')          
          #loop needed
      elif option == 2:
        amount = int(input('Insert the cash you would like to deposit '))
        Balance = Balance + amount
        print('New Balance after deposit is $', Balance)
      elif option == 3:
        print('Current Balance is $', Balance)
      elif option == 4:
        print('Thank you, please take your card')
        break
      else:
        print('Please Enter 1,2,3, or 4 ')
        #Y loop is needed to complete
        
  else:
      
      if error == 4:
        print('Please see customer service inside branch office')
        break
      else:
        print('Please try again')
      error += 1