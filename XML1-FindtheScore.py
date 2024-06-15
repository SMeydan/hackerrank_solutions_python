
def get_attr_number(node):
    count = len(node.attrib)
    for child in node:
        count += get_attr_number(child)
    
    return count
