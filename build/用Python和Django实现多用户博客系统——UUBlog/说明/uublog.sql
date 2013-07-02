-- phpMyAdmin SQL Dump
-- version 3.2.0.1
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2013 年 06 月 23 日 21:00
-- 服务器版本: 5.5.8
-- PHP 版本: 5.3.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `uublog`
--

-- --------------------------------------------------------

--
-- 表的结构 `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk AUTO_INCREMENT=1 ;

--
-- 转存表中的数据 `auth_group`
--


-- --------------------------------------------------------

--
-- 表的结构 `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=43 ;

--
-- 转存表中的数据 `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user'),
(10, 'Can add content type', 4, 'add_contenttype'),
(11, 'Can change content type', 4, 'change_contenttype'),
(12, 'Can delete content type', 4, 'delete_contenttype'),
(13, 'Can add session', 5, 'add_session'),
(14, 'Can change session', 5, 'change_session'),
(15, 'Can delete session', 5, 'delete_session'),
(16, 'Can add site', 6, 'add_site'),
(17, 'Can change site', 6, 'change_site'),
(18, 'Can delete site', 6, 'delete_site'),
(19, 'Can add log entry', 7, 'add_logentry'),
(20, 'Can change log entry', 7, 'change_logentry'),
(21, 'Can delete log entry', 7, 'delete_logentry'),
(22, 'Can add poll', 8, 'add_poll'),
(23, 'Can change poll', 8, 'change_poll'),
(24, 'Can delete poll', 8, 'delete_poll'),
(25, 'Can add choice', 9, 'add_choice'),
(26, 'Can change choice', 9, 'change_choice'),
(27, 'Can delete choice', 9, 'delete_choice'),
(28, 'Can add category', 10, 'add_category'),
(29, 'Can change category', 10, 'change_category'),
(30, 'Can delete category', 10, 'delete_category'),
(31, 'Can add article', 11, 'add_article'),
(32, 'Can change article', 11, 'change_article'),
(33, 'Can delete article', 11, 'delete_article'),
(34, 'Can add comment', 12, 'add_comment'),
(35, 'Can change comment', 12, 'change_comment'),
(36, 'Can delete comment', 12, 'delete_comment'),
(37, 'Can add user profile', 13, 'add_userprofile'),
(38, 'Can change user profile', 13, 'change_userprofile'),
(39, 'Can delete user profile', 13, 'delete_userprofile'),
(40, 'Can add blog', 14, 'add_blog'),
(41, 'Can change blog', 14, 'change_blog'),
(42, 'Can delete blog', 14, 'delete_blog');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=3 ;

--
-- 转存表中的数据 `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$10000$RQkItPnH8YaA$L3sSVZ9fx3IiB+tURKAu2V//cysI0DgvtbfNhUfZpwg=', '2013-06-21 06:14:25', 1, 'admin', '', '', 'admin@uublog.me', 1, 1, '2013-06-21 06:14:25'),
(2, 'pbkdf2_sha256$10000$0mUKHTw3HM9E$tDna0fE8Wi+kEzq9J0UTnuNqv9ZP4ZFIZqtH0BD/oc4=', '2013-06-22 04:30:30', 0, 'uublog', 'uublog', '', 'uublog@sina.com', 0, 1, '2013-06-21 06:47:08');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk AUTO_INCREMENT=1 ;

--
-- 转存表中的数据 `auth_user_groups`
--


-- --------------------------------------------------------

--
-- 表的结构 `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk AUTO_INCREMENT=1 ;

--
-- 转存表中的数据 `auth_user_user_permissions`
--


-- --------------------------------------------------------

--
-- 表的结构 `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk AUTO_INCREMENT=1 ;

--
-- 转存表中的数据 `django_admin_log`
--


-- --------------------------------------------------------

--
-- 表的结构 `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=15 ;

--
-- 转存表中的数据 `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'permission', 'auth', 'permission'),
(2, 'group', 'auth', 'group'),
(3, 'user', 'auth', 'user'),
(4, 'content type', 'contenttypes', 'contenttype'),
(5, 'session', 'sessions', 'session'),
(6, 'site', 'sites', 'site'),
(7, 'log entry', 'admin', 'logentry'),
(8, 'poll', 'polls', 'poll'),
(9, 'choice', 'polls', 'choice'),
(10, 'category', 'UUBlog', 'category'),
(11, 'article', 'UUBlog', 'article'),
(12, 'comment', 'UUBlog', 'comment'),
(13, 'user profile', 'UUBlog', 'userprofile'),
(14, 'blog', 'UUBlog', 'blog');

-- --------------------------------------------------------

--
-- 表的结构 `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

--
-- 转存表中的数据 `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('ny7umb9j35xpqg95rec7ni4o0unjcvb4', 'NTM5MjY1MzQ0YjQ4ZGRjOTkzMTBiYjRkNDVhM2ZkNTQ0YmQ2MDY4NzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==', '2013-07-05 16:03:18'),
('upcj5ro8opsh6mgsw5ieqwrat9qc8ybe', 'NTM5MjY1MzQ0YjQ4ZGRjOTkzMTBiYjRkNDVhM2ZkNTQ0YmQ2MDY4NzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==', '2013-07-06 04:30:30');

-- --------------------------------------------------------

--
-- 表的结构 `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=2 ;

--
-- 转存表中的数据 `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

-- --------------------------------------------------------

--
-- 表的结构 `uublog_article`
--

CREATE TABLE IF NOT EXISTS `uublog_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `channel1_id` int(11) DEFAULT '0',
  `channel2_id` int(11) NOT NULL DEFAULT '0',
  `category_id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `pic` varchar(80) NOT NULL,
  `tags` varchar(120) NOT NULL,
  `summary` varchar(500) NOT NULL,
  `content` longtext NOT NULL,
  `createtime` datetime NOT NULL,
  `views` int(11) NOT NULL,
  `comments` int(11) NOT NULL,
  `goods` int(11) NOT NULL,
  `bads` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `username` varchar(80) NOT NULL,
  `ishome` int(11) NOT NULL,
  `isrecommend` int(11) NOT NULL,
  `istop` int(11) NOT NULL,
  `isoriginal` int(11) NOT NULL,
  `cancomment` int(11) NOT NULL,
  `password` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `UUBlog_article_6f33f001` (`category_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=12 ;

--
-- 转存表中的数据 `uublog_article`
--

INSERT INTO `uublog_article` (`id`, `channel1_id`, `channel2_id`, `category_id`, `title`, `pic`, `tags`, `summary`, `content`, `createtime`, `views`, `comments`, `goods`, `bads`, `status`, `user_id`, `username`, `ishome`, `isrecommend`, `istop`, `isoriginal`, `cancomment`, `password`) VALUES
(1, 10, 0, 2, 'Python 笔记——2 数据运算', '', '', '昨天写了关于Python文法，今天写点关于Python的数据运算的基本知识。1.数字类型运算　　在Python的 / 这个符号的运算中，只会返回float类型的数据。&nbsp;　当然你发现了，上述的最后一个例子中，或许和你想象的不大一样，\\&#39;不应该转义了么？这种情况下就不就结了。　　这时我们就可以使用print()函数来输出字符串，这种方式可读性更强。它会把所有转义字符都处理掉。&gt;', '<p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);"><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 16px; ">昨天写了关于Python文法，今天写点关于Python的数据运算的基本知识。</span></p><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);"><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; color: rgb(163, 133, 233); "><strong style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 16px; ">1.数字类型运算</span></strong></span></p><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);"><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 16px; ">　　在Python的 / 这个符号的运算中，只会返回float类型的数据。</span>&nbsp;</p><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);">　<span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 16px; ">当然你发现了，上述的最后一个例子中，或许和你想象的不大一样，\\&#39;不应该转义了么？这种情况下就不就结了。</span></p><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);"><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 16px; ">　　这时我们就可以使用print()函数来输出字符串，这种方式可读性更强。它会把所有转义字符都处理掉。</span></p><p><span class="cnblogs_code_copy" style="margin: 0px; padding: 0px 5px 0px 0px; line-height: 1.5;"><a title="复制代码" style="margin: 0px; padding: 0px; color: rgb(7, 93, 179); text-decoration: underline; border: none !important;"><img src="http://common.cnblogs.com/images/copycode.gif" alt="复制代码" style="margin: 0px; padding: 0px; border: none !important;"/></a></span></p><pre style="margin-top: 0px; margin-bottom: 0px; padding: 0px; white-space: pre-wrap; word-wrap: break-word; font-family: &#39;Courier New&#39;;">&gt;&gt;&gt;&nbsp;print(&#39;&quot;I\\&#39;m&nbsp;Programmer.&quot;I&nbsp;said.&#39;)\r\n&quot;I&#39;m&nbsp;Programmer.&quot;I&nbsp;said.\r\n&gt;&gt;&gt;&nbsp;a&nbsp;=&nbsp;&#39;C++&nbsp;\\n&nbsp;java&#39;\r\n&gt;&gt;&gt;&nbsp;a\r\n&#39;C++&nbsp;\\n&nbsp;java&#39;\r\n&gt;&gt;&gt;&nbsp;print(a)\r\nC++&nbsp;\r\n&nbsp;java</pre><p><span class="cnblogs_code_copy" style="margin: 0px; padding: 0px 5px 0px 0px; line-height: 1.5;"><a title="复制代码" style="margin: 0px; padding: 0px; color: rgb(7, 93, 179); text-decoration: underline; border: none !important;"><img src="http://common.cnblogs.com/images/copycode.gif" alt="复制代码" style="margin: 0px; padding: 0px; border: none !important;"/></a></span></p><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);">&nbsp;</p><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);">&nbsp;<span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 16px; ">　　有时候会输入文件路径，万一输入了c:\\name，岂不是一个很纠结的情况。这就需要在字符串前面加r，防止转义。</span></p><pre style="margin-top: 0px; margin-bottom: 0px; padding: 0px; white-space: pre-wrap; word-wrap: break-word; font-family: &#39;Courier New&#39;;">&gt;&gt;&gt;&nbsp;print(&#39;c:\\name&#39;)\r\nc:\r\name\r\n&gt;&gt;&gt;&nbsp;print(r&#39;c:\\name&#39;)\r\nc:\\name</pre><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);">&nbsp;<span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 16px; ">　　需要打印跨行字符串时，使用&#39;&#39;&#39;....&#39;&#39;&#39;三引号符，在第一个三引号后面加反斜杠。</span></p><p><span class="cnblogs_code_copy" style="margin: 0px; padding: 0px 5px 0px 0px; line-height: 1.5;"><a title="复制代码" style="margin: 0px; padding: 0px; color: rgb(7, 93, 179); text-decoration: underline; border: none !important;"><img src="http://common.cnblogs.com/images/copycode.gif" alt="复制代码" style="margin: 0px; padding: 0px; border: none !important;"/></a></span></p><pre style="margin-top: 0px; margin-bottom: 0px; padding: 0px; white-space: pre-wrap; word-wrap: break-word; font-family: &#39;Courier New&#39;;">&gt;&gt;&gt;&nbsp;print(&#39;&#39;&#39;\\\r\nList&nbsp;of&nbsp;Number:\r\n&nbsp;&nbsp;&nbsp;&nbsp;one\r\n&nbsp;&nbsp;&nbsp;&nbsp;two\r\n&#39;&#39;&#39;)\r\nList&nbsp;of&nbsp;Number:\r\n&nbsp;&nbsp;&nbsp;&nbsp;one\r\n&nbsp;&nbsp;&nbsp;&nbsp;two</pre><p><span class="cnblogs_code_copy" style="margin: 0px; padding: 0px 5px 0px 0px; line-height: 1.5;"><a title="复制代码" style="margin: 0px; padding: 0px; color: rgb(7, 93, 179); text-decoration: underline; border: none !important;"><img src="http://common.cnblogs.com/images/copycode.gif" alt="复制代码" style="margin: 0px; padding: 0px; border: none !important;"/></a></span></p><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);"><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 15px; ">&nbsp;　　接下来讲解一下字符串的连接，使用+加号连接，或者不加符号。另外可以用*乘号表示几个字符串连接。</span></p><pre style="margin-top: 0px; margin-bottom: 0px; padding: 0px; white-space: pre-wrap; word-wrap: break-word; font-family: &#39;Courier New&#39;;">&gt;&gt;&gt;&nbsp;3&nbsp;*&nbsp;&#39;hi&#39;&nbsp;+&nbsp;&#39;,tom&#39;\r\n&#39;hihihi,tom&#39;\r\n&gt;&gt;&gt;&nbsp;&#39;hi&#39;&#39;,tom&#39;\r\n&#39;hi,tom&#39;</pre><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);"><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 15px; ">　　字符串可作为一个数组使用，它的每一个元素便是一个字符。从左边开始的话，第一个元素的索引（index）是0；从右边开始的话，第一个元素的索引是-1。</span></p><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);"><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 15px; ">　　随便一提，-0和0是一个概念。</span></p><p><span class="cnblogs_code_copy" style="margin: 0px; padding: 0px 5px 0px 0px; line-height: 1.5;"><a title="复制代码" style="margin: 0px; padding: 0px; color: rgb(7, 93, 179); text-decoration: underline; border: none !important;"><img src="http://common.cnblogs.com/images/copycode.gif" alt="复制代码" style="margin: 0px; padding: 0px; border: none !important;"/></a></span></p><pre style="margin-top: 0px; margin-bottom: 0px; padding: 0px; white-space: pre-wrap; word-wrap: break-word; font-family: &#39;Courier New&#39;;">&gt;&gt;&gt;&nbsp;word&nbsp;=&nbsp;&#39;Python&#39;\r\n&gt;&gt;&gt;&nbsp;word[0]\r\n&#39;P&#39;\r\n&gt;&gt;&gt;&nbsp;word[2]\r\n&#39;t&#39;\r\n&gt;&gt;&gt;&nbsp;word[-1]\r\n&#39;n&#39;\r\n&gt;&gt;&gt;&nbsp;word[-3]\r\n&#39;h&#39;</pre><p><span class="cnblogs_code_copy" style="margin: 0px; padding: 0px 5px 0px 0px; line-height: 1.5;"><a title="复制代码" style="margin: 0px; padding: 0px; color: rgb(7, 93, 179); text-decoration: underline; border: none !important;"><img src="http://common.cnblogs.com/images/copycode.gif" alt="复制代码" style="margin: 0px; padding: 0px; border: none !important;"/></a></span></p><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);">　　<span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 15px; ">在Python中截取字符串，</span></p><p><br/></p>', '2013-06-21 07:23:12', 27, 1, 0, 0, 1, 2, 'uublog', 0, 0, 0, 1, 1, ''),
(2, 0, 0, 2, '传微软欲收购诺基亚 但谈判已破裂', '', '', '发言人称，他们与微软有深度的合作，并且他们之间也经常有常规会谈。而微软发言人则拒绝对此作出评论。谈判破裂归结于价格和诺基亚的战略处境微软和诺基亚谈判破裂的部分原因是诺基亚的价格和其目前处境等问题。是的，在格局上诺基亚不仅落后于苹果和三星，而如今许多亚洲新贵公司在智能手机和其他移动设备上也能迅速获得市场份额。两年多前，微软与诺基亚达成战略合作，诺基亚同意在其智能手机中使用微软独家的操作系统，双方这次', '<p style="word-wrap: break-word; ; ; ; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(255, 255, 255); list-style-type: none; color: rgb(51, 51, 51); font-family: Helvetica, Tahoma, Arial, sans-serif; line-height: 24px;">发言人称，他们与微软有深度的合作，并且他们之间也经常有常规会谈。而微软发言人则拒绝对此作出评论。</p><p style="word-wrap: break-word; ; ; ; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(255, 255, 255); list-style-type: none; color: rgb(51, 51, 51); font-family: Helvetica, Tahoma, Arial, sans-serif; line-height: 24px;"><strong style="word-wrap: break-word; ">谈判破裂归结于价格和诺基亚的战略处境</strong></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(255, 255, 255); list-style-type: none; color: rgb(51, 51, 51); font-family: Helvetica, Tahoma, Arial, sans-serif; line-height: 24px;">微软和诺基亚谈判破裂的部分原因是诺基亚的价格和其目前处境等问题。是的，在格局上诺基亚不仅落后于苹果和三星，而如今许多亚洲新贵公司在智能手机和其他移动设备上也能迅速获得市场份额。</p><p style="word-wrap: break-word; ; ; ; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(255, 255, 255); list-style-type: none; color: rgb(51, 51, 51); font-family: Helvetica, Tahoma, Arial, sans-serif; line-height: 24px;">两年多前，微软与诺基亚达成战略合作，诺基亚同意在其智能手机中使用微软独家的操作系统，双方这次的战略合作被称是美国软件巨头和手机领域先锋间的合作，在这方面双方都取得了重大进展。在达成战略合作后的两年时间，两家公司都很努力试图适应这个消费者偏爱苹果和三星手机的世界，但这次合作至今为止也未能显著提升这两家公司的移动命运。</p><p style="word-wrap: break-word; ; ; ; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(255, 255, 255); list-style-type: none; color: rgb(51, 51, 51); font-family: Helvetica, Tahoma, Arial, sans-serif; line-height: 24px;">诺基亚目前的股价约为3.84美元，较去年同期相比上涨了50％，其市值目前大约为140亿美元，这与历史最高点相比其价值是大幅下滑。对于这次可能会达成的收购，最有利的一个因素是微软可以使用离岸现金达成交易。据悉，微软在一海外的子公司目前大约有660亿美元的储备，但由于面临一大笔税单而最终没有带回美国。</p><p style="word-wrap: break-word; ; ; ; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(255, 255, 255); list-style-type: none; color: rgb(51, 51, 51); font-family: Helvetica, Tahoma, Arial, sans-serif; line-height: 24px;">尽管微软的移动操作系统Windows Phone目前已超越 BlackBerry，成为世界第三大智能手机系统，但它仍旧是在Android激烈的竞争中艰难前行。数据分析机构IDC表示，在今年第一季度Windows Phone出货量占了3.2％的市场份额，而三星、摩托罗拉等其他手机商城搭配Android系统的手机出货量则达到了75％。可以说不论是对诺基亚还是微软而言，他们目前这个战略合作并未达到人们预期想象的高度。（文/张勇 责编/魏兵）</p><p><br/></p>', '2013-06-22 01:13:51', 0, 0, 0, 0, 1, 2, 'uublog', 0, 0, 0, 1, 1, ''),
(3, 0, 0, 2, '如何在django中 执行原始SQL', '', '', '如何在django中 执行原始SQLhttp://www.djangochina.cn/forum.php?mod=viewthread&amp;tid=167&amp;fromuid=2(出处: Django中国|Django中文社区)Django提供两种方式执行(performing)原始的SQL查询：（1）、Manager.raw():执行原始查询并返回模型实例（2）、Executing c', '<p>如何在django中 执行原始SQL</p><p>http://www.djangochina.cn/forum.php?mod=viewthread&amp;tid=167&amp;fromuid=2</p><p>(出处: Django中国|Django中文社区)</p><table cellspacing="0" cellpadding="0" data-find="_4" width="757"><tbody data-find="_3" style="word-wrap: break-word; "><tr data-find="_2" style="word-wrap: break-word; "><td class="t_f" id="postmessage_208" data-find="_1" style="word-wrap: break-word; font-size: 14px; "><br style="word-wrap: break-word; "/>Django提供两种方式执行(performing)原始的SQL查询：<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>（1）、Manager.raw():执行原始查询并返回模型实例<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>（2）、Executing custom SQL directly：直接执行自定义SQL，这种方式可以完全避免数据模型，而是直接执行原始的SQL语句。<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/><span style="word-wrap: break-word; font-weight: 700; ">raw()方法</span><br style="word-wrap: break-word; "/>The raw() manager method can be used to perform raw SQL queries that return model instances:<br style="word-wrap: break-word; "/>　　Manager.raw(raw_query, params=None, translations=None)<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>用法：<ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>&gt;&gt;&gt; for p in Person.objects.raw(&#39;SELECT * FROM Person LIMIT 2&#39;):<br style="word-wrap: break-word; "/></p></li><li><p>...&nbsp; &nbsp;&nbsp;&nbsp;print p<br style="word-wrap: break-word; "/></p></li><li><p>John Smith<br style="word-wrap: break-word; "/></p></li><li><p>Jane Jones</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p>注意，原始SQL里的model，如果在db_table 没有定义，则使用app的名称，后面下划线 后面接模型类的名称,如&quot;Myblog_New&quot;;上面的例子，在定义类的时候已经这样处理了：<ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>Class New(models.Model):<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; ......<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; ......<br style="word-wrap: break-word; "/></p></li><li><p>#自定义表名<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; class Meta:<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;db_table = &#39;New&#39;</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p>2、查询字段隐射到模型字段（Mapping query fields to model fields）<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>raw() automatically maps fields in the query to fields on the model.并且是通过名称来匹配，这意味着我们可以使用SQL子句(clause)<ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>&gt;&gt;&gt; Person.objects.raw(&#39;&#39;&#39;SELECT first AS first_name,<br style="word-wrap: break-word; "/></p></li><li><p>...&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;last AS last_name,<br style="word-wrap: break-word; "/></p></li><li><p>...&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;bd AS birth_date,<br style="word-wrap: break-word; "/></p></li><li><p>...&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;pk as id,<br style="word-wrap: break-word; "/></p></li><li><p>...&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;FROM some_other_table&#39;&#39;&#39;)</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p>返回一个RawQuerySet对象<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>3、索引查找(Index lookups)<ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>first_person = Person.objects.raw(&#39;SELECT * from myapp_person&#39;)[0]<br style="word-wrap: break-word; "/></p></li><li><p>first_person = Person.objects.raw(&#39;SELECT * from myapp_person LIMIT 1&#39;)[0]<br style="word-wrap: break-word; "/></p></li><li><p>#然而,索引和切片不是在数据库级别上执行(除LIMIT外)</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p>4、延迟模型字段（Deferring model fields）<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>Fields may also be left out（left out：忽视，不考虑；被遗忘），这意味着该字段的查询将会被排除在根据需要时的加载。<ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>&gt;&gt;&gt; for p in Person.objects.raw(&#39;SELECT id, first_name FROM myapp_person&#39;):<br style="word-wrap: break-word; "/></p></li><li><p>...&nbsp; &nbsp;&nbsp;&nbsp;print p.first_name, # 这将检索到原始查询<br style="word-wrap: break-word; "/></p></li><li><p>...&nbsp; &nbsp;&nbsp;&nbsp;print p.last_name # 这将检索需求<br style="word-wrap: break-word; "/></p></li><li><p>...<br style="word-wrap: break-word; "/></p></li><li><p>John Smith<br style="word-wrap: break-word; "/></p></li><li><p>Jane Jones</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p>这个例子其实检索了三个字段，一个主键(必需)、一个原始SQL字段、一个需求字段。这里主键字段不能省略，否则会出错，如下：<br style="word-wrap: break-word; "/><img id="aimg_CLmSm" class="zoom" width="600" height="209" file="http://images.cnitblog.com/blog/476998/201305/27114117-a12a23e0f4cb421e83e506c6fd6e0b14.png" border="0" alt="" src="http://images.cnitblog.com/blog/476998/201305/27114117-a12a23e0f4cb421e83e506c6fd6e0b14.png" lazyloaded="true" _load="1" style="word-wrap: break-word; cursor: pointer; "/><br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>5、传递参数(Passing parameters into raw())<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>如果需要执行参数化查询,您可以使用params参数原始()<br style="word-wrap: break-word; "/><ignore_js_op style="word-wrap: break-word; "><p><img id="aimg_79" aid="79" src="http://www.djangochina.cn/data/attachment/forum/201305/27/123618uff54ov5hv55hnfk.png" zoomfile="data/attachment/forum/201305/27/123618uff54ov5hv55hnfk.png" file="data/attachment/forum/201305/27/123618uff54ov5hv55hnfk.png" class="zoom" width="600" inpost="1" lazyloaded="true" _load="1" initialized="true" style="word-wrap: break-word; cursor: pointer; "/></p></ignore_js_op><br style="word-wrap: break-word; "/>注意两点：<br style="word-wrap: break-word; "/>（1）、<br style="word-wrap: break-word; "/><ignore_js_op style="word-wrap: break-word; "><p><img id="aimg_80" aid="80" src="http://www.djangochina.cn/data/attachment/forum/201305/27/123715vw5oj3uuwf7uzdnu.png" zoomfile="data/attachment/forum/201305/27/123715vw5oj3uuwf7uzdnu.png" file="data/attachment/forum/201305/27/123715vw5oj3uuwf7uzdnu.png" class="zoom" width="502" inpost="1" lazyloaded="true" _load="1" initialized="true" style="word-wrap: break-word; cursor: pointer; "/></p></ignore_js_op><br style="word-wrap: break-word; "/>（2）、必须使用[参数]，否则出错：<br style="word-wrap: break-word; "/><ignore_js_op style="word-wrap: break-word; "><p><img id="aimg_81" aid="81" src="http://www.djangochina.cn/data/attachment/forum/201305/27/123735pnsgg0wgzgnlsw05.png" zoomfile="data/attachment/forum/201305/27/123735pnsgg0wgzgnlsw05.png" file="data/attachment/forum/201305/27/123735pnsgg0wgzgnlsw05.png" class="zoom" width="479" inpost="1" lazyloaded="true" _load="1" style="word-wrap: break-word; cursor: pointer; "/></p></ignore_js_op><br style="word-wrap: break-word; "/>（3）、这种方式不对：<ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>Error:<br style="word-wrap: break-word; "/></p></li><li><p>&gt;&gt;&gt; query = &#39;SELECT * FROM myapp_person WHERE last_name = %s&#39; % lname<br style="word-wrap: break-word; "/></p></li><li><p>&gt;&gt;&gt; Person.objects.raw(query)</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p><span style="word-wrap: break-word; font-weight: 700; ">直接执行自定义SQL</span><br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>Manager.raw()远远不够，可直接执行自定义SQL，directly execute UPDATE, INSERT, or DELETE queries.<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>django.db.connection：代表默认的数据库连接<br style="word-wrap: break-word; "/>django.db.transaction：代表默认数据库事务（transaction）<br style="word-wrap: break-word; "/>用database connection调用connection.cursor() 得到一个游标(cursor)对象。<br style="word-wrap: break-word; "/>然后调用cursor.execute(sql, [params])执行SQL<br style="word-wrap: break-word; "/>cursor.fetchone() 或者 cursor.fetchall()：返回结果行<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>如果执行修改操作，则调用transaction.commit_unless_managed()来保证你的更改提交到数据库。<ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>def my_custom_sql():<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; from django.db import connection, transaction<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; cursor = connection.cursor()<br style="word-wrap: break-word; "/></p></li><li><p><br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; # 数据修改操作——提交要求<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; cursor.execute(&quot;UPDATE bar SET foo = 1 WHERE baz = %s&quot;, [self.baz])<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; transaction.commit_unless_managed()<br style="word-wrap: break-word; "/></p></li><li><p><br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; # 数据检索操作,不需要提交<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; cursor.execute(&quot;SELECT foo FROM bar WHERE baz = %s&quot;, [self.baz])<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; row = cursor.fetchone()<br style="word-wrap: break-word; "/></p></li><li><p><br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; return row</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p>django.db.connections：针对使用多个数据库<ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>from django.db import connections<br style="word-wrap: break-word; "/></p></li><li><p>cursor = connections[&#39;my_db_alias&#39;].cursor()<br style="word-wrap: break-word; "/></p></li><li><p># Your code here...<br style="word-wrap: break-word; "/></p></li><li><p>transaction.commit_unless_managed(using=&#39;my_db_alias&#39;)</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p>通常我们不需要手动调用transaction.commit_unless_managed(),我们可以这样做：<ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>@commit_on_success<br style="word-wrap: break-word; "/></p></li><li><p>def my_custom_sql_view(request, value):<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; from django.db import connection, transaction<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; cursor = connection.cursor()<br style="word-wrap: break-word; "/></p></li><li><p><br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; # Data modifying operation<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; cursor.execute(&quot;UPDATE bar SET foo = 1 WHERE baz = %s&quot;, [value])<br style="word-wrap: break-word; "/></p></li><li><p><br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; # Since we modified data, mark the transaction as dirty<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; &lt;span style=&quot;color: #ff0000;&quot;&gt;transaction.set_dirty()&lt;/span&gt;<br style="word-wrap: break-word; "/></p></li><li><p><br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; # Data retrieval operation. This doesn&#39;t dirty the transaction,<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; # so no call to set_dirty() is required.<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; cursor.execute(&quot;SELECT foo FROM bar WHERE baz = %s&quot;, [value])<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&lt;span style=&quot;color: #ff0000;&quot;&gt; row = cursor.fetchone()&lt;/span&gt;<br style="word-wrap: break-word; "/></p></li><li><p><br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; &lt;span style=&quot;color: #ff0000;&quot;&gt;return render_to_response(&#39;template.html&#39;, {&#39;row&#39;: row})<br style="word-wrap: break-word; "/></p></li><li><p>&lt;/span&gt;</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p><span style="word-wrap: break-word; font-weight: 700; ">个人常用：</span><ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>def Message(request,msg_id):<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; &nbsp; &nbsp; where=msg_id<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;sql=&#39;&#39;&#39;<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;select t.id, t.real_name, t2.* from auth_user t join (<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;select max(is_red) as is_red,add_user_id,task_id from oa_red_yellow_card 　　　　　　　where msg_id=%s GROUP BY task_id,add_user_id)<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;t2 ON t2.add_user_id=t.id<br style="word-wrap: break-word; "/></p></li><li><p><br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; &#39;&#39;&#39; %where&nbsp;<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;cursor = connection.cursor()<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;cursor.execute(sql)<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;fetchall = cursor.fetchall()<br style="word-wrap: break-word; "/></p></li><li><p><br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;red_yellow_card=[]<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;for obj in fetchall:<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; dic={}<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; dic[&#39;user_id&#39;]=obj[0]<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; dic[&#39;real_name&#39;]=obj[1]<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; dic[&#39;is_red&#39;]=obj[2]<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; dic[&#39;add_user&#39;]=obj[3]<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; dic[&#39;task_id&#39;]=obj[4]<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; red_yellow_card.append(dic)<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;context[&#39;red_yellow_card&#39;]=red_yellow_card</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p></td></tr></tbody></table><p><a title="如何" href="http://www.djangochina.cn/misc.php?mod=tag&amp;id=54" target="_blank" style="word-wrap: break-word; color: rgb(51, 102, 153); text-decoration: none; ">如何</a></p><p><br/></p>', '2013-06-22 01:14:40', 0, 0, 0, 0, 1, 2, 'uublog', 0, 0, 0, 1, 1, ''),
(4, 0, 0, 2, '中国联通ESS系统，读卡器插件异常，请确认插件是否正确安装', '', '', '中国联通ESS系统，读卡器插件异常，请确认插件是否正确安装', '<p><span style="color: rgb(68, 68, 68); font-family: &#39;Microsoft Yahei&#39;, Hei, Tahoma, SimHei, sans-serif; font-weight: bold; orphans: 2; text-align: -webkit-auto;  widows: 2; background-color: rgb(255, 255, 255);">中国联通ESS系统，读卡器插件异常，请确认插件是否正确安装</span></p>', '2013-06-22 01:15:25', 1, 0, 0, 0, 1, 2, 'uublog', 0, 0, 0, 1, 1, ''),
(5, 0, 0, 2, '：军队要形成团结友爱和谐纯洁的内部关系', '', '', '全军党的群众路线教育实践活动工作会议在京召开　　范长龙许其亮出席　　新华网北京6月21日电（记者李宣良）中共中央总书记、国家主席、中央军委主席习近平日前作出重要指示，强调军队开展党的群众路线教育实践活动，既要贯彻中央统一要求，又要体现自身特点和建设规律，着眼永葆人民军队性质、宗旨、本色，着眼形成和发展团结友爱和谐纯洁的内部关系，着眼促进军队各项工作和建设。要坚决反对形式主义、官僚主义、享乐主义和奢', '<p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;"><strong style="margin: 0px; padding: 0px; list-style: none; border: 0px;">全军党的群众路线教育实践活动工作会议在京召开</strong></p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;"><strong style="margin: 0px; padding: 0px; list-style: none; border: 0px;">　　范长龙许其亮出席</strong></p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　新华网北京6月21日电（记者李宣良）中共中央总书记、国家主席、中央军委主席习近平日前作出重要指示，强调军队开展党的群众路线教育实践活动，既要贯彻中央统一要求，又要体现自身特点和建设规律，着眼永葆人民军队性质、宗旨、本色，着眼形成和发展团结友爱和谐纯洁的内部关系，着眼促进军队各项工作和建设。要坚决反对形式主义、官僚主义、享乐主义和奢靡之风，着力在纠治官兵反映强烈的突出问题上见到成效，在解决深层次矛盾和问题上见到成效，在构建规范化、制度化的长效机制上见到成效，努力从思想上、组织上、作风上为实现党在新形势下的强军目标提供坚强保证。</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　经习主席批准，全军党的群众路线教育实践活动工作会议21日在京召开。会议主要任务是认真贯彻党中央的部署要求，坚决落实习主席和军委决策指示，对全军深入开展党的群众路线教育实践活动进行动员部署。中共中央政治局委员、中央军委副主席范长龙，中共中央政治局委员、中央军委副主席许其亮出席会议并讲话。中央军委委员常万全、房峰辉、赵克石、张又侠、吴胜利、马晓天、魏凤和出席，张阳主持。</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　范长龙强调，贯彻党中央、习主席的决策部署和重要指示，搞好军队的教育实践活动，进一步抓好作风建设，要围绕实现党在新形势下的强军目标，贯彻“照镜子、正衣冠、洗洗澡、治治病”的总要求，突出反对形式主义、官僚主义、享乐主义和奢靡之风这个重点，坚持领导带头、严字当头，标本兼治、综合施策，务求改进作风有新成效，官兵士气高，部队风气正，强军底气足，有效履行军队的使命任务。要深化思想认识，充分认清这次教育实践活动的重大意义，站在听党指挥的高度，树立走在前列的标准，打赢改作风这场硬仗。反对形式主义，要着重解决文山会海、贪图虚名、弄虚作假、工作不实的问题；反对官僚主义，要着重解决对广大官兵的根本态度问题；反对享乐主义，要着重克服贪图享受、及时行乐思想和精神懈怠、不思进取的现象；反对奢靡之风，要着重纠治铺张浪费、挥霍无度、骄奢淫逸的不良风气。要认真贯彻整风精神，敢于较真碰硬，抓正反两方面典型。要以具体管用的制度作保证，对于公务接待、军车管理、建房占房、选人用人、资源管理等，要一项一项研究。要把教育实践活动与部队正在开展的各项工作结合起来，与加强党委班子和干部队伍建设结合起来，聚焦到提高战斗力上，贯穿到以军事斗争准备为龙头的各项工作中，确保部队能经受各种考验，圆满完成各项任务。</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　许其亮指出，各级要坚持用党中央、习主席的决策指示统一思想，充分认清开展教育实践活动是永葆党的性质宗旨的内在要求、是传承我党我军优良传统和作风的现实需要、是推动实现中国梦强军梦的战略之举，切实以强烈的政治责任感，高标准抓好教育实践活动，确保取得党中央、习主席满意，人民群众和广大官兵满意的成效。要紧密结合军队特点和实际，着力增强开展教育实践活动的质量和实效。牢牢把握听党指挥、服务人民这一核心要求，突出抓好中国特色社会主义理论体系武装，抓好马克思主义群众观点和党的群众路线、我军性质宗旨和优良传统教育，强化官兵宗旨意识，从思想根源和灵魂深处坚定信念、铸牢军魂，确保部队绝对忠诚、绝对纯洁、绝对可靠，一切行动听从党中央、中央军委和习主席指挥。以整风精神解决作风上的突出问题，坚决贯彻“照镜子、正衣冠、洗洗澡、治治病”的总要求，突出“四反”整治，以解决问题的实际成效取信官兵。始终把提高战斗力作为根本出发点落脚点，促进军事斗争准备往深里抓往实里抓。构建规范化制度化的长效机制推动形成文化自觉，使为民务实清廉成为每个党员干部的信仰追求。要把开展教育实践活动作为重大政治任务，严格落实党委领导责任，尤其是领导干部要带头参加，勇于纠正自身问题。</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　张阳主持会议时指出，要把习主席和军委的决策指示学习领会好，结合实际把教育实践活动工作部署安排好，把教育实践活动与其他工作统筹兼顾好，把加强组织领导的各项要求认真落实好，推动教育实践活动深入发展。</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　会议以电视电话会议形式举行。四总部、驻京各大单位、军委办公厅领导和全军教育实践活动领导小组成员在主会场参加会议。全军和武警部队军以上单位党委常委、部门领导在分会场参加会议。</p><p><br/></p>', '2013-06-22 01:15:53', 0, 0, 0, 0, 1, 2, 'uublog', 0, 0, 0, 1, 1, ''),
(6, 0, 0, 2, '大火启示录：拯救命悬一线的劳动权益', '', '', '　截止至6月4日早7时30分，吉林省德惠市吉林宝源丰禽业有限公司火灾，已造成120人遇难，70人受伤，事故发生后，企业法人代表已被控制。伤者描述，事发时，车间总计有300余人，工人上班后，车间大多数门都会被锁上。（6月4日 新华社）　　火灾猛于虎——吉林大火，再一次让世人看到了这一点。120人死亡、70人受伤的残酷现实，让无数个家庭陷入地狱般的深渊。虽然当地政府已经成立工作组做好维稳及善后工作，但', '<p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　截止至6月4日早7时30分，吉林省德惠市吉林宝源丰禽业有限公司火灾，已造成120人遇难，70人受伤，事故发生后，企业法人代表已被控制。伤者描述，事发时，车间总计有300余人，工人上班后，车间大多数门都会被锁上。（6月4日 新华社）</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　火灾猛于虎——吉林大火，再一次让世人看到了这一点。120人死亡、70人受伤的残酷现实，让无数个家庭陷入地狱般的深渊。虽然当地政府已经成立工作组做好维稳及善后工作，但是逝去的亡灵不再复活，造成的伤痛无法在短期内抚平。</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　我们不妨来看一下遇难者的身份。虽然当地政府并没有给出火灾发生的具体理由，但是可以肯定，这场火灾发生在了生产车间，死亡者基本都是普通工人。在笔者看来，这样的一场大火，烧出了我国众多普通劳动者的工作常态——车间大门紧锁、工人缺乏逃生训练、现场消防条件乏善可陈、现场没有火灾警报系统、没有自动喷水消防系统……</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　表面上看来，这是防火意识、防火条件的问题。实际上，这反映了我国普通劳动者的生命权益无法受到尊重和保护的现实。1995年实施的《劳动法》第六章是关于“劳动安全卫生”的内容。第五十二条规定，“用人单位必须建立、健全劳动安全卫生制度，严格执行国家劳动安全卫生规程和标准，对劳动者进行劳动安全卫生教育，防止劳动过程中的事故”；第五十三条规定，“劳动安全卫生设施必须符合国家规定的标准。”因此，我们有必要问一问当地政府，这家企业为什么没有按这样的标准进行消防配备？为什么没有对劳动者进行“安全教育”？当地劳动部门有没有进行负责任的监管？</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　作为“世界工厂”，如果对于劳动密集产业的安全监管不够，对于劳动者的权益尤其是生命权利不够尊重，则难免会产生惨烈的事故。而出事之后，政府不仅要将企业负责人和政府监管者进行问责，要对受害人及其家属进行到位和及时的赔偿，更要从根本上提高劳动者的权益、尊严和地位，让他们不再工作于命悬一线的危险车间。</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　关于立法进行权益保护，美国的三角内衣大火或许能够给我们一些启示。1911年3月25日，是美国纽约市历史上最大的工业灾难——三角内衣工厂火灾，火灾导致146名服装工人被烧死或因被迫跳楼致死。这也是纽约市2001年911事件之前最严重的工作场所的灾难。灾难的发生，促进了美国《劳动法》的通过实施。在1912年的美国《劳动法》之中，我们看到了这样的详细规定：工作场所每3个月就必须进行一次防火训练；在7层以上超过200名工作人员的楼层，必须安装自动防火喷淋系统；雇员超过25名的工作场所，都必须安装自动报警系统……这些在100年前的美国《劳动法》就已经出现的劳动权益保护规定，值得我们学习。</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　生命的价值重于财富——这是以人为本时代里，最需要普及的常识性价值理念。流水线的劳动者，不是机器，而是人。而人的生命价值是无法衡量的，是最宝贵的。而维护生命的尊严，只处理企业相关责任人，或是问责负责安全生产监管和劳动权益保护的官员，都是不够的。只有从用法律的方式去规范企业和安全生产行为，才可能改变劳动者的弱势地位，让劳动者有尊严的工作，让劳动者的生命不再为草芥。</p><p><br/></p>', '2013-06-22 01:16:20', 0, 0, 0, 0, 1, 2, 'uublog', 0, 0, 0, 1, 1, '');
INSERT INTO `uublog_article` (`id`, `channel1_id`, `channel2_id`, `category_id`, `title`, `pic`, `tags`, `summary`, `content`, `createtime`, `views`, `comments`, `goods`, `bads`, `status`, `user_id`, `username`, `ishome`, `isrecommend`, `istop`, `isoriginal`, `cancomment`, `password`) VALUES
(7, 2, 0, 2, '张东健安七炫朴海镇 来中国捞金的韩男星/图', '', '', '张东健曾是韩国第一小生　　张东健，韩国著名男演员，顶级韩流明星。1992年参加韩国MBC电视台第21期演员培训班出道。出道以来演出多部影视作品，并凭借电视剧《天桥风云》《夏娃的诱惑》等风靡全亚洲。2004年凭借电影《太极旗飘扬》获得韩国电影青龙奖最佳男主角奖，这还使他成为青龙奖有史以来得到男演员类所有奖项大满贯的第一人。2010年5月2日张东健与演员高素荣结婚，2010年10月4日张东健喜得贵子。', '<p style="text-align:center;; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;"><img alt="" src="http://pinglun.youth.cn/wywy/wysh/201306/W020130621373075210333.jpg" oldsrc="W020130621373075210333.jpg" style="margin: 0px; padding: 0px; list-style: none; border: 0px;"/></p><p style="text-align:center;; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">张东健曾是韩国第一小生</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　张东健，韩国著名男演员，顶级韩流明星。1992年参加韩国MBC电视台第21期演员培训班出道。出道以来演出多部影视作品，并凭借电视剧《天桥风云》《夏娃的诱惑》等风靡全亚洲。2004年凭借电影《太极旗飘扬》获得韩国电影青龙奖最佳男主角奖，这还使他成为青龙奖有史以来得到男演员类所有奖项大满贯的第一人。2010年5月2日张东健与演员高素荣结婚，2010年10月4日张东健喜得贵子。2012年时隔12年重返小银幕 ，以韩国SBS TV新剧《绅士的品格》中的&quot;毒舌&quot;金道振形象回归。</p><p><br/></p>', '2013-06-22 01:16:47', 2, 0, 0, 0, 1, 2, 'uublog', 0, 0, 0, 1, 1, ''),
(8, 2, 0, 2, 'Windows 8.1最新版Build 9428曝光', '', '', '今天，一张名为 Windows 8.1 Milestone Preview 的截图出现在网上，如果图片并非伪造，那它就可能是微软将于 6 月 26 日发布的 Windows 8.1 公开预览版（也就是 Beta 公测版）。　　从截图中可以看到，Windows 8.1 Milestone Preview 的具体版本为 Build 9428，编译于 6 月 12 日。早在 5 月份就有传言称，Wind', '<p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); font-family: Verdana, Arial, Helvetica, sans-serif;">今天，一张名为 Windows 8.1 Milestone Preview 的截图出现在网上，如果图片并非伪造，那它就可能是微软将于 6 月 26 日发布的 Windows 8.1 公开预览版（也就是 Beta 公测版）。</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160229-c9974ebdc8f14c61b1b6b67f23382c7c.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); font-family: Verdana, Arial, Helvetica, sans-serif;">　　从截图中可以看到，Windows 8.1 Milestone Preview 的具体版本为 Build 9428，编译于 6 月 12 日。早在 5 月份就有传言称，Windows 8.1 公开预览版将选定 Build 9428，若此截图为真，那么上述传言就比较可信了。</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160228-9b4743c8ac6f4f1ca12694b88e595d81.jpg" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　还有几张应用程序的截图：</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160229-96b626131d1848b18403ef2836433f81.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　天气</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160229-9ef9f093af4c45b8ac66cc8845a005cb.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　计算器</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160228-4a54f0238df743c3bceb6af065bf455b.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　Movie Moments 电影时光</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160229-7e0b08c652764ebab8586b189e99e8d1.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　录音</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160229-a8780936da844105936d150f37cfc239.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　录音</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160229-40268b0a3bd64df990c69fd99375232f.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　闹钟</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160229-2c92a647a39145dd8ab64f9a9993c15e.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　Windows Store</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160230-64c2edf1ffa74c7db809ca9fef07854a.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　Windows Store 中的 Skype</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160230-1a0996eb73e24612b7cc2ddd73fe2fac.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　Windows Store 中的 Skype</p><p><br/></p>', '2013-06-22 01:17:26', 4, 0, 0, 0, 1, 2, 'uublog', 0, 0, 0, 1, 1, ''),
(9, 1, 1, 2, '创造别人想要的东西（1）----创业的本质', '', '', '　创业的本质是从自己出发，从身边的朋友出发，深度了解用户，发现用户的潜需求，做出一款满足用户刚需的产品或者服务。　　一个创业公司想要成功，必要条件（甚至可以说是充要条件）是它能够为人们提供人们想要的东西。这听起来是一个显而易见，无需赘述的道理，但却是创业公司经常没有充分考虑的问题。大张旗鼓，轰轰烈烈的创业，最终却做出了一些没人想要的产品，这样的例子在中外都常见。　　举个例子，Webvan，1999', '<p style=";"><strong>　<span style="background-color: rgb(128, 0, 128); color: rgb(255, 255, 255); font-size: 18pt; ">创业的本质</span></strong><span style="font-size: 15px; ">是从自己出发，从身边的朋友出发，深度了解用户，发现用户的潜需求，做出一款满足用户刚需的产品或者服务。</span></p><p style=";"><span style="font-size: 15px; ">　　一个创业公司想要成功，必要条件（甚至可以说是充要条件）是它能够为人们提供人们想要的东西。这听起来是一个显而易见，无需赘述的道理，但却是创业公司经常没有充分考虑的问题。大张旗鼓，轰轰烈烈的创业，最终却做出了一些没人想要的产品，这样的例子在中外都常见。</span></p><p style=";"><span style="font-size: 15px; ">　　举个例子，Webvan，1999年在加州创立的线上杂货（grocery）销售网站，在融资额高达12亿美金之后，2001年宣告破产！这被证明<strong><span style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 255); ">至少在当时不是一个人们需要的服务</span></strong>。</span></p><p style=";"><span style="font-size: 15px; ">　　创业是艰辛的，从产品设计，到技术实现，到上线，到运营，到营销，到融资，再到面对媒体。</span></p><p style=";"><span style="font-size: 15px; ">　　我以前在的公司就是一个例子，购物搜索，比价，情感挖掘，让用户更便捷的买到自己的宝贝，09年就萌发的想法，时间远远超前于一淘，涉及到技术也比较前沿，但最后成就了一款没用户量的产品，失败在哪里？我个人觉得是在运营。工作几年后发现，发现运营真心重要。</span></p><p style=";">&nbsp;</p><p style=";">　　<span style="font-size: 18pt; "><strong><span style="background-color: rgb(128, 0, 128); color: rgb(255, 255, 255); ">困难</span></strong></span><span style="font-size: 15px; ">是多重的，创造出别人需要的东西，不是一件简单的事情。单单从统计数字上看，大多数创业公司是失败的。华尔街日报曾有报道，3/4的创业公司连投资者的本钱都无法挣回来。找到别人生活中存在的某个问题或者某种需求，然后（用技术手段）创造一个产品或服务将其解决。很多创业者就是这么想的。但实际上，<span style="color: rgb(0, 0, 255); "><strong>发现一个真正的问题，是比找到解决方法，是更有难度的事情</strong></span>。创造新的东西本就是在摸索未知。一次一次的迭代想法，通过数据分析，通过调查，来改进自己的产品服务。</span></p><p style=";"><span style="font-size: 15px; ">　　<span style="color: rgb(0, 0, 255); "><strong>创造者面临的另一个困难是，而真正巨大的需求，往往因为我们所处时代的局限而不能够被察觉</strong></span>。试想我们回到5年前，调研当时的互联网用户，恐怕还没有人会觉得有接收来自不相识的人140个字微博的需求。回想06年左右，Youtube公司于2005年2月15日注册，世界最大的视频分享网站，表现你自己，show出你的风采，你很难理解发现几年后，视频行业这么火。淘宝网2003年成立，你也很难相信你可以在网上与不见面老板进行买卖，这种信用机制在当时很难想象，而现在一天一亿次的亲，也改变了用户的购物习惯。</span></p><p data-find="_9" style=";"><span data-find="_8" style="font-size: 15px; ">　　<strong><span style="color: rgb(0, 0, 255); ">雪上加霜的是</span></strong>，对于天朝互联网界来说，更有一个值得担忧的传统。天朝的互联网行业发展几十年，很长时间一直处在追赶美国的硅谷。形成了一个C2C (copy to China) 的传统。最早一批成功的互联网公司也往往是复制美国已经成型的模式，包括实时通信工具，到搜索引擎，到门户网站。C2C带来了快速成功的可能，但是培养了很多人的思考习惯：更多在关注其他市场的成功案例，而忽略了手边客户的需求。比如视频行业，优酷土豆爱奇艺56酷6模仿youtube，百度搜搜360模仿谷歌，花瓣美丽说蘑菇街模仿pinterest，腾腾讯模仿qicq，知乎模仿quora，人人网模仿facebook但越走越偏，等等，这就是中国的悲剧，从来都是一个没有创意的国度，而模仿能力超级强。让我想起了中国教育，爱国爱社会，从小的洗脑，学微积分却不知道到底有毛用，就tmd知道解题，现在还是不太懂它的来历它到底在那些方面实现了它的价值，从小的教育培养了独特变态的你，这是应试教育的悲哀！</span></p><p style=";"><span style="font-size: 15px; ">　　<span style="color: rgb(0, 0, 255); "><strong>要敢于革自己的命</strong></span>，敢于回避知道的风险赶紧业务转型，敢于不吃老底而一次次的迭代变革自己的产品，在变革中成就自己。想想曾经的暴风影音，现在远没有前几年火了，想想网际快车，不知道还有几个人记得？想想电驴，我已经很久没上电驴了。想想人人网，至少2年没登陆过了。曾经风光无限的开心网，正在被遗忘。还有猫扑，不上了不玩了。怎么让自己的产品接地气，怎么让在残酷的竞争中杀出一条血路。</span></p><p style=";"><span style="font-size: 15px; ">　　中国内互联网企业的厮杀也异常激烈，大企业瞬间复制模仿你，秒杀你，2004年9月，QQ游戏平台将联众赶下了中国第一休闲游戏门户的宝座。我记得那个时候室友还在上面玩游戏，现在联众早已被网民遗忘，以至于记得当时的新闻是，&quot;多年以后，在北京知春路的一家咖啡馆，联众创始人鲍岳桥谈起当年腾讯对联众的围剿和逼迫，仍然耿耿于怀。在两个小时的采访中，他连续抽了两包烟&quot;。2006年底，鲍岳桥离开了江河日下的联众，成为了一名天使投资人。他告诉记者，现在他做投资的原则之一就是：<span style="color: rgb(0, 0, 255); "><strong>只做腾讯不会做、不能做的项目，</strong></span><span style="color: rgb(0, 0, 255); "><strong>别让腾讯盯上</strong></span>。腾讯，都是山寨。</span><em><br/></em></p><p style=";">&nbsp;</p><p style=";">　　<span style="background-color: rgb(128, 0, 128); color: rgb(255, 255, 255); font-size: 18pt; "><strong>己之所欲，可施于人</strong></span><span style="font-size: 15px; ">，我想说的是“实践是检验真理的唯一标准”。一个产品或者服务，是否是人们所要的，唯有试了才知道。逻辑的分析，其他市场，其他人的成功，只能作为一个维度或者指标来评判对产品的一个估计。从你自己的需求出发，你可以保证至少这个需求是确实存在，而不是你臆想出来。你有的问题，很有可能很多人都有。所谓”己之所欲，可施于人“。很多伟大的公司都如此诞生：苹果公司是因为 Steve Wozniak 自己想要一台个人电脑，Dropbox是因为Drew Houston 厌烦了每天拿着优盘，hotmail是几位程序员需要更方便的查自己的邮箱，Ben Silbermann 为他的女朋友寻找订婚戒指之时。他发现了很多还算中意的戒指，但又需要反复比较，于是他就开发了 Pinterest，把它们随手贴在同一个页面上。</span></p><p style=";"><span style="font-size: 15px; ">　　仅仅作为一个尝试，想想你能够简单快速的做出什么来，满足你自己的需求，进而满足别人的需求。也许，下一个让用户疯狂的产品就在从你这里诞生！轻松自己，轻松世界，改变自我，影响世界。</span></p><p style=";">　　<span style="font-size: 15px; ">本文参考网易公开课百科青年第二期峰哥的文章进行润色整理，</span><span style="font-size: 15px; ">欢迎微博互粉<span style="background-color: rgb(255, 255, 255); color: rgb(255, 0, 0); ">&nbsp;<strong>@板栗小羊</strong></span></span></p><p style=";">　　<img src="http://images.cnitblog.com/blog/388574/201306/22122557-6d04810b636748779ec95c84406b9592.jpg" alt="" style="border-top-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px; border-style: initial; border-color: initial; border-image: initial; "/></p><p>分类:&nbsp;<a href="http://www.cnblogs.com/banli/category/479394.html" style="color: rgb(0, 102, 255); text-decoration: none; ">视野扩展</a></p><p><br/></p>', '2013-06-22 05:02:38', 5, 1, 0, 0, 1, 2, 'uublog', 0, 0, 0, 1, 1, ''),
(10, 3, 3, 2, '普林斯顿大学算法公开课（1）----介绍', '', '', '课程概况这个课程是什么？（1）中级研究课程。（2）编程解决问题。（3）算法：解决问题的思路方法。（4）数据结构：存储信息的方法。课程分为两个部分为什么学习算法？算法的影响力是宽广和深远的。影响的领域不完全列表如下。（1）网络。包括搜索，包路由，分布式共享文件。（2）生物。包括基因工程，蛋白质折叠。（3）计算机。电路草图，文件系统，编译器。（4）计算机图形图像。电影，电子游戏，虚拟现实。（5）安全。', '<p style=";"><span style="font-size: 14px; background-color: rgb(0, 51, 0); color: rgb(255, 255, 255); "><strong>课程概况</strong></span></p><p style=";"><strong><span style="font-size: 14px; ">这个课程是什么？</span></strong></p><p style=";"><span style="font-size: 14px; ">（1）中级研究课程。</span></p><p style=";"><span style="font-size: 14px; ">（2）编程解决问题。</span></p><p style=";"><span style="font-size: 14px; ">（3）算法：解决问题的思路方法。</span></p><p style=";"><span style="font-size: 14px; ">（4）数据结构：存储信息的方法。</span></p><p style=";"><strong><span style="font-size: 14px; ">课程分为两个部分</span></strong></p><p style=";"><span style="font-size: 14px; "><img src="http://images.cnitblog.com/blog/388574/201306/16184114-f1d82ba5e5a244d7862a413ed6a2a5a7.jpg" alt="" width="666" height="321" style="border-top-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px; border-style: initial; border-color: initial; border-image: initial; "/></span></p><p style=";"><span style="font-size: 14px; background-color: rgb(0, 51, 0); color: rgb(255, 255, 255); "><strong>为什么学习算法？</strong></span></p><p style=";"><strong><span style="font-size: 14px; ">算法的影响力是宽广和深远的。影响的领域不完全列表如下。</span></strong></p><p style=";"><span style="font-size: 14px; ">（1）网络。包括搜索，包路由，分布式共享文件。</span></p><p style=";"><span style="font-size: 14px; ">（2）生物。包括基因工程，蛋白质折叠。</span></p><p style=";"><span style="font-size: 14px; ">（3）计算机。电路草图，文件系统，编译器。</span></p><p style=";"><span style="font-size: 14px; ">（4）计算机图形图像。电影，电子游戏，虚拟现实。</span></p><p style=";"><span style="font-size: 14px; ">（5）安全。手机，电子商务，投票计算机。</span></p><p style=";"><span style="font-size: 14px; ">（6）多媒体。mp3，jpg，divx，hdtv，人脸识别。</span></p><p style=";"><span style="font-size: 14px; ">（7）社会网络。推荐系统，新闻feeding，广告学。</span></p><p style=";"><span style="font-size: 14px; ">（8）物理学。n体模拟，粒子碰撞模拟。</span></p><p style=";"><strong><span style="font-size: 14px; ">针对个人，公司，学习算法有什么好处？</span></strong></p><p style=";"><span style="font-size: 14px; ">（1）智力激发。</span></p><p style=";"><span style="font-size: 14px; ">（2）成为高效的程序员。</span></p><p style=";"><span style="font-size: 14px; ">（3）揭开宇宙中生活的秘密。</span></p><p style=";"><span style="font-size: 14px; ">（4）为了乐趣和利润。</span></p><p style=";"><span style="background-color: rgb(0, 51, 0); color: rgb(255, 255, 255); "><strong><span style="font-size: 14px; ">资源</span></strong></span></p><p style=";"><span style="font-size: 14px; ">textbook，<a href="http://pan.baidu.com/share/link?shareid=4082772650&amp;uk=2483086068" style="color: rgb(0, 102, 255); text-decoration: none; ">http://algs4.cs.princeton.edu/home/</a></span></p><p style=";"><span style="font-size: 14px; ">公开课的视频和课件可以从我的百度网盘下载，<a href="http://pan.baidu.com/share/link?shareid=4082772650&amp;uk=2483086068" style="color: rgb(0, 102, 255); text-decoration: none; ">http://pan.baidu.com/share/link?shareid=4082772650&amp;uk=2483086068</a></span></p><p style=";"><strong><span style="background-color: rgb(255, 0, 0); color: rgb(255, 255, 255); ">今天是父亲节，祝福所有的程序员爸爸和程序员的爸爸节日快乐！</span></strong></p><p style=";"><img src="http://images.cnitblog.com/blog/388574/201306/16191903-7ce1f92c0cc74dc6a41e8deb9daef5e1.jpg" alt="" style="border-top-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px; border-style: initial; border-color: initial; border-image: initial; "/>　</p><p>分类:&nbsp;<a href="http://www.cnblogs.com/banli/category/479395.html" style="color: rgb(0, 102, 255); text-decoration: none; ">算法研究</a></p><p><br/></p>', '2013-06-22 05:03:09', 1, 0, 0, 0, 1, 2, 'uublog', 0, 0, 0, 1, 1, ''),
(11, 1, 0, 2, '第一次当面试官', '', '', '　今天第一面试别人，感觉还行，大概80分钟的样子结束了我的第一次，其实还是蛮长。应该有80*60/12多雷。　　以前都是别人面试我，这次终于也当了一次面试官。这次才真正体会到，其实面试官有时候可能比求职者，要付出更多时间来准备面试。面试官要根据简历的情况，来准备面试题目，要在短短的几十分钟内，还是需要面试官根据面试情况来调整面试题目等，以最短的时间获得准确的信息，了解一个人，其实很多时候还是看感觉', '<p style=";"><span style="font-family: 宋体; font-size: 15px; ">　今天第一面试别人，感觉还行，大概80分钟的样子结束了我的第一次，其实还是蛮长。应该有80*60/12多雷。</span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; ">　　以前都是别人面试我，这次终于也当了一次面试官。这次才真正体会到，其实面试官有时候可能比求职者，要付出更多时间来准备面试。面试官要根据简历的情况，来准备面试题目，要在短短的几十分钟内，还是需要面试官根据面试情况来调整面试题目等，以最短的时间获得准确的信息，了解一个人，其实很多时候还是看感觉的。</span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; ">　　前几天看了下<span style="color: rgb(255, 0, 0); "><span style="color: rgb(0, 0, 255); ">@左耳朵耗子</span></span>博客上的关于面试的几篇文章，收获到很多干货。其实面试的目标是想获得下面三件事情：</span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; ">　　（1）<span style="line-height: 22px; background-color: rgb(255, 255, 255);">这个</span><span style="line-height: 22px; background-color: rgb(255, 255, 255);">程序员的是否够聪明？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（2）</span><span style="line-height: 22px; background-color: rgb(255, 255, 255);">这个程序员能否把事情搞定？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（3）</span><span style="line-height: 22px; background-color: rgb(255, 255, 255);">这个程序员能和我的团队在一起工作吗？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　我的处女面试大概分下面几个步骤：</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　<span style="color: rgb(255, 0, 0); ">　<strong>开场</strong></span></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　我是XX的工程师，很高兴由我来和你聊聊技术，聊聊项目等，其实我也是第一次面试别人，可能我比你还紧张，所以也不用太紧张太严肃。Ok，我们开始！</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　<strong><span style="color: rgb(255, 0, 0); ">针对简历上提到的项目经验</span></strong></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（1）根据详细问项目怎么做的，具体细节等，第一来考察求职者是不是真参与了这个项目。</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（2）明白项目的用途，场景，或者指标等，做这个项目，哪里没做好，那些地方还有优化之处。　</span></span></p><p style=";"><span style="color: rgb(255, 0, 0); font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　<strong>　针对简历上提到的技能</strong></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　这里针对“熟悉hadoop”来提的几个问题</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（1）<span style="color: rgb(0, 0, 0); line-height: normal;">setMapOutputKeyClass</span>和<span style="color: rgb(0, 0, 0); line-height: normal;">setOutputKeyClass</span>的区别？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（2）<span lang="EN-US" style="color: rgb(0, 0, 0); line-height: 26px;">Combiner</span><span style="color: rgb(0, 0, 0); line-height: 26px;">的作用？partition的作用？</span></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);"><span style="color: rgb(0, 0, 0); line-height: 26px;">　　（3）setup和cleanup函数的用途？</span></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; ">　　（4）mapreduce的流程？具体讲下shuffle的细节？</span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; ">　　（5）hadoop的二次排序，代码上大概应该怎么写？具体内部原理是什么？</span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　<span style="color: rgb(255, 0, 0); "><strong>　针对面试的职位</strong></span></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　针对面试的岗位需要的技能面试，这里会针对数据挖掘面试一些基本知识。</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（1）knn，k-means，svm关联规则等的一些知识。</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（2）tf-idf的概念。</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><strong><span style="color: rgb(255, 0, 0); "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　算法</span></span></strong></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　这里会出几个大数据的算法，几个可以引导求职者一起攻克的循环更新的面试题。</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（1）快速从几亿个宝贝中找出今天点击量最大的top100个宝贝。</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（2）hashmap的内部实现原理？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　<span style="color: rgb(255, 0, 0); "><strong>产品</strong></span></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);"><strong>　　</strong>（1）你觉得你现在做的产品那些地方，不管是ui，还是交互，还是算法上，有那些可以改进的？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（2）你觉得我们这的产品，那些地方设计的不够人性化，影响了用户体验的？哪些功能有些badcace？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（3）说一下你经常用的一个app中，优秀的设计和需要改进的地方？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　<span style="color: rgb(255, 0, 0); "><strong>工作态度</strong></span></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（1）为什么换工作？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（2）工作几年来，有什么心得感悟和恼火的经历？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　<strong><span style="color: rgb(255, 0, 0); ">　面试者提问</span></strong></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（1）对我们团队，对我们公司，有什么需要，或者感兴趣想了解的？</span></span></p><p style=";"><span style="color: rgb(255, 0, 0); font-size: 15px; "><strong><span style="font-family: 宋体; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　结尾</span></span></strong></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　<span style="color: rgb(0, 0, 0); line-height: normal;">OK，那就先到这里，如果有后续面试的话，再通知你。拜拜。</span></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　<span style="color: rgb(255, 0, 0); "><strong>面试别人的收获总结：</strong></span></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（1）在面试的过程中，不断穿插聊天方式的打断，来easy求职者，使得整个面试不那么严肃，就像同事之间的聊天，一个问题的解决探讨，这样才能让面试者发挥正常，也能让面试官更全面容易的了解求职者。我现在穿插的方式问一些平常有什么爱好，玩游戏嘛，玩dota吗，我们这经常和老大一起玩，老家哪里的等。</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　我的第一次面试，还是很粗糙，需要完善的地方好多，希望自己和求职者一起进步！也希望其他<span style="color: rgb(0, 0, 255); ">博友</span>能给我一些建议和经验之谈。谢谢。</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　<img src="http://images.cnitblog.com/blog/388574/201305/13234303-25bbf3100b9443938d4f8f8c5d6adade.jpg" alt="" style="border-top-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px; border-style: initial; border-color: initial; border-image: initial; "/></span></span></p><p>分类:&nbsp;<a href="http://www.cnblogs.com/banli/category/479394.html" style="color: rgb(0, 102, 255); text-decoration: none; ">视野扩展</a></p><p><br/></p>', '2013-06-22 05:03:49', 4, 0, 0, 0, 1, 2, 'uublog', 0, 0, 0, 1, 1, '');

-- --------------------------------------------------------

--
-- 表的结构 `uublog_blog`
--

CREATE TABLE IF NOT EXISTS `uublog_blog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `domain` varchar(200) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` varchar(200) NOT NULL,
  `keywords` varchar(200) NOT NULL,
  `about` varchar(500) NOT NULL,
  `announcement` varchar(500) NOT NULL,
  `modules` varchar(200) NOT NULL,
  `template` varchar(50) NOT NULL,
  `css` varchar(500) NOT NULL,
  `headhtml` varchar(500) NOT NULL,
  `footerhtml` varchar(500) NOT NULL,
  `todayviews` int(11) NOT NULL,
  `totalviews` int(11) NOT NULL,
  `articles` int(11) NOT NULL,
  `comments` int(11) NOT NULL,
  `createtime` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=3 ;

--
-- 转存表中的数据 `uublog_blog`
--

INSERT INTO `uublog_blog` (`id`, `user_id`, `domain`, `title`, `description`, `keywords`, `about`, `announcement`, `modules`, `template`, `css`, `headhtml`, `footerhtml`, `todayviews`, `totalviews`, `articles`, `comments`, `createtime`) VALUES
(1, 1, '', 'admin的博客', '', '', '', '', 'profile,hotarticlelist,hotcommentlist', 'default', '', '', '', 3, 3, 0, 0, '2013-06-21 06:34:56'),
(2, 2, '', 'uublog的博客', '', '', '', '', 'profile,category,hotcommentlist,hotarticlelist', 'default', '', '', '', 68, 68, 11, 2, '2013-06-21 06:47:09');

-- --------------------------------------------------------

--
-- 表的结构 `uublog_category`
--

CREATE TABLE IF NOT EXISTS `uublog_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `sortnum` int(11) NOT NULL,
  `articles` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=3 ;

--
-- 转存表中的数据 `uublog_category`
--

INSERT INTO `uublog_category` (`id`, `name`, `sortnum`, `articles`, `user_id`) VALUES
(1, '未分类', -1, -1, -1),
(2, '明星', 1, 11, 2);

-- --------------------------------------------------------

--
-- 表的结构 `uublog_channel`
--

CREATE TABLE IF NOT EXISTS `uublog_channel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `parent_id` int(11) NOT NULL DEFAULT '0',
  `name` varchar(80) NOT NULL DEFAULT '',
  `sortnum` int(11) NOT NULL DEFAULT '0',
  `articles` int(11) NOT NULL DEFAULT '0',
  `users` int(11) NOT NULL DEFAULT '0',
  `user_id` int(11) NOT NULL DEFAULT '0',
  `username` varchar(80) NOT NULL DEFAULT '',
  `isenable` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=28 ;

--
-- 转存表中的数据 `uublog_channel`
--

INSERT INTO `uublog_channel` (`id`, `parent_id`, `name`, `sortnum`, `articles`, `users`, `user_id`, `username`, `isenable`) VALUES
(1, 0, '摄影', 0, 2, 0, 0, '', 1),
(2, 0, '旅游', 0, 0, 0, 0, '', 1),
(3, 0, '美食', 0, 2, 0, 0, '', 1),
(4, 0, '宠物', 0, 0, 0, 0, '', 1),
(5, 0, '家居', 0, 0, 0, 0, '', 1),
(6, 0, '时尚', 0, 0, 0, 0, '', 1),
(7, 0, '文学', 0, 0, 0, 0, '', 1),
(8, 0, '艺术', 0, 0, 0, 0, '', 1),
(9, 0, '创意', 0, 0, 0, 0, '', 1),
(10, 0, '影视', 0, 0, 0, 0, '', 1),
(11, 0, '美女', 0, 0, 0, 0, '', 1),
(12, 0, '音乐', 0, 0, 0, 0, '', 1),
(13, 0, '游戏', 0, 0, 0, 0, '', 1),
(14, 0, '动漫', 0, 0, 0, 0, '', 1),
(15, 0, '搞笑', 0, 0, 0, 0, '', 1),
(16, 0, '星座', 0, 0, 0, 0, '', 1),
(17, 0, '恋物', 0, 0, 0, 0, '', 1),
(18, 0, '体育', 0, 0, 0, 0, '', 1),
(19, 0, '数码', 0, 0, 0, 0, '', 1),
(20, 0, '科学', 0, 0, 0, 0, '', 1),
(21, 0, '育儿', 0, 0, 0, 0, '', 1),
(22, 0, '心情', 0, 0, 0, 0, '', 1),
(23, 0, '自然', 0, 0, 0, 0, '', 1),
(24, 0, '插画', 0, 0, 0, 0, '', 1),
(25, 0, '明星', 0, 0, 0, 0, '', 1),
(26, 0, '资讯', 0, 0, 0, 0, '', 1),
(27, 0, '生活', 0, 0, 0, 0, '', 1);

-- --------------------------------------------------------

--
-- 表的结构 `uublog_comment`
--

CREATE TABLE IF NOT EXISTS `uublog_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `username` varchar(80) NOT NULL,
  `content` longtext NOT NULL,
  `createtime` datetime NOT NULL,
  `goods` int(11) NOT NULL,
  `bads` int(11) NOT NULL,
  `reply_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `UUBlog_comment_e669cc35` (`article_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=3 ;

--
-- 转存表中的数据 `uublog_comment`
--

INSERT INTO `uublog_comment` (`id`, `article_id`, `user_id`, `username`, `content`, `createtime`, `goods`, `bads`, `reply_id`) VALUES
(1, 1, 2, 'uublog', 'asdfafds', '2013-06-21 09:38:51', 0, 0, 0),
(2, 9, 2, 'uublog', '残酷的竞争中杀出一条血路。\r\n　　中国内互联网企业的厮杀也异常激烈，大企业瞬间复制模仿你，秒杀你，2004年9月，QQ游戏平台将联众赶下了中国第一休闲游戏门户的宝座。我记得那个时候室友还在上面玩游戏，现在联众早已被网民遗忘，以至于记得当时的新闻是，"多年以后，在北京知春路的一家咖啡馆，联众创始人鲍岳桥谈起当年腾讯对联众的围剿和逼迫，仍然耿耿于怀。在两个小时的采访中，他连续抽了两包烟"。20', '2013-06-22 05:24:02', 0, 0, 0);

-- --------------------------------------------------------

--
-- 表的结构 `uublog_userprofile`
--

CREATE TABLE IF NOT EXISTS `uublog_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `avatar` varchar(100) NOT NULL,
  `nickname` varchar(80) NOT NULL,
  `realname` varchar(80) NOT NULL,
  `gender` int(11) NOT NULL,
  `birthday` datetime NOT NULL,
  `birthcity` varchar(80) NOT NULL,
  `residecity` varchar(80) NOT NULL,
  `affectivestatus` int(11) NOT NULL,
  `lookingfor` int(11) NOT NULL,
  `bloodtype` int(11) NOT NULL,
  `site` varchar(80) NOT NULL,
  `bio` varchar(255) NOT NULL,
  `interest` varchar(255) NOT NULL,
  `sightml` varchar(255) NOT NULL,
  `timeoffset` varchar(80) NOT NULL,
  `qq` varchar(80) NOT NULL,
  `msn` varchar(80) NOT NULL,
  `taobao` varchar(80) NOT NULL,
  `email` varchar(80) NOT NULL,
  `phone` varchar(80) NOT NULL,
  `mobile` varchar(80) NOT NULL,
  `address` varchar(80) NOT NULL,
  `zipcode` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=3 ;

--
-- 转存表中的数据 `uublog_userprofile`
--

INSERT INTO `uublog_userprofile` (`id`, `user_id`, `avatar`, `nickname`, `realname`, `gender`, `birthday`, `birthcity`, `residecity`, `affectivestatus`, `lookingfor`, `bloodtype`, `site`, `bio`, `interest`, `sightml`, `timeoffset`, `qq`, `msn`, `taobao`, `email`, `phone`, `mobile`, `address`, `zipcode`) VALUES
(1, 1, '', 'admin', '', 0, '2013-06-21 06:23:14', '', '', 0, 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', ''),
(2, 2, 'avatar/000/00/02.gif', 'uublog', '', 0, '2013-06-21 06:23:14', '', '', 0, 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', '');

--
-- 限制导出的表
--

--
-- 限制表 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- 限制表 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `uublog_article`
--
ALTER TABLE `uublog_article`
  ADD CONSTRAINT `category_id_refs_id_4c266c54` FOREIGN KEY (`category_id`) REFERENCES `uublog_category` (`id`);

--
-- 限制表 `uublog_comment`
--
ALTER TABLE `uublog_comment`
  ADD CONSTRAINT `article_id_refs_id_ec096e86` FOREIGN KEY (`article_id`) REFERENCES `uublog_article` (`id`);

--
-- 限制表 `uublog_userprofile`
--
ALTER TABLE `uublog_userprofile`
  ADD CONSTRAINT `user_id_refs_id_3acc5dbb` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
