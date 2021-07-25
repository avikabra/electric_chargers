import candidate_locations
import csv
import random
import numpy
import math

candidates = candidate_locations.candidate_process()

candidates = [3, 5, 6, 7, 19, 22, 24]

from ortools.sat.python import cp_model

model = cp_model.CpModel()

from ortools.linear_solver import pywraplp

# solver = pywraplp.Solver.CreateSolver('SCIP')

from scipy.optimize import minimize, LinearConstraint

# load data
with open(r'data/data_optimization.csv', 'r') as nodecsv: # Open the file
    nodereader = csv.reader(nodecsv) # Read the csv
    data = [n for n in nodereader][1:] # remove the table headers

for i in range(len(data)):
    for j in range(len(data[i])):
        if j != 0 and data[i][j] != '':
            data[i][j] = float(data[i][j])

# assign data to constants 

rate_of_interest = 0.075
planning_period = 10

C_install = data[-8][1]
max_charging_stations = len(candidates)
cost_of_electricity = data[-6][1] / 1000

penalty_VD = 1000000
voltage_deviation = data[5][1:]
N_D = len(voltage_deviation)
penalty_AENS = 0.18 / 1000
load = data[13][1:]
u = data[9][1:]
number_of_consumers = data[11][1:]

utilization_rate = data[-2][1]
prob_no_evs_waiting = 0.75
arrival_rate = data[-3][1]

power_loss = data[7][1:]

# scipy

"""def objective_function(F):
    return (
        #((sum([F[2*i] + F[2*i + 1] for i in range(max_charging_stations)]) * (cost_of_electricity + C_install)) - 49000.98)/931018.6200000001
        (sum([sum([utilization_rate for j in range(int(F[2*i + 1]+1))]) / (numpy.math.factorial(int(F[2*i+1]-1)) * ((F[2*i+1]-utilization_rate)**2)) for i in range(max_charging_stations)]) * prob_no_evs_waiting / arrival_rate)
    )"""

def objective_function(F):
    return (
        sum(initial_F) * (C_install + cost_of_electricity) * rate_of_interest * ((1 + rate_of_interest) ** planning_period) / (((1 + rate_of_interest) ** planning_period) - 1)/3569.3767421581256
        + (sum([sum([utilization_rate for j in range(int(F[i]+1))]) / (numpy.math.factorial(int(F[i]-1)) * ((F[i]-utilization_rate)**2)) for i in range(max_charging_stations)]) * prob_no_evs_waiting / arrival_rate)
    )

#initial_F = [20] * max_charging_stations * 2
initial_F = [1] * max_charging_stations

res = minimize(objective_function, initial_F, method='SLSQP', bounds=[(1, 20)] * len(initial_F))

print(res)

# pywraplp
"""
# create variables

F = [solver.IntVar(1, 5, 'F_' + str(i)) for i in range(max_charging_stations)]
f = [solver.IntVar(1, 20, 'f_' + str(i)) for i in range(max_charging_stations)]

solver.Minimize(
    sum([F[i] + f[i] for i in range(max_charging_stations)]) * (cost_of_electricity + C_install)
    + penalty_VD * sum(voltage_deviation) + penalty_AENS * sum(numpy.dot(load, u))/sum(number_of_consumers)
    + sum([sum([utilization_rate for j in range(f[i]+1)]) / (numpy.math.factorial(f[i]-1) * ((f[i]-utilization_rate)**2)) for i in range(max_charging_stations)]) * prob_no_evs_waiting / arrival_rate
)
"""

# cp_model
"""
# create variables 

F = [model.NewIntVar(1, 5, 'F_' + str(i)) for i in range(max_charging_stations)]
f = [model.NewIntVar(1, 20, 'f_' + str(i)) for i in range(max_charging_stations)]

# equations
# constraints

# none? 

# objective function

model.Minimize(
    #sum([F[i] * f[i] for i in range(max_charging_stations)]) * (cost_of_electricity + C_install)
    penalty_VD * sum(voltage_deviation) + penalty_AENS * numpy.dot(load, u)/sum(number_of_consumers)
    + sum([sum([utilization_rate for j in range(f[i]+1)]) / (numpy.math.factorial(f[i]-1) * ((f[i]-utilization_rate)**2)) for i in range(max_charging_stations)]) * prob_no_evs_waiting / arrival_rate
)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL:
    print('Maximum of objective function: %i' % solver.ObjectiveValue())
    print()
    print('x value: ', solver.Value(F))
    print('y value: ', solver.Value(f))
"""