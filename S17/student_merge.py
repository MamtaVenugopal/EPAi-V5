from collections import defaultdict
from collections import Counter
from collections import OrderedDict
def merge_with_defaultdict(*dicts):
    """Merges word frequency dictionaries using defaultdict.

    Args:
        *dicts: Any number of word frequency dictionaries.

    Returns:
        A merged dictionary containing all the words and their combined frequencies.
    """

    merged_dict = defaultdict(int)  # Use int to set default value to 0
    for dictionary in dicts:

        for word, frequency in dictionary.items():
            merged_dict[word] += frequency  # Automatically handles missing keys

    # Sort by values (descending order)
    sorted_dict = dict(sorted(merged_dict.items(), key=lambda item: item[1], reverse=True))
    print(sorted_dict)
    return sorted_dict  # Convert back to regular dictionary if needed


def merge_with_counter(*dicts):
    """Merges word frequency dictionaries using Counter.

    Args:
        *dicts: Any number of word frequency dictionaries.

    Returns:
        A merged dictionary containing all the words and their combined frequencies.
    """

    merged_counter = Counter()
    for dictionary in dicts:
        merged_counter.update(dictionary)  # Update counter with each dictionary
    sorted_dict = dict(sorted(merged_counter.items(), key=lambda item: item[1], reverse=True))
    print(sorted_dict)
    return dict(sorted_dict)  # Convert back to a regular dictionary