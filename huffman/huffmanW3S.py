class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

nodes = []

def calculate_frequencies(word):
    frequencies = {}
    for c in word:
        if c not in frequencies:
            freq = word.count(c)
            node = Node(c, freq)
            nodes.append(node)
def generate_huffman_tree():
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)

        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        nodes.append(merged)
    return nodes[0]

def generate_huffman_coding(node, current_code, codes):
    if node is None:
        return
    
    if node.char is not None:
        codes[node.char] = current_code
    
    generate_huffman_coding(node.left, current_code + '0', codes)
    generate_huffman_coding(node.right, current_code + '1', codes)

def huffman_encode(word):
    global nodes
    nodes = []
    calculate_frequencies(word)
    root = generate_huffman_tree()
    codes = {}
    generate_huffman_coding(root,'', codes)
    return codes

def huffman_decoding(encoded_word, codes):
    current_code = ''
    decoded_chars = []

    decoding_codes = {v: k for k,v in codes.items()}

    for c in encoded_word:
        current_code += c
        if current_code in decoding_codes:
            decoded_chars.append(decoding_codes[current_code])
            current_code = ''
    
    return ''.join(decoded_chars)
        


        
    