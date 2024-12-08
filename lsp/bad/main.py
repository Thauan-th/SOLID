from models.manager import Manager
from models.member import Member
from models.owner import Owner


if __name__ == '__main__':
  member = Member('Thauan', 'thauanandre09@gmail.com')
  manager = Manager('John Doe', 'johndoe@gmail.com')
  owner = Owner('Jeff', 'realjeff@gmail.com')
  
  print(member.members())
  print(manager.members())
  print(owner.members())