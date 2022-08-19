import json
import re
from typing import Any


def convert_array(blob: str) -> str:
    """
    Convert the array portion of a struct blob to a json
    format.

    Args:
        blob (str): The blob of text that contains array<>

    Returns:
        str
    """
    new_word: str = ""
    last_six = []
    is_array = False
    left = 1
    right = 0
    for letter in blob:
        if len(last_six) < 6:
            last_six.append(letter)
        if "".join(last_six) == "array<":
            is_array = True
            new_word += "["
        elif is_array:
            if letter == "<":
                left += 1
            elif letter == ">":
                right += 1

            if left == right and letter == ">":
                new_word += "]"
                is_array = False
                left = 1
                right = 0
            else:
                new_word += letter
        else:
            new_word += letter

        if len(last_six) == 6:
            last_six.pop(0)
    return new_word


def clean_struct(blob: str) -> dict[str, Any]:
    """
    Clean the struct blob of text into a dictionary that can
    be dumped to JSON.

    Args:
        blob (str): The struct blob to convert

    Returns:
        (str)
    """
    blob = convert_array(blob)
    pattern = re.compile(r"([A-Za-z0-9_]+)")
    blob = blob.replace("struct<", "{").replace(">", "}").replace("array", "")
    blob = re.sub(pattern, r'"\1"', blob)
    json_blob = json.loads(blob)
    return json_blob
