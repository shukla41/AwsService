from ruamel.yaml import YAML
from pathlib import Path

print("Python started")
yaml = YAML()
path = Path(r'C:\Users\shumondal\PycharmProjects\Lambda\example.yaml')
newPath=Path(r'C:\Users\shumondal\PycharmProjects\Lambda\examplereplace.yaml')

data = yaml.load(path)
parameters = data['parameters']
# replace assigned values with user input
parameters['private_network_id']['default'] = '999','220'
parameters['floating_ip']['default'] = '777'
yaml.dump(data, newPath)