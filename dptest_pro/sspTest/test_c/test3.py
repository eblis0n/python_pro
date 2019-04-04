# 营业收入
def test_allIncome(self):
    print("开始测试test_allIncome")
    # self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
    print("接口返回结果:" + str(self.res_date))
    inf_allIncome = self.res_date['data'].get("allIncome")

    # 执行SQL查询
    sql = "SELECT SUM(amount) as allamount FROM ssp_play_summary WHERE ssp_id = {0} AND transaction_date BETWEEN '{1}' and '{2}';".format( media_provider_id, startDate, endDate)
    print("数据库查询使用语句：" + sql)
    self.pymysqlcursor.execute(sql)
    allamount = self.pymysqlcursor.fetchall()
    slq_allamount = allamount[0].get("allamount")

    # 判断 接口数据与数据库查询结果
    print('接口返回结果：{0} , 数据库查询结果：{1}'.format(str(inf_allIncome), str(slq_allamount)))
    self.assertEquals(str(inf_allIncome), str(slq_allamount), "test_allIncome数据对不上")