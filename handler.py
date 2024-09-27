"""
This module contains a handler function for a serverless HTTP API.
"""

import json
import random


def print_good_old_fashioned_christmas_tree(height=10, log_height=3, log_width=3):
    """
    Print a good old fashioned Christmas tree.
    """
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (i * 2 - 1))
    for i in range(1, log_height + 1):
        print(" " * (height - log_width // 2 - 1) + "|" * log_width)


def print_colorful_christmas_tree(height=10, with_decorations=True):
    """
    Print a colorful Christmas tree with optional decorations.

    :param height: The height of the tree (default 10)
    :param with_decorations: Whether to add decorations (default True)
    """
    GREEN = "\033[32m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"

    decorations = ["o", "8", "@"] if with_decorations else [" "]

    for i in range(1, height):
        spaces = " " * (height - i)
        if with_decorations:
            row = [
                random.choice(
                    [
                        GREEN + "^",
                        random.choice([RED, YELLOW]) + random.choice(decorations),
                    ]
                )
                for _ in range(i * 2 - 1)
            ]
        else:
            row = [GREEN + "*" for _ in range(i * 2 - 1)]
        print(spaces + "".join(row) + RESET)

    # Print the trunk
    trunk_width = max(height // 6, 1)
    for _ in range(height // 3):
        print(
            " " * (height - trunk_width) + YELLOW + "|" * (trunk_width * 2 - 1) + RESET
        )


def hello(event, context):
    body = {
        "message": "Go Serverless v4.0! Your function executed successfully!",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    print_good_old_fashioned_christmas_tree()
    print_good_old_fashioned_christmas_tree(4, 2, 2)
    print_good_old_fashioned_christmas_tree(6, 3, 3)
    print_good_old_fashioned_christmas_tree(6, 4, 4)
    print_good_old_fashioned_christmas_tree(8, 5, 5)
    print_colorful_christmas_tree(10, True)

    return response
