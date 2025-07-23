data = '{"member_id":#member_id#,"amount": "1"}'
member_id = 100

data = data.replace("#member_id#", str(member_id))
print(data)