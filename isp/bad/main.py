from models.manager import Manager
from models.member import Member
from models.owner import Owner


if __name__ == '__main__':
  member = Member('Thauan', 'thauanandre09@gmail.com')
  manager = Manager('John Doe', 'johndoe@gmail.com')
  owner = Owner('Jeff', 'realjeff@gmail.com')

  print(member.code())
  print(manager.code())
  print(owner.code())

  print(member.pay_bills())
  print(manager.pay_bills())
  print(owner.pay_bills())