#!/usr/bin/env python3

def print_fibonacci(length):
    
    if length == 0:
        fib_sequence = []  # Initialize an empty sequence for length 0
    elif length == 1:
        fib_sequence = [0]  # Initialize sequence with 0 for length 1
    else:
        fib_sequence = [0, 1]  # Initialize sequence with 0 and 1
        while len(fib_sequence) < length:
            next_number = fib_sequence[-1] + fib_sequence[-2]  # Calculate the next number in the sequence
            fib_sequence.append(next_number)  # Add the next number to the sequence
    print(fib_sequence)  # Print the Fibonacci sequence
