# The below is a script to help recall the details of the data types(structures) in python.
# This script was written with Microsoft Copilot.
# Date: 11/20/2024

def describe_data_types():
    data_types = {
        "List": {
            "example": [1, 2, 3],
            "mutable": True,
            "ordered": True,
            "allows_repetition": True,
            "brackets": "square brackets []"
        },
        "Set": {
            "example": {1, 2, 3},
            "mutable": True,
            "ordered": False,
            "allows_repetition": False,
            "brackets": "curly braces {}"
        },
        "Tuple": {
            "example": (1, 2, 3),
            "mutable": False,
            "ordered": True,
            "allows_repetition": True,
            "brackets": "parentheses ()"
        },
        "Dictionary": {
            "example": {"key1": "value1", "key2": "value2"},
            "mutable": True,
            "ordered": True,  # As of Python 3.7, dictionaries maintain insertion order
            "allows_repetition": False,  # Keys must be unique
            "brackets": "curly braces {}"
        }
    }

    for data_type, details in data_types.items():
        print(f"{data_type}:")
        print(f"  Example: {details['example']}")
        print(f"  Mutable: {'Yes' if details['mutable'] else 'No'}")
        print(f"  Ordered: {'Yes' if details['ordered'] else 'No'}")
        print(f"  Allows Repetition: {'Yes' if details['allows_repetition'] else 'No'}")
        print(f"  Brackets: {details['brackets']}\n")

if __name__ == "__main__":
    describe_data_types()
