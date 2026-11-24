"""Shared exact coefficient notation for the 8227 authored expressions."""
from fractions import Fraction

def coefficient(value, atom):
    """Attach an exact coefficient, suppressing unit multipliers and doubled signs."""
    number = Fraction(value)
    if not number:
        return '0'
    sign = '-' if number < 0 else ''
    magnitude = abs(number)
    if magnitude == 1:
        return sign + atom
    scalar = (str(magnitude.numerator) if magnitude.denominator == 1
              else rf'\frac{{{magnitude.numerator}}}{{{magnitude.denominator}}}')
    return sign + scalar + atom
