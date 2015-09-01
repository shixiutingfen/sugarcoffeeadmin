--用户表
create table c_user 
(
	userid int(19) not null primary key,
	username varchar(20) not null,
	password varchar(40) not null,
	chinesename varchar(20) ,
	email  varchar(25) ,
	address varchar(50) ,
	phone BIGINT(15) ,
	mobile BIGINT(13),
	sex  int(1),
	age  int(3),
	qq BIGINT(12),
	logintimes int(5),
	userlevel int(2)  ,
	usertype int(2) comment '用户类型 0客户 1员工 2员工家属 ',
	lastlogintime varchar(20),
	createtime varchar(20) not null
);
--类目表 belongto 
create table c_catagory 
(
	catagoryid int(5)  not null primary key,
	catagoryname varchar(20) not null,
	belongto  int(2) not null comment '1文章分类2图片3FAQ分类4投票分类',
	parentid int(5) comment '上级类目id',
	createuser int(19),
	createtime varchar(20) not null 
);
--文章表  
create table c_article 
(
	articleid int(15)  not null primary key,
	catagoryid int(5),
	title varchar(50),
	content text,
	istop int(1) default 0 comment '0不置顶 1置顶',
	ishot int(1) default 0 comment '0非热门 1热门',
	createtype int(1) comment '0客户文章 1系统文章',
	createuser int(19) ,
	createtime varchar(20) not null 
);

--附件表
create table c_attach 
(
	attachid int(19)  not null primary key,
	catagoryid int(5) comment '关联分类id',
	tite varchar(50) comment '附件标题',
	content text comment '附件描述',
	realpath varchar(50),
	attachpath varchar(50),
	realname varchar(50),
	attachname varchar(50),
	createuser int(19) ,
	createtime varchar(20) 
);

--帮助提示表
create table c_faq 
(
	faqid int(19)  not null primary key,
	catagoryid int(5) comment '关联分类id',
	title varchar(100),
	content text,
	readtimes int(8),
	createuser int(19) ,
	createtime varchar(20)
);

--好友表
create table c_friend
(
	friendid  int(19)  not null primary key,
	friendusername varchar(20)  ,
	userid  int(19)  ,
	status int(1),
	level int(1),
	createuser int(19),
	createtime varchar(20)
);