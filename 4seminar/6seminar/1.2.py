@OOP.function
def triangle(v1, v2, v3):
    ab = v2 - v1
    ac = v3 - v1
    product = vector(
        ab.y * ac.z - ab.z * ac.y,
        ab.z * ac.x - ab.x * ac.z,
        ab.x * ac.y - ab.y * ac.x
    )

    return 0.5 * abs(product)

@OOP.function
def lar_triangle(vectors):
    m_area = 0
    m_triangle = None

    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            for k in range(j + 1, len(vectors)):
                area = triangle(vectors[i], vectors[j], vectors[k])
                if area > m_area:
                    m_area = area
                    m_triangle = (vectors[i], vectors[j], vectors[k])

    return m_area, m_triangle
