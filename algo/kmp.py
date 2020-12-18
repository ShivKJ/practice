from typing import List


def failure_function(pattern: str) -> List[int]:
    """
    :param pattern:
    :return:
    """
    m = len(pattern)
    fail = [0] * m  # ith index is length of length of largest prefix
    # array which is also suffix of pattern[0 -> i]

    j = 1  # current index of text which is being processed
    k = 0  # will be used to store length of prefix array
    # which is also suffix up to index j

    while j < m:
        if pattern[j] == pattern[k]:
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]  # moving k to previous fail value and next
            # time jth char will be compared with kth index
        else:
            j += 1

    return fail


def kmp(text: str, pattern: str) -> int:
    """
    if we have matched pattern up to ith index and matching at (i+1)th
    fails then we find largest prefix of pattern which is also suffix of
    pattern[:i+1] and store it in "fail" attribute.

    :param text:
    :param pattern:
    :return: index where pattern matches with text. If no such index
             exists then returning -1
    """
    if not pattern:
        return 0

    if not text:
        return -1

    n, m = len(text), len(pattern)

    fail = failure_function(pattern)

    curr_index, matched_char = 0, 0

    while curr_index < n:
        if text[curr_index] == pattern[matched_char]:
            if matched_char == m - 1:
                return curr_index - m + 1  # first index from where matching with pattern starts
            curr_index += 1
            matched_char += 1
        elif matched_char > 0:
            # k = largest prefix that matched
            matched_char = fail[matched_char - 1]
        else:
            curr_index += 1

    return -1
