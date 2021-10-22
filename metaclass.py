class MakeCustomMetaclass(type):

    def __new__(mcs, class_name,
                class_parents, class_attr):

        case_attr = {}
        for name, val in class_attr.items():
            if not name.startswith('__'):
                case_attr["custom_" + name] = val
            else:
                case_attr[name] = val

        return super(MakeCustomMetaclass, mcs).__new__(mcs, class_name,
                                                       class_parents, case_attr)


class CustomClass(metaclass=MakeCustomMetaclass):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100