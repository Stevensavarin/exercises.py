# ' '.join(chickens)
# creative[0]
# creative[-4]
# type(website[0])
# len(website[0])
# website[0] == website[0:1] == 'e'
# <str>[<start>:stop:<step>]
# <str>.split(<separator>) 
# cat_ipsum.split()
# cat_ipsum.split()[-1]
# for index, item in enumerate(<str>)

"""Functions for creating, transforming, and adding prefixes to strings."""

def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    
    prefix = "un"
    return prefix + word

print(add_prefix_un("happy"))
print(add_prefix_un("manageable"))


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    return f"{prefix} :: {' :: '.join([prefix + word for word in vocab_words[1:]])}"

vocab_words = ['en', 'close', 'joy', 'lighten']
result = make_word_groups(vocab_words)
print(result)

vocab_words = ['pre', 'serve', 'dispose', 'position']
result = make_word_groups(vocab_words)
print(result)

vocab_words = ['auto', 'didactic', 'graph', 'mate']
result = make_word_groups(vocab_words)
print(result)

vocab_words = ['inter', 'twine', 'connected', 'dependent']
result = make_word_groups(vocab_words)
print(result)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    
    root = word[:-4]
    if root.endswith('i'):
        root = root[:-1] + 'y'
    return root

print(remove_suffix_ness("heaviness"))
print(remove_suffix_ness("sadness"))


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    words = sentence.split()

    adjective = words[index].strip('.,!?')
    verb = adjective + 'en'
    return verb

print(adjective_to_verb('I need to make that bright.', -1))
print(adjective_to_verb('It got dark as the sun set.', 2))
