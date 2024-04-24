import re
import ast
import astor
import pyperclip

class MutateCode(ast.NodeTransformer):
    def visit_ImportFrom(self, node):
        return None
    def visit_Call(self, node):
        match node.func.id:
            case "rprint":
                return ast.Return(value=node.args[0])
            case "print" | "inputLoop":
                return ast.Expr(value=None)
        return node

def removeDefAndTab(source):
    raw = re.sub(r"^[ ]{4}", "", source, flags=re.MULTILINE)
    _, content = raw.split('\n', 1)
    return content

def copyCode(source):
    pyperclip.copy(source)

with open("test.py") as file:
    content = file.read()
    tree = ast.parse( content )
    modified = MutateCode().visit(tree)

    source = astor.to_source(modified)
    source = removeDefAndTab( source )

    copyCode( source )
