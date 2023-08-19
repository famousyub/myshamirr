

import secrets
import numpy as np
import sympy
import itertools


class SSS:
    """
        k = the key
        p = prime number for modulo operations in the set Z_p
        w = number of shares
        t = minimum number of shares required to reconstruct the key k
    """

    def __init__(self, k, p, w, t):
        if not (sympy.isprime(p)):
            raise ValueError('p is not prime')
        else:
            self.k = k
            self.p = p
            self.w = w
            self.t = t

    '''
        SHARES GENERATION
    '''

    '''
        choose_x chooses w distinct, non-zero elements of Z_p
        these are the public x_i values, 1 <= i <= w
    '''

    def choose_x(self):
        x = []
        for element in range(0, self.w):
            new_x = secrets.randbelow(self.p)
            while new_x == 0 or new_x in x:  # elements must be non-zero and distinct
                new_x = secrets.randbelow(self.p)
            x.append(new_x)
        self.x = x
        return self.x

    '''
        choose_a chooses t-1 elements of Z_p
        these are the random a_i values, 1 <= i <= t-1
    '''

    def choose_a(self):
        a = []
        for element in range(0, self.t - 1):
            a.append(secrets.randbelow(self.p))
        self.a = a
        return self.a

    '''
        generate_shares creates the secret shares to distribute
        these are the y_i values, 1 <= i <= w
    '''

    def generate_shares(self):
        y = []
        self.choose_a()
        for idx, element in enumerate(range(0, self.w)):
            poly = np.array(self.a + [self.k], dtype=object)
            ecs = np.array(self.x[idx], dtype=object)
            y.append(np.polyval(poly, ecs) % self.p)
        self.y = y
        return self.y

    '''
        KEY RECONSTRUCTION
    '''

    '''
        The following two functions are used to calculate the inverse modulo p
        of a number (we need it when we calculate the b values, to handle
        the denominator)
        
        Adapted from https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
    '''

    def egcd(self, number1, number2):
        if number1 == 0:
            return (number2, 0, 1)
        else:
            g, y, x = self.egcd(number2 % number1, number1)
            return g, x - (number2 // number1) * y, y

    def modinv(self, number, m):
        g, x, y = self.egcd(number, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    '''
        calculate_b is needed to reconstruct the key from the shares
        Part of the Lagrange interpolation formula
        
        This is the simplified version that we can use when we want to reconstruct the key
        (since x=0 in this case)
    '''

    def calculate_b(self, x, x_values):
        acc = 1
        for element in x_values:
            if element != x:  # do not multiply the current x in the formula
                acc = acc * element
                if element - x >= 0:
                    inverse = self.modinv(element - x, self.p)
                else:
                    inverse = self.modinv(self.p - abs(element - x),
                                          self.p)  # https://math.stackexchange.com/questions/355066/find-the-inverse-modulo-of-a-number-got-a-negative-result
                acc = acc * inverse
        return acc % self.p

    '''
        calculate_b_full is the full Lagrange interpolation formula
        
        This is the formula we need when we want to calculate the share for a specific x != 0
        In this case, since x is not zero, we need to use the full formula
    '''

    def calculate_b_full(self, root, x, x_values):
        acc = 1
        for element in x_values:
            if element != x:  # do not multiply the current x in the formula
                acc = acc * (root-element)
                if element - x >= 0:
                    inverse = self.modinv(element - x, self.p)
                else:
                    inverse = self.modinv(self.p - abs(element - x),
                                          self.p)  # https://math.stackexchange.com/questions/355066/find-the-inverse-modulo-of-a-number-got-a-negative-result
                acc = acc * inverse
        return acc % self.p

    '''
        Take the values of x and the values of y as input
        (i.e. the coordinates of the points on the plane)
        and reconstruct the key by summing the products of b_i * y_i mod p
    '''

    def reconstruct_key(self, x, y):
        if len(y) < self.t:
            print("Not enough shares. Key reconstruction won't be possible.")
        else:
            b = []
            k = 0
            for index in range(len(y)):
                b.append(self.calculate_b(x[index], x))
                k = k + b[index] * y[index]
            return k % self.p

    def calculate_y(self, x, x_values, y_values):
        b = []
        y = 0
        for index in range(len(y_values)):
            b.append(self.calculate_b_full(x, x_values[index], x_values))
            y = y + b[index] * y_values[index]
        return y % self.p

    def validate_shares(self, x_values, y_values):
        comb_x = list(itertools.combinations(x_values, self.t))
        comb_y = list(itertools.combinations(y_values, self.t))
        key = self.reconstruct_key(comb_x[0], comb_y[0])
        for index, element in enumerate(comb_x):
            next_key = self.reconstruct_key(comb_x[index], comb_y[index])
            if (not(next_key == key)):
                return False
                exit()
        return True

    def find_defective_share(self, x_values, y_values):
        comb_x = list(itertools.combinations(x_values, self.t))
        comb_y = list(itertools.combinations(y_values, self.t))
        array_of_keys = []
        for index, element in enumerate(comb_x):
            key = self.reconstruct_key(comb_x[index], comb_y[index])
            array_of_keys.append([comb_x[index], key])

        # Count how many times a key appears
        # The one with most occurrences is likely the correct key
        array_count = []
        for element in array_of_keys:
            array_count.append([element[1], sum(x.count(element[1]) for x in array_of_keys)])

        # Sort the array to find the most common key
        sorted_array = sorted(array_count, key=lambda x: x[1], reverse=True)
        likely_key = sorted_array[0][0]

        # Find the defective share, i.e. the intersection of every share returning the wrong result
        array_of_x = []
        for element in array_of_keys:
            if element[1] != likely_key: # only consider shares with the wrong key
                array_of_x.append(element[0])
        result = set(array_of_x[0]).intersection(*array_of_x)
        return list(result)[0]

