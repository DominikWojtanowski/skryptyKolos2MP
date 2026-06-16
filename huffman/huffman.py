# Huffman Coding in python

string = 'BCAADDDCCACACAC'

# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)

def huffman_encoding(node, binString = ''):
    if type(node) is str:
        return {node: binString}
    
    (l,r) = node.children()
    d = dict()
    d.update(huffman_encoding(l, binString + '0'))
    d.update(huffman_encoding(r,binString+'1'))

    return d
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

nodes = sorted(freq.items(), key=lambda x: x[1], reverse=True)
while len(nodes) > 1:
    (k1, c1) = nodes[-1]
    (k2,c2) = nodes[-2]

    nodes = nodes[:-2]
    node = NodeTree(k1,k2)

    nodes.append((node,c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_encoding(nodes[0][0])
