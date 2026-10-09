# Semana 05: leitura de CSV, regex e tratamento de exceções.

"""Semana 05 - Análise de CSV com regex e tratamento de exceções."""

import csv
import re
from pathlib import Path


                                                                                  
class FormatoInvalidoError(Exception):
    """Indica que um registro não atende às regras de negócio."""


                                                                      
PADROES = {
    "email": re.compile(r"^[\w.+-]+@[\w-]+(?:\.[\w-]+)+$"),
    "cpf": re.compile(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"),
    "telefone": re.compile(r"^\(\d{2}\) \d{4,5}-\d{4}$"),
    "data_nascimento": re.compile(r"^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$"),
}


                                                                            
def validar_campo(campo, valor):
    if not PADROES[campo].fullmatch(valor):
        raise FormatoInvalidoError(f"{campo} com formato inválido: {valor}")


                                                                        
def analisar_arquivo(caminho):
    validos, invalidos = [], []
    try:
                                                                                    
        with open(caminho, "r", encoding="utf-8", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)
            campos_obrigatorios = set(PADROES) | {"nome"}
            if not leitor.fieldnames or not campos_obrigatorios.issubset(leitor.fieldnames):
                raise KeyError("Uma ou mais colunas obrigatórias não existem no CSV")
            for numero, registro in enumerate(leitor, start=2):
                try:
                    for campo in PADROES:
                        validar_campo(campo, registro[campo].strip())
                    validos.append(registro)
                except (FormatoInvalidoError, ValueError, KeyError) as erro:
                    invalidos.append({"linha": numero, "motivo": str(erro), "registro": registro})
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")
    except (KeyError, csv.Error) as erro:
        print(f"Erro estrutural no arquivo: {erro}")
    else:
        print("Leitura concluída com sucesso.")
    finally:
        print("Arquivo encerrado com segurança.")
    return validos, invalidos


                                                                            
def main():
    caminho = Path(__file__).with_name("dados.csv")
    validos, invalidos = analisar_arquivo(caminho)
    total = len(validos) + len(invalidos)
    print("\n=== RELATÓRIO DA ANÁLISE ===")
    print(f"Total de registros: {total}")
    print(f"Registros válidos: {len(validos)}")
    print(f"Registros inválidos: {len(invalidos)}")
    for registro in validos:
        print(f"[OK] {registro['nome']} — {registro['email']}")
    for erro in invalidos:
        print(f"[ERRO] Linha {erro['linha']}: {erro['motivo']}")


if __name__ == "__main__":
    main()
