class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self):

        # root > left > right
        result = []
        if self.root is None:
            raise ValueError("No Root! Empty Tree.")

        def walk(root):

            if root is None:
                return result

            result.append(root.value)

            walk(root.left)
            walk(root.right)
            return result

        walk(self.root)
        return result

    def in_order(self):
        result = []
        if self.root is None:
            raise ValueError("No Root! Empty Tree.")

        def walk(root):

            if root is None:
                return result

            walk(root.left)
            result.append(root.value)
            walk(root.right)
            return result

        walk(self.root)
        return result


    def post_order(self):
        result = []
        if self.root is None:
            raise ValueError("No Root! Empty Tree.")

        def walk(root):

            if root is None:
                return result

            walk(root.left)
            walk(root.right)
            result.append(root.value)
            return result

        walk(self.root)
        return result
