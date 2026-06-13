import math

def main():
    can_names = ["Chocolate","Mango","Pineapple"]
    can_radiuses = ["6.83","7.78","8.73"]

    can_heights = [10.16, 11.91, 11.59]

    can_costs = [0.28, 0.43, 0.45]

    best_store = None
    best_cost = None
    max_store_eff = -1
    max_cost_eff = -1
# for each can in the parallel lists, unpack the values.
# into the variables name, radius, height, and cost.
    for i in range(len(can_names)):
        name = can_names[i]
        radius = can_radiuses[i]
        height = can_heights[i]
        cost = can_costs[i]
# call the function efficiency like, storage and cost
compute_storage_efficiency = float()
compute_cost_efficiency = float()

store_eff = compute_storage_efficiency(radius,height)
cost_eff = compute_cost_efficiency(radius, height, cost)

# print the can size name. storage
# efficiency, and cost efficiency.

print(f"{name} {store_eff:.2f} {cost_eff:.2f}")