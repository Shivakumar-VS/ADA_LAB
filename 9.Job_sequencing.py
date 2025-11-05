class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit


def job_sequencing(jobs):
    # Step 1: Sort all jobs by descending profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    n = len(jobs)
    result = [None] * n   # Stores job sequence
    slot = [False] * n    # Slot availability

    # Step 2: Assign jobs
    for job in jobs:
        # Find a slot for this job (before or on its deadline)
        for j in range(min(n, job.deadline) - 1, -1, -1):
            if not slot[j]:
                slot[j] = True
                result[j] = job.job_id
                break

    # Step 3: Print the sequence
    print("Job sequence to maximize profit:")
    for job_id in result:
        if job_id:
            print(job_id, end=" ")

# Example usage
jobs = [
    Job('a', 2, 100),
    Job('b', 1, 19),
    Job('c', 2, 27),
    Job('d', 1, 25),
    Job('e', 3, 15)
]

job_sequencing(jobs)
