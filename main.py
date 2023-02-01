# Read arabic text
# Created by Terry Chang - Jan 30, 2023

def read_arabic(file_location='sample_data/iq-2021-annual-report-arabic.txt'):  # default file location
    with open(file_location) as raw_file:
        with open('output_file.txt', 'w') as output_file:
            reader = False
            line_to_write = []  # write line by line
            for line in raw_file:
                line = line.strip()  # skip the space
                source_line = False  # check if the line contains <source ...>
                end_line = False
                if line.startswith('<source'):
                    reader = True
                    source_line = True
                elif line.startswith('</source'):
                    reader = False
                    # write the whole list as a string (in reverse order) into the output file
                    for word in line_to_write[::-1]:
                        output_file.write(word)
                    output_file.write('\n')
                    line_to_write = []  # clear the list
                if reader and not source_line:   # skip the source line ( start line is the next line to the start line)
                    line_to_write.append(extract(line))


def extract(raw_string):  # 保留第一次出现'>'到最后一次出现'<'之间的全部字符
    return raw_string.split('>', 1)[1].rsplit('<', 1)[0]


# l leave the input validation function
def input_validation(file_location):
    pass


if __name__ == '__main__':
    # input
    # file_location = input('Enter file location: ')
    # input validation skipped
    read_arabic()  # pass input file path as parameter

