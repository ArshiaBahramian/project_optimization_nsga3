class CostCal:
    def __init__(self, mc, ac, ec,activities,i):
        self.i = i
        self.mc = mc
        self.ac = ac
        self.ec = ec
        self.activities = activities

    def computee(self):
        administartion = {1: {'Option1': {'Cost': 90, 'Quality': 0.7},
                              'Option2': {'Cost': 120, 'Quality': 0.85},
                              'Option3': {'Cost': 150, 'Quality': 1.0}},
                          2: {'Option1': {'Cost': 90, 'Quality': 0.7},
                              'Option2': {'Cost': 120, 'Quality': 0.85},
                              'Option3': {'Cost': 150, 'Quality': 1.0}},
                          3: {'Option1': {'Cost': 90, 'Quality': 0.7},
                              'Option2': {'Cost': 120, 'Quality': 0.85},
                              'Option3': {'Cost': 150, 'Quality': 1.0}},
                          4: {'Option1': {'Cost': 90, 'Quality': 0.7},
                              'Option2': {'Cost': 120, 'Quality': 0.85},
                              'Option3': {'Cost': 150, 'Quality': 1.0}},
                          5: {'Option1': {'Cost': 90, 'Quality': 0.7},
                              'Option2': {'Cost': 120, 'Quality': 0.85},
                              'Option3': {'Cost': 150, 'Quality': 1.0}},
                          6: {'Option1': {'Cost': 90, 'Quality': 0.7},
                              'Option2': {'Cost': 120, 'Quality': 0.85},
                              'Option3': {'Cost': 150, 'Quality': 1.0}},
                          7: {'Option1': {'Cost': 90, 'Quality': 0.7},
                              'Option2': {'Cost': 120, 'Quality': 0.85},
                              'Option3': {'Cost': 150, 'Quality': 1.0}},
                          8: {'Option1': {'Cost': 90, 'Quality': 0.7},
                              'Option2': {'Cost': 120, 'Quality': 0.85},
                              'Option3': {'Cost': 150, 'Quality': 1.0}},
                          9: {'Option1': {'Cost': 90, 'Quality': 0.7},
                              'Option2': {'Cost': 120, 'Quality': 0.85},
                              'Option3': {'Cost': 150, 'Quality': 1.0}},
                          10: {'Option1': {'Cost': 90, 'Quality': 0.7},
                               'Option2': {'Cost': 120, 'Quality': 0.85},
                               'Option3': {'Cost': 150, 'Quality': 1.0}},
                          11: {'Option1': {'Cost': 90, 'Quality': 0.7},
                               'Option2': {'Cost': 120, 'Quality': 0.85},
                               'Option3': {'Cost': 150, 'Quality': 1.0}},
                          12: {'Option1': {'Cost': 90, 'Quality': 0.7},
                               'Option2': {'Cost': 120, 'Quality': 0.85},
                               'Option3': {'Cost': 150, 'Quality': 1.0}},
                          13: {'Option1': {'Cost': 90, 'Quality': 0.7},
                               'Option2': {'Cost': 120, 'Quality': 0.85},
                               'Option3': {'Cost': 150, 'Quality': 1.0}},
                          14: {'Option1': {'Cost': 90, 'Quality': 0.7},
                               'Option2': {'Cost': 120, 'Quality': 0.85},
                               'Option3': {'Cost': 150, 'Quality': 1.0}},
                          15: {'Option1': {'Cost': 90, 'Quality': 0.7},
                               'Option2': {'Cost': 120, 'Quality': 0.85},
                               'Option3': {'Cost': 150, 'Quality': 1.0}},
                          16: {'Option1': {'Cost': 90, 'Quality': 0.7},
                               'Option2': {'Cost': 120, 'Quality': 0.85},
                               'Option3': {'Cost': 150, 'Quality': 1.0}},
                          17: {'Option1': {'Cost': 90, 'Quality': 0.7},
                               'Option2': {'Cost': 120, 'Quality': 0.85},
                               'Option3': {'Cost': 150, 'Quality': 1.0}},
                          18: {'Option1': {'Cost': 90, 'Quality': 0.7},
                               'Option2': {'Cost': 120, 'Quality': 0.85},
                               'Option3': {'Cost': 150, 'Quality': 1.0}},
                          19: {'Option1': {'Cost': 90, 'Quality': 0.7},
                               'Option2': {'Cost': 120, 'Quality': 0.85},
                               'Option3': {'Cost': 150, 'Quality': 1.0}},
                          20: {'Option1': {'Cost': 90, 'Quality': 0.7},
                               'Option2': {'Cost': 120, 'Quality': 0.85},
                               'Option3': {'Cost': 150, 'Quality': 1.0}}}

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

        equipment = {
            1: {"Option1": {"Cost": 1440.0, "Quality": 0.8},
                "Option2": {"Cost": 1200.0, "Quality": 0.9},
                "Option3": {"Cost": 1040.0, "Quality": 1.0}},
            2: {"Option1": {"Cost": 1210.0, "Quality": 0.8},
                "Option2": {"Cost": 1150.0, "Quality": 0.9},
                "Option3": {"Cost": 1100.0, "Quality": 1.0}},
            3: {"Option1": {"Cost": 341.3, "Quality": 0.8},
                "Option2": {"Cost": 310.9, "Quality": 0.9},
                "Option3": {"Cost": 288.0, "Quality": 1.0}},
            4: {"Option1": {"Cost": 520.0, "Quality": 0.9},
                "Option2": {"Cost": 490.3, "Quality": 0.95},
                "Option3": {"Cost": 468.0, "Quality": 1.0}},
            5: {"Option1": {"Cost": 14062.5, "Quality": 0.8},
                "Option2": {"Cost": 12375.0, "Quality": 0.9},
                "Option3": {"Cost": 11250.0, "Quality": 1.0}},
            6: {"Option1": {"Cost": 360.0, "Quality": 0.8},
                "Option2": {"Cost": 360.0, "Quality": 0.9},
                "Option3": {"Cost": 360.0, "Quality": 1.0}},
            7: {"Option1": {"Cost": 3150.0, "Quality": 0.9},
                "Option2": {"Cost": 2778.9, "Quality": 0.95},
                "Option3": {"Cost": 2509.1, "Quality": 1.0}},
            8: {"Option1": {"Cost": 1024.0, "Quality": 0.8},
                "Option2": {"Cost": 870.4, "Quality": 0.9},
                "Option3": {"Cost": 768.0, "Quality": 1.0}},
            9: {"Option1": {"Cost": 1371.4, "Quality": 0.9},
                "Option2": {"Cost": 1242.4, "Quality": 0.95},
                "Option3": {"Cost": 1152.0, "Quality": 1.0}},
            10: {"Option1": {"Cost": 19220.0, "Quality": 0.8},
                 "Option2": {"Cost": 16913.6, "Quality": 0.9},
                 "Option3": {"Cost": 15376.0, "Quality": 1.0}},
            11: {"Option1": {"Cost": 2362.5, "Quality": 0.8},
                 "Option2": {"Cost": 2100.0, "Quality": 0.9},
                 "Option3": {"Cost": 1909.1, "Quality": 1.0}},
            12: {"Option1": {"Cost": 784.0, "Quality": 0.8},
                 "Option2": {"Cost": 666.4, "Quality": 0.9},
                 "Option3": {"Cost": 588.0, "Quality": 1.0}},
            13: {"Option1": {"Cost": 1105.7, "Quality": 0.9},
                 "Option2": {"Cost": 986.5, "Quality": 0.95},
                 "Option3": {"Cost": 903.0, "Quality": 1.0}},
            14: {"Option1": {"Cost": 15125.0, "Quality": 0.8},
                 "Option2": {"Cost": 13310.0, "Quality": 0.9},
                 "Option3": {"Cost": 12100.0, "Quality": 1.0}},
            15: {"Option1": {"Cost": 2442.9, "Quality": 0.8},
                 "Option2": {"Cost": 2179.4, "Quality": 0.9},
                 "Option3": {"Cost": 1995.0, "Quality": 1.0}},
            16: {"Option1": {"Cost": 484.0, "Quality": 0.8},
                 "Option2": {"Cost": 411.4, "Quality": 0.9},
                 "Option3": {"Cost": 363.0, "Quality": 1.0}},
            17: {"Option1": {"Cost": 950.0, "Quality": 0.9},
                 "Option2": {"Cost": 813.6, "Quality": 0.95},
                 "Option3": {"Cost": 722.0, "Quality": 1.0}},
            18: {"Option1": {"Cost": 12500.0, "Quality": 0.8},
                 "Option2": {"Cost": 11000.0, "Quality": 0.9},
                 "Option3": {"Cost": 10000.0, "Quality": 1.0}},
            19: {"Option1": {"Cost": 300.0, "Quality": 0.8},
                 "Option2": {"Cost": 289.3, "Quality": 0.9},
                 "Option3": {"Cost": 281.3, "Quality": 1.0}},
            20: {"Option1": {"Cost": 400.0, "Quality": 0.8},
                 "Option2": {"Cost": 391.1, "Quality": 0.9},
                 "Option3": {"Cost": 384.0, "Quality": 1.0}}
        }
        labor_cost = {
            1: 700,
            2: 300,
            3: 600,
            4: 750,
            5: 1700,
            6: 430,
            7: 450,
            8: 800,
            9: 1000,
            10: 750,
            11: 460,
            12: 800,
            13: 100,
            14: 750,
            15: 470,
            16: 800,
            17: 1000,
            18: 750,
            19: 300,
            20: 750
        }

        lc_day = labor_cost[self.i+1]
        time = self.activities
        dur = time["{}".format(self.i+1)]
        cost_of_labor = lc_day*dur

        c_wc = cost_of_labor * 0.139
        c_mo = cost_of_labor * 0.05
        c_fo = 150 * dur
        c_fs = 150 * dur

        indirect_cost = c_wc+c_mo+c_fo+c_fs

        cost_of_material = material[self.i+1]["Option{}".format(self.mc)]["Cost"]
        cost_of_administartion = administartion[self.i+1]["Option{}".format(self.ac)]["Cost"]*dur
        cost_of_equipment = equipment[self.i+1]["Option{}".format(self.ec)]["Cost"]

        direct_cost = cost_of_labor + cost_of_material + cost_of_administartion + cost_of_equipment

        total_cost = direct_cost + indirect_cost

        return total_cost


# activities = {'1': 2}
# NB = CostCal(2,2,2,activities,0)
# ZX = print(NB.computee())