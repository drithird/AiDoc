import ast
import aidoc.python_parser as pp
import os


def main(file_path) -> None:
    line = 0
    print(os.getcwd())
    with open(file_path, "r") as file:
        for _ in file:
            line += 1
    app = pp.Application("Test_Parsing", __file__, os.path.relpath(__file__), line)
    source = ""
    with open(file_path, "r") as file:
        source = file.read()
    tree = ast.parse(source)
    for node in ast.walk(tree):
        match (type(node)):
            case ast.Module:
                module = pp.Module(
                    os.path.basename(__file__),
                    __file__,
                    os.path.relpath(__file__),
                    line,
                    app
                )
                #print(module)
            case ast.Import:

                break
            case _:
                print(node)
    print(app)


if __name__ == "__main__":
    main("src/aidoc/test_parsing.py")
