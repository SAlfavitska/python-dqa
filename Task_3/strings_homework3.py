from re import findall, sub, split
from os import linesep

invalid_string = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

def count_spaces(text):
    """ Takes some text, returns count of spaces in the text."""
    spaces = sum(i.isspace() for i in text)
    print(f'The count of spaces is {spaces}.')


def make_sentence(text):
    """ Takes some text, returns the sentence created from the last word of each sentence in the text."""
    sentence = ' '
    last_words = findall(r" [a-zA-Z\d]*\.", text)
    for word in last_words:
        sentence += word[:-1]
    return sentence[1:] + '.'


def put_the_sentence_on_position(sentence, position, text):
    """Takes sentence to be inserted into the text, position - the place the sentence should be inserted,
    text - the text where the sentence needs to be inserted, returns the text with inserted sentence on defined position."""
    split_text = text.splitlines()
    split_text[position] += sentence
    return '\n'.join(split_text)


def make_title(text):
    """Takes the text and returns the text with the capitalized first word in each sentence."""
    text = split('([.!?\t\n] *)', text)
    text = "".join(i.capitalize() for i in text)
    return text


def find_and_replace_text(text, regex_pattern, replacement):
    """Takes the input text, regex_pattern - to find some text by this pattern, replacement - to replace found text with,
    returns text with replaced some text in the sentences."""
    return sub(regex_pattern, replacement, text)


def remove_empty_lines(text):
    """Takes the text, returns the text without empty lines."""
    print(linesep.join([s for s in text.splitlines() if s]))


if __name__ == "__main__":
    count_spaces(invalid_string)
    remove_empty_lines(find_and_replace_text(
        make_title(put_the_sentence_on_position(make_sentence(invalid_string), 3, invalid_string)), r'\b iz\b', ' is'))
