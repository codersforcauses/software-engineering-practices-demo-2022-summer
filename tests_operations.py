import multiplication


def test_addition():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function addition
    THEN:  the resulting is the addition of the two numbers
    """
    pass


def test_subtraction():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function subtraction
    THEN:  the resulting is the subtraction of the two numbers
    """
    pass


def test_multiplication():
    assert multiplication(3, 5) == (15)
    assert multiplication(0, 4) == (0)
    assert multiplication(1, -7) == (-7)
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function multiplication
    THEN:  the resulting is the multiplication of the two numbers
    """


def test_division():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function division
    THEN:  the resulting is the division of the two number
    """
    pass


def test_division_exception_on_zero():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function division
    THEN:  the resulting is the division of the two number

    Hint: https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest
    """
    pass


def test_exponentiation():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function exponentiation
    THEN:  the resulting is the exponentiation of the two number
    """
    assert exponentiation(2, 5) == 32
    assert exponentiation(3, 3) == 27
    assert exponentiation(4, 1) == 4


def test_modulo():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function modulo
    THEN:  the resulting is the modulo of the two number
    """
    pass
