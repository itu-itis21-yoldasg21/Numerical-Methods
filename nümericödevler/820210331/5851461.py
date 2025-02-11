#Gülce Su Yoldaş 820210331

import math

def f(x):
    return 4 * math.log(x) - x   #for f(x)

def f_derivative(x):          #for f'(x)
    return 4 / x - 1

def newton_method(x0, max_num_iterations):
    iteration = [x0]
    x = x0
    for a in range(max_num_iterations):
        x = x - f(x) / f_derivative(x)
        iteration.append(x)
    return iteration

def secant_method(x0, x1, max_num_iterations):
    iteration = [x0, x1]
    x_before = x0
    x = x1
    for a in range(max_num_iterations):
        x_next = x - f(x)/ (f(x) - f(x_before)) * (x - x_before)
        x_before = x
        x = x_next
        iteration.append(x)
    return iteration

def error_estimation(iteration):
    errors = []
    for a in range(1, len(iteration)):
        error = abs(iteration[a] - iteration[a-1])
        errors.append(error)
    return errors

def convergence_rate(iteration, solution):
    rates = []
    for a in range(len(iteration)):
        rate = abs(iteration[a] - solution) / abs(iteration[a-1] - solution) if a > 0 else None
        rates.append(rate)
    return rates

x0 = 1
x1 = 2
max_num_iterations = 5


newton_iteration = newton_method(x0, max_num_iterations)
print("Newton Method Iteration: ", newton_iteration)


secant_iteration = secant_method(x0, x1, max_num_iterations)
print("Secant Method Iteration: ", secant_iteration)


newton_errors = error_estimation(newton_iteration)
print("Error Estimation for Newton Method: ", newton_errors)


secant_errors = error_estimation(secant_iteration)
print("Error Estimation for Secant Method: ", secant_errors)


newton_convergence_rates = convergence_rate(newton_iteration, 0)
print("Convergence Rate for Newton Method: ", newton_convergence_rates)


secant_convergence_rates = convergence_rate(secant_iteration, 0)
print("Convergence Rate for Secant Method: ", secant_convergence_rates)
