import re

L_VAL, R_VAL, OPER = range(3)

def calculate(phrase):
    operations = {"plus": op_plus, "minus": op_minus, "multiplied by": op_mult, "divided by": op_div}
    if not phrase.startswith("What is ") or not phrase.endswith("?"):
        raise ValueError()
    phrase = phrase[8:-1]
    phrase = phrase.lower()
    lines = re.findall("(-?\d+|[a-z ]+)", phrase)
    wait_for = L_VAL
    lval = None
    for elem in lines:
        if wait_for==L_VAL:
            lval = int(elem)
            wait_for = OPER
        elif wait_for == OPER:
            try:
                oper = operations[elem.strip()]
            except KeyError:
                raise ValueError
            wait_for = R_VAL
        else:
            rval = int(elem)
            wait_for = OPER
            lval = oper(lval, rval)
    return lval


def op_plus(lval, rval):
    return lval + rval

def op_minus(lval, rval):
    return lval - rval

def op_mult(lval, rval):
    return lval * rval

def op_div(lval, rval):
    return lval / rval
