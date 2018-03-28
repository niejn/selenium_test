
# INSTRUMENTID PRODUCTNAME PRODUCTSORTNO PARTICIPANTID1	PARTICIPANTID2	PARTICIPANTID3

def main():
    temp = {'名次':'rank',	'期货公司会员简称':'participantabbr1',	'成交量':'',
     '比上交易日增减':'cj1_chg',	'期货公司会员简称':'participantabbr2',
     '持买单量':'',	'比上交易日增减':'cj2_chg',
     '期货公司会员简称':'participantabbr3',	'持卖单量':'cj3',
     '比上交易日增减/变化':'cj3_chg',
     }

    temp = {'期货公司会员简称1':'PARTICIPANTABBR1',	'成交量':'CJ1',
            '比上交易日增减1':'CJ1_CHG',	'名次':'rank',
            '期货公司会员简称2':'PARTICIPANTABBR2',	'持买单量':'CJ2',
            '比上交易日增减2':'CJ2_CHG',
            '期货公司会员简称3':'PARTICIPANTABBR3',
            '持卖单量':'CJ3',	'比上交易日增减3':'CJ3_CHG',
}
    # for key, val in temp.items():
    #     # print(key)
    #     str = "Column('{key}', Integer(), comment='{comment}'),".format(key = val, comment=key)
    #     print(str)

    str = 'INSTRUMENTID PRODUCTNAME PRODUCTSORTNO PARTICIPANTID1	PARTICIPANTID2	PARTICIPANTID3'
    str = 'PARTICIPANTID1	PARTICIPANTID2	PARTICIPANTID3'
    headers = str.split()
    print(headers)
    for key in headers:
        key = key.lower()
        str = "Column('{key}', Integer(), comment='{comment}'),".format(key=key, comment=key)
        print(str)
    return

if __name__ == '__main__':
    main()