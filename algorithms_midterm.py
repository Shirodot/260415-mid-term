from collections import deque
import math

# ─────────────────────────────────────────────────────────────────────────────
# Q1. Sorting - Bubble Sort
# ─────────────────────────────────────────────────────────────────────────────

def bubble_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [5, 1, 4, 2, 8]
print("Q1 Bubble Sort:", bubble_sort(arr))
# Expected: [1, 2, 4, 5, 8]


# ─────────────────────────────────────────────────────────────────────────────
# Q2. Recurrence / Recursive Thinking - Factorial
# ─────────────────────────────────────────────────────────────────────────────

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Q2 Factorial(5):", factorial(5))
# Expected: 120


# ─────────────────────────────────────────────────────────────────────────────
# Q3. Greedy - Minimum Coins
# ─────────────────────────────────────────────────────────────────────────────

def min_coins(amount):
    coins = [25, 10, 5, 1]
    used = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            used.append(coin)
    return used

used = min_coins(63)
print(f"Q3 Number of coins: {len(used)}")
print(f"Q3 Coins used: {used}")
# Expected: 6 coins; [25, 25, 10, 1, 1, 1]


# ─────────────────────────────────────────────────────────────────────────────
# Q4. Tree Construction and DFS Search
# ─────────────────────────────────────────────────────────────────────────────

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_search(root, target):
    if root is None:
        return False
    if root.val == target:
        return True
    return dfs_search(root.left, target) or dfs_search(root.right, target)

#        5
#       / \
#      3   8
#     / \    \
#    2   4    7

root = TreeNode(5,
                TreeNode(3, TreeNode(2), TreeNode(4)),
                TreeNode(8, None, TreeNode(7)))

print("Q4 DFS Search for 7:", "Found" if dfs_search(root, 7) else "Not Found")
# Expected: Found


# ─────────────────────────────────────────────────────────────────────────────
# Q5. Stack and Queue
# ─────────────────────────────────────────────────────────────────────────────

# Stack
stack = []
stack.append(10)
stack.append(20)
stack.pop()
stack.append(30)
print("Q5 Stack:", stack)

# Queue
queue = deque()
queue.append(10)
queue.append(20)
queue.popleft()
queue.append(30)
print("Q5 Queue:", list(queue))
# Expected: Stack: [10, 30]; Queue: [20, 30]


# ─────────────────────────────────────────────────────────────────────────────
# Q6. Linked List
# ─────────────────────────────────────────────────────────────────────────────

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Q6 Linked List:", end=" ")
curr = head
while curr:
    print(curr.val, end=" ")
    curr = curr.next
print()
# Expected: 1 2 3 4


# ─────────────────────────────────────────────────────────────────────────────
# Q7. Nearest Neighbor with L1 and L2 Distance
# ─────────────────────────────────────────────────────────────────────────────

A = (1, 1)
B = (4, 4)
C = (6, 1)
P = (3, 2)

def l1(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

def l2(p, q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)

points = {"A": A, "B": B, "C": C}

print("\nQ7 L1 (Manhattan) distances:")
for name, pt in points.items():
    print(f"  {name}: {l1(P, pt)}")

print("Q7 L2 (Euclidean) distances:")
for name, pt in points.items():
    print(f"  {name}: {round(l2(P, pt), 3)}")

nearest_l1 = min(points, key=lambda name: l1(P, points[name]))
nearest_l2 = min(points, key=lambda name: l2(P, points[name]))
print(f"Q7 Nearest under L1: {nearest_l1}")
print(f"Q7 Nearest under L2: {nearest_l2}")
# Expected: Nearest under both L1 and L2: A