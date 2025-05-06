# /// script
# dependencies = [
#   "requests",
# ]
# ///

import requests
from urllib.parse import urlparse


def extract_owner_repo(github_url: str) -> tuple:
    """Extract owner and repository name from GitHub URL."""
    try:
        # Parse the URL and split the path
        path_parts = urlparse(github_url.strip()).path.strip("/").split("/")

        if len(path_parts) < 2:
            raise ValueError("Invalid GitHub repository URL")

        return path_parts[0], path_parts[1]
    except Exception as e:
        raise ValueError(f"Invalid GitHub URL format: {str(e)}")


def get_repo_info(github_url):
    # Extract owner and repo from URL
    owner, repo = extract_owner_repo(github_url)

    # Headers for GitHub API
    github_token = ...
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json",
    }

    # Get repository information including the description (about section)
    repo_url = f"https://api.github.com/repos/{owner}/{repo}"
    repo_response = requests.get(repo_url, headers=headers)

    if repo_response.status_code != 200:
        raise Exception(f"Failed to fetch repository info: {repo_response.status_code}")

    repo_data = repo_response.json()
    about_section = repo_data.get("description", "")

    return {"title": repo, "about": about_section}


def main():
    with open("export.txt", "r") as f:
        data = f.read().splitlines()

    output = []

    for url in data:
        if url.startswith("https://github.com/"):
            repo_info = get_repo_info(url)
            about = repo_info["about"].strip().split(". ")[0]
            if about[-1] == ".":
                about = about[:-1]
            about = about[0].lower() + about[1:]
            output.append(f"- [{repo_info['title']}: {about}]({url})")

    print("\n".join(output))


if __name__ == "__main__":
    main()
