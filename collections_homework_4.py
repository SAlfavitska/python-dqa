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
    dict_with_value_list = {}  # Creating the empty list for storing key, list of values and list if value indexes
    for i in range(len(dict_list)):  # Iterating through length of taken list of dicts
        for key, value in dict_list[i].items():  # Iterating through each key/value pair
            if key not in dict_with_value_list.keys():  # Checking if the key is not in dict_with_value_list.
                dict_with_value_list[key] = [[value], [i]]
                # If the key isn't in dict_with_value_list then add key, lists of values and value indexes
            elif key in dict_with_value_list.keys():  # Checking if the key is in dict_with_value_list.
                # If the key is already in dict_with_value_list then append its value with new one.
                dict_with_value_list[key][0].append(value)
                # Appending the index list for this value
                dict_with_value_list[key][1].append(i)
    print(f"Dict with list of value(s) and index(es) :\n{dict_with_value_list}")  # Print to console.
    return dict_with_value_list  # Return list_of_dicts


def dict_key_renaming_and_assigning_max_value(dict_with_value_list):  # Creating the function.

    """
    Takes in the dict of key:[values] pairs,
    returns the dict of renamed key and assigned the max value to it
    """

    final_dict = {}  # Creating an empty dict to store the final result.
    for key, value in dict_with_value_list.items():  # Iterating through the taken dict with list of values.
        if len(value[0]) > 1:  # If the list of values has more than one element.
            max_value = max(value[0])  # Storing max_value of the values list.
            final_dict[key + '_' + str(value[1][value[0].index(max_value)]+1)] = max_value
            # Renaming the key with _x there x is the number of dict with max value and assign the max value to it.
        else:
            final_dict[key] = value[0][0]
            # If the list of values is empty or has one element then assign the values to it.
    print(f"Final dict with renamed duplicate keys and max values:\n{final_dict}")   # Print to console.
    return final_dict  # Return final_dict


dict_key_renaming_and_assigning_max_value(generate_dict_with_value_list(generate_list_of_dicts(5, 3)))
# Calling the function.
