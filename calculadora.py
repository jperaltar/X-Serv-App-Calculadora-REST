#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Calculator with +, -, *, / operators
"""

import sys

operations = {'mult': '*', 'add': '+', 'sub': '-', 'div': '/'}


def mult(operand1, operand2):
    return operand1 * operand2


def add(operand1, operand2):
    return operand1 + operand2


def sub(operand1, operand2):
    return operand1 - operand2


def div(operand1, operand2):
    try:
        return operand1 / operand2
    except ZeroDivisionError:
        sys.exit("\nError: Cannot solve this operation, divided by Zero\n")

if __name__ == '__main__':

    if (len(sys.argv) != 4):
        sys.exit("\nUsage error: calculadora.py Operation Operand1 Operand2\n")

    operation = sys.argv[1]
    try:
        operand1 = float(sys.argv[2])
        operand2 = float(sys.argv[3])
    except ValueError:
        sys.exit("\nError: One of the values entered is not a number\n")

    if operation not in operations:
        sys.exit("\nError: Operation entered is not available\n")

    if (operation == "mult"):
        result = mult(operand1, operand2)
    elif (operation == "add"):
        result = add(operand1, operand2)
    elif (operation == "sub"):
        resutl = sub(operand1, operand2)
    elif (operation == "div"):
        result = div(operand1, operand2)

    print str(operand1), operations[operation], str(operand2), "=", str(result)
