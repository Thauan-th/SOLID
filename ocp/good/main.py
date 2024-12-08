from clients.github import GithubClient
from repos.github import GithubReport
from reports.generator import ReportGenerator

from generators.html import HtmlGenerator
from generators.markdown import MarkdownGenerator

if __name__ == "__main__":
    response = GithubClient.get_repos_by_user("Thauan-th")

    if response["status_code"] == 200:
        repos = GithubReport.parse(response["body"])

        html = ReportGenerator.build(HtmlGenerator, repos)
        markdown = ReportGenerator.build(MarkdownGenerator, repos)

        print(html)
        print(markdown)
    else:
        print("[Error] Something went wrong")
