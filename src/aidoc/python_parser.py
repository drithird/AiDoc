import ast
from enum import Enum


class NodeType(Enum):
    APPLICATION = "APPLICATION"
    MODULE = "MODULE"
    CLASS = "CLASS"
    METHOD = "METHOD"


class ProgramNode:
    def __init__(self, type, name, size):
        self.type = type
        self.name = name
        self.size = size
        self.nodes = []


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
        return f"Application: {self.name}"


class Module(ProgramNode):
    def __init__(self, name, absolute_location, relative_location, size):
        super().__init__(NodeType.MODULE, name, size)
        self.absolute_location = absolute_location
        self.relative_location = relative_location


class Class(ProgramNode):
    def __init__(self, name, size):
        super().__init__(NodeType.CLASS, name, size)


class Method(ProgramNode):
    def __init__(self, name, size):
        super().__init__(NodeType.METHOD, name, size)
