def min_boxes(n, k, boxes):
    boxes.sort(key=lambda x: (x[0], -x[1]))
    remaining_boxes = []
    for x, h in boxes:
        low, high = 0, len(remaining_boxes)
        while low < high:
            mid = (low + high) // 2
            if remaining_boxes[mid] >= h * k:
                high = mid
            else:
                low = mid + 1
        if low < len(remaining_boxes):
            remaining_boxes[low] = h
        else:
            remaining_boxes.append(h)
    return len(remaining_boxes)

n, k = map(int, input().split())
boxes = [tuple(map(int, input().split())) for _ in range(n)]
print(min_boxes(n, k, boxes))