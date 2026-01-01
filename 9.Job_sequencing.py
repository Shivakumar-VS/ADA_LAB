# Program to implement Greedy algorithm for job sequencing with deadlines
class Job:
  def __init__(self, job_id, deadline, profit):
    self.job_id = job_id
    self.deadline = deadline
    self.profit = profit
def job_sequencing(jobs):
    jobs.sort(key = lambda x: x.profit, reverse=True)
    n = len(jobs)
    result = [None] * n
    slot = [False] * n

    for job in jobs:
        for j in range(min(n,job.deadline)-1,-1,-1):
            if not slot[j]:
                slot[j] = True
                result[j] = job.job_id
                break
    print("Job sequence to maximize profit:")
    for job_id in result:
        if job_id:
            print(job_id, end=' ')

jobs = [Job('J1', 2, 100),
        Job('J2', 1, 19),
        Job('J3', 2, 27),
        Job('J4', 1, 25),
        Job('J5', 3, 15)
    ]
job_sequencing(jobs)

