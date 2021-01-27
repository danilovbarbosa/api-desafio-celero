import psycopg2 as db
from bd.util import carregar_csv

class Config:
    def __init__(self):
        self.config = {
            "postgres":{
                "user": "postgres",
                "password": "12345",
                "host": "localhost",
                "database": "api_desafio_celero"
            }
        }

class Connection(Config):
    def __init__(self):
        Config.__init__(self)
        try:
            self.conn = db.connect(**self.config['postgres'])
            self.cur = self.conn.cursor()
        except Exception as e:
            print(f'Erro na conexão. {e}')
            exit(1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self.conn


    @property
    def cursor(self):
        return self.cur


    def commit(self):
        self.connection.commit()


    def fetchall(self):
        return self.cur.fetchall()


    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())


    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()


class NocRegions(Connection):
    def __init__(self):
        Connection.__init__(self)


    def insert(self, *args):
        try:
            sql = 'INSERT INTO historia_olimpica_nocregions (noc, region, notes) VALUES (%s, %s, %s) RETURNING id;'
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print(f'Erro ao inserir: {e}')

    def select(self, *args):
        pass

class AthleteEvents(Connection):
    def __init__(self):
        Connection.__init__(self)


    def insert(self, *args):
        try:
            sql = '''
            INSERT INTO 
            historia_olimpica_athleteevents (name, sex, age, height, weight, team, noc_id, games, year, season, 
            city, sport, event, medal) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
            RETURNING id;
            '''
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print(f'Erro ao inserir: {e}')

### Scripts para a execução da inserção dos itens no BD

def inserir_dados_na_tabela_noc_regions(df):
    noc_regions = NocRegions()

    for i in df[:][1:]:
        noc = i[0]
        region = i[1]
        notes = i[2]

        noc_regions.insert(noc, region, notes)


def selecionar_id_na_tabela_noc_regions(noc: str):
    noc_regions = NocRegions()
    query_set = noc_regions.query(f"SELECT id FROM historia_olimpica_nocregions WHERE noc LIKE '{noc}'")
    return query_set[0][0]


def inserir_dados_na_tabela_athlete_events(df):
    athlete_events = AthleteEvents()

    for index, i in enumerate(df[:100][1:]):
        name = i[1]
        sex = i[2]
        age = i[3]
        height = i[4]
        weight = i[5]
        team = i[6]
        noc = selecionar_id_na_tabela_noc_regions(i[7])
        games = i[8]
        year = i[9]
        season = i[10]
        city = i[11]
        sport = i[12]
        event = i[13]
        medal = i[14]

        try:
            print(name, sex, age, height, weight, team, noc, games, year, season,
            city, sport, event, medal)
            # athlete_events.insert(name, sex, age, height, weight, team, noc, games, year, season,
            # city, sport, event, medal)
        except Exception as e:
            print(f'Erro ao inserir item {index}, veja: {e}')

#
# if __name__ == '__main__':
#     # df_noc_regions = carregar_csv('noc_regions.csv')
#     # inserir_dados_na_tabela_noc_regions(df_noc_regions)
#
#     df_athlete_events = carregar_csv('athlete_events.csv')
#     inserir_dados_na_tabela_athlete_events(df_athlete_events)

