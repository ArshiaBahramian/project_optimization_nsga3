# # import numpy as np
# #
# # from pymoo.algorithms.soo.nonconvex.ga import GA
# # from pymoo.core.problem import Problem
# # from pymoo.operators.crossover.sbx import SBX
# # from pymoo.operators.mutation.pm import PM
# # from pymoo.operators.repair.rounding import RoundingRepair
# # from pymoo.operators.sampling.rnd import IntegerRandomSampling
# # from pymoo.optimize import minimize
# #
# #
# # class MyProblem(Problem):
# #
# #     def __init__(self):
# #         super().__init__(n_var=2, n_obj=1, n_ieq_constr=1, xl=0, xu=10, vtype=int)
# #
# #     def _evaluate(self, x, out, *args, **kwargs):
# #         print(x)
# #         print(len(x))
# #         out["F"] = - np.min(x * [3, 1], axis=1)
# #         out["G"] = x[:, 0] + x[:, 1] - 10
# #
# #
# # problem = MyProblem()
# #
# # method = GA(pop_size=20,
# #             sampling=IntegerRandomSampling(),
# #             crossover=SBX(prob=1.0, eta=3.0, vtype=float, repair=RoundingRepair()),
# #             mutation=PM(prob=1.0, eta=3.0, vtype=float, repair=RoundingRepair()),
# #             eliminate_duplicates=True,
# #             )
# #
# # res = minimize(problem,
# #                method,
# #                termination=('n_gen', 1),
# #                seed=1,
# #                save_history=True
# #                )
# # xl = [1, 1, 1, 5, 8]
# # repeated_xl = xl * 20
# # print(repeated_xl)
#
# v = {
#     1: 1.9,
#     2: 10.0,
#     3: 2.3,
#     4: 3.0,
#     5: 7.5,
#     6: 2.7,
#     7: 12.6,
#     8: 3.2,
#     9: 5.6,
#     10: 12.4,
#     11: 11.1,
#     12: 2.8,
#     13: 5.1,
#     14: 11.0,
#     15: 11.2,
#     16: 2.2,
#     17: 4.5,
#     18: 10.0,
#     19: 6.4,
#     20: 3.6
# }
# print(v[1])

material = {
            1: {"Option1": {"Cost": 3200, "Quality": 0.7},
                "Option2": {"Cost": 3850, "Quality": 0.85},
                "Option3": {"Cost": 4500, "Quality": 1.0}},
            2: {"Option1": {"Cost": 800, "Quality": 0.7},
                "Option2": {"Cost": 950, "Quality": 0.85},
                "Option3": {"Cost": 1100, "Quality": 1.0}},
            3: {"Option1": {"Cost": 5600, "Quality": 0.7},
                "Option2": {"Cost": 6400, "Quality": 0.85},
                "Option3": {"Cost": 7200, "Quality": 1.0}},
            4: {"Option1": {"Cost": 18200, "Quality": 0.7},
                "Option2": {"Cost": 20800, "Quality": 0.85},
                "Option3": {"Cost": 23400, "Quality": 1.0}},
            5: {"Option1": {"Cost": 16000, "Quality": 0.7},
                "Option2": {"Cost": 18000, "Quality": 0.85},
                "Option3": {"Cost": 20000, "Quality": 1.0}},
            6: {"Option1": {"Cost": 6400, "Quality": 0.7},
                "Option2": {"Cost": 7500, "Quality": 0.85},
                "Option3": {"Cost": 8600, "Quality": 1.0}},
            7: {"Option1": {"Cost": 1200, "Quality": 0.7},
                "Option2": {"Cost": 1450, "Quality": 0.85},
                "Option3": {"Cost": 1700, "Quality": 1.0}},
            8: {"Option1": {"Cost": 11200, "Quality": 0.7},
                "Option2": {"Cost": 12800, "Quality": 0.85},
                "Option3": {"Cost": 14400, "Quality": 1.0}},
            9: {"Option1": {"Cost": 16800, "Quality": 0.7},
                "Option2": {"Cost": 19200, "Quality": 0.85},
                "Option3": {"Cost": 21600, "Quality": 1.0}},
            10: {"Option1": {"Cost": 13200, "Quality": 0.7},
                 "Option2": {"Cost": 14900, "Quality": 0.85},
                 "Option3": {"Cost": 16600, "Quality": 1.0}},
            11: {"Option1": {"Cost": 1100, "Quality": 0.7},
                 "Option2": {"Cost": 1350, "Quality": 0.85},
                 "Option3": {"Cost": 1600, "Quality": 1.0}},
            12: {"Option1": {"Cost": 9800, "Quality": 0.7},
                 "Option2": {"Cost": 11200, "Quality": 0.85},
                 "Option3": {"Cost": 12600, "Quality": 1.0}},
            13: {"Option1": {"Cost": 15050, "Quality": 0.7},
                 "Option2": {"Cost": 17200, "Quality": 0.85},
                 "Option3": {"Cost": 19350, "Quality": 1.0}},
            14: {"Option1": {"Cost": 11700, "Quality": 0.7},
                 "Option2": {"Cost": 13200, "Quality": 0.85},
                 "Option3": {"Cost": 14700, "Quality": 1.0}},
            15: {"Option1": {"Cost": 1100, "Quality": 0.7},
                 "Option2": {"Cost": 1350, "Quality": 0.85},
                 "Option3": {"Cost": 1600, "Quality": 1.0}},
            16: {"Option1": {"Cost": 7700, "Quality": 0.7},
                 "Option2": {"Cost": 8800, "Quality": 0.85},
                 "Option3": {"Cost": 9900, "Quality": 1.0}},
            17: {"Option1": {"Cost": 13300, "Quality": 0.7},
                 "Option2": {"Cost": 15200, "Quality": 0.85},
                 "Option3": {"Cost": 17100, "Quality": 1.0}},
            18: {"Option1": {"Cost": 10600, "Quality": 0.7},
                 "Option2": {"Cost": 11950, "Quality": 0.85},
                 "Option3": {"Cost": 13300, "Quality": 1.0}},
            19: {"Option1": {"Cost": 3200, "Quality": 0.7},
                 "Option2": {"Cost": 3500, "Quality": 0.85},
                 "Option3": {"Cost": 3800, "Quality": 1.0}},
            20: {"Option1": {"Cost": 7000, "Quality": 0.7},
                 "Option2": {"Cost": 7750, "Quality": 0.85},
                 "Option3": {"Cost": 8500, "Quality": 1.0}}
        }
i = 2
mc = 3
cost_of_material = material[i + 1]["Option{}".format(mc)]["Cost"]
print(cost_of_material)