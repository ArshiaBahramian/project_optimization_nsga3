import networkx as nx


def critical_path(activities, predecessors, durations):
    """
  مسیر بحرانی پروژه را با استفاده از کتابخانه NetworkX محاسبه می‌کند.

  آرگومان‌ها:
    activities: لیست نام فعالیت‌ها
    predecessors: دیکشنری که کلیدهای آن نام فعالیت‌ها و مقادیر آن لیست پیش‌نیازهای هر فعالیت است.
    durations: دیکشنری که کلیدهای آن نام فعالیت‌ها و مقادیر آن زمان انجام هر فعالیت است.

  برمی‌گرداند:
    مسیر بحرانی به عنوان لیست نام فعالیت‌ها
    زمان کل پروژه
  """

    # ایجاد گراف پروژه
    G = nx.DiGraph()
    for activity in activities:
        G.add_node(activity)
    for activity, preds in predecessors.items():
        for pred in preds:
            G.add_edge(pred, activity)

    # محاسبه طول مسیر بحرانی
    critical_path = nx.dag_longest_path(G)
    critical_path_length = 0
    for i in range(len(critical_path) - 1):
        critical_path_length += durations[critical_path[i]]

    return critical_path, critical_path_length


# مثال

activities = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
              "20"]
predecessors = {
    '2': ['1'],
    '3': ['2'],
    '4': ['3'],
    '5': ['4'],
    '6': ['5'],
    '7': ['5'],
    '8': ['7'],
    '9': ['8'],
    '10': ['9'],
    '11': ['7'],
    '12': ['8', '11'],
    '13': ['9', '12'],
    '14': ['10', '13'],
    '15': ['11'],
    '16': ['15', '12'],
    '17': ['13', '16'],
    '18': ['14', '17'],
    '19': ['18'],
    '20': ['19']
}

durations = {
    '1': 1,
    '2': 1,
    '3': 1,
    '4': 1,
    '5': 1,
    '6': 1,
    '7': 1,
    '8': 1,
    '9': 2,
    '10': 1,
    '11': 2,
    '12': 2,
    '13': 2,
    '14': 2,
    '15': 3,
    '16': 3,
    '17': 3,
    '18': 3,
    '19': 1,
    '20': 1,
}

# محاسبه مسیر بحرانی
critical_path, critical_path_length = critical_path(activities, predecessors, durations)

# چاپ نتایج
print("مسیر بحرانی:", critical_path)
print("زمان کل پروژه:", critical_path_length)
