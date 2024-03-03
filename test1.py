
from pymoo.core.problem import ElementwiseProblem
import numpy as np


class ProjectSchedulingProblem(ElementwiseProblem):
    def __init__(self, n_activities, d, c, q, w, l, E_FS, E_SF, E_SS, E_FF):
        """
        Initialize the project scheduling problem.
        :param n_activities: Number of real activities in the project.
        :param d: Duration for each activity and execution mode.
        :param c: Cost for each activity and execution mode.
        :param q: Quality for each activity and execution mode.
        :param w: Weight of each activity.
        :param l: Lag or lead time between activities.
        :param E_FS, E_SF, E_SS, E_FF: Sets of precedence relationships.
        """
        n_vars = n_activities * max([len(m) for m in d])  # Assuming each activity has m modes
        super().__init__(n_var=n_vars, n_obj=3, n_constr=4, xl=0, xu=1)

        self.n_activities = n_activities
        self.d = d
        self.c = c
        self.q = q
        self.w = w
        self.l = l
        self.E_FS = E_FS
        self.E_SF = E_SF
        self.E_SS = E_SS
        self.E_FF = E_FF

    def _evaluate(self, x, out, *args, **kwargs):
        # Convert x to binary decision variables
        x_bin = np.round(x).astype(int)

        # Calculate objectives
        F_n_plus_2 = self._calculate_project_duration(x_bin)
        total_cost = np.sum(
            [self.c[j][m] * x_bin[j, m] for j in range(self.n_activities) for m in range(len(self.c[j]))])
        total_quality = np.sum(
            [self.w[j] * self.q[j][m] * x_bin[j, m] for j in range(self.n_activities) for m in range(len(self.q[j]))])

        # Set objectives
        out["F"] = [F_n_plus_2, total_cost, -total_quality]  # Maximize quality by minimizing its negative value

        # Calculate constraints
        constraints = self._calculate_constraints(x_bin)
        out["G"] = constraints

    def _calculate_project_duration(self, x_bin):
        # Placeholder for project duration calculation
        return 0  # Needs to be implemented

    def _calculate_constraints(self, x_bin):
        # Placeholder for constraints calculation
        return np.zeros(self.n_constr)  # Needs to be implemented
