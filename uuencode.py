from itertools import zip_longest

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

def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"""
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

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
    """ take a list of strings as the argument, and return a list
        of uuencoded strings """
    encoded_output = []
    three_char_lines = []
    encoded_string = ''

    for char in string:
        three_char_blocks = grouper(char, 3, fillvalue='0')
        three_char_lines.append(three_char_blocks)

    for three_char_line in three_char_lines:
        for three_char_block in three_char_line:
            # three_char_block will be = ['char1', 'char2', 'char3']
            # the last three_char_block will be = ['char1', 'char2', '0']
            # if there are an uneven amount of 3 character blocks
            three_char_string = ''.join(three_char_block)
            binary_string = make_bin_string(three_char_string)
            binary_string_split = split_into_6(binary_string)
            encoded_char_block = add32(binary_string_split)
            encoded_string += encoded_char_block

    # create the length value for the beginning of each line 
    #for line in string:
        #length_value = chr(len(line) + 32)

    # break the encoded string into a list of 60 characters each
    substrings = [encoded_string[x:x+60] for x in
                  range(0, len(encoded_string), 60)]

    for i in range(len(substrings)):
        print(substrings[i])
    
my_input = 'I feel very strongly about you doing duty. Would you give \
me a little more documentation about your reading in French? \
I am glad you are happy - but I never believe much in happiness. \
I never believe in misery either. Those are things you see on the \
stage or the screen or the printed pages, they never really happen \
to you in life.'

formatted_input = split_lines(my_input)
uuencode(formatted_input)
