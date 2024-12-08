import requests

# This class is an example of what not to do, because it handles with a bunch of responsabilites
# Generate tests for this class will be a problem because it handles requests, serializing data, https status and reports
# It is likely to continue and get worse every time

class ListUserRepositories:

    API_BASE_URL = "https://api.github.com"

    def __init__(self, user):
        self._user = user

    # Client
    def list_repositories(self):
        response = requests.get(f"{self.API_BASE_URL}/users/{self._user}/repos")

        # Serializing
        if response.status_code == 200:
            return {"status_code": 200, "body": response.json()}
        else:
            return {"status_code": response.status_code, "body": "Something went wrong"}

    # Report Logic
    def report(self):
        response = self.list_repositories()

        if response["status_code"] == 200:
            body = response["body"]

            for idx in range(len(body)):
                repo = body[idx]
                print(f"{repo['id']} - {repo['name']}")

        else:
            return "Something went wrong"


list_repos = ListUserRepositories("Thauan-th")
list_repos.report()
