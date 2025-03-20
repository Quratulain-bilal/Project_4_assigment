import time

#function for user is enter another type of value
def valid_input():
  while True:
    try:
      user_input=int(input("Enter the time in seconds: "))
      return user_input
    except:
      print("Invalid input, Please enter a number")

def count_down(seconds):
  while seconds > 0:
    print (f"Time left: {seconds} seconds")
    time.sleep(1)
    seconds -=1
  print("Times Up!")

user_input = valid_input()
count_down(user_input)