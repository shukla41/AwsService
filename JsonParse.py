import yaml

class MyStruct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

if __name__ == '__main__':

    with open(r"C:\Users\shumondal\PycharmProjects\Lambda\Transform_hierarchy.yaml") as stream:
        data=yaml.full_load(stream)
        for i in (range(len(data))):
            for key, val in dict(data[i]).items():
                if key == 'step':
                    print(val)
                    y = MyStruct(**val[1])
                    for key,val in val[1].items():
                        print(val)