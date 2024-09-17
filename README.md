#первая
input_data = input("введите карты, их кол-во и номиналы:")
data = list(map(int, input_data.split()))

n = data[0]
aaa = data[1:]

k = n*(n+1) // 2

ku = sum(aaa)

vo = k - ku

print(vo)

##
#вторая
def tunis(s):

    polis = [s[i:i+2] for i in range(0, len(s), 2)]
    kupol = [pair[::-1] for pair in reversed(polis)]
    ote = ''.join(kupol)
    return ote

s = input("введите строку: ")

ote = tunis(s)
print(ote)

##
#четвертая

def istambul(s):
    polis = list(s)

    for i in range(0, len(polis) - 1, 2):
        polis[i], polis[i + 1] = polis[i + 1], polis[i]
        ote = ''.join(polis)
    return ote

s = input("Введите строку: ")

ote = istambul(s)
print(ote)

##
#пятая

iu = input("введите цифры через побел: ").split()
iu = [iu[-1]] + iu[:-1]
print(iu)

##
#шестая

def klop(k):
    wolf = {}

    for cif in k:
        if cif in wolf:
            wolf[cif] += 1
        else:
            wolf[cif] = 1

    vespo = [cif for cif in k if wolf[cif] == 1]

    return vespo

user = input("введите цифры через пробел: ")
cif = user.split()

res = klop(cif)

print(res)
