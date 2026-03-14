# Problem 6.27, Page 141 — Merkle-Hellman
# Label: exr:merkle
# An Introduction to the Analysis of Algorithms (4th Edition)

import random
import sys

argument = sys.argv[1] if len(sys.argv) > 1 else '-h'

def receive_binary():
    return input("Enter Binary String: ")

def super_increasing(n):
    print(n)
    a = []
    rolling_sum = 1
    for entry in n:
        a.append(rolling_sum)
        rolling_sum = 2 * rolling_sum
    return a

def farey(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def simplify(a, b):
        g = gcd(a, b)
        return (a // g, b // g)

    fs = dict()
    for i in range(1, n + 1):
        for i2 in range(1, i + 1):
            if i2 < n and i != i2:
                r = simplify(i2, i)
                fs[float(i2) / i] = r
    return [fs[k] for k in sorted(fs.keys())]

def coprime_pairs(sigma):
    q = int(random.random() * 100)
    q = q + sigma
    coprimes = farey(q)
    for item in coprimes:
        if item[1] > sigma:
            if item[0] > q // 4:
                used_pair = item
                break
    return used_pair

def public_key(w, pairs):
    beta = []
    for item in w:
        beta.append(item * pairs[0] % pairs[1])
    return beta

def encrypt(inp, beta_key):
    knapsack = 0
    counter = 0
    for item in inp:
        knapsack = knapsack + (int(item) * beta_key[counter])
        print("string: (%s)   beta: (%s)" % (item, beta_key[counter]))
        counter += 1
    return knapsack

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

def decrypt(encrypted, r, q, w):
    modular_inv = modinv(r, q)
    counter = 0
    rebuild_array = []
    decrypted_message_array = []
    decrypted_message = ""

    midcrypt = (encrypted * modular_inv) % q

    for entry in reversed(w):
        decrypted_message_array.append(0)
        if entry <= midcrypt:
            midcrypt = midcrypt - entry
            rebuild_array.append(counter)
        counter += 1

    for entry in rebuild_array:
        decrypted_message_array[entry] = 1

    decrypted_message_array.reverse()

    for item in decrypted_message_array:
        decrypted_message = decrypted_message + str(item)

    return decrypted_message

def write_encrypted_message(message):
    print('Generating encrypted.txt')
    with open('encrypted.txt', 'w') as f:
        f.write(str(message))

def write_decrypted_message(message):
    print('Generating decrypted.txt')
    with open('decrypted.txt', 'w') as f:
        f.write(str(message))

def write_public_key(key):
    print('Generating public.txt')
    with open('public.txt', 'w') as f:
        for item in key:
            f.write(str(item) + "\n")

def write_private_key(w, q, r):
    print('Generating private.txt')
    with open('private.txt', 'w') as f:
        for item in w:
            f.write(str(item) + "|")
        f.write("\n" + str(q) + "\n" + str(r))

def parse_private():
    with open("private.txt") as f:
        lines = f.readlines()
    w = lines[0].rstrip('\n').split('|')
    w.pop(-1)
    w = list(map(int, w))
    q = int(lines[1].rstrip('\n'))
    r = int(lines[2].rstrip('\n'))
    return (w, q, r)

def parse_encrypted_message():
    with open("encrypted.txt") as f:
        content = int(f.read())
    return content

def check_super_increasing(w):
    rolling_total = 0
    check = True
    for item in w:
        if item > rolling_total:
            rolling_total = rolling_total + item
        else:
            print("W is not a Super Increasing Sequence")
            check = False
            sys.exit(0)
    if check:
        print("W: %s is a Super Increasing Sequence" % (w,))

if argument == '-e':
    binary_string = str(receive_binary())
    s_i_sequence = super_increasing(binary_string)
    sigma_sequence = s_i_sequence[-1] + (s_i_sequence[-1] - 1)
    used_pairs = coprime_pairs(sigma_sequence)
    beta = public_key(s_i_sequence, used_pairs)
    encrypted_mess = encrypt(binary_string, beta)
    write_encrypted_message(encrypted_mess)
    write_public_key(beta)
    write_private_key(s_i_sequence, used_pairs[1], used_pairs[0])

elif argument == '-d':
    keys = parse_private()
    encrypted_mess = parse_encrypted_message()
    decrypted = decrypt(encrypted_mess, keys[2], keys[1], keys[0])
    print(decrypted)
    write_decrypted_message(decrypted)

elif argument == '-v':
    keys = parse_private()
    check_super_increasing(keys[0])
    print("2r[n] < B" if (2 * keys[0][-1]) < keys[1] else "2r[n] !< B")
    if egcd(keys[1], keys[2])[0] == 1:
        print("The greatest common denominator of %s and %s is 1" % (keys[1], keys[2]))
    else:
        print("The greatest common denominator of %s and %s is **NOT** 1" % (keys[1], keys[2]))
    print("The public key is as follows:")
    print(public_key(keys[0], (keys[2], keys[1])))
else:
    print('Invalid Argument Passed')
