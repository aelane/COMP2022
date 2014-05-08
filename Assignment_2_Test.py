#COMP2022 Assignment 2

#----------------------------Input Processing Functions----------------------------#
#This also includes functions necessary to read input .txt files

#Read file
#file_object = open(filename, mode) where file_object is the variable to put the file object.
#mode is just 'r' since we are just reading
#file_object.close() in order to close the file

#Remove spaces and line breaks (CRs)
#supposedly that's just string.strip() but we can look that up

#Add $ to end of string to indicate end of string

#We need to decide how we'd like to store our input
#It could just be a string
#the input will only have terminals, no variables, so that's practical
#However, strings are immutable (so you can't change them once they are created, so that's a bit annoying)
#Perhaps a list of strings would be best and then we just delete the ones we don't want

#I think we probably do want to just save it as a list...


#--------------------------Print derivation and Stack------------------------------#
#Format the strings properly
#
#I think we'll want to represent terminals such as "else" as a single character like 'e' or else a variable e
#If so, we need make sure it prints out "else" instead

#Also how do we want to represent Terminals vs. Variables (probably lowercase vs. capital)

#We may want to make a class of objects that are variables and that are terminals?



#------------------------Modifying the Stack---------------------------------------#
 #We will use lists as our stack
 #We will call it: stack
 #It will be intialized with '$'


#Function initializes the stack with '$'
#Call at the beginning (each time a new string is input to be considered)

def init_stack():
    stack = []
    stack.insert(0,'$')
    stack.insert(0,'S')
    return stack

def pop_stack(T,stack):
    stack.remove(T)
    return stack



 #Whenever we add anything, we will use the function append()
 #For example: stack.append($)

 #Remember, we will be adding to the stack in reverse order
 #For example, if the production rule says add B C to the stack:
 #  stack.append(C)
 #  stack.append(B)

 #To retrieve new item from the top of the stack use pop()
#pop() removes and returns the last item in the list

 #Random thought... Maybe, because of the way these things print...
 #We'd want to instead use insert(index,value) where index is 0
 #And then we're always adding from the front...
 #I'm not sure how this would work with removing values later...

#-------------------------Error Message Functions----------------------------------#

#When input is not accepted
#I think this occurs whenever the parse table doesn't have a recommendation?

#Example: “expected a ‘;’ instead of ‘if’”


#--------------------------Example Grammar and Parse Table-------------------------#

##S -> BC | a
##
##B -> aA | Epsilon
##
##C -> cC | Epsilon


##        a         b       c       $
##S      S->a     S->BC   S->BC   S->BC
##B               B->bB   B->Epi  B->Epi
##C                       C->cC   C->Epi

#---------------------------Parse Table Functions----------------------------------#

#We need to decide on how we want to represent functions
#I think we should probably just make class objects


#Table_Entry Class has 3 member variables
#variable is the variable read off the stack as a string
#Terminal is the input symbol read as a string
#Alpha is a list of of strings composed of Terminals and/or Variables
class Table_Entry:
    def __init__(self,var,term,a):
        self.variable = var
        self.terminal = term
        self.alpha = a
    #Member function prints the entry in desired format
    def print_entry(self):
        print("P[" + self.variable + "," + self.terminal + "] yields " + self.variable + " -> " + ''.join(self.alpha))

#List of Table_Entry Objects
Table = []
#Set all entries of the table
Table.append(Table_Entry('S','a',['a']))
Table.append(Table_Entry('S','b',['B','C']))
Table.append(Table_Entry('S','c',['B','C']))
Table.append(Table_Entry('S','$',['B','C']))
Table.append(Table_Entry('B','b',['b','B']))
Table.append(Table_Entry('B','c',['Epsilon']))
Table.append(Table_Entry('B','$',['Epsilon']))
Table.append(Table_Entry('C','c',['c','C']))
Table.append(Table_Entry('C','$',['Epsilon']))

#Prints all entries in the Table
def print_table(Table):
    for example in Table:
        example.print_entry()


#print_table(Table)

#These might not be necessary, but they are here
#Basically, it helps to define our grammar
variables = ['S','B','C']
terminals = ['a','b','c']

#--------------------------Parser Psuedo-Code (Slide 28-Week 5)-------------------#

##loop
##    T = symbol on top of stack
##    I = current input symbol
##    if T == I == $ then accept
##    elif T is a terminal or T = $ then
##        if T == I then pop T, consume the input I
##        else error
##    elif P[T,I] == alpha (means if the entry in table contains the production T -> alpha)
##        pop T and push the symbols of alpha on the stack in reverse order
##        else error
##endloop

#Functions inspired by psuedocode:
#   get_top_stack(stack) Extract top symbol from stack 
#   get_cur_in_sym(input_string) Extract the current input symbol from input string (strings act like lists with index) 
#   is_accepted(T,I) due to matching of T and I to '$'
#   is_terminal(T) to see if is a terminal (otherwise, error message)
#   is_matching_terminals(T,I) will check if yes: pop T, consume I (and then update T and I)
#       else: error message
#   print_error(T,I) basically should be able to determine whatever error we have and print a message
#       May be composed of other error detecting functions
#   look_in_table(T,I,Table) to find out alpha (and if don't find anything then error message)
#   popT(T, stack) we might not even need both of those arguments
#   push_alpha(alpha,stack) pushes in reverse order


def get_top_stack(stack):
    if stack != []:
        return stack[0]
    else:
        return False

def get_cur_in_sym(in_string):
    if in_string != []:
        return in_string[0]
    else:
        return False

def is_accepted(T,I):
    if T == '$' and I == '$':
        return True
    else:
        return False

def is_terminal(T,terminals):
    for term in terminals:
        if T == term:
            return True
        else:
            return False

def is_matching_terminal(T,I):
    if T == I:
        return True
    else:
        return False

#Removes I from the the in_string
#"Consumes" it
def consume_I(I,in_string):
    in_string.remove(I)
    return in_string

def print_error(T,I):
    print("P[" + T + "," + I + "] does not have corresponding rule in Parse Table for this Grammar")

#Iterates through table in search of matching Terminal and Variable Pair
#Returns entry if match is found
def look_in_table(T,I,Table):
    for entry in Table:
        if T == entry.variable and I == entry.terminal:
            entry.print_entry()
            return entry
    print_error(T,I)
    return False

def entry_exists(entry):
    if entry == False:
        return False
    else:
        return True

#See above for pop_stack(stack) function

#According to the entry in parse table, pushes alpha (in reverse) to the stack
def push_alpha(entry,stack):
    if entry.alpha == ['Epsilon']:
        return stack
    alpha_reverse = list(entry.alpha)
    alpha_reverse.reverse()
    for val in alpha_reverse:
        stack.insert(0,val)
    return stack

#--------------------------Function Calls------------------------------------------#

#This is usually where I kind of write the "Main Function"
#I also tend to do a lot of testing down here

#Initializing the stack
stack = init_stack()


in_string = ['b','c','c','$']
count = 0

while len(in_string) > 0 and count < 15:
    T = get_top_stack(stack)
    I = get_cur_in_sym(in_string)
    print("Stack: " + ''.join(stack))
    print("Input: " + ''.join(in_string))
    print('T: ' + T + " I: " + I)
    if is_accepted(T,I):
        print("String is Accepted!")
    if T == I:
        stack = pop_stack(T,stack)
        in_string = consume_I(I, in_string)
    elif is_terminal(T, terminals):
        print('We found a terminal in the stack!')
        if is_matching_terminal(T, I):
            stack = pop_stack(T, stack)
            in_string = consume_I(I, in_string)
            print("New stack: " + ''.join(stack) + "Remaining Input: " + ''.join(in_string))
        else:
            print_error(T,I)
    else:
        entry = look_in_table(T, I, Table)
        if entry_exists(entry):
            stack = pop_stack(T, stack)
            stack = push_alpha(entry,stack)
        else:
            print_error(T,I)
    count = count + 1
                
            
##loop
##    T = symbol on top of stack
##    I = current input symbol
##    if T == I == $ then accept
##    elif T is a terminal or T = $ then
##        if T == I then pop T, consume the input I
##        else error
##    elif P[T,I] == alpha (means if the entry in table contains the production T -> alpha)
##        pop T and push the symbols of alpha on the stack in reverse order
##        else error
##endloop

