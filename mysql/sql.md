#显示所有的数据库
show databases;
#使用数据库
use test;
#创建数据表
CREATE TABLE student IF NOT EXISTS(
	ID int PRIMARY KEY NOT NULL AUTO_INCREMENT,
	name varchar(30) NOT NULL,
	age varchar(10) DEFAULT '100' NOT NULL
)
