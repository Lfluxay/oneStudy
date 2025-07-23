import yaml

with open('data.yaml', 'r', encoding='utf-8') as f:
    res = yaml.load(f, Loader=yaml.Loader)

print(res)

host = res['mysql']['host']
print(host)