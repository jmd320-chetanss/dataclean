import math
import re


def remove_duplicates(lst: list) -> list:
    """
    Remove duplicates from a list while preserving the order.

    Args:
        lst (list): The input list from which duplicates need to be removed.

    Returns:
        list: A new list with duplicates removed.
    """
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]


def floor_float(value: float, decimal_places: int = 2) -> float:
    """
    Floor a float value to a specified number of decimal places.

    Args:
        value (float): The float value to floor.
        decimal_places (int): The number of decimal places to keep. Defaults to 2.

    Returns:
        float: The floored float value.
    """
    factor = 10**decimal_places
    return math.floor(value * factor) / factor


def parse_int(value: str) -> int | None:
    try:
        return int(value)
    except ValueError:
        return None


def parse_float(value: str) -> float | None:
    try:
        return float(value)
    except ValueError:
        return None


def to_snake_case(text: str) -> str:
    """
    Convert a given string to snake_case.

    Args:
        text (str): The input string to convert.

    Returns:
        str: The converted string in snake_case.
    """
    text = text.strip()
    text = re.sub(r"([a-z])([A-Z])", r"\1_\2", text)
    text = re.sub(r"\W+", "_", text)
    text = re.sub(r"_+", "_", text)
    text = text.lower()
    return text


def to_pascal_case(text: str) -> str:
    """
    Convert a given string to PascalCase.

    Args:
        text (str): The input string to convert.

    Returns:
        str: The converted string in PascalCase.
    """
    words = re.split(r"[\W_]+", text)
    return "".join(word.capitalize() for word in words if word)


def to_camel_case(text: str) -> str:
    """
    Convert a given string to camelCase.

    Args:
        text (str): The input string to convert.

    Returns:
        str: The converted string in camelCase.
    """
    if text == "":
        return ""
    words = re.split(r"[\W_]+", text)
    return words[0].lower() + "".join(word.capitalize() for word in words[1:] if word)
