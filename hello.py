# Michael Schumaker
# Building Research Software

# Simple Hello World, argument parsing, and documentation tutorial code

import argparse

# refactor the hello world program as a function
# rewrite the command-line arguments as function parameters
# write a docstring for the function
# call the hello world function based on the parsed arguments

def hello_world_greeting(name : str, repeats : int, goodbye : bool) -> str:
    """A function to generate a string message based on function parameters.

    This function generates a string that may consist of multiple lines,
    separated by newlines. The number of lines is determined by the repeats argument.
    Each line begins with either 'Hello' or 'Goodbye', depending on the value of
    the goodbye argument. If True, each line begins with 'Goodbye', if False, 'Hello'.
    Each line ends with the text in the name argument and an exclamation mark.

    Parameters
    ----------
    name : str
        The name of the person or other definite article to direct a greeting to.

    repeats : int
        The number of repetitions of the same greeting, separated by newlines.

    goodbye : bool
        If goodbye is true, say 'Goodbye', if false, say 'Hello'.

    Returns
    -------
    greeting : str
        The full text of the greeting as a string, including newlines.

    Examples
    --------
    >> print(hello_world_greeting("World", 2, False))
    Hello World!
    Hello World!

    >> print(hello_world_greeting("2023", 1, True))
    Goodbye 2023!
    """

    greeting = ""
    one_line = f"{'Goodbye' if goodbye else 'Hello'} {name}!"
    greet_list = []
    for x in range(the_args.repeats):
        greet_list.append(one_line)
    greeting = '\n'.join(greet_list)
    return greeting
# end hello_world_greeting

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

###### MAIN ###### 
the_args = the_parser.parse_args()

message_out = hello_world_greeting(the_args.name, the_args.repeats, the_args.goodbye)
print(message_out)


