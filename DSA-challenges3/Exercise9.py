def is_valid_bst(root):

    def validate(node, minimum, maximum):
        if node is None:
            return True

        if not minimum < node.val < maximum:
            return False

        return (
            validate(node.left, minimum, node.val)
            and
            validate(node.right, node.val, maximum)
        )

    return validate(root, float("-inf"), float("inf"))