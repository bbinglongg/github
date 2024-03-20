import requests

def get_repos_containing_string(org, token, search_string):
    repos_containing_string = []
    page = 1
    while True:
        url = f'https://api.github.com/orgs/{org}/repos?type=all&page={page}'
        headers = {'Authorization': f'token {token}'}
        response = requests.get(url, headers=headers)
        response_json = response.json()
        if response.status_code != 200 or not response_json:
            break
        for repo in response_json:
            if search_string in repo['name']:
                repos_containing_string.append(repo['name'])
        page += 1
    return repos_containing_string

# 替换下面的值
org = 'your_org_name'  # 组织名
token = 'your_github_token'  # GitHub Token
search_string = '/1'  # 要搜索的字符串

repos = get_repos_containing_string(org, token, search_string)
print(f'Repos in {org} containing "{search_string}":')
for repo in repos:
    print(repo)
