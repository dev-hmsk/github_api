import requests

def get_repo_languages(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/languages"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Provide the owner and repository name
owner = "dev-hmsk"
repo = "noshgrab"

# Call the function
languages = get_repo_languages(owner, repo)

if languages:
    print("Languages used in the repository:")
    total_line_count = 0

    for language, lines in languages.items():
        total_line_count += lines
        print(f"{language}: {lines} lines")

    for language, lines in languages.items():
        percent = round(lines / total_line_count * 100, 2)
        print(f"{language}: {percent}% of {repo}")
else:
    print("Unable to retrieve repository information.")
