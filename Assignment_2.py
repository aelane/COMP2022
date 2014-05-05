#COMP2022 Assignment 2

#This is Annie

#Hi!

#----------------------------Input Processing Functions----------------------------#
#This also includes functions necessary to read input .txt files

#Read file
#file_object = open(filename, mode) where file_object is the variable to put the file object.
#mode is just 'r' since we are just reading
#file_object.close() in order to close the file

#Remove spaces and line breaks (CRs)
#supposedly that's just string.strip() but we can look that up

#Add $ to end of string to indicate end of string





#---------------------------Parse Table Functions----------------------------------#

#We need to decide on how we want to represent functions



#--------------------------Parser Psuedo-Code (Slide 28)---------------------------------#

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
