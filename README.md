# Fraction Class
## Description
A fraction class written in Python that should perfrom the basic operations (add, substract, divide, multiply) that fractions can do. Also will automatically reduce the fractions to the lowest reduced form.

## Basic Operations
For the following operations, will be using:
```python
frac_1 = Fraction(1,5)
frac_2 = Fraction(2,5)
print("frac1",frac_1.value()) # would get 1.0/5.0
print("frac2",frac_2.value()) # would get 2.0/5.0
```
* adding fractions:
```python
sum_frac_1 = frac_1+frac_2
print("frac1+frac2",sum_frac_1.value()) # would get 3.0/5.0
```
* substract fractions:
```python
sub_frac_1 = frac_1-frac_2
print("frac1-frac2 = ",sub_frac_1.value()) # get -1.0/5.0
```
* divide fractions:
```python
div_frac_1 = frac_1/frac_2
print("frac1/frac2 = ", div_frac_1.value()) #get 1.0/2.0
```
* multiply fractions:
```python
mult_frac_1 = frac_1*frac_2
print("frac1*frac2 = ",mult_frac_1.value()) # get 2.0/25.0
```