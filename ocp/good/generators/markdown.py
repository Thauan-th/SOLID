class MarkdownGenerator:
    @classmethod
    def build(cls, repos):
        items = ' '.join(
            f'ID: {repo.id} - **{repo.name}**\n' for repo in repos
        )
        return f'## Repos \n\n {items}'
