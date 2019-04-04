def test_playTimeLen(self):
    print("开始测试test_playTimeLen")
    # 执行接口查询
    # self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
    print("接口返回结果:" + str(self.res_date))
    inf_playTimeLen = self.res_date['data']
    # 执行SQL查询
    sql = "SELECT COUNT(DISTINCT dsp_id) AS play_time_len  FROM dsp_play_summary WHERE transaction_date BETWEEN '{0}' and '{1}';".format(
        startDate, endDate)
    print("数据库查询使用语句：" + sql)
    self.pymysqlcursor.execute(sql)
    play_time_len = self.pymysqlcursor.fetchall()
    sql_play_time_len = play_time_len[0].get("play_time_len")
    # 判断 接口数据与数据库查询结果
    print('接口返回结果：{0} , 数据库查询结果：{1}'.format(len(inf_playTimeLen), len(sql_play_time_len)))
    self.assertEquals(str(len(inf_playTimeLen)), str(len(sql_play_time_len)), "test_playTimeLen数据对不上")

