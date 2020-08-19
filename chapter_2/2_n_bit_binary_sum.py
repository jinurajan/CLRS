"""
Sum of n bit binary integers
Consider the problem of adding two n-bit binary integers, stored in two n-element arrays A and B.
The sum of the two integers should be stored in binary form in an .n C 1/-element array C .
State the problem formally and write pseudocode for adding the two integers.

Psuedo Code
    
    initialize  C with n-1 zeros
    initialize remainder rem = 0
    initialize last index of c_n = (len(A) + 1) - 1
    from n = len(A)-1 to 0
        val, rem = binSum(rem, binSum(A[n], B[n]))
        Insert val in the last position of c
        decrement c_n by 1
        decrement n by 1
    return C



"""


def binSum(a, b):
    if a == 1 and b == 1:
        return 10
    elif a == 0 and b == 0:
        return 0
    else:
        return 1


def nbitsum(A, B):
    if len(A) != len(B):
        # invalid case
        return
    c = [0] * (len(A) + 1)
    c_n = len(A)
    rem = 0
    n = len(A) - 1
    while n >= 0:
        val = binSum(A[n], B[n])
        if val == 10:
            if not rem:
                val = 0
                rem = 1
            else:
                val = 1
                rem = 1
        else:
            if rem:
                val = binSum(val, rem)
        c[c_n] = val
        c_n -= 1
        n -= 1
    if rem:
        c[c_n] = rem
    return c


if __name__ == "__main__":
    A = [1, 1, 1]
    B = [1, 1, 1]
    print nbitsum(A, B)
    A = [1, 0, 0]
    B = [1, 1, 0]
    print nbitsum(A, B)
