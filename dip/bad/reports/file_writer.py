class FileWriter:
  
  @staticmethod
  def wrife_file(report):
    file = open('file-bad-dip.txt',  'w')
    file.write(report)
    file.close()