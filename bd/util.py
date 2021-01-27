import sys
import csv


def carregar_csv(path: str):
    '''
    Função para ler um arquivo csv e devolver um matriz
    :param path: nome do arquivo csv
    :return: matriz/lista com os itens do arquivo csv
    '''
    path_absoluto = sys.path[0] + '/' + path
    df = []
    with open(path_absoluto, 'rt', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            df.append(linha)
    return df

# if __name__ == '__main__':
#     df_noc_regions = carregar_csv('noc_regions.csv')
#     # df_athlete_events = carregar_csv('athlete_events.csv')
#     print(df_noc_regions)