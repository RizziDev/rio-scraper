# utils/file_utils.py

import os

def save_text_to_file(text, file_path):
    """Salva um texto em um arquivo, criando os diretórios se necessário."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

def save_data_to_csv(data, file_path):
    """
    Salva uma lista de dicionários em um arquivo CSV.
    Exemplo simples; ajuste conforme a necessidade.
    """
    import csv
    if not data:
        return
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    keys = data[0].keys()
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
