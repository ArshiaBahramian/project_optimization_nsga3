import networkx as nx


def calculate_critical_path(activities, dependencies):
    # ایجاد یک گراف جهت‌دار
    G = nx.DiGraph()

    # اضافه کردن گره‌ها به گراف با وزن برابر با زمان اجرای فعالیت
    for activity, duration in activities.items():
        G.add_node(activity, duration=duration)

    # اضافه کردن یال‌ها بر اساس پیش‌نیازها
    for activity, prereqs in dependencies.items():
        for prereq in prereqs:
            # افزودن یک یال از پیش‌نیاز به فعالیت با وزن برابر با زمان اجرای پیش‌نیاز
            G.add_edge(prereq, activity, weight=activities[prereq])

    # محاسبه مسیر بحرانی با استفاده از طولانی‌ترین مسیر
    critical_path = nx.dag_longest_path(G)
    critical_path_duration = nx.dag_longest_path_length(G)

    return critical_path, critical_path_duration




dependencies = {
    '1': ['start'],
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
    '20': ['19'],
    'end': ['20', '6']
}

activities = {
    'start': 0,
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
    'end': 0
}
activities = {
    'Start': 0,
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 4,
    'E': 6,
    'F': 1,
    'End': 0
}
dependencies = {
    'A': ['Start'],
    'B': ['Start'],
    'C': ['A', 'B'],
    'D': ['C'],
    'E': ['C'],
    'F': ['E'],
    'End': ['D', 'F']}
# محاسبه مسیر بحرانی و چاپ آن
critical_path, total_duration = calculate_critical_path(activities, dependencies)
print("Critical Path:", " -> ".join(critical_path))
print("Total Duration:", total_duration)
