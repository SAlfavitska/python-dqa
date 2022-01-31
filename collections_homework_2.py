from random import randrange, choice  # Library used to generate random integers
from string import ascii_lowercase  # Library used to get ascii_lowercase letters


def generate_list_of_dicts(dict_count, number_key_value_pairs):  # Creating the function.
    """
    Takes in a number dict_count - count of dicts to be in list,
    number_key_value_pair - number of key-value pairs to be in each dict,
    returns the list of dicts with random key, value
    """
    list_of_dicts = []  # Creating an empty list to inserting dicts.
    for i in range(dict_count):  # Iterate through number of dicts
        keys = [choice(ascii_lowercase) for m in range(number_key_value_pairs)]
        # Generating list of random key letters in range of number_key_value_pair.
        values = [randrange(0, 10, 1) for k in range(number_key_value_pairs)]
        # Generating list of random value numbers in range of number_key_value_pair.
        random_dict = {k: v for k, v in zip(keys, values)}
        # Creating dict using random keys, values generated above
        list_of_dicts.append(random_dict)  # Appending dict generated on previous step to the list_of_dicts.
        dict_count -= 1  # Decrementing the dict_count by 1
    print(f"List of random dict(s):\n{list_of_dicts}")  # Printing to console.
    return list_of_dicts  # Returning the list_of_dicts.


# list_of_dicts = [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}, {'a': 8, 'c': 35, 'g': 42}]
# list of dicts with duplicate keys for testing purposes
# print(f"List of random dict(s):\n{list_of_dicts}")  # Print to console.


def generate_dict_with_value_list(dict_list):  # Creating the function.
    """
    Takes in list of dicts (dict_list),
    returns the dict with key and list of value(s) for each key
    """
    dict_with_value_list = {}  # Creating the empty list for storing key and list of values per key.
    for each_dict in dict_list:  # Iterating through taken list of dicts.
        for key, value in each_dict.items():  # Iterating through key, value in each dict.
            if key in dict_with_value_list:  # Checking if the key is in dict_with_value_list.
                dict_with_value_list[key].append(value)
                # If the key is already in dict_with_value_list then append its value with new one.
            else:
                dict_with_value_list[key] = [value]
                # If key is not in dict_with_value_list then just insert key and value as list.
    print(f"Dict with list of value(s):\n{dict_with_value_list}")  # Print to console.
    return dict_with_value_list  # Return list_of_dicts


def dict_key_renaming_and_assigning_max_value(dict_with_value_list):  # Creating the function.

    """
    Takes in the dict of key:[values] pairs,
    returns the dict of renamed key and assigned the max value to it
    """

    final_dict = {}  # Creating an empty dict to store the final result.
    for key, value in dict_with_value_list.items():  # Iterating through the taken dict with list of values.
        if len(value) > 1:  # If the list of values has more than one element.
            max_index = value.index(max(value))  # Storing in max_index the index of max value in values list.
            final_dict[key + '_' + str(max_index + 1)] = max(value)
            # Renaming the key with _max_index and assign the max value to it.
        else:
            final_dict[key] = value[0]
            # If the list of values is empty or has one element then assign the values to it.
    print(f"Final dict with renamed duplicate keys and max values:\n{final_dict}")   # Print to console.
    return final_dict  # Return final_dict


dict_key_renaming_and_assigning_max_value(generate_dict_with_value_list(generate_list_of_dicts(1, 0)))
# Calling the function.
# dict_kye_renaming(generate_dict_with_value_list(list_of_dicts))  # for testing purposes
