import random
one_time_pass = (random.randrange(100000,999999))
print (one_time_pass)
count= 0
while (count < 3):
    try:
        response = int(input("please enter the displayed one time password  :   "))
        print()
        if one_time_pass == response:
          print ("@@@@@@@@@@@@@@ OTP AUTHENTICATED SUCCESSFULLY @@@@@@@@@@@@@ ")
          print()
          count = 3
          break
        else:
            print("Please provide correct otp")
            print()
    except ValueError:
        print()
        print ("!!!!!!!!! PLEASE PROVIDE THE ACCURATE INTEGER !!!!!!!!!")
        print()
        print()
        attempts_left = 3

    except Exception:
        print ("$$$$$  SOME THING WRONG OCCURRED   $$$$$")
        print()
    attempts_left = 2
    attempts_to_display = attempts_left - count
    print(attempts_to_display, "Attempts left")
    count = count + 1

    if attempts_to_display == 0:
        print("&&&&    SORRY LOGIN UNSUCCESSFUL    &&&&")
print("^^^^^^^^ CODE EXECUTION COMPLETED ^^^^^^^^" )