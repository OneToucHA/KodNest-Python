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
        # Add the received job object
        self.job_descriptions.append(job_description)

    def display_job_descriptions(self):
        # Handle an empty collection
        if not self.job_descriptions:
            print("No job descriptions available")
            return
        
        # Display all job descriptions
        print("JOB DESCRIPTIONS")
        for job in self.job_descriptions:
            print(job)

manager = PlacementManager()
n = int(input())

for _ in range(n):
    job_id = input()
    company = input()
    role = input()
    job = JobDescription(job_id, company, role)
    manager.add_job_description(job)

manager.display_job_descriptions()