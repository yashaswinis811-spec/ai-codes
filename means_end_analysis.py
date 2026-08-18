from collections import deque


def means_end_analysis(capacity_a, capacity_b, target):
    """
    Solve the Water Jug Problem using Means-End Analysis.

    capacity_a: Capacity of Jug A
    capacity_b: Capacity of Jug B
    target: Amount of water we want to obtain
    """

    # State = (amount in Jug A, amount in Jug B)
    start_state = (0, 0)

    # Queue for exploring states
    queue = deque([start_state])

    # Keep track of visited states
    visited = {start_state}

    # Store the path to the solution
    parent = {start_state: None}

    # Store the action used to reach each state
    action = {}

    while queue:

        current = queue.popleft()
        a, b = current

        # Goal test
        if a == target or b == target:
            return get_solution_path(current, parent, action)

        # Generate possible actions
        possible_moves = [
            ((capacity_a, b), "Fill Jug A"),
            ((a, capacity_b), "Fill Jug B"),
            ((0, b), "Empty Jug A"),
            ((a, 0), "Empty Jug B"),
        ]

        # Pour A -> B
        amount = min(a, capacity_b - b)
        possible_moves.append(
            ((a - amount, b + amount), "Pour Jug A -> Jug B")
        )

        # Pour B -> A
        amount = min(b, capacity_a - a)
        possible_moves.append(
            ((a + amount, b - amount), "Pour Jug B -> Jug A")
        )

        # Explore each possible state
        for new_state, move in possible_moves:

            if new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)

                parent[new_state] = current
                action[new_state] = move

    return None


def get_solution_path(goal, parent, action):
    """
    Reconstruct the path from the initial state to the goal.
    """

    path = []

    current = goal

    while current is not None:
        path.append((current, action.get(current)))
        current = parent[current]

    path.reverse()

    return path


def main():

    print("========================================")
    print(" Means-End Analysis - Water Jug Problem")
    print("========================================")

    capacity_a = int(input("Enter capacity of Jug A: "))
    capacity_b = int(input("Enter capacity of Jug B: "))
    target = int(input("Enter target amount: "))

    # Basic validation
    if target > max(capacity_a, capacity_b):
        print("\nTarget cannot be greater than both jug capacities.")
        return

    print("\nSearching for solution...\n")

    solution = means_end_analysis(
        capacity_a,
        capacity_b,
        target
    )

    if solution is None:
        print("No solution exists.")
    else:
        print("Solution found!\n")

        for step, (state, move) in enumerate(solution):

            if move is None:
                print(f"Step {step}: Start -> {state}")
            else:
                print(f"Step {step}: {move} -> {state}")

        print("\nGoal reached!")


if __name__ == "__main__":
    main()
