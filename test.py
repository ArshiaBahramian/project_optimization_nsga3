import networkx as nx


def calculate_critical_path(activities, dependencies):
    # ایجاد یک گراف جهت‌دار
    G = nx.DiGraph()

    # اضافه کردن فعالیت‌ها به عنوان گره‌ها و تعریف مدت زمان هر یک
    for activity, duration in activities.items():
        G.add_node(activity, duration=duration)

    # اضافه کردن پیش‌نیازها به عنوان یال‌ها
    for activity, prereqs in dependencies.items():
        for prereq in prereqs:
            G.add_edge(prereq, activity)

    # محاسبه تمام مسیرهای ساده از منبع تا سینک
    all_paths = list(nx.all_simple_paths(G, source='Start', target='End'))

    # محاسبه طول هر مسیر بر اساس مدت زمان فعالیت‌ها
    path_durations = []
    for path in all_paths:
        path_duration = sum(activities[node] for node in path)
        path_durations.append((path, path_duration))

    # یافتن مسیر با بیشترین طول (مسیر بحرانی)
    critical_path, max_duration = max(path_durations, key=lambda x: x[1])

    return critical_path, max_duration


# نمونه اطلاعات فعالیت‌ها و پیش‌نیازها
activities = {
    'Start': 0,
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
    'End': 0,
}

dependencies = {
    'Start': ['1'],
    '1': ['2'],
    '2': ['3'],
    '3': ['4'],
    '4': ['5'],
    '5': ['6', '7'],
    '6': ['End'],
    '7': ['8', '11'],
    '8': ['9', '12'],
    '9': ['10', '13'],
    '10': ['14'],
    '11': ['12', '15'],
    '12': ['13', '16'],
    '13': ['14', '17'],
    '14': ['18'],
    '15': ['16'],
    '16': ['17'],
    '17': ['18'],
    '18': ['19'],
    '19': ['20'],
    '20': ['End'],
}

# محاسبه مسیر بحرانی و چاپ آن
critical_path, total_duration = calculate_critical_path(activities, dependencies)
print("Critical Path:", " -> ".join(critical_path))
print("Total Duration:", total_duration)
