#当前GUI表格中的项目个数
stuNum = 0
#新建档案，利用全局变量传递
newStu = None
#检测新建档案的ID的合法性
status = 0
#查询条件，用全局变量传方便点
condition = None
#修改条件，用全局变量传方便点
editStu = None
#修改时的标志位，记录是否有进行修改
hasEdited = 0
#查询时的标志位，记录是否有查询操作
hasQuery = 0
#登录验证位，0登录失败，1普通用户，2管理员, 待删
verify = 0
#登录ok按钮，如果尝试登录，则退出循环
okPush = 0
#数据库位置，由打开数据库操作指定
dbPath = None
#用户名
uname = None
#权限 0管理 1学生
authority = 0
#升降序
ascend = 0
#和上次升降序 是否一致
col_index = 0
#本地数据库还是阿里云, 0 for local, 1 for aliyun
web = 0
