# import numpy as np
#
# from pymoo.algorithms.soo.nonconvex.ga import GA
# from pymoo.core.problem import Problem
# from pymoo.operators.crossover.sbx import SBX
# from pymoo.operators.mutation.pm import PM
# from pymoo.operators.repair.rounding import RoundingRepair
# from pymoo.operators.sampling.rnd import IntegerRandomSampling
# from pymoo.optimize import minimize
#
#
# class MyProblem(Problem):
#
#     def __init__(self):
#         super().__init__(n_var=2, n_obj=1, n_ieq_constr=1, xl=0, xu=10, vtype=int)
#
#     def _evaluate(self, x, out, *args, **kwargs):
#         print(x)
#         print(len(x))
#         out["F"] = - np.min(x * [3, 1], axis=1)
#         out["G"] = x[:, 0] + x[:, 1] - 10
#
#
# problem = MyProblem()
#
# method = GA(pop_size=20,
#             sampling=IntegerRandomSampling(),
#             crossover=SBX(prob=1.0, eta=3.0, vtype=float, repair=RoundingRepair()),
#             mutation=PM(prob=1.0, eta=3.0, vtype=float, repair=RoundingRepair()),
#             eliminate_duplicates=True,
#             )
#
# res = minimize(problem,
#                method,
#                termination=('n_gen', 1),
#                seed=1,
#                save_history=True
#                )
# xl = [1, 1, 1, 5, 8]
# repeated_xl = xl * 20
# print(repeated_xl)

v = {
    1: 1.9,
    2: 10.0,
    3: 2.3,
    4: 3.0,
    5: 7.5,
    6: 2.7,
    7: 12.6,
    8: 3.2,
    9: 5.6,
    10: 12.4,
    11: 11.1,
    12: 2.8,
    13: 5.1,
    14: 11.0,
    15: 11.2,
    16: 2.2,
    17: 4.5,
    18: 10.0,
    19: 6.4,
    20: 3.6
}
print(v[1])