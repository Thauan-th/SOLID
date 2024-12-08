from clients.github import GithubClient
from repos.github import GithubReport
from reports.generator import ReportGenerator

if __name__ == "__main__":
    response = GithubClient.get_repos_by_user("Thauan-th")

    if response["status_code"] == 200:
        repos = GithubReport.parse(response["body"])

        html = ReportGenerator.build('html', repos)
        markdown = ReportGenerator.build('md', repos)

        print(html)
        print(markdown)
    else:
        print("[Error] Something went wrong")
