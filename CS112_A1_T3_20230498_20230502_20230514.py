'''
team members :
1> youssef saad eldeen
  ID:20230498
  solved problems : 1 & 5

2> youssef amr mohamed
  ID:20230502
  solved problems : 3 & 4

3> youssef moris kamal
  ID:20230514
  solved problems : 2 & 6

Date : 2023/2/27
'''
print("Welcome in our program\nFor grade calculator;please enter 1\nFor checking if a number is armstrong or not;please enter 2\nFor computing pi;please enter 3\nFor cesar cipher;please enter 4\nFor checking if two lists are the same; please enter 5\nFor getting factors of any positive integer;please enter 6")
# a list that contains the only 6 valid options for the user.
choices_list = [1,2,3,4,5,6]
# a while loop to check the validity of the input.
while True :
      try:
            choice = int(input("enter an option :"))
            if choice not in choices_list :
                  print("please enter a valid option:")
            else:
                  break
      except ValueError :
            print("please enter a valid option :")

# the main while loop that contains the 6 problems.

while True :

      # problem 1
      
      if choice == choices_list[0]:
            mark = int(input("give me the mark :"))  # to get a mark form the user
            while "true":
                  if mark > 100 or mark < 0:  # to check if the mark that the user gave correct
                        print("please give ma a corect mark :")
                        mark = int(input())
                        continue  # to make the user input again a correct mark
                  elif mark >= 90:
                        print("the grade is A+")
                        break
                  elif 90 > mark and mark >= 85:
                        print("the garde is A")
                        break
                  elif mark < 85 and mark >= 80:
                        print("the grade is B+")
                        break
                  elif mark >= 75 and mark < 80:
                        print("the grade i B")
                        break
                  elif mark < 75 and mark >= 70:
                        print("the grade is C+")
                        break
                  elif mark < 70 and mark >= 65:
                        print("the grade is C")
                        break
                  elif mark < 65 and mark >= 60:
                        print("the grade is D+")
                        break
                  elif mark < 60 and mark >= 50:
                        print("the grade is D")
                        break
                  else:
                        print("the grade is F")
                        break

      #problem 2

      elif choice == choices_list[1] :
            def pro_2():
                  while True: # to repeat the conditions until a correct input is given
                        print("=== Welcome to Armstrong Numbers Calculator ===")
                        num = int(input("Please enter a number: "))
                        if num == 0 or num <= 0:  # to check that  if  the input number not less than or equal zero to continue
                              print("Invalid input , please try again")
                              continue
                        else:
                              string = str(num)
                              power = len(string)
                              total = sum(int(digit) ** power for digit in string)
                              print('Total = ', total)
                              if total == num: # checking if the input number equals the total to make sure that the number is an armstrong
                                    print("The number is an Armstrong")
                              else:
                                    print("The number is not an Armstrong")


            pro_2()

      #problem 3

      elif choice == choices_list[2]:
            def pi_calculator():
                  pi = 0
                  print("=== Welcome to Pi Calculator ===")
                  num_of_terms = int(input("Please, enter number of terms you want: "))
                  for i in range(num_of_terms):
                        term_num = ((1) ** i) / (2 * i + 1) # this is the sequence of the pi value divided by 4
                        if i % 2 == 0:  # If the term number is even
                              pi += term_num
                        else:  # If the term number is odd
                              pi -= term_num
                  pi *= 4
                  print(pi)


            pi_calculator()

      #problem 4

      elif choice == choices_list[3]:
            def prob_4():
                  while True:
                        print("=== Welcome to Cesar cipher rule ===")
                        string_given = str(input("Please,enter your message: "))
                        if not string_given.replace(' ', '').isalpha(): # this is to check if there are spaces or anything  to remove other than alphabetic characters
                              print("Invalid input, please enter only alphabetic characters and spaces.")
                              break
                        string = ""
                        for letter in string_given:
                              if letter == ' ': # checking if there are spaces  to not change them
                                    string += ' '
                                    continue
                              if letter == ',': # checking if there are commas to not change them
                                    string += ','
                                    continue
                              if letter == 'z': # checking if the letter is z small change it automatic to the beginning of the alphabetic small letters
                                    string += 'a'
                              elif letter == 'Z':# checking if the letter is Z capital change it automatic to the beginning of the alphabetic capital letters
                                    string += 'A'

                              else:
                                    order = ord(letter) # getting the order of the letter to add 1 to it
                                    order += 1
                                    chr(order) # converting again the the new order into the new following character
                                    string += chr(order)

                        print(string)


            prob_4()

      #problem 5

      elif choice == choices_list[4]:
            def prop_5():
                  # creating an empty list
                  list1 = []
                  # number of elements as input
                  num_of_elements1 = int(input("Enter number of elements of list 1: "))
                  # iterating till the range
                  while "true":
                        if num_of_elements1 < 0:
                              print("please inter correct numbers of elements:")
                              num_of_elements1 = int(input("Enter number of elements : "))
                              continue
                        else:
                              for i in range(0, num_of_elements1):
                                    elements = input()
                                    # add1ing the element
                                    list1.append(elements)
                              print(list1)
                        break
                  # creating an another empty list
                  list2 = []
                  # number of elements as input
                  num_of_elements2 = int(input("Enter number of elements for list 2 : "))
                  # iterating till the range
                  while "true":
                        if num_of_elements2 < 0:
                              print("please inter correct numbers of elements:")
                              num_of_elements2 = int(input("Enter number of elements : "))
                              continue
                        else:
                              for i in range(0, num_of_elements2):
                                    elements = input()
                                    # add1ing the element
                                    list2.append(elements)
                              print(list2)
                        break
                  if all(ele in list1 for ele in list2) and all(
                          ele in list2 for ele in
                          list1):  # to check that all elements in list1 also in list2 and the The opposite

                        print("TRUE")
                  else:
                        print("FALSE")


            prop_5()

       #problem 6 : the user should enter a positive integer and the program will return it's factors.

      elif choice == choices_list[5]:
            # a while loop containing a try-except block to check the validity of the input.
            while True:
                  try:
                        number = int(input("Please enter a positive integer to get its factors: "))
                        if number <= 0:
                              print("Please enter a positive number.")
                        else:
                              break  # Valid input, exit the loop

                  except ValueError:
                        print("Invalid input. Please enter a valid positive integer.")
            # assigning a list to which the factors will be added at the end.
            factors = []
            # a second while loop that starts the operation of getting the factors.
            z = 0
            while (number - z) != 0:
                  x = number / (number - z)
                  if x.is_integer() == True:  # if the result of the division is integer;then it's one of the factors of the number
                        factors.append(int(x))
                  z = z + 1
            print(f"the factors of {number} : {factors}")



