from sqlalchemy import create_engine


def create_rds_engine(master_username, master_password, endpoint, db_name):
    engine = create_engine(
        f"mysql+pymysql://{master_username}:{master_password}@{endpoint}/{db_name}"
    )
    return engine
