from clients.github import GithubClient
from repos.github import GithubReport
from reports.generator import ReportGenerator
from reports.writer import ReportWriter
from reports.file_writer import FileWriter

if __name__ == "__main__":
    response = GithubClient.get_repos_by_user("Thauan-th")

    if response["status_code"] == 200:
        repos = GithubReport.parse(response["body"])

        html = ReportGenerator.build('html', repos)
        markdown = ReportGenerator.build('md', repos)

        ReportWriter.write(markdown)  # A default writer exists
        # ReportWriter.write(html, ExternalApiWriter) # a new writer can be added, very easy
    else:
        print("[Error] Something went wrong")
