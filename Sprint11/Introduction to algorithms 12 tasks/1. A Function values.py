# y = ax2 + bx + c
# a, x, b, c
def function_values(variables):
    y = (
        variables[0] * variables[1] ** 2
        + variables[2] * variables[1]
        + variables[3]
    )
    return y


function_variables = list(map(int, input().split()))
print(function_values(function_variables))
