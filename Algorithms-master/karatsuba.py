def karatsuba(x,y):
    # Get lengths
    la = len(str(x))
    lb = len(str(y))
    # Check base case
    if la == 1 and lb == 1:
        return x*y
    else:
        # Grab lengths
        ml = max(la, lb)
        ml2 = ml // 2
        # Split into a,b,c,d
        a = x // 10 ** (ml2)
        b = int(x % 10 ** (ml2))
        c = y // 10 ** (ml2)
        d = int(y % 10 ** (ml2))
        # Get ac and bd
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        # Final steps
        ab_x_cd = karatsuba(a+b,c+d)
        gauss = ab_x_cd - bd - ac
        final = ((10 ** (ml2*2)) * ac) + (10 ** int(ml2) * gauss) + bd
        return final

if __name__ == "__main__":
    print(karatsuba(5678,1234))