s = [x for x in range(256)]

k = 'saputra1'
p = '2028'
# p = 'äSªx'
# p = 'äRªz'
k = [ord(x) for x in k]
# p = [ord(x) for x in p]
# print(k[1])
# print(type(k[1]))

j = 0
for i in range(len(k)):
    j = (j + s[i] + k[i % len(k)]) % 256
    s[i], s[j] = s[j], s[i]
# print(s)
# print("===========================")

i, j = 0, 0
ks = []
for i in range(len(p)):
    i = (i+1) % 256
    j = (j+s[i]) % 256
    s[i], s[j] = s[j], s[i]
    t = (s[i]+s[j]) % 256
    keys = (s[t])
    ks.append(keys)
print("keystream:")
print(ks)

chip = []
for i in range(len(p)):
    c = ((ks[i]) ^ ord(p[i]))
    chip.append(c)
print("hasil XOR (desimal chiperteks):")
print(chip)
print("chiperteks:")
for x in chip:
    print(chr(x), end='')
# c = ord(s[t])
# print(c, end=' ')
# c = (ord(s[t]) ^ ord(char)), 'x'
# chip.append(c)

# print(s)
# print("chiperteks adalah:")


# def keys(key):
#     s = [x for x in range(256)]
#     j = 0
#     key = [ord(x) for x in key]
#     for i in range(256):
#         j = (j + s[i] + int(key[i % len(key)])) % 256
#         s[i], s[j] = s[j], s[i]
#     return s


# def encryptor(s, p):
#     i, j = 0, 0
#     chip = []
#     for char in p:
#         i = (i+j) % 256
#         j = (j+s[i]) % 256
#         s[i], s[j] = s[j], s[i]
#         t = (s[i]+s[j]) % 256
#         c = format(ord(chr(s[t] ^ ord(char))), 'x')
#         chip.append(c)
#     return chip


# key = input("Masukkan key: ")
# s = keys(key)
# chip = encryptor(s, input("Masukkan plainteks: "))

# print("S adalah : ")
# for x in s:
#     print(x, end=" ")
# print('\n')

# print("chiperteks adalah : ")
# for x in chip:
#     print(x, end=" ")
# print('\n')

# for x in chip:
#     print(chr(int(x)), end=" ")
#     # print(chr(x), end=" ")
# print('\n')

# print(chr(int(x)))
# print(chr(int(x)), end=" ")

# ascii_code = ord("a")
# print("ASCII number dari a : " + str(ascii_code))
# data = 32
# print("Character dari ascii code 32 : " + chr(data))

#  ▲▲▼
