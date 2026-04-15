# Algorithms Midterm — Python Solutions

Reference implementations for a 7-question algorithms midterm covering core CS concepts.

---

## 📁 File Structure

```
.
├── algorithms_midterm.py   # All solutions in one runnable file
├── .gitignore
└── README.md
```

---

## 🚀 How to Run

**Requirements:** Python 3.7+

```bash
python algorithms_midterm.py
```

**Expected output:**

```
Q1 Bubble Sort: [1, 2, 4, 5, 8]
Q2 Factorial(5): 120
Q3 Number of coins: 6
Q3 Coins used: [25, 25, 10, 1, 1, 1]
Q4 DFS Search for 7: Found
Q5 Stack: [10, 30]
Q5 Queue: [20, 30]
Q6 Linked List: 1 2 3 4

Q7 L1 (Manhattan) distances:
  A: 3
  B: 3
  C: 4
Q7 L2 (Euclidean) distances:
  A: 2.236
  B: 2.236
  C: 3.162
Q7 Nearest under L1: A
Q7 Nearest under L2: A
```

---

## 📚 Topics Covered

| # | Topic | Function(s) |
|---|-------|-------------|
| 1 | Sorting | `bubble_sort(arr)` |
| 2 | Recursion | `factorial(n)` |
| 3 | Greedy Algorithm | `min_coins(amount)` |
| 4 | Tree + DFS Search | `TreeNode`, `dfs_search(root, target)` |
| 5 | Stack & Queue | Python `list` + `collections.deque` |
| 6 | Linked List | `ListNode` |
| 7 | Nearest Neighbor (L1 / L2) | `l1(p, q)`, `l2(p, q)` |

---

## 🔍 Algorithm Notes

### Q1 — Bubble Sort
Repeatedly compares adjacent elements and swaps them if out of order.  
Time complexity: **O(n²)** | Space: **O(1)**

### Q2 — Factorial (Recursion)
Classic base case `n ≤ 1 → 1`, recursive case `n * factorial(n-1)`.  
Time complexity: **O(n)** | Space: **O(n)** call stack

### Q3 — Greedy Coin Change
Always pick the largest denomination that fits.  
Works correctly for standard coin sets `[25, 10, 5, 1]`.

### Q4 — Binary Tree DFS
Tree structure:
```
        5
       / \
      3   8
     / \    \
    2   4    7
```
Recursive DFS visits left and right subtrees to locate the target.

### Q5 — Stack & Queue
- **Stack**: Python `list` with `.append()` / `.pop()`
- **Queue**: `collections.deque` with `.append()` / `.popleft()`

### Q6 — Singly Linked List
Manual node chaining via `.next` pointers; traversal with a `while curr` loop.

### Q7 — Nearest Neighbor (L1 / L2)
| Metric | Formula |
|--------|---------|
| L1 (Manhattan) | `Σ |pᵢ - qᵢ|` |
| L2 (Euclidean) | `√(Σ (pᵢ - qᵢ)²)` |

Training points: A(1,1), B(4,4), C(6,1) — Test point: P(3,2)  
Nearest neighbor under **both** metrics: **A**

---

## 📝 License

This project is for educational purposes only.