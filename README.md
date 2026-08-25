# Starting off

initially, the project is organised into two seperate files, main.py and stats.py

main.py will become the file that will be run in the terminal for submissions.

stats.py is the file with all the code to complete the assessment, it handles the logic of the BookBot.


# First Function (get_book)

The first function for this project is the **get_book** function.

With this function, the code extracts the book (initally frankenstein) from the users computer to then be used to gain further info.

## The function includes:

- with open
- pathname
- converts the full path into f
- **.read()**
- a variable called **string**

to explain this, the with open is used to go into the users computer and extract the book,

The pathname is to tell where to go to find the book

the **as f** statement is used to simplify the path into an easily accessible letter (f)

the **.read()** function converts the contents of the path into the string

the **string** variable holds the converted string to use later in the code.


# Second Function (main)

The **main()** function is used to get the word count of the whole book.

## The function includes:

- The previously defined **string** variable
- A variable named **count**
- A variable called **message**
- An *f string* with a *len* statement
- A **.split()** command

this function works by bringing in the **string** variable that was defined in the **get_book** function.

It is then used to define the **count** variable by using a **.split** to seperate the individual words from the text.

The **count** variable is then used to define the **message** variable.

The **message** variable puts the **count** variable and combines it with text in an *f string* to then print to the console.

The final output of **message** variable is the finished word count.


# Third Function (Return Characters)

This one was really painful and time consuming but eventually I got through it

For this part of the project, the Boot.Dev spellbook became a very helpful tool. By going to back to the loops section in python and how to iterate over lists became very helpful with this one.

for this function, the main idea was to analyse the book and return the number of times each character in the whole text was present in the book alongside the previous main function which counted the words.

this function brought up a few issues, mainly because of small mistakes and forgetting to use the **.lower()** statement which wasted a lot of time trying to fix the code.

## The function includes:

- An empty dictionary named **letters**
- A for loop
- An if and Else statement
- Mathematical operatators *+=* and *=*
- The **string** varible (back again from get_book)
- A **.lower()** statement

Outside the loop there is print statement containing the loop and the original **get_book** loop.

The empty dictionary, **letters**, is used to contain the letters. Initially this dictionary is empty but though the use of the **for loop** and the **if** and **else** statements it eventually fills up and gives the desired result.

the **for loop** iterates over the **string** variable and the **.lower()** converts all the letters into lowercase form.

While iterating over the list **if** and **else** statements decide whether the current letter that it is iterating over is already in the new **letters** dictionary or not, if it is, it adds 1 to the letter counter, or else it creates a completely new entry in the dictionary and starts from 1.



