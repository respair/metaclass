"""metaclass"""

class MakeCustomMetaclass(type):
    """a metaclass that changes the name of attributes (except for special ones)"""

    def __new__(mcs, class_name,
                class_parents, class_attr):
        """adding custom_ to the beginning of the name"""

        case_attr = {}
        for name, val in class_attr.items():
            if not name.startswith('__'):
                case_attr["custom_" + name] = val
            else:
                case_attr[name] = val

        return super(MakeCustomMetaclass, mcs).__new__(mcs, class_name,
                                                       class_parents, case_attr)


class CustomClass(metaclass=MakeCustomMetaclass):
    """used in main to validate metaclass"""
    x = 50

    def __init__(self, val=99):
        """constructor"""
        self.val = val

    def line(self):
        """just function"""
        return 100