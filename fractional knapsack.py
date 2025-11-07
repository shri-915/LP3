def fractional_knapsack(W, wt, val, n):
    ratio = [(val[i]/wt[i], wt[i], val[i]) for i in range(n)]  # value/weight ratio
    ratio.sort(reverse=True)  # Sort by ratio descending
    total_value = 0.0

    for r, w, v in ratio:
        if W >= w:       # Take full item if it fits
            W -= w
            total_value += v
        else:             # Take only fraction of the item
            total_value += v * (W / w)
            break
    return total_value

n = int(input("Enter number of items: "))
wt = []
val = []
for i in range(n):
    wt.append(int(input(f"Weight {i+1}: ")))
    val.append(int(input(f"Value {i+1}: ")))

W = int(input("Enter capacity of knapsack: "))
print("Maximum value in Knapsack =", fractional_knapsack(W, wt, val, n))