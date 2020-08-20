first_command = "I shall Give Coffee Sir..."
second_command = "I shall protect you..."
third_command = "Playing Soothing Music ~EVERYBODY POOPS by Jason Shaw~"
forth_command = "--SHUTTING DOWN--"
fifth_command = "Importing data..."

system_running = True
print("Hello, Sir")
print("I am the Mutton Assistant Bot V1.4 programmed to assist you") 
 
while system_running:
 guess = input("Please give me an order (press 1 for coffee,2 for protection,3 for music,4 to shut down or 5 to import data):")
 print("Initializing the request....")
 print("Understanding the command...")
 print("Transcripting the command...")
 print("Checking Variables...")
 print("Executing the command...")
 print("Command successfully executed...") 
 
 if guess == "4":
     print(forth_command)
     print("System successfully shut down,Goodbye Sir...") 
     system_running = False
     break

 if guess == "1":
     print() 
     print(first_command)
     print("Coffee has been delivered...") 

 if guess == "2":
     print()
     print(second_command)
     print("Boss successfully protected...") 

 if guess == "3":
     print()
     print(third_command)
     print("Music successfully played,enjoy...") 

 if guess == "5":
     print()
     print(fifth_command)
     print("Data successfully imported...") 
  
     






    

