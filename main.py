from indeed import get_jobs as get_indeed_jobs
from stackover import get_jobs as get_so_jobs
from save import save_to_file

stackover_jobs = get_so_jobs()
indeed_jobs = get_indeed_jobs()

jobs = stackover_jobs + indeed_jobs

save_to_file(jobs)