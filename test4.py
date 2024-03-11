import numpy as np
from pymoo.optimize import minimize
from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.operators.mutation.bitflip import BitflipMutation
from pymoo.util.ref_dirs import get_reference_directions
import networkx as nx
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.operators.sampling.rnd import *
from criticalpath import CriticalPath
from pymoo.termination import get_termination
from pymoo.termination.default import DefaultMultiObjectiveTermination
import matplotlib.pyplot as plt

options = [np.arange(5) for _ in range(5)]


class MyProblem(ElementwiseProblem):
    def __init__(self, options):
        self.options = options
        super().__init__(n_var=len(options), n_obj=3, n_constr=0,
                         xl=np.zeros(len(options)), xu=np.array([len(opt) - 1 for opt in options]))

    def _evaluate(self, x, out, *args, **kwargs):
        # محاسبه توابع هدف بر اساس اندیس‌های انتخاب شده برای هر گزینه
        f1 = sum(self.options[i][int(x[i])] for i in range(len(x)))
        f2 = sum((self.options[i][int(x[i])] - 2) ** 2 for i in range(len(x)))
        f3 = sum((self.options[i][int(x[i])] - 3) ** 3 for i in range(len(x)))

        out["F"] = [f1, f2, f3]


problem = MyProblem()

ref_dirs = get_reference_directions("das-dennis", 3, n_partitions=12)
algorithm = NSGA3(pop_size=500,
                  n_offsprings=500,
                  sampling= IntegerRandomSampling(),
                  crossover=SBX(prob=0.8, eta=15),
                  mutation=BitflipMutation(prob=0.1),
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
print(X)


# xl, xu = problem.bounds()
# plt.figure(figsize=(7, 5))
# plt.scatter(X[:, 0], X[:, 1], s=30, facecolors='none', edgecolors='r')
# plt.xlim(xl[0], xu[0])
# plt.ylim(xl[1], xu[1])
# plt.title("Design Space")
# plt.show()

