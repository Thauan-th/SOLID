class HtmlGenerator:
    @classmethod
    def build(cls, repos):
        items = ' '.join(
            f'<strong>{repo.id}</strong>:  <strong>{repo.name}</strong>\n' for repo in repos
        )
        return f'<p>{items}</p>'
