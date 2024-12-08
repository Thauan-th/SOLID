from clients.github import GithubClient
from reports.github import GithubReport


if __name__ == "__main__":
    response = GithubClient.get_repos_by_user("Thauan-th")

    if response["status_code"] == 200:
        GithubReport.parse(response["body"])
    else:
        print("[Error] Something went wrong")
