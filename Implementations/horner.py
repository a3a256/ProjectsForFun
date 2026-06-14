from fractions import Fraction

def divisors(variables: list) -> list:
    val = abs(variables[-1])
    negs = []
    pos = []
    for i in range(1, int(val/2)+1):
        if val%i == 0:
            negs += [i*(-1)]
            pos += [i]
    negs += [val*(-1)]
    pos += [val]
    above = negs + pos
    val = abs(variables[0])
    negs = []
    pos = []
    for i in range(1, int(val/2)+1):
        if val%i == 0:
            negs += [i*(-1)]
            pos += [i]
    negs += [val*(-1)]
    pos += [val]
    below = negs + pos
    res = []
    for i in above:
        for j in below:
            res += [i/j]
    return res

def divide_polynomials(og: list, value) -> list:
    res_vars = []
    prev = og[0]
    value = value*(-1)
    for i in range(1, len(og)):
        res_vars += [prev]
        cur = prev*value
        prev = og[i] - cur
    return res_vars

def polynomials_div_check(og: list, value) -> bool:
    res = 0
    p = 0
    for i in range(len(og)-1, -1, -1):
        res += og[i]*pow(value, p)
        p += 1

    res = abs(res)
    res = round(res, 5)
    return res == 0

def find_quadratic_roots(variables: list) -> list:
    discriminant = pow(variables[1], 2) - 4*variables[0]*variables[-1]

    if discriminant < 0:
        return None
    
    square_root = pow(discriminant, 0.5)
    if square_root * square_root == discriminant:
    
        first_root = ((-1)*variables[1] + pow(discriminant, 0.5))/(2*variables[0])
        second_root = ((-1)*variables[1] - pow(discriminant, 0.5))/(2*variables[0])
        frac = Fraction(first_root).limit_denominator()
        if frac.denominator == 1:
            first_root = str(int(first_root))
        else:
            first_root = str(frac.numerator)+"/"+str(frac.denominator)
        
        frac = Fraction(second_root).limit_denominator()
        if frac.denominator == 1:
            second_root = str(int(second_root))
        else:
            second_root = str(frac.numerator)+"/"+str(frac.denominator)

    else:
        first_root = "(" + str(variables[1]) + "+("+str(discriminant)+")^(0.5))/("+str(variables[0])+")"
        second_root = "(" + str(variables[1]) + "-("+str(discriminant)+")^(0.5))/("+str(variables[0])+")"

    return [first_root, second_root]



def horner_calculate(variables: list):
    divs = divisors(variables)
    roots = []
    while len(variables) > 3:
        divided = False
        for i in divs:
            if polynomials_div_check(variables, i):
                variables = divide_polynomials(variables, i)
                frac = Fraction(i).limit_denominator()
                if frac.denominator == 1:
                    roots += [str(int(i))]
                else:
                    roots += [str(frac.numerator)+"/"+str(frac.denominator)]
                divs = divisors(variables)
                divided = True
                break
        if not divided:
            break
    quad_roots = find_quadratic_roots(variables) if len(variables) == 3 else None
    if quad_roots is not None:
        roots += quad_roots

    return roots


if __name__ == '__main__':
    roots = horner_calculate([1, 1, -2])
    print(roots)