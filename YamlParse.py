import yaml
from collections import defaultdict

class MyStruct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)

class Step:
    def __init__(self,sql,stepName):
        self.sql= list(sql)
        self.stepname= list(stepName)
        return

class Event(object):
    def __init__(self,events):
        self.evnt= Step
        return

def object_decoder(arg):
    l= []
    for u in range((len(arg))):
        for i, k in arg[u].items():
            if i == 'sql':
                l.append(str(k))
    return l

class getObjectFromYaml(object):
    def __init__(self,*krgs):
        self.sql= krgs
        return

if __name__ == '__main__':
    with open(r"C:\Users\shumondal\PycharmProjects\Lambda\example.yaml") as stream:
        data = yaml.full_load(stream)

        y = MyStruct(**data)
        print(y.step)
        print(y.flag)
        v= object_decoder(y.step)
        g=getObjectFromYaml(v)
        print(g.sql)
