
def dec_to_bin(number):
    """ take int number as the argument, and return
        number in 8 bit binary as a string. """
    binary = format(number, 'b')
    if len(binary) < 8:
        zeroes = 8 - len(binary)
        binary = ('0' * zeroes) + binary
    return binary

def make_bin_string(string):
    """ take str string as the argument, and return
        the ordinal values of the characters in string
        as 8 bit binary as a str. """
    binary_string = ''
    for char in string:
        ordinal = ord(char)
        binary_string += dec_to_bin(ordinal)
    return binary_string

def split_into_6(string):
    """ take str string as the argument, and split
        into 4 6-bit groupings. Return as a list """
    the_list = []
    offset = 6
    for i in range(4):
        slice_left = offset * i
        slice_right = offset * (i+1)
        the_list += [string[slice_left:slice_right]] 
    return the_list

def add32(the_list):
    """ take list the_list containing 4 strings of 6-bit
        binary as the argument, convert each string to
        decimal, add 32, convert to ASCII, and return the
        result """
    string = ''
    for item in the_list:
        decimal_value = int(item, 2)
        new_char = chr(decimal_value + 32)
        string += new_char
    return string

def split_lines(string):
    """ takes a str string as the argument, and splits it
        into a list of strings, each 45 characters in length """
    line_list = []
    new_line = ''
    count = 0
    for char in string:
        if count < 45:
            new_line += char
            count += 1
        else:
            line_list.append(new_line)
            new_line = ''
            new_line += char
            count = 1
    line_list.append(new_line)
    return line_list

def uuencode(string):
    three_chars = ''
    for i in range(3):
        three_chars += string[i]

    binary_string = make_bin_string(three_chars)
    binary_string_split = split_into_6(binary_string)
    print(add32(binary_string_split))
    
    
my_input = 'I feel very strongly about you doing duty. Would you give \
me a little more documentation about your reading in French? \
I am glad you are happy — but I never believe much in happiness. \
I never believe in misery either. Those are things you see on the \
stage or the screen or the printed pages, they never really happen \
to you in life.'

formatted_input = split_lines(my_input)
uuencode(formatted_input[0])
