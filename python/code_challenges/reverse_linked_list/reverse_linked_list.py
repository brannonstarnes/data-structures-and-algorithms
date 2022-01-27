def reverse_list(ll):
    """Reverses a linked list
    Args:
        ll: linked list
    Returns:
        linked list in reversed form
    """
    # put your function implementation here

    def reverse_linked_list(linked_list):
        previous = None
        while linked_list.head:
            temp = linked_list.head
            temp.next = temp
            previous = temp

            return linked_list
