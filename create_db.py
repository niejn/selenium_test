from datetime import datetime
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String,
                        DateTime, ForeignKey, Boolean, create_engine, func, text)
from sqlalchemy.sql import insert

# CJ1	CJ1_CHG	CJ2	CJ2_CHG	CJ3	CJ3_CHG	INSTRUMENTID	PARTICIPANTABBR1	PARTICIPANTABBR2
# PARTICIPANTABBR3	PARTICIPANTID1	PARTICIPANTID2	PARTICIPANTID3	PRODUCTNAME	PRODUCTSORTNO	RANK
'''{'名次':'rank',	'期货公司会员简称':'participantabbr1',	'成交量':'',
     '比上交易日增减':'cj1_chg',	'名次':'',	'期货公司会员简称':'participantabbr2',
     '持买单量':'',	'比上交易日增减':'cj2_chg',	'名次':'',
     '期货公司会员简称':'participantabbr3',	'持卖单量':'cj3',
     '比上交易日增减/变化':'cj3_chg',
     }
     '''


class DataAccessLayer:
    connection = None
    engine = None
    conn_string = 'sqlite:///exchange.sqlite'
    metadata = MetaData()
    ranks = Table('ranks',
                  metadata,
                  Column('id', Integer(), primary_key=True, autoincrement=True),
                  Column('rank', Integer(), comment='名次'),
                  Column('CJ1', Integer(), comment='成交量'),
                  Column('CJ2', Integer(), comment='持买单量'),
                  Column('CJ3', Integer(), comment='持卖单量'),
                  Column('PARTICIPANTABBR3',  String(50), comment='期货公司会员简称3'),
                  Column('PARTICIPANTABBR2',  String(50), comment='期货公司会员简称2'),
                  Column('PARTICIPANTABBR1',  String(50), comment='期货公司会员简称1'),
                  Column('CJ3_CHG', Integer(), comment='比上交易日增减3'),
                  Column('CJ2_CHG', Integer(), comment='比上交易日增减2'),
                  Column('CJ1_CHG', Integer(), comment='比上交易日增减1'),
                  Column('instrumentid', String(50), comment='instrumentid'),
                  Column('productname', String(50), comment='productname'),
                  Column('productsortno', Integer(), comment='productsortno'),
                  Column('participantid1', Integer(), comment='participantid1'),
                  Column('participantid2', Integer(), comment='participantid2'),
                  Column('participantid3', Integer(), comment='participantid3'),
                  # Column('date', DateTime(timezone=True),server_default=datetime.now()),
                  Column('utc_date', DateTime(timezone=True), server_default=func.current_timestamp()),
                  # Column('date1', DateTime(timezone=False), server_default=text('CURRENT_TIMESTAMP')),
                  # func.current_timestamp()
                  Column('report_date', DateTime,),
                  # last_modified_date=Column(DateTime, default=datetime.datetime.now)
                  )



    def db_init(self, conn_string=None):
        # create_engine("...", connect_args={"options": "-c timezone=utc"})
        self.engine = create_engine(conn_string or self.conn_string)
        self.engine.execute('''
            drop table {name}'''.format(name='ranks'))
        ans = self.metadata.create_all(self.engine)
        print(ans)
        # self.connection = self.engine.connect()


dal = DataAccessLayer()
dal.db_init('sqlite:///exchange.sqlite')

'''
insert时候要初始化，负责没有反应
PMS_Opt_mtable = Table(tablename, meta,
                           Column('id', Integer, Sequence(seq_name), primary_key=True),
                           Column('last_modified_date', DateTime, default=datetime.datetime.now),
                           autoload=True)
                           '''