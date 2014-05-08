def read_input_file(file_name):
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

def user_input_filename():
    file_name = input("Please enter the name of a file to parse: ")
    if file_name.lower() == "exit":
        return "exit"
    input_string = read_input_file(file_name.lower())
    return input_string

user_input = user_input_filename()
print(user_input)
