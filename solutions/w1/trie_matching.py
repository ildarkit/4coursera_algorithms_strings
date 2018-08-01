# python3
import sys

NA = -1


class Node:
    def __init__ (self):
        self.next = [NA] * 4


def solve(text, n, patterns):
    # write your code here
    trie = build_trie(patterns)
    result = prefix_trie_matching(text, trie)
    return result


def build_trie(patterns):
    """
    Return the trie built from patterns
    in the form of a dictionary of dictionaries,
    e.g. {0:{'A':1,'T':2},1:{'C':3}}
    where the key of the external dictionary is
    the node ID (integer), and the internal dictionary
    contains all the trie edges outgoing from the corresponding
    node, and the keys are the letters on those edges, and the
    values are the node IDs to which these edges lead.
    """
    tree = dict()
    # write your code here
    i = 0
    for pattern in patterns:
        current_node = 0
        for c in pattern:
            current_symbol = c
            if current_symbol in tree.get(current_node, {}):
                current_node = tree[current_node][current_symbol]
            else:
                i += 1
                if current_node not in tree:
                    tree[current_node] = {c: i}
                else:
                    tree[current_node].update({c: i})
                current_node = i
    return tree


def prefix_trie_matching(text, trie):
    result = []
    for i in range(len(text)):
        symbol = text[i]
        v = 0
        j = i
        while True:
            if trie.get(v) is None:
                result.append(i)
                break
            elif symbol in trie.get(v, {}):
                j += 1
                if j < len(text):
                    symbol = text[j]
                else:
                    break
                v = trie[v][symbol]
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
