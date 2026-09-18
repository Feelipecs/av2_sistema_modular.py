
# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno: 
# Data: 
# Link do Repositório: 
# ==============================================================================

# Lista inicial de dados brutos (Exemplo: Sistema de RH / Atendimento)
# Os dados estão no formato: "nome_completo;cargo_ou_setor;telefone_ou_cpf"
dados_brutos = [
   "  felipe;desenvolvedor,11824395321  ",
   "  ana paula mendes;desenvolvedor;479666621977  ",
   "  roberto carlos oliveira;desenvolvedor;31665552468  "
]


def limpar_e_formatar_texto(texto):
    texto = texto.strip()
    texto = texto.upper()
    return texto


def extrair_codigo_ou_ddd(dado):
    dado = dado.strip()
    ddd = dado[0:2]
    return ddd


def processar_e_exibir_cadastros(lista_dados):
    total_processado = 0

    for dado in lista_dados:
        partes = dado.split(";")

        nome = limpar_e_formatar_texto(partes[0])
        cargo = limpar_e_formatar_texto(partes[1])
        telefone = partes[2]

        ddd = extrair_codigo_ou_ddd(telefone)

        print(f"Nome: {nome} | Cargo: {cargo} | DDD: {ddd}")

        total_processado += 1

    return total_processado
def main():
    print("==================================================")
    print("     SISTEMA DE GESTÃO MODULARIZADO - AV2        ")
    print("==================================================\n")

    print("Iniciando o processamento dos dados...\n")
    total_processado = processar_e_exibir_cadastros(dados_brutos)

    # Exibe a quantidade total de registros processados.
    print(f"\nTotal de registros processados: {total_processado}")

    print("\n==================================================")
    print("             PROCESSAMENTO CONCLUÍDO              ")
    print("==================================================")
if __name__ == "__main__":
    main()
