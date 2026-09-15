# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Just replace each `pass` with your code, using `return` to send the answer
# back (not `print`).


def seconds_to_hms(total_seconds):
    # TODO (Part 1): return the time as a string "H:MM:SS"
    #   e.g. seconds_to_hms(3661) should return "1:01:01"

    hours = total_seconds // 3600
    time_remaining = total_seconds - (hours * 3600)
    minutes = time_remaining // 60
    time_remaining = time_remaining -(minutes * 60)
    seconds = time_remaining
    time = f"{hours}:{minutes:02d}:{seconds:02d}"
    return time


def admission_price(age):
    # TODO (Part 2): return the ticket price (a number) for someone of this age
    if age < 5:
        price = 0
    elif age < 13:
        price = 8
    elif age < 65:
        price = 15
    else:
        price = 10
    return price



def sum_multiples(limit):
    # TODO (Part 3): return the sum of every whole number below `limit`
    #   that is a multiple of 3 or of 5
    
    # Multiples of 3
    count_3 = 0
    for i in range(limit):
        if i % 3 == 0 and i != 0:
            count_3 += 1

    sum_multiples_3 = 0
    for i in range (count_3):
        current_multiple_3 = (i * 3) + 3
        sum_multiples_3 += current_multiple_3

    # Multiples of 5
    count_5 = 0
    for i in range(limit):
        if i % 5 == 0 and i != 0:
            count_5 += 1

    sum_multiples_5 = 0
    for i in range (count_5):
        current_multiple_5 = (i * 5) + 5
        if current_multiple_5 % 3 != 0:
            sum_multiples_5 += current_multiple_5

    return sum_multiples_3 + sum_multiples_5


def total_of_positives(numbers):
    # TODO (Part 4 - STRETCH, optional): return the sum of just the
    #   positive numbers in the list `numbers`
    sum_pos = 0
    for i in range(len(numbers)):
        if int(numbers[i]) > 0:
            current_pos = int(numbers[i])
            sum_pos += current_pos
    return sum_pos



def main():
    # Optional scratch space - use this to try your functions with sample values.
    # Uncomment a line and run `python lab02.py` to see the result.
    # print(seconds_to_hms(3661))            # 1:01:01
    # print(admission_price(10))             # 8
    # print(sum_multiples(10))               # 23
    # print(total_of_positives([1, -2, 3]))  # 4
    pass


if __name__ == "__main__":
    main()
