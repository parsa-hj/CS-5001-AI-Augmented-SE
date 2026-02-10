import pytest
from src.app import is_prime

def test_is_prime_negative():
    assert not is_prime(-1)
    assert not is_prime(-10)
    assert not is_prime(-100)

def test_is_prime_zero():
    assert not is_prime(0)

def test_is_prime_one():
    assert not is_prime(1)

def test_is_prime_two():
    assert is_prime(2)

def test_is_prime_three():
    assert is_prime(3)

def test_is_prime_four():
    assert not is_prime(4)

def test_is_prime_five():
    assert is_prime(5)

def test_is_prime_six():
    assert not is_prime(6)

def test_is_prime_seven():
    assert is_prime(7)

def test_is_prime_eight():
    assert not is_prime(8)

def test_is_prime_nine():
    assert not is_prime(9)

def test_is_prime_ten():
    assert not is_prime(10)

def test_is_prime_large_prime():
    assert is_prime(7919)

def test_is_prime_large_non_prime():
    assert not is_prime(7920)

def test_is_prime_even_numbers():
    for n in range(4, 100, 2):
        assert not is_prime(n)

def test_is_prime_odd_numbers():
    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for n in primes:
        assert is_prime(n)

def test_is_prime_square_numbers():
    for n in range(4, 100, 3):
        if n % 2 == 0:
            assert not is_prime(n)
