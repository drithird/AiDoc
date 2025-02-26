import ast
from enum import Enum


class NodeType(Enum):
    APPLICATION = "APPLICATION"
    MODULE = "MODULE"
    CLASS = "CLASS"
    METHOD = "METHOD"


class ProgramNode:
    def __init__(self, node_type, name, size):
        self.node_type = node_type
        self.node_name = name
        self.node_size = size
        self.modules = []
        self.functions = []
        self.variables = []


class Application(ProgramNode):
    def __init__(self, name, absolute_location, relative_location, size):
        self.super(NodeType.APPLICATION, name, size),
        self.absolute_location = (absolute_location,)
        self.relative_location = (relative_location,)
        self.files = []


class Module(ProgramNode):
    def __init__(self, name, absolute_location, relative_location, size):
        self.super(NodeType.MODULE, name, size)
        self.absolute_location = absolute_location
        self.relative_location = relative_location


class Class(ProgramNode):
    def __init__(self, name, size):
        self.super(NodeType.CLASS, name, size)
        self.methods = []
        self.instance_variables = []


class Method(ProgramNode):
    def __init__(self, name, size):
        self.super(NodeType.METHOD, name, size)
