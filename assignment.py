def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"My name is {name} and I am {age} years old"


def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
        return "Greater"
    elif number == 10:
        return "Equal"
    else:
        return "Lesser"

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    t=0
    for i in range(1,n+1):
        t += i
    return t

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, maximum, minimum

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    student_name = []
    for name, score in students_dict.items():
        if score > 80:
            student_name.append(name)
    return student_name

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    common_elements=set()
    for x in list1:
        for y in list2:
            if x == y:
                common_elements.add(x)
    return common_elements

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    addition = a+b
    subtraction = a-b
    multiplication = a*b
    division = a/b
    return {"sum":addition,
            "difference":subtraction,
            "product":multiplication,
            "quotient":division}

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    and_result=  x and y
    or_result = x or y
    not_x_result = not x
    not_y_result= not y
    return {"and":and_result,"or":or_result,"not_x":not_x_result,'"not_y"':not_y_result}

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    return { "and" : a & b,
    "or" : a | b,
    "xor" : a ^ b,
    }
