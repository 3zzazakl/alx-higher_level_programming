#!/usr/bin/python3
"""print text with two new lines."""


def text_indentation(text):
    """
    print text with two new lines
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delim = (".", "?", ":")

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        new = ""
        for i in text:
            new += i
            if i in delim:
                print(new.strip(), end="\n\n")
                new = ""
        print(new.strip(), end="")
