from urllib.parse import quote_plus
import cred
import sqlalchemy  as sa
from sqlmodel import  create_engine, Session

class DbSession:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            # print('inside the Db Calls2')
            cls._instance = super(DbSession, cls).__new__(cls)
            connection_url = sa.URL.create(
                "postgresql",
                username=cred.db_user,
                password=cred.db_password,
                host=cred.db_host,
                database=cred.database,
                port=cred.db_port
            )
            cls._instance.engine = create_engine(connection_url,
                pool_size=cred.db_conn_pool, max_overflow=cred.db_conn_pool_max, echo=cred.echo
            )

            # print("Connection successful!")

        cls._instance.session = Session(cls._instance.engine)
        return cls._instance

    def get_db(self):
        return self.session

    def close_session(self):
        self.session.expunge_all()
        self.session.close()



