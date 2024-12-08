from models.repo import Repo


class GithubReport:
    @classmethod
    def parse(cls, response):
        return [Repo(repo["id"], repo["name"]) for repo in response]
