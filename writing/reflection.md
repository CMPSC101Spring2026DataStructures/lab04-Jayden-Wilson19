# Reflection: Rock, Paper, Scissors Lab

Name: Jayden Wilson
Date: 2/27/26

Please answer the following questions after you have completed the programming lab. Write your answers in complete sentences and provide thoughtful responses.

## Comprehension Questions

1. What is the purpose of breaking a program into functions? How did this help you in completing the lab?

Your Response:

Dividing any project into functions helps keep everything nicely organized as best as it can be, especially for longer code. There are many reasons why this is very helpful, for example: It serves as a great point to pause your project as it can be looked as subsections for different parts of the code. 

Another example is to easily identify a part of your code. With comments and docstrings, they serve as a further extension to help notify you about that part of the code and what its main purpose.


2. Describe how you validated user input in your version of the Rock, Paper, Scissors game. Why is input validation important?

Your Response:

I created a function (user_choice), the first part of my code confirms what the user has inputed are 1 of the 3 numbers given that are connected to rock, paper, and scissors. If the user input for whatever reason is invalid, it will print a message reminding them of the choices they can choose.

Projects like this for example will have a number(s) already given that could be changed to your liking. But for projects like this, you would want something to check if the input given from the user is valid as without any set directions, the user won't know what exactly to type and may pass through with an input that doesn't follow the rest of the code.

3. How did you use comments and docstrings in your code? Give an example of a helpful comment or docstring you wrote.

Your Response:

The main purpose of comments and docstrings are to keep not only you, but others who will also have to look at your code of what's happening in a certain area. I used a docstring for every function to summarize what's the code doing in this section, for example: 

def print_round_result(user_choice, computer_choice, winner):
	"""
	Prints the choices and the result of the round in a colorful format using the 'rich' library.

    """

I didn't have many comments as most of it was kinda basic information, but one of the many spots I used a comment was in places that could somewhat confuse anyone looking at my code, for example:

if user_choice == computer_choice:
		return 'tie' # If both choices are the same, it's a tie.
	elif (user_choice == 'rock' and computer_choice == 'scissors') or \
		 (user_choice == 'paper' and computer_choice == 'rock') or \
		 (user_choice == 'scissors' and computer_choice == 'paper'): # Block of code goes through all the possible options to show the outcome of each game



4. Explain how the computer's move is generated in your program. What Python features did you use to accomplish this?

Your Response:

Mos would think, after writing the code for the user input, it would also be the same for the computer. However, since this isn't a 2 player game that requires another persons inout as that would be kinda weird to execute, we instead use random.choice and connect it to the choices dictionary with all of the options it can choose from, randomly.

In my code, theres a message for the computer to choose from the available options that of course won't display for the user. That's when the random.choice function will start and end.

5. What was the most challenging part of refactoring the spaghetti code into a more structured program? How did you overcome this challenge?

Your Response:

I normally like following directions, although there was clear directions for my main program, giving it its own identity and setting it apart from the already given code while still outputting a similar message was a bit challenging.

## Ethical Reflection Questions

1. Why is it important to write code that is easy for others to read and maintain? How does this relate to your responsibilities as a programmer?

Your Response:

There will be instances when your code might just be long, but there are many ways to minimize them so it's a lot easier for you to read and other around. Different functions main purpose is to simplify a longer method into a smaller and easier to read method that will not only help you understand your own code, but employeers and employees aswell when looking into future jobs.

2. Consider the use of open source code (like the spaghetti code provided). What are some ethical considerations when using, modifying, or sharing code written by others?

Your Response:

Similar to writing an essay, given free access to sources that will help support your point, but still being written from your perspective will show the evidence, but written in a way you understood it while not having it completely ripped from that source by including extra information and ideas from yourself.

Copying someone elses code doesn't properly show that you understand whats happening and doesn't show anything written by you.

---

(Did you remember to add your name and date at the top of your reflection file?)

yeah yeah yeah
yeah yeah yeah yeah yeah -  LCD Soundsystem