#COMP2022 Assignment 2
#----------------------------Introduction------------------------------------------#
#Written by Annie Lane and Michaela Kerem
#For Assignment 2 for COMP2022: Formal Languages and Logic
#Semester 1, 2014

#LL(1) Parser for Grammar G'
#Reads input from a .txt file
#Prints line showing remaining input and stack for each step
#Determines if input is accepted or rejected
#Provides error messages when incorrect token found
#Includes error recovery feature

#This program is organized into the following sections
#   Input Processing
#   Derivation and Stack Printing
#   Modifying the Stack
#   Error Messages
#   Parse Table Class and Function
#   Parser While Loop Functions
#   Function Calls

#----------------------------Input Processing-------------------------------------#
#This also includes functions necessary to read input .txt files

#Read .txt file by name of file
#remove leading and following white space
#remove newline characters
#concatenate 'id :=' into 'id:=' so there is no space
#split along spaces to create separate tokens
#concatenate list in tokens with the input_string
#add '$' to the end of the list to indicate end of input string
def read_input(file_name):
    file_object = open(file_name, 'r')
    input_string = []
    temp_string = []
    temp_string = file_object.readlines()
    for token in temp_string:
        token = token.strip()
        token = token.replace('\n','')
        token = token.replace('id :=','id:=')
        token = token.split(' ')
        input_string = input_string + token
    file_object.close()
    input_string.append('$')
    return input_string

output_string = read_input('accept.txt')
print(output_string)

#--------------------------Print derivation and Stack------------------------------#
#Format the strings properly
#
#I think we'll want to represent terminals such as "else" as a single character like 'e' or else a variable e
#If so, we need make sure it prints out "else" instead

#Also how do we want to represent Terminals vs. Variables (probably lowercase vs. capital)

#We may want to make a class of objects that are variables and that are terminals?

def format_input(in_string):
    return "".join(in_string)

print(format_input(output_string))

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

def error_message(T, I, Table):
    expected_terminals = []
    for entry in Table:
        if entry.variable == T:
            if entry.terminal != 'Epsilon' and entry.terminal != '$':
                expected_terminals.append(entry.terminal)
    print("Error: Expected a '" + "', '".join(expected_terminals) + "' instead of '" + I + "'")



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
Table.append(Table_Entry('P','if',['L']))
Table.append(Table_Entry('P','while',['L']))
Table.append(Table_Entry('P','id',['L']))

Table.append(Table_Entry('L','if',['I','M']))
Table.append(Table_Entry('L','while',['I','M']))
Table.append(Table_Entry('L','id',['I','M']))

Table.append(Table_Entry('M',';',[';','L']))
Table.append(Table_Entry('M','end',['Epsilon']))
Table.append(Table_Entry('M','endif',['Epsilon']))
Table.append(Table_Entry('M','$',['Epsilon']))

Table.append(Table_Entry('I','if',['C']))
Table.append(Table_Entry('I','while',['W']))
Table.append(Table_Entry('I','id',['A']))

Table.append(Table_Entry('A','id',['id',':=','E']))

Table.append(Table_Entry('C','if',['if','E','then','L','O','endif']))

Table.append(Table_Entry('O','else',['else','L']))
Table.append(Table_Entry('O','end',['Epsilon']))
Table.append(Table_Entry('O','endif',['Epsilon']))
Table.append(Table_Entry('O','$',['Epsilon']))

Table.append(Table_Entry('W','while',['while','E','do','L','end']))
 
Table.append(Table_Entry('E','c',['E2','R']))
Table.append(Table_Entry('E','id',['E2','R']))

Table.append(Table_Entry('R',';',['Epsilon']))
Table.append(Table_Entry('R','<',['Op1','E2','R']))
Table.append(Table_Entry('R','=',['Op1','E2','R']))
Table.append(Table_Entry('R','!=',['Op1','E2','R']))
Table.append(Table_Entry('R','do',['Epsilon']))
Table.append(Table_Entry('R','endif',['Epsilon']))

Table.append(Table_Entry('E2','c',['T','K']))
Table.append(Table_Entry('E2','id',['T','K']))

Table.append(Table_Entry('K',';',['Epsilon']))
Table.append(Table_Entry('K','<',['Epsilon']))
Table.append(Table_Entry('K','=',['Epsilon']))
Table.append(Table_Entry('K','!=',['Epsilon']))
Table.append(Table_Entry('K','+',['Op2','E2']))
Table.append(Table_Entry('K','-',['Op2','E2']))
Table.append(Table_Entry('K','do',['Epsilon']))
Table.append(Table_Entry('K','endif',['Epsilon']))

Table.append(Table_Entry('T','c',['c']))
Table.append(Table_Entry('T','id',['id']))

Table.append(Table_Entry('Op1','<',['<']))
Table.append(Table_Entry('Op1','=',['=']))
Table.append(Table_Entry('Op1','!=',['!=']))

Table.append(Table_Entry('Op2','+',['+']))
Table.append(Table_Entry('Op2','-',['-']))

#Table.append(Table_Entry('S','a',['a']))
#Table.append(Table_Entry('S','b',['B','C']))
#Table.append(Table_Entry('S','c',['B','C']))
#Table.append(Table_Entry('S','$',['B','C']))
#Table.append(Table_Entry('B','b',['b','B']))
#Table.append(Table_Entry('B','c',['Epsilon']))
#Table.append(Table_Entry('B','$',['Epsilon']))
#Table.append(Table_Entry('C','c',['c','C']))
#Table.append(Table_Entry('C','$',['Epsilon']))

#Prints all entries in the Table
def print_table(Table):
    for example in Table:
        example.print_entry()

#print_table(Table)


#These might not be necessary, but they are here at least for reference

#Basically, it helps to define our grammar
variables = ['P','L','M','I','A','C','O','W','E','R','E2','K','T','Op1','Op2'] 
#['S','B','C']
terminals = ['id', 'if', 'while', ';', 'else', 'c', '<', '=', '!=', '+', '-']
#['a','b','c']

#--------------------------Functions for Parser While Loop-------------------#

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

#Extract top symbol from stack
def get_top_stack(stack):
    if stack != []:
        return stack[0]
    else:
        return False

#Extract the current input symbol from input string
def get_cur_in_sym(in_string):
    if in_string != []:
        return in_string[0]
    else:
        return False

#True when T and I match to '$' (so the input is accepted)
def is_accepted(T,I):
    if T == '$' and I == '$':
        return True
    else:
        return False

#compares top of stack to list of terminals to see if it is a terminal
#Otherwise, produces an error message
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


in_string = ['b','c','a','$']
count = 0

error_message('S','z',Table)


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
            error_message(T,I,Table)
    else:
        entry = look_in_table(T, I, Table)
        if entry_exists(entry):
            stack = pop_stack(T, stack)
            stack = push_alpha(entry,stack)
        else:
            error_message(T,I,Table)
    count = count + 1
                


