from collections import defaultdict
import heapq
def min_time_to_attach_photos(n, times, parents):
    tree = defaultdict(list)
    for child, parent in enumerate(parents, start=2):
        tree[parent].append(child)
    min_time = [0] * (n + 1)
    def dfs(node):
        if not tree[node]:
            return times[node - 1]
        child_times = []
        for child in tree[node]:
            heapq.heappush(child_times, -dfs(child))
        required_children = (len(tree[node]) + 1) // 2
        total_time = 0
        for _ in range(required_children):
            total_time += -heapq.heappop(child_times)
        min_time[node] = total_time + times[node - 1]
        return min_time[node]
    return dfs(1)

n = int(input("Введите количество людей: "))
times = list(map(int, input("Введите времена ti через пробел: ").split()))
parents = list(map(int, input("Введите родителей для узлов от 2 до n через пробел: ").split()))
print(min_time_to_attach_photos(n, times, parents))