import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # define the regex to match the time format 'hh:mm AM/PM'
    regex = r"(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)"

    # Use the regex to match the entire input string
    match = re.search(rf"^[regex] to {regex}$", s)

    # if the input matches pattern, convert the times
    if match:
        # Extract matched groups and convert using 'standard' function
        start_time = standard(match.group(1), match.group(2), match.group(3))
        end_time = standard(match.group(4), match.group(5), match.group(6))

        # Return the converted times in 24hr format, concatenated with 'to'
        return f"{start_time} to {end_time}"
    else:
        # Raise ValueError if input format is invalid
        raise ValueError("Invalid input format")


def standard(hr, min, period):
    # Convert the hour part to 24hr format
    if hr == "12":
        hour = "00" if period == "AM" else "12"
    else:
        hour = f"{int(hr):02}" if period == "AM" else f"{int(hr) + 12:02}"

    minute = f"{int(min):02}" if min else "00"
    return f"{hour}:{minute}"


if __name__ == "__main__":
    main()
