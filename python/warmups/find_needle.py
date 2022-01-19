def find_needle(tree, needle):

   if tree.root is None:
        raise ValueError("No Root! Empty Tree.")

   def walk(root, total):
        # nonlocal result

        if root is None:
            return total

        if root == needle:
            total += 1

        total = walk(root.left, total)

        total = walk(root.right, total)

        return total

   return walk(tree.root, 0)



