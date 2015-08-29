--键表
create table t_cataname
(
	id varchar(5) not null,
	cataname varchar(8) not null,
	chiname varchar(30)
);
COMMENT on TABLE t_cataname is '键表';
COMMENT on COLUMN t_cataname.cataname is '主键id';
COMMENT on COLUMN t_cataname.chiname is '主键中文名称';

CREATE SEQUENCE cataname_sequence;


--值表
create table t_catavalue
(
	id varchar(7) not null,
	cataname varchar(8) not null,
	cataid varchar(8),
	catalabel varchar(20)
);
COMMENT on TABLE t_catavalue is '值表';
COMMENT on COLUMN t_catavalue.cataname is '主键id';
COMMENT on COLUMN t_catavalue.cataid is '值id';
COMMENT on COLUMN t_catavalue.catalabel is '值中文名称';

CREATE SEQUENCE catavalue_sequence;

--博客表 
create table t_blog
(
	id VARCHAR(12) not null,
	title VARCHAR(50) ,
	content text,
	themes varchar(30),
	catagoryid varchar(8),
	author varchar(20),
	state varchar(2),
	isprivate varchar(2),
	createtime varchar(20),
	updatetime varchar(20),
	updateuser varchar(20)
);
COMMENT on TABLE t_blog is '博客表';
COMMENT on COLUMN t_blog.title is '标题';
COMMENT on COLUMN t_blog.content is '内容';
COMMENT on COLUMN t_blog.themes is '主题';
COMMENT on COLUMN t_blog.catagoryid is '目录id';
COMMENT on COLUMN t_blog.author is '作者';
COMMENT on COLUMN t_blog.state is '审批状态-10001';
COMMENT on COLUMN t_blog.isprivate is '是否只能自己看，0否，1是';
COMMENT on COLUMN t_blog.createtime is '创建时间';
COMMENT on COLUMN t_blog.updatetime is '更新时间';
COMMENT on COLUMN t_blog.updateuser is '更新人';

CREATE SEQUENCE blog_sequence;

--评论表
create table t_blog_comment
(
 	id  VARCHAR(12) not null PRIMARY key,
 	blog_id VARCHAR(12) not null,
 	content text,
 	commentUser varchar(20),
 	createTime varchar(20)
);
COMMENT on TABLE t_blog_comment is '评论表';
COMMENT on COLUMN t_blog_comment.blog_id is '博客id';
COMMENT on COLUMN t_blog_comment.content is '评论内容';
COMMENT on COLUMN t_blog_comment.commentUser is '评论人';
COMMENT on COLUMN t_blog_comment.createTime is '创建时间';

CREATE SEQUENCE blog_comment_sequence;

--附件表
create table t_attach
(
	id  VARCHAR(12) not null PRIMARY key,
	catagory varchar(2) ,
	attachid varchar(20),
	attachname varchar(30),
	realpath varchar(30),
	createtime varchar(20)
);
COMMENT on TABLE t_attach is '评论表';
COMMENT on COLUMN t_attach.catagory is '附件类别';
COMMENT on COLUMN t_attach.attachid is '附件类别对应id';
COMMENT on COLUMN t_attach.attachname is '附件名称';
COMMENT on COLUMN t_attach.realpath is '真实路径';
COMMENT on COLUMN t_attach.createtime is '创建时间';

CREATE SEQUENCE attach_sequence;


create table t_catagory
(
	id varchar(20),
	catagoryname varchar(30),
	belongto varchar(1), --1问答 2博客
	createuser varchar(20),
	createtime varchar(20),
	updateuser varchar(20),
	updatetime varchar(20)
);
CREATE SEQUENCE catagory_sequence;

create table t_question
(
	id varchar(20),
	title varchar(80),
	content text,
	ismulty varchar(1),--是否多选 0单选 1多选
	answer varchar(20),
	catagoryid varchar(20),
	createuser varchar(20),
	createtime varchar(20),
	updateuser varchar(20),
	updatetime varchar(20)
);
CREATE SEQUENCE question_sequence;






