from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

#全量导出
def read_whole_tb(name_of_tables=None, con=None, out_path=".", current_date='20180605'):
    if (name_of_tables and con):
        for name_of_table in name_of_tables:
            # name_of_table = 'account_summary'
            the_frame = pd.read_sql_table(name_of_table, con=con)
            print(the_frame)
            the_frame.to_csv("{out_path}/{current_date}_{name}.csv".format(
                out_path=out_path,
                name=name_of_table,
                current_date=current_date,
            ), encoding='gbk')


    return



#通过指定日期范围获取表数据，指定日期格式为日期类型
def read_date_tb(name_of_tables=None, con=None, out_path=".",
                         date_schema='last_modified_date', beg_date='2018-06-04', end_date=None):
    engine = create_engine(con, echo=True)
    if (name_of_tables and con):

        for name_of_table in name_of_tables:

            if end_date:
                sql_cmd = "SELECT * FROM {db_table} WHERE " \
                          "{date_schema} >= to_date('{beg_date}', 'yyyy-mm-dd') " \
                          "and {date_schema} < to_date('{end_date}', 'yyyy-mm-dd')".format(
                    db_table=name_of_table, beg_date=beg_date, date_schema=date_schema, end_date=end_date
                )
            else:
                sql_cmd = "SELECT * FROM {db_table} WHERE " \
                          "{date_schema} >= to_date('{beg_date}', 'yyyy-mm-dd') " \
                          "and {date_schema} < (to_date('{beg_date}', 'yyyy-mm-dd') + 1)".format(
                    db_table=name_of_table, beg_date=beg_date, date_schema=date_schema
                )
            the_frame = pd.read_sql_query(
                                            sql=(sql_cmd),
                                            con=engine)
            the_frame.to_csv("{out_path}/{name}_last_modified_date.csv".format(out_path=out_path,name=name_of_table, ), encoding='gbk')
    return

#通过指定日期获取表数据，指定日期格式为Int类型
def read_int_date_tb(name_of_tables=None, con=None, out_path=".",
                         date_schema='last_modified_date', current_date='20180528'):
    engine = create_engine(con, echo=True)
    sql_cmd = 'SELECT max(HOLDING_DATE) FROM r_g_kn_account_summary'
    ans = pd.read_sql_query(sql=(sql_cmd), con=engine)
    print(ans)
    ans1 = ans.iat[0, 0]
    current_date = str(ans1)
    ans = pd.read_sql(sql=(sql_cmd), con=engine)
    ans1 = ans.iat[0, 0]
    print(ans)
    if (name_of_tables and con):
        for name_of_table in name_of_tables:

            sql_cmd = 'SELECT * FROM %s WHERE holding_date=%s' % (name_of_table, current_date)
            the_frame = pd.read_sql_query(
        sql=(sql_cmd),
        con=engine)
            the_frame.to_csv("{out_path}/{name}_latest.csv".format(out_path=out_path,name=name_of_table, ), encoding='gbk')
    return

def main():

    name_of_tables = ['r_g_kn_account_summary', 'r_g_kn_positions', 'r_g_kn_transaction_record',
                      'r_g_kn_positions_detail', 'r_g_kn_position_closed', ]
    oracle_con = "oracle://test2:test2@10.21.68.211:1521/hsfa?charset=utf8"
    oracle_con_production = 'oracle://sc:sc2017@10.21.69.198:1521/riskdb?charset=utf8'
    # read_whole_tb(name_of_tables,oracle_con_production,)
    read_int_date_tb(name_of_tables,oracle_con_production,)
    # read_date_tb(name_of_tables,oracle_con_production,)


    return

if __name__ == '__main__':
    main()