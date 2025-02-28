import ast
from enum import Enum
from multiprocessing import parent_process


class NodeType(Enum):
    APPLICATION = "APPLICATION"
    MODULE = "MODULE"
    CLASS = "CLASS"
    METHOD = "METHOD"
    IMPORT = "IMPORT"


class ProgramNode:
    def __init__(self, type, name, size, parent=None):
        self.type = type
        self.name = name
        self.size = size
        self.nodes = []
        self.children = []
        self.parent = parent
        self.level = parent.level + 1 if parent is not None else 1

        if parent:
            parent.add_child(self)

    def add_child(self, node):
        self.children.append(node)

    def __repr__(self):
        return f"{self.type.value}({self.name}, children={len(self.children)})"


class Application(ProgramNode):
    def __init__(self, name, absolute_location, relative_location, size):
        super().__init__(NodeType.APPLICATION, name, size),
        self.absolute_location = (absolute_location,)
        self.relative_location = (relative_location,)
        self.files = []

    def __repr__(self):
        return f"Application(name={self.name},\
                absolute_location={self.absolute_location},\
                relative_location={self.relative_location},\
                size={self.size},\
                )"

    def __str__(self):
        tabs = "\t" * (self.level - 1)
        string = tabs + f"Application: {self.name} {{\n"
        for module in self.children:
            string += str(module) + "\n"
        string += tabs + "\t}"
        return string


class Module(ProgramNode):
    def __init__(self, name, absolute_location, relative_location, size):
        super().__init__(NodeType.MODULE, name, size)
        self.absolute_location = absolute_location
        self.relative_location = relative_location


class Import(ProgramNode):
    def __init__(self, name, size, parent):
        super().__init__(NodeType.IMPORT, name, size, parent)


class Class(ProgramNode):
    def __init__(self, name, size):
        super().__init__(NodeType.CLASS, name, size)


class Method(ProgramNode):
    def __init__(self, name, size):
        super().__init__(NodeType.METHOD, name, size)
