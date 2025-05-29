from ast import (
    AST,
    FunctionDef,
    NodeVisitor,
    parse,
    unparse,

)
from typing import (
    Any,
    Literal,
    List,
    Union,
    Optional
)


class VisitNodes(NodeVisitor):
    def __init__(self):
        self._all_nodes = []
        self._all_func_nodes = []
    
    def parse_all_nodes(self, code: str) -> AST:
        return parse(code)
    
    def visit(self, node: AST) -> AST:
        self._all_nodes.append(node)
        return super().visit(node) #* move to next node
    
    def visit_FunctionDef(self, node: FunctionDef) -> Any:
        self._all_func_nodes = [
            node for node in self._all_nodes if isinstance(node, FunctionDef)
        ]
    
    def get_all_nodes(self) -> List[AST]:
        return self._all_nodes
    
    def get_all_func_nodes(self) -> List[FunctionDef]:
        return self._all_func_nodes
    
RUNTIME_TYPE = Literal['local', 'global']

class EvalCode:
    def __init__(self, code: str, runtime: RUNTIME_TYPE = 'local'):
        tree = VisitNodes()
        self.code = code
        self.runtime = runtime
        tree.visit(tree.parse_all_nodes(self.code))
        self.__restricted_locals = locals()
        self.__restricted_globals = globals()
        self.all_nodes = tree.get_all_nodes()
        self.all_func_nodes = tree.get_all_func_nodes()
        #* create runtime
        self.create_runtime()


    def create_runtime(self):
        for node in self.all_nodes:
            code = compile(unparse(node), '<string>', 'exec')
            exec(code, self.__restricted_locals if self.runtime == 'local' else self.__restricted_globals)
        
    def get_restricted_locals(self):
        return self.__restricted_locals
    
    def get_restricted_globals(self):
        return self.__restricted_globals
    
    def run_func_code(self, 
                    args: Optional[List[Any]] = None,
                    func_name: Optional[str] = 'main',
                    ) -> Any:
        try:
            if self.runtime == 'local':
                return self.__restricted_locals[func_name]() if args is None else self.__restricted_locals[func_name](*args)
            
            return self.__restricted_globals[func_name]() if args is None else self.__restricted_globals[func_name](*args)
        except Exception as e:
            print(e)
            return None
    

    









