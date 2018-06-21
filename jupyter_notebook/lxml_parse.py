with open("../dalian_res.txt", 'r') as da:
    text = da.read()
    print(text)
    from lxml import html
    from lxml import etree

    tree = html.fromstring(text)
    table = tree.xpath('//*[@id="printData"]/div/table[2]')[0]
    print(table)
    data = [
        [td.text_content().strip() for td in row.findall('td')]
        for row in table.findall('tr')
    ]
    print(data)
    print()
    # tree = etree.HTML(text, )
    # tables = tree.xpath('//div/table')
    # build_text_list = tables[1].xpath("//text()")
    # print(build_text_list)
    # for table in tables:
    #     data = [
    #         [td.xpath("text()") for td in row.xpath("//td")]
    #         for row in table.xpath("//tr")
    #     ]
    #     # print(data)
    # from bs4 import BeautifulSoup
    #
    # soup = BeautifulSoup(text, 'html.parser')
    #
    # print(soup.prettify())
    # print(soup.title)
    # soup.title.name
    # soup.title.string
    # soup.title.parent.name
    # soup.p
    # soup.p['class']
    # soup.a
    # soup.find_all('a')
    # soup.find(id="link3")

#     list = ['a', 'b', 'm', 'y', 'p', 'c', 'cs', 'jd', 'fb', 'bb', 'l', 'v', 'pp', 'j', 'jm', 'i']



