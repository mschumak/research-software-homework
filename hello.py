# Michael Schumaker
# Building Research Software

# Simple Hello World and argument parsing tutorial code

import argparse

# print("Hello World!")

the_parser = argparse.ArgumentParser(description="Simple Hello World and argument parsing tutorial code.")
the_parser.add_argument(
    'name',
    default="World",
    type=str,
    nargs="?",
    help="Enter a name for the program to offer greetings to.",
)

the_parser.add_argument(
    '--repeats',
    '-r',
    type=int,
    default=1,
    help="The number of times to write the greeting."
)

the_parser.add_argument(
    '--goodbye',
    '-g',
    action="store_true",
    help="I don't know why you say, 'Goodbye', I say, 'Hello!'"
)

# 
the_args = the_parser.parse_args()

the_message = f"{'Goodbye' if the_args.goodbye else 'Hello'} {the_args.name}!"

for x in range(the_args.repeats):
    print(the_message)


