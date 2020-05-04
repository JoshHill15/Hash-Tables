



capacity = 2
def hash_djb2(s):
    hash = 5381
    for x in s:
        hash = ((hash << 5) + hash) + ord(x)
    hash = hash % capacity
    return hash & 0xFFFFFFFF


print(hash_djb2("line_3"))
