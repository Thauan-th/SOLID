from models.manager import Manager
from models.member import Member

if __name__ == '__main__':
  member = Member('Thauan', 'thauanandre09@gmail.com')
  manager = Manager('John Doe', 'johndoe@gmail.com')

  print(member.work())
  print(manager.work())