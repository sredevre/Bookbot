# Starting off

**Project Notebook is at the end of this README**

initially, the project is organised into two seperate files, main.py and stats.py

main.py will become the file that will be run in the terminal for submissions.

stats.py is the file with all the code to complete the assessment, it handles the logic of the BookBot.

## Stats.py Work

## First Function (get_book)

The first function for this project is the **get_book** function.

With this function, the code extracts the book (initally frankenstein) from the users computer to then be used to gain further info.

### The function includes:

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


## Second Function (main)

The **main()** function is used to get the word count of the whole book.

### The function includes:

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


## Third Function (Return Characters)

This one was really painful and time consuming but eventually I got through it

For this part of the project, the Boot.Dev spellbook became a very helpful tool. By going to back to the loops section in python and how to iterate over lists became very helpful with this one.

for this function, the main idea was to analyse the book and return the number of times each character in the whole text was present in the book alongside the previous main function which counted the words.

this function brought up a few issues, mainly because of small mistakes and forgetting to use the **.lower()** statement which wasted a lot of time trying to fix the code.

### The function includes:

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

## Fourth Function (sort_on)

This function is a very small and simpler one compared to the previous and upcoming functions. It contains only two lines. The purpose of this function is to help sort the current dictionary and convert it into the upcoming sorted list.

### The function includes:

- Importing of the **letters** variable
- Type hints
- a return variable which indexes the **letters** variable

The function is pretty self explanatory:

 type hints tell python what the expected data type of the variable should be after the function. 
 
 The index seperated the count which will be used in the next function.

## Fifth Function (chars_dict_to_sorted_list)

The first function really starts putting the BookBot together. In this function, the previously returned **letters** variable from the *Return Characters* function gets sorted into a neat and readable version. It gets rid of all the excess junk and sends out a neat list of the letters in a *(tuple, int)* list. 

### The function includes

- An empty list named **sorted_list**
- A for loop
- A *.append* inside the for loop (Used double brackets because *.append* requires a single argument)
- use of the previous **sort_on** function
- Returning of the new **sorted_list**

To explain the function, the empty **sorted_list** will be used to hold the new neat list of the characters count, replacing the old *Return Characters* function.

The for loop iterates through the **letters** variable which was given by the old *Return Characters* function.

the *.append* tool adds the letters and counts to the new **sorted_list** which returns a clean list. In the *.append*, you may realise that it has two sets of brackets and a set of square brackets, the square brackets it's obvious you need them, but the extra set of normal brackets is because without them, it would be classed as two different arguments, the *.append* can only pass 1, so the extra brackets wrap those two together into one so *.append* works.

the *return* is pretty self explanatory, it returns the new **sorted_list** for use.

## Main.py Work

## Sixth Function (print_report)

# Project Notebook
