from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file

so_jobs =get_so_jobs()
indeed_jobs = get_indeed_jobs()
jobs = so_jobs + indeed_jobs
print(jobs)

#csv -> 윈도우, 맥, 구글드라이브 등에서 모두 사용 가능
#Comma Separated Values
# colum = comma로 나눔
# row = new line 
save_to_file(jobs)