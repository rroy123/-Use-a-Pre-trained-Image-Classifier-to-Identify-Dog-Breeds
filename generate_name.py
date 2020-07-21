'''
Helper function to make word lower case and to remove whitespaces
'''
def generate_name(input_name):
    #makes iterator
    i = 0
    #iterates through each character in word
    for element in range(0, len(input_name)-1):
        #defines current_char as the current character
        current_char = input_name[element]
        #finds index of the last character that is not a number
        if current_char.isalpha() or current_char == '_':
            i = i + 1
        #creates temporary variable that removes everything after the last alphabetic/non underscore character
        temp1 = input_name[0 : i-2]
        #creates temporary variable that replaces underscores with spaces
        temp2 = temp1.replace("_", " ")
        #creates temporary variable that makes the name lower case
        temp3 = temp2.lower()
        #creates variable 'output_name' that strips whitespaces from previously defined name
        output_name = temp3.strip()     
    #returns updated name
    return(output_name)
