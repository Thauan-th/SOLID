class FileWriter:

    @staticmethod
    def write(report):
        file = open('file-good-dip.txt',  'w')
        file.write(report)
        file.close()
