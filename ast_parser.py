from tree_sitter import Parser
from tree_sitter_languages import get_language

PY_LANGUAGE = get_language("python")

parser = Parser()
parser.set_language(PY_LANGUAGE)


def get_node_text(node, source_bytes):
    return source_bytes[node.start_byte:node.end_byte].decode("utf8")


def parse_code(file_content):
    """
    Parse Python file into structured AST chunks.
    Returns list of dicts with metadata.
    """

    source_bytes = bytes(file_content, "utf8")
    tree = parser.parse(source_bytes)
    root_node = tree.root_node

    chunks = []

    def traverse(node):
        # Function
        if node.type == "function_definition":
            name_node = node.child_by_field_name("name")
            func_name = get_node_text(name_node, source_bytes)

            chunks.append({
                "type": "function",
                "name": func_name,
                "content": get_node_text(node, source_bytes),
                "start_line": node.start_point[0] + 1,
                "end_line": node.end_point[0] + 1
            })

        # Class
        if node.type == "class_definition":
            name_node = node.child_by_field_name("name")
            class_name = get_node_text(name_node, source_bytes)

            chunks.append({
                "type": "class",
                "name": class_name,
                "content": get_node_text(node, source_bytes),
                "start_line": node.start_point[0] + 1,
                "end_line": node.end_point[0] + 1
            })

        for child in node.children:
            traverse(child)

    traverse(root_node)

    return chunks
