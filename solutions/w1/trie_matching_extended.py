# python3
import sys


def solve(text, n, patterns):
    # write your code here
    trie = build_trie(patterns)
    result = prefix_trie_matching(text, trie)
    return result


def build_trie(patterns):
    """
    Return the trie built from patterns
    in the form of a dictionary of dictionaries,
    e.g. {0:{'A':[1, False],'T':[2, True]},1:{'C':[3, True]}}
    where the key of the external dictionary is
    the node ID (integer), and the internal dictionary
    contains all the trie edges outgoing from the corresponding
    node, and the keys are the letters on those edges, and the
    values are the node IDs to which these edges lead
    and sign of pattern end.
    """
    tree = dict()
    # write your code here
    i = 0
    prev_node = -1
    current_symbol = ''
    for pattern in patterns:
        current_node = 0
        for c in pattern:
            current_symbol = c
            if current_symbol in tree.get(current_node, {}):
                # save the last current node corresponding
                # to the end of the pattern
                prev_node = current_node
                # next node in pattern traversal of trie
                current_node = tree[current_node][current_symbol][0]
            else:
                # save the last current node corresponding
                # to the end of the pattern
                prev_node = current_node
                # the next node
                i += 1
                if current_node not in tree:
                    # create new node with edge "c" to node "i"
                    tree[current_node] = {c: [i, False]}
                else:
                    # update/add new edge "c" from "current_node"
                    # to "i" node
                    tree[current_node].update({c: [i, False]})
                current_node = i
        if tree.get(prev_node, {}).get(current_symbol):
            # flag of the end of the pattern
            pattern_end_node = tree[prev_node][current_symbol]
            pattern_end_node[1] = True

    return tree


def prefix_trie_matching(text, trie):
    """
    Search for matches in the prefix trie.
    :param text: The text in which the match with patterns in the prefix trie.
    :param trie: Prefix trie.
    :return: list of matched positions.
    """
    result = []
    prev_index = -1
    for i in range(len(text)):
        symbol = text[i]
        v = 0
        j = i
        while True:
            if trie.get(v) is None:
                # reached the leaf of a branch
                # the pattern matched
                break
            elif symbol in trie.get(v, {}):
                if trie[v][symbol][1]:
                    # if the node "1" with the edge "symbol"
                    # from the outgoing node "v" has the end character of the pattern,
                    # then try to add the index "i" to the result
                    if result:
                        prev_index = result[-1]
                    if prev_index < i:
                        # Add a new non-repeating index in the text
                        result.append(i)
                # get next node in the trie of patterns
                v = trie[v][symbol][0]
                j += 1
                if j < len(text):
                    # getting the next symbol
                    symbol = text[j]
                else:
                    # reached the end of the text
                    symbol = '$'
            else:
                break
    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    patterns = []
    for i in range(n):
        patterns += [sys.stdin.readline().strip()]
    ans = solve(text, n, patterns)
    sys.stdout.write(' '.join(map(str, ans)) + '\n')
