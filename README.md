# Starting off

### ***Project Notebook is at the end of this README***

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

This function is the final step in making the Bookbot, before all the paths nonsense coming up. This function creates the report by utilising multiple *print* calls.

### This function includes:

- 6 *print* calls to build the report
- A *for* loop
- An *if* statement
- An *f string* inside the *if* statement

To explain this function, we have first the *print* calls. In total there are 6. 5 of them are at the very top, they create the main lines of the report and utilise *f strings* to also bring in the previously defined variables of **path** and **w_count**.

These variables (**path** and **w_count**) were created specifically for this report.

Then the *for* loop iterates over the whole **sorted_list** to bring in the individual items of the list with the *index[0]*, it then uses *.isalpha()* to check whether each of the items is a letter or not. If it is it passes a *True* in the *if* statement, which then gets put into another *f string* which has the sorted letter *(index[0])* and the count of how many times the letter was seen in the book *(index[1])*

The *f string* is then returned and the report has now completed.

## Seventh Function (main - moved back out of stats.py)

It turns out main(), wasn't meant to be in stats.py because it doesn't make sense to have your logic in the stats instead of the actual logic file/

Before *main()* had a word count variable in it, the variable and the code that defines the variable itself stays, but the string that created the **message** variable is now gone.

Now the *main()* function houses the *sys.argv* for the path related code and brings in and defines variables from stats.py.

*sys.argv* allows the Bookbot to use any book path instead of the hardcoded previously used frankenstain.txt. This makes the bookbot more usable, instead of manually changing the path every time you want to analyse a new book, now all you need to do is upload your book into the folder.

# Project Notebook

## IPO Table

### Get Book

| Input              | Process                                                       | Output                                                                              |
|--------------------|---------------------------------------------------------------|-------------------------------------------------------------------------------------|
|      Book Text     | The *Get_book* function converts text from the books path to a string.                    | The books text is converted to a string to be used later in Bookbot                 |


### Return Characters

| Input              | Process                                                       | Output                                                                              |
|--------------------|---------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Character Counting | The *Return_Characters* function counts letters, then puts it into a dictionary.   | The Bookbot reads the string and counts the letters to be used in the next function |

### chars_dict_to_sorted_list

| Input              | Process                                                       | Output                                                                              |
|--------------------|---------------------------------------------------------------|-------------------------------------------------------------------------------------|
|    List Creation   | *chars_dict_to_sorted_list* converts the dictionary into a much nicer looking list. | The counted letters are then formatted into a neat readable list                    |
### print_report

| Input              | Process                                                       | Output                                                                              |
|--------------------|---------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Report Generation  | *print_report* converts the list from the *chars_dict_to_sorted_list* function into a nicely formatted report          | The list is turned into a very nice report, leading to better readability           |


## Design Decisions and Justifications

For this project, most of the code is all functional towards the Bookbot, there isn't much unique code that I have decided to implement to add somewhat of a twist to this Bookbot. Most of the code used is the code that Boot.dev has required in order for the Bookbot to work and to pass the CLI tests.

However throughout the code, there are numerous comments written to brief descriptions of the function uses and to eliminate any confusions.

It also may be noticed that all code has some clear gaps in between functions and lines, this is to keep the code editor looking as neat and decluttered as possible.

## Test Cases

For this Bookbot, there are three test cases, all of which are provided by boot.dev

There are the books:

- frankenstein.txt
- mobydick.txt
- prideandprejudice.txt

The follwing test cases have produced the results as seen below:

### franktenstein.txt

============ BOOKBOT ============                
Analyzing book found at books/frankenstein.txt...

----------- Word Count ----------                
Found 75767 total words                          
--------- Character Count -------                
e: 44538                                         
t: 29493                                         
a: 25894                                         
o: 24494                                         
i: 23927                                         
n: 23643                                         
s: 20360                                         
r: 20079                                         
h: 19176                                         
d: 16318                                         
l: 12306                                         
m: 10206                                         
u: 10111                                         
c: 9011                                          
f: 8451                                          
y: 7756                                          
w: 7450                                          
p: 5952                                          
g: 5795                                          
b: 4868                                          
v: 3737                                          
k: 1661                                          
x: 691                                           
j: 497                                           
q: 325                                           
z: 235                                           
æ: 28                                            
... output visually truncated      

### mobydick.txt

============ BOOKBOT ============            
Analyzing book found at books/mobydick.txt...

----------- Word Count ----------            
Found 215838 total words                     
--------- Character Count -------            
e: 119354                                    
t: 89875                                     
a: 79224                                     
o: 70809                                     
n: 66781                                     
i: 66675                                     
s: 65139                                     
h: 63769                                     
r: 53593                                     
l: 43351                                     
d: 38840                                     
u: 27204                                     
m: 23627                                     
c: 23319                                     
w: 22557                                     
g: 21287                                     
f: 21252                                     
p: 17874                                     
y: 17243                                     
b: 17204                                     
v: 8725                                      
k: 8228                                      
q: 1581                                      
j: 1177                                      
x: 1064                                      
z: 636                                       
æ: 23                                        
... output visually truncated           

### prideandprejudice.txt

============ BOOKBOT ============                     
Analyzing book found at books/prideandprejudice.txt...

----------- Word Count ----------                     
Found 130410 total words                              
--------- Character Count -------                     
e: 74451                                              
t: 50837                                              
a: 44834                                              
o: 43383                                              
i: 41198                                              
n: 40686                                              
h: 36162                                              
s: 35695                                              
r: 35168                                              
d: 23723                                              
l: 23475                                              
u: 16303                                              
m: 15676                                              
c: 14838                                              
y: 13579                                              
w: 13017                                              
f: 12996                                              
g: 11007                                              
b: 9762                                               
p: 9154                                               
v: 6118                                               
k: 3497                                               
x: 1032                                               
j: 1014                                               
z: 971                                                
q: 660                                                
ê: 8                                                  
... output visually truncated   

## Reflection

Througout this whole Bookbot projects, there have been countless challenges that I have faced throughout the way, this project has required immense dedication and problem solving skills. During the project, even the smallest of mistakes has led to the whole code breaking, making patience a very important skill.

However challenging and annoying it was, the end result was very much worth all this stress.

Throughout the project some challenges I faces included:

- Accidentally pressing a letter which ended up breaking the whole code
- forgetting small things like brackets when calling a function
- Lots and lots of revisiting code to create changes
- Lots of tweaking of original code that worked to make it compatible with new code
- Revisiting Python throught the Boot.dev spellbook because I forgot some code
- Not clearly understanding some segments of the assessment (on Boot.dev)
- The project notebook IPO table...
- Forgetting and using wrong syntax many times

Although these challenges came up, trial and error was my best choice, eventually it finally was done. 

**This is the finished Bookbot project!**
