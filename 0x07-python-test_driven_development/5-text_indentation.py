#!/usr/bin/python3
"""print text with two new lines."""

def text_indentation(text):
    """
    print text with two new lines
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sep = [".", "?", ":"]
    lines = []
    current_line = ""

    for char in text:
        current_line += char
        if char in sep:
            lines.append(current_line.strip())
            lines.append("")
            current_line = ""

    lines.append(current_line.strip())

    for line in lines:
        print(line)
