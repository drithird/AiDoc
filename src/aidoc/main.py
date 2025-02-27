import ast
import aidoc.python_parser as pp
import os


def main(file_path) -> None:
    line = 0
    print(os.getcwd())
    with open(file_path, "r") as file:
        for _ in file:
            line += 1
    source = ""
    with open(file_path, "r") as file:
        source = file.read()
    app = pp.Application("Python Parser", os.path.abspath(__file__), __file__, line)
    tree = ast.parse(source)
    with open(file_path, "r") as file:
        parsed_ast = ast.parse(file.read())
        with open("dump.json", "w") as json_file:
            json_file.write(ast.dump(parsed_ast, indent=4))


#    for node in ast.walk(tree):
#        match (type(node)):
#            case ast.Module:
#                node: ast.Module = node
#                print()


if __name__ == "__main__":
    main("src/aidoc/test_parsing.py")
