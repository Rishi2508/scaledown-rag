import os
def load_python_files(folder_path):
    documents = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)

                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    documents.append({
                        "path": full_path,
                        "content": content
                    })

                except Exception as e:
                    print(f"Error reading {full_path}: {e}")

    return documents
