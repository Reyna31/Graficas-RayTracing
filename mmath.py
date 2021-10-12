
PI = 3.1415926536

def dot(vect0,vect1):
    result = 0
    for i in range(len(vect0)):
        result += vect0[i] * vect1[i]
    return result

def norm(vec):
    resul =[]

    c = 0
    for a in vec:
        c += pow(a,2)

    c = pow(c,0.5)

    if c != 0:
        for a in vec:
            resul.append(a/c)
        else:
            return vec

    return resul

def normal(vec):
    magnitud = (vec[0] * vec[0] + vec[1] * vec[1] + vec[2] * vec[2]) ** 0.5
    resultado = [vec[0] / magnitud,
                 vec[1] / magnitud,
                 vec[2] / magnitud]
    return resultado

def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]]

def resta(vec1, vec2):
    resul = []

    if len (vec1) == len (vec2):
        for i in range (len (vec1)):
            resul.append (vec1 [i] - vec2 [i])
    else:
        return

    return resul

def deg2rad(deg):
    return (deg * PI) / 180

def mult(A,B):
    result = []
    if len (A [0]) != len (B):
        return None
    Result = [[0] * len (B [0]) for t in range (len (A))]

    for m in range (len (A)):
        for n in range (len (B [0])):
            for i in range (len (B)):
                Result [m] [n] += A [m] [i] * B [i] [n]

    return Result