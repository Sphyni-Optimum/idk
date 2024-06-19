{'So today, we will be making the bin() function of our own. So let"s kick off'}

import math

def binary(decimal):
  decimal__num = decimal
  binary, process = '', ''   #Setting up the variabels
  
  while process != 'done':   
    if decimal__num > 1:  #This will check the decimal number can still be divided by 2 or not
      binary = str(decimal__num % 2) + binary #Adding the remainder and converting into biary
      decimal__num = math.floor((decimal__num / 2))      

    else:
      binary = str(decimal__num) + binary
      process = 'done' # breaking the loop  

  return binary # returning the binary

print(binary(33))   #You can test yourself by changing the value 
