# import numpy as np
# from pymoo.core.problem import ElementwiseProblem
# from pymoo.algorithms.moo.nsga3 import NSGA3
# from pymoo.operators.mutation.bitflip import BitflipMutation
# from pymoo.util.ref_dirs import get_reference_directions
# import networkx as nx
# from pymoo.operators.crossover.sbx import SBX
# from pymoo.operators.mutation.pm import PM
# from pymoo.operators.sampling.rnd import BinaryRandomSampling
# from criticalpath import CriticalPath
# from pymoo.termination import get_termination
# from pymoo.optimize import minimize
# import matplotlib.pyplot as plt
#
#
# class ConstructionSchedulingProblem(ElementwiseProblem):
#     def __init__(self, w, c, q, V, LC):
#         n_activities = 20
#         super().__init__(n_var=n_activities * 5, n_obj=3, n_constr=0, xl=0, xu=1, elementwise_evaluation=True)
#         self.w = w
#         self.c = c
#         self.q = q
#         self.V = V
#         self.LC = LC
#         self.n_activities = n_activities
#
#     def _evaluate(self, x, out, *args, **kwargs):
#         x_bin = x.reshape(self.n_activities, 5)
#         total_cost, total_quality, durations = self.calculate_objectives(x_bin)
#         cp = CriticalPath(durations)
#         duration = cp.calculate_critical_path()
#         out["F"] = [duration, total_cost, -total_quality]
#
#     def calculate_objectives(self, x_bin):
#         total_cost = 0
#         total_quality = 0
#         durations = {}
#
#         for j in range(self.n_activities):
#             A, M, E, D, H = x_bin[j]
#             A_idx, M_idx, E_idx = int(A * 3), int(M * 3), int(E * 3)
#             D_idx, H_idx = int(D * 3), int(H * 5)
#
#             AC = self.c[j][A_idx]
#             MC = self.c[j + self.n_activities][M_idx]
#             EC = self.c[j + 2 * self.n_activities][E_idx]
#             AQ = self.q[j][A_idx]
#             MQ = self.q[j + self.n_activities][M_idx]
#             EQ = self.q[j + 2 * self.n_activities][E_idx]
#             LC = self.LC[j]
#
#             PP = [(5, 8, 1), (5, 9, 0.9), (5, 10, 0.85), (5, 11, 0.65), (5, 12, 0.6),
#                   (6, 8, 0.9), (6, 9, 0.85), (6, 10, 0.8), (6, 11, 0.65), (6, 12, 0.6),
#                   (7, 8, 0.75), (7, 9, 0.7), (7, 10, 0.65), (7, 11, 0.6), (7, 12, 0.55)]
#             E_val = PP[D_idx * 5 + H_idx][2]
#             LQ = E_val
# 77
#             duration = self.V[j] / ((H_idx + 1) * 8 * E_val)
#             durations[str(j + 1)] = duration
#
#             total_cost += LC * duration + MC + EC + AC * duration
#             total_quality += (LQ + MQ + EQ + AQ) * 0.25
#
#         Cws = sum(self.LC) * 0.139
#         Cmo = sum(self.LC) * 0.05
#         Cfo = 150 * sum(list(durations.values()))
#         Cfs = 150 * sum(list(durations.values()))
#         total_cost += Cws + Cmo + Cfo + Cfs
#         total_quality /= 20
#
#         return total_cost, total_quality, durations
#
#
# class CriticalPath:
#     def __init__(self, activities):
#         self.activities = activities
#         self.graph = nx.DiGraph()
#         self.create_graph()
#
#     def create_graph(self):
#         for activity, duration in self.activities.items():
#             self.graph.add_node(activity, duration=duration)
#
#         self.graph.add_node('Start')
#         self.graph.add_node('End')
#
#         for activity in self.activities:
#             self.graph.add_edge('Start', activity)
#             self.graph.add_edge(activity, 'End')
#
#     def calculate_critical_path(self):
#         distances = nx.shortest_path_length(self.graph, 'Start', 'End', weight='duration')
#         return distances['End']
#
#
# # Input data
# w = np.random.rand(20)
# c = [np.random.rand(3) for _ in range(60)]
# q = [np.random.rand(3) for _ in range(60)]
# V = [1.9, 10.0, 2.3, 3.0, 7.5, 2.7, 12.6, 3.2, 5.6, 12.4, 11.1, 2.8, 5.1, 11.0, 11.2, 2.2, 4.5, 10.0, 6.4, 3.6]
# LC = [700, 300, 600, 750, 1700, 430, 450, 800, 1000, 750, 460, 800, 100, 750, 470, 800, 1000, 750, 300, 750]
#
# problem = ConstructionSchedulingProblem(w, c, q, V, LC)
#
# ref_dirs = get_reference_directions("das-dennis", 3, n_partitions=12)
# algorithm = NSGA3(pop_size=500,
#                   n_offsprings=500,
#                   sampling=BinaryRandomSampling(),
#                   crossover=SBX(prob=0.8, eta=15),
#                   mutation=BitflipMutation(prob=0.1),
#                   eliminate_duplicates=True,
#                   ref_dirs=ref_dirs)
#
# termination = get_termination("n_gen", 10000)
#
# res = minimize(problem, algorithm, termination, seed=1, save_history=True, verbose=True)
#
# # Optimization results
# X = res.X
# F = res.F
#
# # Compare with the results from the study
# study_results = [(5, 9, 1400, 2, 2, 2, 2),
#                  (6, 8, 3000, 3, 2, 3, 10),
#                  (5, 11, 1200, 3, 1, 2, 2),
#                  (5, 9, 2250, 3, 3, 1, 3),
#                  (5, 8, 11900, 1, 3, 2, 7),
#                  (7, 8, 1290, 3, 1, 1, 3),
#                  (6, 8, 4950, 3, 3, 2, 11),
#                  (5, 11, 2400, 3, 3, 1, 3),
#                  (5, 9, 5000, 1, 3, 1, 5),
#                  (5, 9, 8250, 1, 3, 2, 11),
#                  (6, 11, 5060, 3, 3, 2, 11),
#                  (5, 9, 1600, 1, 3, 2, 2),
#                  (6, 8, 5000, 3, 3, 1, 5),
#                  (5, 10, 7500, 3, 3, 1, 10),
#                  (6, 9, 4700, 3, 3, 1, 10),
#                  (5, 12, 2400, 3, 1, 3, 3),
#                  (5, 8, 4000, 2, 3, 2, 4),
#                  (5, 8, 6750, 1, 3, 2, 9),
#                  (6, 9, 1800, 2, 3, 1, 6),
#                  (5, 8, 3000, 3, 3, 1, 4)]
#
# study_duration = 79
# study_cost = 450460
# study_quality = 0.912
#
# xl, xu = problem.bounds()
# plt.figure(figsize=(7, 5))
# plt.scatter(X[:, 0], X[:, 1], s=30, facecolors='none', edgecolors='r')
# plt.xlim(xl[0], xu[0])
# plt.ylim(xl[1], xu[1])
# plt.title("Design Space")
# plt.show()
# # Compare the optimization results with the study results
# # ... (code to compare and analyze the results)
