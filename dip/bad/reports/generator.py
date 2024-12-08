from generators.html import HtmlGenerator
from generators.markdown import MarkdownGenerator

class ReportGenerator:
    # The problem lives here, this class makes a logic to handle with report format but it's a problem
    # a new if will be placed below when a new format comes up

    @classmethod
    def build(cls, format, repos):
        if format == 'html':
            return HtmlGenerator.build(repos)
        elif format == 'md':
            return MarkdownGenerator.build(repos)
        # ...
        # ...
        # ...
        else:
            raise 'Invalid Format'

# This class "hides" a very necessary logic and if some reports take another params for exemple, it will be handled here
# which can introduce bugs or unucessary code
