import ast


def main() -> None:
    source = """def greet(name):
        pass 
    """
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            print(node.name)


if __name__ == "__main__":
    main()
