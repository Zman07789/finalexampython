#Create a python program that reads in numbers and stores them in a list till the user enters 
#"quit" have that program then output the total, count, and average of those numbers. Make
#sure there are try catch block, include a flow chart(in jpeg of pdf format), source code,
#and a screenshot of source code and the program running. You can attach all of this to the 
#assignment, or put it in a github folder and send a link to that.


# By Zackary Paulson


numbers = [] # created a list called numbers

while True: #This is a while loop that gets an input from the user and if the user doesn't enter quit the loop appends the new number that the user entered onto the list but if the user enters quit it breaks from the loop. There is also an except which prints out if the user didn't enter quit. 
	userInput = input("Please enter a number or 'quit': ")
	if userInput == 'quit':
		break
	try:
		numbers.append(float(userInput))
	except:
		print("Error: Please enter a number or 'quit'")
		
if len(numbers) > 0: # This is an if statement that assigns values to total, count and average and prints out the number for each of the vars. 
	total = sum(numbers)
	count = len(numbers)
	average = total/count
	
	print("Total:", total)
	print("Count:", count)
	print("Average:", average)
else: # This is if the user immediatly enters quit, because you can't do any computations without numbers! unless you use 0 I guess but I don't think that will work in this case. 
	print("No numbers processed")
	