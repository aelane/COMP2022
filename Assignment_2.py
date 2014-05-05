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


#--------------------------Print derivation and Stack------------------------------#
#Format the strings properly
#
#I think we'll want to represent terminals such as "else" as a single character like 'e' or else a variable e
#If so, we need make sure it prints out "else" instead

#Also how do we want to represent Terminals vs. Variables (probably lowercase vs. capital)

#We may want to make a class of objects that are variables and that are terminals?


#Potential Example:
##Input string (remaining) Stack
##bcc$                   S$
##bcc$                    BC$ 
##bcc$                    bBC$ 
##cc$                     BC$ 
##cc$                     C$ 
##cc$                    cC$
##c$                      C$ 
##$                       $
 




#-------------------------Error Message Functions----------------------------------#

#When input is not accepted

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



#--------------------------Parser Psuedo-Code (Slide 28-Week 5)-------------------#

##loop
##    T = symbol on top of stack
##    C = current input symbol
##    if T == C == $ then accept
##    elif T is a terminal or T = $ then
##        if T == c then pop T, consume the input c
##        else error
##    elif P[T,c] = alpha (means if the entry in table contains the production T -> alpha)
##        pop T and push the symbols of alpha on the stack in reverse order
##        else error
##endloop

#--------------------------Function Calls------------------------------------------#
