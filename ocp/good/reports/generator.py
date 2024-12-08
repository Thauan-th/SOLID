# Now this class looks more clean, but maybe you can think this is unecessary
# But more processing can be added here, so I can use many generators here and not more code will be added to this class
# To add a new format, now we have to just implement the generator

class ReportGenerator:
    @classmethod
    def save_on_db(cls, content):
        # just for example
        print('[TRANSACTION INIT] saving the raw content on DB')
        print('[TRANSACTION FINISHED] saving the raw content on DB, took 0,015ms')
        return content

    @classmethod
    def build(cls, generator, repos):
        report = generator.build(repos)
        cls.save_on_db(report)
        return report
