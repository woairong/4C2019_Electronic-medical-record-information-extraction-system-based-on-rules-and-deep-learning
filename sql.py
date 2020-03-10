# coding: utf8

DB_NAME = "reportData.db"

CREATE_USERS_TABLE_SQL = """
	create table if not exists users(
		'username' text not null,
		'password' text not null,
		'ownTable' text not null
	);
	"""
INSERT_USER_SQL = "insert into users values('{0}', '{1}', '{2}')"
#SEARCH_ROOT_SQL = "select username from users where username='root';"
SEARCH_ROOT_PWORD_SQL = "select password from users where username='root' limit 1;"
SEARCH_ALL_TABLES_SQL = "select ownTable from users;"
SEARCH_USER_TABLE_SQL = "select ownTable from users where username='%s' and password=md5('%s')"
UPDATE_USER_PASSWORD_SQL = "update users set password=md5('%s') where username='%s'"
DELETE_TABLE_RECORD_SQL = "delete from users where ownTable='%s'"

'''
DEFAULT_TABLE_NAME = "securityInspect"

CREATE_DEFAULT_TABLE_SQL = """
	create table if not exists securityInspect(
		'单位性质' text,
		'网站名称' text,
		'域名' text unique,
		'IP地址' text,
		'是否接入创宇盾' text,
		'服务器所在地' text,
		'源代码安全扫描' text,
		'未绕过web漏洞扫描' text,
		'白名单web漏洞扫描' text,
		'禁止IP访问' text,
		'是否有旁站' text,
		'IP白名单添加' text,
		'单位名称' text,
		'联系人' text,
		'联系方式' text,
		'运营商' text,
		'网站管理单位' text,
		'管理人员' text,
		'管理人联系方式' text,
		'维护单位' text,
		primary key('域名')
	)
	"""
'''

CREATE_TABLE_SQL = "create table if not exists %s( '%s' );"

DROP_TABLE_SQL = "drop table %s;"

ADD_COLUMN_SQL = "alter table %s add column '%s' text;"

# sqlite doesn't support syntax: "alter table .. drop ...", replace with:
DELETE_COLUMN_SQL = """
	alter table %s rename to tempTableXXX;
	create table %s as select %s from tempTableXXX;
	drop table tempTableXXX;
	"""

INSERT_DATA_SQL = "insert into {0}({1}) values('%s');"

DELETE_DATA_SQL = "delete from %s"

UPDATE_DATA_SQL = "update %s set %s"

SELECT_ALL_DATA_SQL = "select * from %s"

OUTPUT_DATA_SQL = ".output {tables}.csv"
