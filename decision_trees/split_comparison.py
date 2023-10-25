import numpy as np

# initial 800 DP, davon 4 in Class 0, 4 in Class 1
initial = np.array([0.5, 0.5])

def entropy(p) -> float:
    return -np.sum( p * np.log2(p) )

print(f"Initîally: {initial} -> Entropy {entropy(initial)}")
# Split A 
left = entropy(np.array([300.0 / 400 , 100.0 / 400]))
right = entropy(np.array([100.0 / 400 , 300.0 / 400]))
# value of split
costs_after = (1./2)*left + (1./2)*right
print("Split A costs: ", costs_after)

# Split B
left = entropy(np.array([200.0 / 600 , 400.0 / 600]))
right = 0 # entropy(np.array([1 , 0]))
# value of split
costs_after = (600./800)*left + (200./800)*right
print("Split B costs: ", costs_after)
