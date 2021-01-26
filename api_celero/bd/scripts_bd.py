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

if __name__ == '__main__':
    df_noc_regions = carregar_csv('noc_regions.csv')
    noc_regions = NocRegions()

    for i in df_noc_regions[:][2:].itertuples():
        noc = i[1]
        region = i[2]
        notes = i[3]

        noc_regions.insert(noc, region, notes)

    df_athlete_events = carregar_csv('athlete_events.csv')


