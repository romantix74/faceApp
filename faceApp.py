import requests
import json


"""
https://api.github.com/repos/gvanrossum/patma  STAR: 401
https://api.github.com/repos/gvanrossum/500lines  STAR: 230
https://api.github.com/repos/gvanrossum/pyxl3  STAR: 119
https://api.github.com/repos/gvanrossum/cpython  STAR: 83
https://api.github.com/repos/gvanrossum/guidos_time_machine  STAR: 68
"""

username = 'romantix74'

password = "..INSERT PASSWORD HERE..."

git_repo_user = "gvanrossum"


def parse_github():

    headers_data = {'Accept': 'application/vnd.github.v3+json'}
    
    r = requests.get(f"https://api.github.com/users/{git_repo_user}/repos",
        headers=headers_data
        )
    
    res = json.loads(r.text) 
        
    sorted_res = sorted(res, key=lambda i: i['stargazers_count'], reverse=True)[0:5]  

    for i in sorted_res:
        print(f"{i['url']}")   # STAR: {i['stargazers_count']}")

if __name__ == '__main__':

    parse_github()