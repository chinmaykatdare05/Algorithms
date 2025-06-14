def job_sequencing(jobs):
    """
    Solves the Job Sequencing Problem using a greedy approach.

    Time Complexity: O(N log N + N * M)
    Space Complexity: O(N)
    """
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find the maximum deadline
    max_deadline = max(job[1] for job in jobs)

    # Initialize slots (-1 indicates empty slot)
    slots = [-1] * max_deadline
    total_profit = 0
    selected_jobs = []

    # Schedule jobs
    for job_id, deadline, profit in jobs:
        for slot in range(
            min(deadline, max_deadline) - 1, -1, -1
        ):  # Find latest available slot
            if slots[slot] == -1:
                slots[slot] = job_id
                total_profit += profit
                selected_jobs.append(job_id)
                break  # Move to the next job

    return selected_jobs, total_profit


# Example Usage
jobs = [(1, 2, 100), (2, 1, 50), (3, 2, 10)]  # (Job ID, Deadline, Profit)
selected_jobs, profit = job_sequencing(jobs)
print("Selected Jobs:", selected_jobs)  # Output: [1, 2]
print("Total Profit:", profit)  # Output: 150
