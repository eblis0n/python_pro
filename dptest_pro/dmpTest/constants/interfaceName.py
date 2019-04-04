###########################################第4章 入口模块接口协议###################################

# 4.1.1 终端请求订单新接口
entryAdrequest='/entry/adrequest'
# 4.4.1 终端初始化新接口
entryInitrequest='/entry/initrequest'

###########################################第5章 排队模块接口协议###################################

# 5.1.1 订单请求新接口
dispatcherAdrequest='/dispatcher/adrequest'
# 5.9异步接收增量策略结果回调
dispatcherStrategyPush='/dispatcher/strategy/push'

###########################################第6章匹配模块接口协议###################################

# 6.1.1 订单请求新接口
matchingAdrequest='/matching/adrequest'


###########################################第7章 屏画像模块接口协议###################################

# 7.5终端初始化请求 (入口模块转发)
screenfeatureInitrequest='/screenfeature/initrequest'
# 7.6广告请求新接口 (排队模块发起)
screenfeatureAdrequest='/screenfeature/adrequest'
# 7.5终端初始化请求 (入口模块转发)
screenfeatureInitrequest='/screenfeature/initrequest'
# 7.6广告请求新接口 (排队模块发起)
screenfeatureAdrequest='/screenfeature/adrequest'
# 7.7请求屏的价格 (计费模块发起)
screenfeaturePrices='/screenfeature/prices'
# 7.8.1 导入屏数据到讯飞的屏表
iflyImportscreen='/screenfeature/ifly/importscreen'
# 7.8.2同步讯飞的媒体位/广告位(至讯飞)
iflyMedia='/screenfeature/ifly/media'
# 7.8.3同步讯飞的广告位(至讯飞)
iflyAdunit='/screenfeature/ifly/adunit'
# 7.8.4 关联讯飞的媒体位与广告位(至讯飞)
screenfeatureIflyRelationMediaadunit='/screenfeature/ifly/relation/mediaadunit'
# 7.8.3同步讯飞至平台
iflyUpdateScreen='/screenfeature/ifly/updateScreen'
# 7.10屏参数更新
screenUpdate='/screenfeature/screen/update'

###########################################第8章选单模块接口协议###################################

###########################################第9章账户计费模块接口协议###################################

###########################################第10章持久模块接口协议###################################

# 10.1订单请求 (匹配模块转发)
persistenceReq='/persistence/req'
# 10.2播放完成 (排队模块或入口模块转发)
persistencePlaydone='/persistence/playdone'
# 10.3终端状态/告警上报 (排队转发)
persistenceStatusreport='/persistence/statusreport'

##########################################第11章广告管理模块接口协议###################################

# 11.1创建广告
admanageAdCreate='/admanage/ad/create'
# 11.1创建广告
admanageAdCreate='/admanage/ad/create'
# 11.2素材查询
admanageMaterialQuery='/admanage/material/query'
# 11.6广告状态更新
admanageAdStatusUpdate='/admanage/ad/status/update'
# 11.17.1添加监控链
admanageAdMonitorUpdate='/admanage/ad/monitor/update'
# 11.18.1.2查询素材
admanageMaterialV2QueryMaterial='/admanage/material/v2/query/material'
# 11.18.1.1查询广告
admanageMaterialV2QueryPlan='/admanage/material/v2/query/plan'
# 11.18.1.3查询终端
admanageMaterialV2QueryScreen='/admanage/material/v2/query/screen'
# 11.18.1.4一键审核
admanageMaterialV2ReviewPlan='/admanage/material/v2/review/plan'
# 11.18.1.1	查询广告
admanageMaterialV2QueryPlan='/admanage/material/v2/query/plan'

###########################################第12章财务模块接口协议###################################

# 12.16.7仪表盘数据汇总查询
financeDmpV2AnalysisTotalsummary='/finance/dmp/v2/analysis/totalsummary'
# 12.14.2播放统计分析查询
financeAnalysisPlayList='/finance/analysis/play/list'
# 12.16.4广告商数据明细查询
financeAnalysisDspList='/finance/dmp/v2/analysis/dsp/list'

###########################################第13章素材文件模块接口协议###################################

# 13.3从文件服务删除素材
materialDelete='/material/delete'
# 13.4获取点屏素材路径
materialSspGeturl='/material/ssp/geturl'

###########################################第14章登录认证模块接口协议###################################

# 14.1登录
authLogin='/auth/login'

###########################################第15章 广告入口模块接口协议###################################

# 15.1新建广告计划 (众盟发起)
planCreate='/plan/create.json'
# 15.3素材查询 (前端发起)
sspMaterialQuery='/ssp/material/query'
# 15.3素材查询 (前端发起)(旧接口)
planMaterialGet='/plan/material/get'
# 15.4素材审核 (前端发起)
sspMaterialReview='/ssp/material/review'
# 15.4素材审核 (前端发起)（旧接口）
planMaterialReview='/plan/material/review'
# 15.5获取素材地址 (前端发起)
sspMaterialGeturl='/ssp/material/geturl'
# 15.6创建广告计划(讯飞)
iflyNew='/plan/ifly/new'
# 15.6创建广告计划(点屏)
adCreate='/plan/ad/create'
# 15.8登录(转发至认证模块)
authLogin='/auth/login'
# 15.15.1新建二级账户
sspUsermanageSubaccountRegister='/ssp/usermanage/subaccount/register'
# 15.15.5更新二级账户
sspUsermanageSubaccountUpdate='/ssp/usermanage/subaccount/update'
# 16.4用户添加
usermanageUserInsert='/usermanage/user/insert'
# 15.15.3删除二级账户
sspUsermanageSubaccountDelete='/ssp/usermanage/subaccount/delete'
# 15.15.2查询二级账户
sspUsermanageSubaccountQuery='/ssp/usermanage/subaccount/query'
# 15.19.1DMP登录
dmpAuthLogin='dmp/auth/login'
# 15.19.2 DMP用户列表
dmpUserQuery='/dmp/user/query'
# 15.19.3 DMP重置密码
dmpUserResetpassword='dmp/user/resetpassword'
# 15.19.4 DMP修改密码
dmpUserChangepassword='dmp/user/changepassword'
# 15.19.5 DMP修改用户信息
dmpUserUpdate='dmp/user/update'
# 15.19.6 DMP添加用户
dmpUserInsert='dmp/user/insert'
# 15.19.7 DMP媒体商列表
dmpScreenSspDeviceQuerymediaprovider='dmp/screen/ssp/device/querymediaprovider'
# 15.19.8 DMP终端列表
dmpScreenSspDeviceQuery='dmp/screen/ssp/device/query'
# 15.19.9 DMP终端详情
dmpScreenSspDeviceQueryone='dmp/screen/ssp/device/queryone'
# 15.20.1 探针原始数据推送
probeZhimaOriginalCreate='/probe/zhima/original/create'
# 15.20.2 探针角色数据推送
probeZhimaRoleCreate='/probe/zhima/role/create'
# 15.22 增加探针和广告位的绑定
probeScreenCreate='/probe/screen/create'
# 15.23 一键审核 (前端发起)
sspV2ReviewPlan='/ssp/v2/review/plan'

# 15.23 一键审核 (前端发起)
dmpAnalysisDspList='/dmp/v2/analysis/dsp/list'

###########################################第16章 用户管理模块接口协议###################################

# 16.1账户注册
usermanageAccountRegister='/usermanage/account/register'
# 16.2账户查询
usermanageAccountQuery='/usermanage/account/query'
# 16.3账户更新
usermanageAccountUpdate='/usermanage/account/update'
# 16.5用户更新
usermanageUserUpdate='/usermanage/user/update'
# 16.9登录验证
usermanageuserVerify='/usermanage/user/verify'



###########################################第17章消息通告模块接口协议###################################

###########################################第18章 查询入口模块接口协议###################################

# 18.1.1查询二级账户统计概要列表
queryentrySubsspSummarylist='/queryentry/subssp/summarylist'
# 18.4请求初始化配置
sysparamDeviceInitparams='/sysparam/device/initparams'
# 18.8.1播放统计分析查询
sspFinanceAnalysisPlaySummary='/ssp/finance/analysis/play/summary'
# 18.8.1播放统计分析查询
sspFinanceAnalysisPlayList='/ssp/finance/analysis/play/list'
# 18.20修改初始化返回参数
sysparamDeviceUpd='/sysparam/device/upd'
# 18.1媒体商的统计数据概览
queryentrySspSummary='/queryentry/ssp/summary'
# 18.2媒体商的每日统计数据
queryentrySspStatisdaily = '/queryentry/ssp/statisdaily'

###########################################第19章广告代理模块接口协议###################################

# 19.1请求广告商的广告 (屏模块发起)
adagentAdrequest='/adagent/adrequest'

###########################################第20章屏管理模块接口协议###################################

# 20.1查询媒体位
screenmanageSspDeviceQuery='/screenmanage/ssp/device/query'
# 20.2增加媒体位
screenmanageSspDeviceAdd='/screenmanage/ssp/device/add'
# 20.3删除媒体位
screenmanageSspDeviceDelete='/screenmanage/ssp/device/delete'
# 20.4修改媒体位
screenmanageSspDeviceUpdate='/screenmanage/ssp/device/update'
# 20.4.1媒体位状态修改
screenmanageSspDeviceStatusUpdate='/screenmanage/ssp/device/status/update'
# 20.20设置轮询请求广告主
screenmanageSetrollpoll='/screenmanage/setrollpoll'
# 20.21查询轮询请求广告主设置
screenmanageSelectrollpoll='/screenmanage/selectrollpoll'

###########################################第21章播放监控模块接口协议###################################


###########################################其他###################################

# 增加外部策略
dispatcherStrategyAdd='/dispatcher/strategy/add'
# 查看外部策略
dispatcherStrategyList='/dispatcher/strategy/list'
# 将历史数据生成报表数据
accountProcessDataDmp='/account/process/data/dmp'
# 手动平账结算
accountBalanceAccount ='/account/balanceAccount '