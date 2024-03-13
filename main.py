import numpy as np
from pymoo.optimize import minimize
from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.operators.mutation.bitflip import BitflipMutation
from pymoo.util.ref_dirs import get_reference_directions
import networkx as nx
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.operators.sampling.rnd import BinaryRandomSampling, IntegerRandomSampling
from criticalpath import CriticalPath
from dur_cal import DurCal
from cost_cal import CostCal
from quality_cal import QualityCal
from pymoo.termination import get_termination
from pymoo.termination.default import DefaultMultiObjectiveTermination
import matplotlib.pyplot as plt
from pymoo.operators.repair.rounding import RoundingRepair
from mpl_toolkits.mplot3d import Axes3D


class ConstructionSchedulingProblem(ElementwiseProblem):
    def __init__(self):
        ti = [1, 1, 1, 5, 8]
        tf = [3,3,3,7,12]
        super().__init__(n_var=100, n_obj=3, n_constr=0, xl=ti*20, xu=tf*20, elementwise_evaluation=True,vtype=int)

    def _evaluate(self, x, out, *args, **kwargs):
        x_bin = x.reshape(20, 5)
        activities = {}
        e_lq = []
        total_cost = 0
        total_quality = 0

        for i in range(20):
            zd = DurCal(x_bin[i, 3],x_bin[i, 4],i)
            activities["{}".format(i+1)] , Ec = zd.computee()
            e_lq.append(Ec)
        cp = CriticalPath(activities)
        duration = cp.calculate_critical_path()


        for i in range(20):
            zc = CostCal(x_bin[i, 0],x_bin[i, 1],x_bin[i, 2],activities,i)
            cost = zc.computee()
            total_cost = total_cost + cost

        for i in range(20):
            zq = QualityCal(x_bin[i, 0],x_bin[i, 1],x_bin[i, 2],activities,i,e_lq)
            quality = zq.computee()
            total_quality = total_quality + quality

        out["F"] = [duration, total_cost, -total_quality]



problem = ConstructionSchedulingProblem()

ref_dirs = get_reference_directions("das-dennis", 3, n_partitions=12)
algorithm = NSGA3(pop_size=500,
                  n_offsprings=500,
                  sampling=IntegerRandomSampling(),
                  crossover=SBX(prob=0.8, eta=15, vtype=float, repair=RoundingRepair()),
                  mutation=PM(prob=1.0, vtype=float, repair=RoundingRepair()),
                  eliminate_duplicates=True,
                  ref_dirs=ref_dirs
                  )
termination = get_termination("n_gen", 1)

# termination = DefaultMultiObjectiveTermination(
#     xtol=1e-8,
#     cvtol=1e-6,
#     ftol=0.0025,
#     period=30,
#     n_max_gen=10000,
#     n_max_evals=100000
# )

res = minimize(problem, algorithm, termination, seed=1, save_history=True, verbose=True)
X = res.X
F = res.F

# print(X)
# print(F)

# xl, xu = problem.bounds()
# plt.figure(figsize=(7, 5))
# plt.scatter(X[:, 0], X[:, 1], s=30, facecolors='none', edgecolors='r')
# plt.xlim(xl[0], xu[0])
# plt.ylim(xl[1], xu[1])
# plt.title("Design Space")
# plt.show()


# ایجاد یک نمودار سه بعدی
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# نام‌گذاری محورها
ax.set_xlabel('Time')
ax.set_ylabel('Cost')
ax.set_zlabel('Quality')

# رسم نقاط بر روی نمودار با استفاده از داده‌های موجود در F
# F[:, 0]، F[:, 1]، و F[:, 2] به ترتیب نشان‌دهنده توابع هدف اول، دوم و سوم هستند.
ax.scatter(F[:, 0], F[:, 1], F[:, 2], c='b', marker='o')

# نمایش نمودار
plt.show()