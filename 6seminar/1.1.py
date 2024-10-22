@OOP.function
def center_mass(vectors):
    n = len(vectors)
    if n == 0:
        print('пустое множество')
    else:
        sum_vector = vector(0, 0, 0)
        for vec in vectors:
            sum_vector += vec
        return vector(sum_vector.x /n, sum_vector.y /n, sum_vector.z /n)
