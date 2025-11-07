def job_sequencing(jobs, n):
    jobs.sort(key=lambda x: x[2], reverse=True)
    result = [False]*n
    job_seq = ['-1']*n
    for job in jobs:
        for j in range(min(n, job[1])-1, -1, -1):
            if not result[j]:
                result[j] = True
                job_seq[j] = job[0]
                break
    print("Job sequence:", job_seq)

n = int(input("Enter number of jobs: "))
jobs = []
for i in range(n):
    job_id = input("Job ID: ")
    deadline = int(input("Deadline: "))
    profit = int(input("Profit: "))
    jobs.append((job_id, deadline, profit))

job_sequencing(jobs, n)