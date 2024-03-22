class TreeNode: # clase que tiene comoa tributos valor, izquierda y derecha
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_path(root, target): #funcion para encontrar el target, a partit del root
    if not root: #si no es root
        return [] #devuleve lista vacía
    
    def backtrack(node, target, path): #funcion de backtrack
        if not node: 
            return []
        
        path.append(node.val) #añadimos a path el valor
        
        if node.val == target: #si el valor es el target
            return path #regresamos el camino
        
        left_path = backtrack(node.left, target, path.copy()) #recorremos por la izquierda
        right_path = backtrack(node.right, target, path.copy()) #recorremos por la derecha

        if left_path:
            return left_path
        elif right_path:
            return right_path
        else:
            return []
    
    return backtrack(root, target, [])

# Construcción de árbol
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

target_value = 5
path = find_path(root, target_value)
if path:
    print(f"Camino hacia el valor {target_value}: {path}")
else:
    print(f"No se encontró el valor {target_value} en el árbol.")
