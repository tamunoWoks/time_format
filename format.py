import re

def main():
    ...


def convert(s):
    #define the regex to match the time format 'hh:mm AM/PM'
    regex = r'(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)'

    #Use the regex to match the entire input string
    match = re.search(rf'^[regex] to {regex}$', s)



if __name__ == '__main__':
    main()

