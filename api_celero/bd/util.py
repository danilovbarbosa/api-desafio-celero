import pandas as pd
import sys


def carregar_csv(path: str):
    path_absoluto = sys.path[0] + '/' + path
    print(path_absoluto)
    df = pd.read_csv(path_absoluto, header=None)
    return df

# if __name__ == '__main__':
#     df_noc_regions = carregar_csv('noc_regions.csv')
#     df_athlete_events = carregar_csv('athlete_events.csv')
#
#     print(df_noc_regions[2])