from models.repo import Repo


class GithubReport:

    @classmethod
    def parse(cls, response):
        for i in range(len(response)):
            repo = response[i]
            repo = Repo(repo["id"], repo["name"])
            print(repo)
