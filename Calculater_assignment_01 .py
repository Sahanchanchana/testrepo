#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2
def addition (num_1:float,num_2:float) ->float:
  result_add = num_1 + num_2
  return result_add

def Substract (num_1:float,num_2:float) ->float:
  result_sub = num_1 - num_2
  return result_sub

def Multiply (num_1:float,num_2:float) ->float:
  result_multi = num_1 * num_2
  return result_multi

def Divide (num_1:float,num_2:float) ->float:
  if num_2 == 0:
    result_divid = None
    return result_divid
  else:
    result_divid = num_1 / num_2
    return result_divid

def Power (num_1:float,num_2:float) ->float:
  result_pow = num_1 ** num_2
  return result_pow
def Remainder (num_1:float,num_2:float) ->float:
  result_remain = num_1 % num_2
  return result_remain
#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
def select_op (choice:str,input_01:int,input_02:int):

  if choice == "+":
    added_value = addition (input_01,input_02)
    return added_value
  
  elif choice == "-":
    substracted_value = Substract (input_01,input_02)
    return substracted_value
  
  elif choice == "*":
    multiply_value = Multiply (input_01,input_02)
    return multiply_value
  
  elif choice == "/":
    Divide_value = Divide (input_01,input_02)
    return Divide_value
   
  elif choice == "^":
    Power_value = Power (input_01,input_02)
    return Power_value
  
  elif choice == "/":
    Remain_value = Remainder (input_01,input_02)
    return Remain_value

#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  
  mathematical_operations_list = ['+','-','*','/','^','%']
  if choice in mathematical_operations_list : 
    input_01 = float(input("Enter first number: "))
    input_02 = float(input("Enter second number: "))
  elif choice == "#" :
    #program ends here
    print("Done. Terminating")
    exit()
  elif choice == "$" :
    print ("Reset")
    continue
  else :
    print ("Invalide input Please Enter valide charater.Thank you.")
    continue
  
  print(choice)
  
  

  value = select_op (choice,input_01,input_02)
  print (f"{input_01} "  f"{choice} "  f"{input_02} "  "=  "f"{value}")