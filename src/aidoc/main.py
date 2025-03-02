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
    current_node = ast.walk(tree)[0]
    parent_stack = []
    processed_nodes = []
    parent_stack.append((current_node,processed_nodes))

    while(parent_stack):
        current_stack = parent_stack.pop()
        parent_node, processed_nodes = current_stack[0], current_stack[1] 
        for node in parent_node.body:
            if node in processed_nodes:
                continue
            match (type(node)):
                case ast.Module:
                    current_stack[1].append(node)
                    parent_stack.append(current_stack)
                    current_stack = (node,processed_nodes)
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
