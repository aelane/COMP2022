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


#--------------------------Print derivation and Stack------------------------------#
#Format the strings properly
#
#I think we'll want to represent terminals such as "else" as a single character like 'e' or else a variable e
#If so, we need make sure it prints out "else" instead

#Also how do we want to represent Terminals vs. Variables (probably lowercase vs. capital)

#We may want to make a class of objects that are variables and that are terminals?


#Potential Example:
##Reading input string 'bcc'
##Input string (remaining) Stack
##bcc$                   S$
##bcc$                    BC$ 
##bcc$                    bBC$ 
##cc$                     BC$ 
##cc$                     C$ 
##cc$                    cC$
##c$                      C$ 
##$                       $
 

#------------------------Modifying the Stack---------------------------------------#
 #We will use lists as our stack
 #We will call it: stack
 #It will be intialized with '$'

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
#   look_in_table(T,I) to find out alpha (and if don't find anything then error message)
#   popT(T, stack) we might not even need both of those arguments
#   push_alpha(alpha,stack) pushes in reverse order



#--------------------------Function Calls------------------------------------------#

#This is usually where I kind of write the "Main Function"
#I also tend to do a lot of testing down here




