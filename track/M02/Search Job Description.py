class JobDescription:
    def __init__(self, job_id, company, role):
        self.job_id = job_id
        self.company = company
        self.role = role

    def __str__(self):
        return f"{self.job_id} - {self.company} - {self.role}"


class PlacementManager:
    def __init__(self):
        self.job_descriptions = []

    def add_job_description(self, job_description):
        self.job_descriptions.append(job_description)

    def find_job_by_id(self, job_id):
        # Search for and return the matching object
        for job in self.job_descriptions:
            if str(job.job_id) == str(job_id):
                return job
        # Return None if no match is found
        return None


# Driver Code
if __name__ == "__main__":
    manager = PlacementManager()

    # Read number of jobs
    n = int(input().strip())

    # Read details for each job
    for _ in range(n):
        job_id = input().strip()
        company = input().strip()
        role = input().strip()
        
        job = JobDescription(job_id, company, role)
        manager.add_job_description(job)

    # Read target job ID to search for
    search_id = input().strip()

    # Find the job using PlacementManager
    result = manager.find_job_by_id(search_id)

    # Output results
    if result:
        print(result)
    else:
        print(f"Job description with ID {search_id} not found")