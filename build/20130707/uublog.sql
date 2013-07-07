-- phpMyAdmin SQL Dump
-- version 3.2.0.1
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2013 年 07 月 07 日 22:39
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
-- 表的结构 `accounts_userprofile`
--

CREATE TABLE IF NOT EXISTS `accounts_userprofile` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=22 ;

--
-- 转存表中的数据 `accounts_userprofile`
--

INSERT INTO `accounts_userprofile` (`id`, `user_id`, `avatar`, `nickname`, `realname`, `gender`, `birthday`, `birthcity`, `residecity`, `affectivestatus`, `lookingfor`, `bloodtype`, `site`, `bio`, `interest`, `sightml`, `timeoffset`, `qq`, `msn`, `taobao`, `email`, `phone`, `mobile`, `address`, `zipcode`) VALUES
(1, 1, '', 'admin', '', 0, '2013-06-21 06:23:14', '', '', 0, 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', ''),
(2, 2, 'avatar/000/00/02.gif', 'uublog', '', 0, '2013-06-21 06:23:14', '', '', 0, 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', ''),
(3, 3, 'avatar/000/00/03.jpg', 'test5', '', 0, '2013-06-28 04:55:10', '', '', 0, 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', ''),
(4, 4, 'avatar/000/00/04.jpg', 'test6', '', 0, '2013-06-28 05:49:48', '', '', 0, 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', ''),
(5, 5, '', 'xiaohuang', '', 0, '2013-06-29 10:36:41', '', '', 0, 0, 2, '', '', '', '', '', '', '', '', '', '', '', '', ''),
(6, 6, '', 'dd', '', 0, '2013-06-30 00:12:12', '', '', 0, 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', ''),
(7, 7, '', 'kongjian1', '', 0, '2013-06-30 12:52:09', '', '', 0, 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', ''),
(8, 8, '', 'kongjian2', '', 0, '2013-06-30 12:52:09', '', '', 0, 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', ''),
(9, 9, '', 'kongjian3', '', 0, '2013-06-30 12:52:09', '', '', 0, 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', ''),
(10, 10, '', 'kongjian4', '', 0, '2013-06-30 12:52:09', '', '', 0, 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', ''),
(11, 11, '', 'qiqi', '', 0, '2013-06-30 13:06:42', '', '', 0, 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', ''),
(12, 12, 'avatar/000/00/12.jpg', 'didi', 'a', 1, '2013-07-01 04:40:08', 'b', 'c', 0, 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', ''),
(13, 13, '', 'bbb', '', 0, '2013-07-02 15:15:49', '', '', 0, 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', ''),
(14, 14, '', 'ddd', '', 0, '2013-07-02 15:34:17', '', '', 0, 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', ''),
(18, 15, '', 'ccc', '', 0, '2013-07-03 01:10:43', '', '', 0, 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', ''),
(19, 16, '', 'ttt', '', 0, '2013-07-03 12:19:10', '', '', 0, 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', ''),
(20, 17, '', 'aaa', '', 0, '2013-07-06 12:07:34', '', '', 0, 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', ''),
(21, 18, '', 'night', '', 0, '2013-07-06 14:38:12', '', '', 0, 0, 0, '', '', '', '', '', '', '', '', '', '', '', '', '');

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
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=46 ;

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
(42, 'Can delete blog', 14, 'delete_blog'),
(43, 'Can add user profile', 15, 'add_userprofile'),
(44, 'Can change user profile', 15, 'change_userprofile'),
(45, 'Can delete user profile', 15, 'delete_userprofile');

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
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=19 ;

--
-- 转存表中的数据 `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$10000$RQkItPnH8YaA$L3sSVZ9fx3IiB+tURKAu2V//cysI0DgvtbfNhUfZpwg=', '2013-06-21 06:14:25', 1, 'admin', '', '', 'admin@uublog.me', 1, 1, '2013-06-21 06:14:25'),
(2, 'pbkdf2_sha256$10000$0mUKHTw3HM9E$tDna0fE8Wi+kEzq9J0UTnuNqv9ZP4ZFIZqtH0BD/oc4=', '2013-07-06 12:07:46', 0, 'uublog', 'uublog', '', 'uublog@sina.com', 0, 1, '2013-06-21 06:47:08'),
(3, 'pbkdf2_sha256$10000$IOHN3DUOYQE0$gqCi+gqQmFqVHzQVxtO45bH31nzmLCmXvjWSzQnj7tM=', '2013-06-30 00:16:29', 0, 'test5', 'test5', '', 'test5@qq.com', 0, 1, '2013-06-28 04:53:05'),
(4, 'pbkdf2_sha256$10000$oUou0un4rs2k$ripZqXRrkFrx1dSIO1M3TUulUBijRulvSx3h/ZxIRxI=', '2013-06-28 06:27:59', 0, 'test6', 'test6', '', 'test6@qq.com', 0, 1, '2013-06-28 06:21:41'),
(5, 'pbkdf2_sha256$10000$mYk4Efs08xDI$6DkQCYDEJnhCXSGvbCR6jc+D7I31s449wZrQ65y7Y5w=', '2013-06-29 10:37:53', 0, 'xiaohuang', 'xiaohuang', '', 'xiaohuang@qq.com', 0, 1, '2013-06-29 10:37:35'),
(6, 'pbkdf2_sha256$10000$y4VTLTmtsPbx$HzXsgLXlV0JJEmGF5mf9xIREiHU5W8DyDikJ44x5Nj4=', '2013-07-02 09:15:29', 0, 'dd', 'dd', '', 'dd@ss.com', 0, 1, '2013-06-30 12:46:42'),
(7, 'pbkdf2_sha256$10000$p4AHhNiNMo5F$0nMVach9vG8Z/QcldgjYHKRVyxEcVOt/xFRecJCH4AU=', '2013-06-30 13:09:35', 0, 'kongjian1', 'kongjian1', '', 'kongjian1', 0, 1, '2013-06-30 12:55:25'),
(8, 'pbkdf2_sha256$10000$xOJzvBRKqZfB$tck/NPcQIZQIGp0dIc5Nds+ijHr8EjYYgznTfirrl3c=', '2013-06-30 12:55:35', 0, 'kongjian2', 'kongjian2', '', 'kongjian2', 0, 1, '2013-06-30 12:55:35'),
(9, 'pbkdf2_sha256$10000$aKyuapmTvy5Y$ju7DprXfMGesATeDCRg7U/c8M1r9+4ckywt9iVIeB68=', '2013-06-30 12:55:44', 0, 'kongjian3', 'kongjian3', '', 'kongjian3', 0, 1, '2013-06-30 12:55:44'),
(10, 'pbkdf2_sha256$10000$aHxTTan3UG27$JDDmDv4hF5a8XiaxvxfoN3cVOzCOv+/tfbELveflYw0=', '2013-06-30 12:56:15', 0, 'kongjian4', 'kongjian4', '', 'kongjian4', 0, 1, '2013-06-30 12:55:54'),
(11, 'pbkdf2_sha256$10000$Opy3n56oaHST$Eo4mGSw4I0yI+ySVHXwcgEdxFuaxJms2wYSThUpRYYY=', '2013-06-30 13:07:16', 0, 'qiqi', 'qiqi', '', 'qiqi', 0, 1, '2013-06-30 13:06:57'),
(12, 'pbkdf2_sha256$10000$4yrKj9hw3bvP$waLBi0eygby0SF7BwCfvKOrtjTWqZ/poVrAh/+JVJOQ=', '2013-07-01 04:49:52', 0, 'didi', 'didi', '', 'didi', 0, 1, '2013-07-01 04:49:43'),
(13, 'pbkdf2_sha256$10000$icBzi2zKue6L$UxNesVA/ndlDuOri3Eh4jOWwYnjfwcGXMrfLxhRLbBs=', '2013-07-02 15:30:15', 0, 'bbb', 'bbb', '', 'bbb', 0, 1, '2013-07-02 15:30:15'),
(14, 'pbkdf2_sha256$10000$cSRHUfMH1sMO$VzkY7J++it7SUskUIkMHwhHi0gK7Gru9DA23SV74te4=', '2013-07-03 01:04:03', 0, 'ddd', 'ddd', '', 'ddd', 0, 1, '2013-07-02 15:34:17'),
(15, 'pbkdf2_sha256$10000$VHI7Ct4ls5Bm$JgQS2bw21fYpgdXxtwpCHfuwj8L60DvUafA+3nOqXbA=', '2013-07-03 01:11:13', 0, 'ccc', 'ccc', '', 'ccc', 0, 1, '2013-07-03 01:11:02'),
(16, 'pbkdf2_sha256$10000$H8dZTbK9C6VI$bWUT0cq0+6i3ieifvhTtFaqfN38FcII1RoNsChlQbuY=', '2013-07-03 12:20:20', 0, 'ttt', 'ttt', '', 'ttt', 0, 1, '2013-07-03 12:20:06'),
(17, 'pbkdf2_sha256$10000$kmOcQqxBylvO$eovLDn6vM7fDPQo1ZfVTQitTB2B6pQc8TiuheXV14Jc=', '2013-07-06 12:08:46', 0, 'aaa', 'aaa', '', 'aaa', 0, 1, '2013-07-06 12:08:32'),
(18, 'pbkdf2_sha256$10000$REm0LX6IIV7e$3JQ+HbTglD0AYioBQDoRgVQjVrFKAyN08VFEy6q79f4=', '2013-07-06 14:46:16', 0, 'night', 'night', '', 'night', 0, 1, '2013-07-06 14:45:59');

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
-- 表的结构 `blog_article`
--

CREATE TABLE IF NOT EXISTS `blog_article` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=31 ;

--
-- 转存表中的数据 `blog_article`
--

INSERT INTO `blog_article` (`id`, `channel1_id`, `channel2_id`, `category_id`, `title`, `pic`, `tags`, `summary`, `content`, `createtime`, `views`, `comments`, `goods`, `bads`, `status`, `user_id`, `username`, `ishome`, `isrecommend`, `istop`, `isoriginal`, `cancomment`, `password`) VALUES
(1, 10, 0, 2, 'Python 笔记——2 数据运算', '', '', '昨天写了关于Python文法，今天写点关于Python的数据运算的基本知识。1.数字类型运算　　在Python的 / 这个符号的运算中，只会返回float类型的数据。&nbsp;　当然你发现了，上述的最后一个例子中，或许和你想象的不大一样，\\&#39;不应该转义了么？这种情况下就不就结了。　　这时我们就可以使用print()函数来输出字符串，这种方式可读性更强。它会把所有转义字符都处理掉。&gt;', '<p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);"><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 16px; ">昨天写了关于Python文法，今天写点关于Python的数据运算的基本知识。</span></p><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);"><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; color: rgb(163, 133, 233); "><strong style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 16px; ">1.数字类型运算</span></strong></span></p><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);"><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 16px; ">　　在Python的 / 这个符号的运算中，只会返回float类型的数据。</span>&nbsp;</p><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);">　<span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 16px; ">当然你发现了，上述的最后一个例子中，或许和你想象的不大一样，\\&#39;不应该转义了么？这种情况下就不就结了。</span></p><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);"><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 16px; ">　　这时我们就可以使用print()函数来输出字符串，这种方式可读性更强。它会把所有转义字符都处理掉。</span></p><p><span class="cnblogs_code_copy" style="margin: 0px; padding: 0px 5px 0px 0px; line-height: 1.5;"><a title="复制代码" style="margin: 0px; padding: 0px; color: rgb(7, 93, 179); text-decoration: underline; border: none !important;"><img src="http://common.cnblogs.com/images/copycode.gif" alt="复制代码" style="margin: 0px; padding: 0px; border: none !important;"/></a></span></p><pre style="margin-top: 0px; margin-bottom: 0px; padding: 0px; white-space: pre-wrap; word-wrap: break-word; font-family: &#39;Courier New&#39;;">&gt;&gt;&gt;&nbsp;print(&#39;&quot;I\\&#39;m&nbsp;Programmer.&quot;I&nbsp;said.&#39;)\r\n&quot;I&#39;m&nbsp;Programmer.&quot;I&nbsp;said.\r\n&gt;&gt;&gt;&nbsp;a&nbsp;=&nbsp;&#39;C++&nbsp;\\n&nbsp;java&#39;\r\n&gt;&gt;&gt;&nbsp;a\r\n&#39;C++&nbsp;\\n&nbsp;java&#39;\r\n&gt;&gt;&gt;&nbsp;print(a)\r\nC++&nbsp;\r\n&nbsp;java</pre><p><span class="cnblogs_code_copy" style="margin: 0px; padding: 0px 5px 0px 0px; line-height: 1.5;"><a title="复制代码" style="margin: 0px; padding: 0px; color: rgb(7, 93, 179); text-decoration: underline; border: none !important;"><img src="http://common.cnblogs.com/images/copycode.gif" alt="复制代码" style="margin: 0px; padding: 0px; border: none !important;"/></a></span></p><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);">&nbsp;</p><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);">&nbsp;<span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 16px; ">　　有时候会输入文件路径，万一输入了c:\\name，岂不是一个很纠结的情况。这就需要在字符串前面加r，防止转义。</span></p><pre style="margin-top: 0px; margin-bottom: 0px; padding: 0px; white-space: pre-wrap; word-wrap: break-word; font-family: &#39;Courier New&#39;;">&gt;&gt;&gt;&nbsp;print(&#39;c:\\name&#39;)\r\nc:\r\name\r\n&gt;&gt;&gt;&nbsp;print(r&#39;c:\\name&#39;)\r\nc:\\name</pre><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);">&nbsp;<span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 16px; ">　　需要打印跨行字符串时，使用&#39;&#39;&#39;....&#39;&#39;&#39;三引号符，在第一个三引号后面加反斜杠。</span></p><p><span class="cnblogs_code_copy" style="margin: 0px; padding: 0px 5px 0px 0px; line-height: 1.5;"><a title="复制代码" style="margin: 0px; padding: 0px; color: rgb(7, 93, 179); text-decoration: underline; border: none !important;"><img src="http://common.cnblogs.com/images/copycode.gif" alt="复制代码" style="margin: 0px; padding: 0px; border: none !important;"/></a></span></p><pre style="margin-top: 0px; margin-bottom: 0px; padding: 0px; white-space: pre-wrap; word-wrap: break-word; font-family: &#39;Courier New&#39;;">&gt;&gt;&gt;&nbsp;print(&#39;&#39;&#39;\\\r\nList&nbsp;of&nbsp;Number:\r\n&nbsp;&nbsp;&nbsp;&nbsp;one\r\n&nbsp;&nbsp;&nbsp;&nbsp;two\r\n&#39;&#39;&#39;)\r\nList&nbsp;of&nbsp;Number:\r\n&nbsp;&nbsp;&nbsp;&nbsp;one\r\n&nbsp;&nbsp;&nbsp;&nbsp;two</pre><p><span class="cnblogs_code_copy" style="margin: 0px; padding: 0px 5px 0px 0px; line-height: 1.5;"><a title="复制代码" style="margin: 0px; padding: 0px; color: rgb(7, 93, 179); text-decoration: underline; border: none !important;"><img src="http://common.cnblogs.com/images/copycode.gif" alt="复制代码" style="margin: 0px; padding: 0px; border: none !important;"/></a></span></p><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);"><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 15px; ">&nbsp;　　接下来讲解一下字符串的连接，使用+加号连接，或者不加符号。另外可以用*乘号表示几个字符串连接。</span></p><pre style="margin-top: 0px; margin-bottom: 0px; padding: 0px; white-space: pre-wrap; word-wrap: break-word; font-family: &#39;Courier New&#39;;">&gt;&gt;&gt;&nbsp;3&nbsp;*&nbsp;&#39;hi&#39;&nbsp;+&nbsp;&#39;,tom&#39;\r\n&#39;hihihi,tom&#39;\r\n&gt;&gt;&gt;&nbsp;&#39;hi&#39;&#39;,tom&#39;\r\n&#39;hi,tom&#39;</pre><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);"><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 15px; ">　　字符串可作为一个数组使用，它的每一个元素便是一个字符。从左边开始的话，第一个元素的索引（index）是0；从右边开始的话，第一个元素的索引是-1。</span></p><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);"><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 15px; ">　　随便一提，-0和0是一个概念。</span></p><p><span class="cnblogs_code_copy" style="margin: 0px; padding: 0px 5px 0px 0px; line-height: 1.5;"><a title="复制代码" style="margin: 0px; padding: 0px; color: rgb(7, 93, 179); text-decoration: underline; border: none !important;"><img src="http://common.cnblogs.com/images/copycode.gif" alt="复制代码" style="margin: 0px; padding: 0px; border: none !important;"/></a></span></p><pre style="margin-top: 0px; margin-bottom: 0px; padding: 0px; white-space: pre-wrap; word-wrap: break-word; font-family: &#39;Courier New&#39;;">&gt;&gt;&gt;&nbsp;word&nbsp;=&nbsp;&#39;Python&#39;\r\n&gt;&gt;&gt;&nbsp;word[0]\r\n&#39;P&#39;\r\n&gt;&gt;&gt;&nbsp;word[2]\r\n&#39;t&#39;\r\n&gt;&gt;&gt;&nbsp;word[-1]\r\n&#39;n&#39;\r\n&gt;&gt;&gt;&nbsp;word[-3]\r\n&#39;h&#39;</pre><p><span class="cnblogs_code_copy" style="margin: 0px; padding: 0px 5px 0px 0px; line-height: 1.5;"><a title="复制代码" style="margin: 0px; padding: 0px; color: rgb(7, 93, 179); text-decoration: underline; border: none !important;"><img src="http://common.cnblogs.com/images/copycode.gif" alt="复制代码" style="margin: 0px; padding: 0px; border: none !important;"/></a></span></p><p style="; ; line-height: 19px; font-size: 13px; font-family: Verdana, Arial, Helvetica, sans-serif; orphans: 2; white-space: normal; widows: 2; background-color: rgb(254, 254, 242);">　　<span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; line-height: 1.5; font-size: 15px; ">在Python中截取字符串，</span></p><p><br/></p>', '2013-06-21 07:23:12', 29, 1, 0, 0, 1, 2, 'uublog', 0, 0, 0, 1, 1, ''),
(2, 0, 0, 2, '传微软欲收购诺基亚 但谈判已破裂', '', '', '发言人称，他们与微软有深度的合作，并且他们之间也经常有常规会谈。而微软发言人则拒绝对此作出评论。谈判破裂归结于价格和诺基亚的战略处境微软和诺基亚谈判破裂的部分原因是诺基亚的价格和其目前处境等问题。是的，在格局上诺基亚不仅落后于苹果和三星，而如今许多亚洲新贵公司在智能手机和其他移动设备上也能迅速获得市场份额。两年多前，微软与诺基亚达成战略合作，诺基亚同意在其智能手机中使用微软独家的操作系统，双方这次', '<p style="word-wrap: break-word; ; ; ; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(255, 255, 255); list-style-type: none; color: rgb(51, 51, 51); font-family: Helvetica, Tahoma, Arial, sans-serif; line-height: 24px;">发言人称，他们与微软有深度的合作，并且他们之间也经常有常规会谈。而微软发言人则拒绝对此作出评论。</p><p style="word-wrap: break-word; ; ; ; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(255, 255, 255); list-style-type: none; color: rgb(51, 51, 51); font-family: Helvetica, Tahoma, Arial, sans-serif; line-height: 24px;"><strong style="word-wrap: break-word; ">谈判破裂归结于价格和诺基亚的战略处境</strong></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(255, 255, 255); list-style-type: none; color: rgb(51, 51, 51); font-family: Helvetica, Tahoma, Arial, sans-serif; line-height: 24px;">微软和诺基亚谈判破裂的部分原因是诺基亚的价格和其目前处境等问题。是的，在格局上诺基亚不仅落后于苹果和三星，而如今许多亚洲新贵公司在智能手机和其他移动设备上也能迅速获得市场份额。</p><p style="word-wrap: break-word; ; ; ; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(255, 255, 255); list-style-type: none; color: rgb(51, 51, 51); font-family: Helvetica, Tahoma, Arial, sans-serif; line-height: 24px;">两年多前，微软与诺基亚达成战略合作，诺基亚同意在其智能手机中使用微软独家的操作系统，双方这次的战略合作被称是美国软件巨头和手机领域先锋间的合作，在这方面双方都取得了重大进展。在达成战略合作后的两年时间，两家公司都很努力试图适应这个消费者偏爱苹果和三星手机的世界，但这次合作至今为止也未能显著提升这两家公司的移动命运。</p><p style="word-wrap: break-word; ; ; ; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(255, 255, 255); list-style-type: none; color: rgb(51, 51, 51); font-family: Helvetica, Tahoma, Arial, sans-serif; line-height: 24px;">诺基亚目前的股价约为3.84美元，较去年同期相比上涨了50％，其市值目前大约为140亿美元，这与历史最高点相比其价值是大幅下滑。对于这次可能会达成的收购，最有利的一个因素是微软可以使用离岸现金达成交易。据悉，微软在一海外的子公司目前大约有660亿美元的储备，但由于面临一大笔税单而最终没有带回美国。</p><p style="word-wrap: break-word; ; ; ; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(255, 255, 255); list-style-type: none; color: rgb(51, 51, 51); font-family: Helvetica, Tahoma, Arial, sans-serif; line-height: 24px;">尽管微软的移动操作系统Windows Phone目前已超越 BlackBerry，成为世界第三大智能手机系统，但它仍旧是在Android激烈的竞争中艰难前行。数据分析机构IDC表示，在今年第一季度Windows Phone出货量占了3.2％的市场份额，而三星、摩托罗拉等其他手机商城搭配Android系统的手机出货量则达到了75％。可以说不论是对诺基亚还是微软而言，他们目前这个战略合作并未达到人们预期想象的高度。（文/张勇 责编/魏兵）</p><p><br/></p>', '2013-06-22 01:13:51', 1, 0, 0, 0, 0, 2, 'uublog', 0, 0, 0, 1, 1, ''),
(3, 0, 0, 2, '如何在django中 执行原始SQL', '', '', '如何在django中 执行原始SQLhttp://www.djangochina.cn/forum.php?mod=viewthread&amp;tid=167&amp;fromuid=2(出处: Django中国|Django中文社区)Django提供两种方式执行(performing)原始的SQL查询：（1）、Manager.raw():执行原始查询并返回模型实例（2）、Executing c', '<p>如何在django中 执行原始SQL</p><p>http://www.djangochina.cn/forum.php?mod=viewthread&amp;tid=167&amp;fromuid=2</p><p>(出处: Django中国|Django中文社区)</p><table cellspacing="0" cellpadding="0" data-find="_4" width="757"><tbody data-find="_3" style="word-wrap: break-word; "><tr data-find="_2" style="word-wrap: break-word; "><td class="t_f" id="postmessage_208" data-find="_1" style="word-wrap: break-word; font-size: 14px; "><br style="word-wrap: break-word; "/>Django提供两种方式执行(performing)原始的SQL查询：<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>（1）、Manager.raw():执行原始查询并返回模型实例<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>（2）、Executing custom SQL directly：直接执行自定义SQL，这种方式可以完全避免数据模型，而是直接执行原始的SQL语句。<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/><span style="word-wrap: break-word; font-weight: 700; ">raw()方法</span><br style="word-wrap: break-word; "/>The raw() manager method can be used to perform raw SQL queries that return model instances:<br style="word-wrap: break-word; "/>　　Manager.raw(raw_query, params=None, translations=None)<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>用法：<ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>&gt;&gt;&gt; for p in Person.objects.raw(&#39;SELECT * FROM Person LIMIT 2&#39;):<br style="word-wrap: break-word; "/></p></li><li><p>...&nbsp; &nbsp;&nbsp;&nbsp;print p<br style="word-wrap: break-word; "/></p></li><li><p>John Smith<br style="word-wrap: break-word; "/></p></li><li><p>Jane Jones</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p>注意，原始SQL里的model，如果在db_table 没有定义，则使用app的名称，后面下划线 后面接模型类的名称,如&quot;Myblog_New&quot;;上面的例子，在定义类的时候已经这样处理了：<ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>Class New(models.Model):<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; ......<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; ......<br style="word-wrap: break-word; "/></p></li><li><p>#自定义表名<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; class Meta:<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;db_table = &#39;New&#39;</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p>2、查询字段隐射到模型字段（Mapping query fields to model fields）<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>raw() automatically maps fields in the query to fields on the model.并且是通过名称来匹配，这意味着我们可以使用SQL子句(clause)<ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>&gt;&gt;&gt; Person.objects.raw(&#39;&#39;&#39;SELECT first AS first_name,<br style="word-wrap: break-word; "/></p></li><li><p>...&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;last AS last_name,<br style="word-wrap: break-word; "/></p></li><li><p>...&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;bd AS birth_date,<br style="word-wrap: break-word; "/></p></li><li><p>...&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;pk as id,<br style="word-wrap: break-word; "/></p></li><li><p>...&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;FROM some_other_table&#39;&#39;&#39;)</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p>返回一个RawQuerySet对象<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>3、索引查找(Index lookups)<ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>first_person = Person.objects.raw(&#39;SELECT * from myapp_person&#39;)[0]<br style="word-wrap: break-word; "/></p></li><li><p>first_person = Person.objects.raw(&#39;SELECT * from myapp_person LIMIT 1&#39;)[0]<br style="word-wrap: break-word; "/></p></li><li><p>#然而,索引和切片不是在数据库级别上执行(除LIMIT外)</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p>4、延迟模型字段（Deferring model fields）<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>Fields may also be left out（left out：忽视，不考虑；被遗忘），这意味着该字段的查询将会被排除在根据需要时的加载。<ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>&gt;&gt;&gt; for p in Person.objects.raw(&#39;SELECT id, first_name FROM myapp_person&#39;):<br style="word-wrap: break-word; "/></p></li><li><p>...&nbsp; &nbsp;&nbsp;&nbsp;print p.first_name, # 这将检索到原始查询<br style="word-wrap: break-word; "/></p></li><li><p>...&nbsp; &nbsp;&nbsp;&nbsp;print p.last_name # 这将检索需求<br style="word-wrap: break-word; "/></p></li><li><p>...<br style="word-wrap: break-word; "/></p></li><li><p>John Smith<br style="word-wrap: break-word; "/></p></li><li><p>Jane Jones</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p>这个例子其实检索了三个字段，一个主键(必需)、一个原始SQL字段、一个需求字段。这里主键字段不能省略，否则会出错，如下：<br style="word-wrap: break-word; "/><img id="aimg_CLmSm" class="zoom" width="600" height="209" file="http://images.cnitblog.com/blog/476998/201305/27114117-a12a23e0f4cb421e83e506c6fd6e0b14.png" border="0" alt="" src="http://images.cnitblog.com/blog/476998/201305/27114117-a12a23e0f4cb421e83e506c6fd6e0b14.png" lazyloaded="true" _load="1" style="word-wrap: break-word; cursor: pointer; "/><br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>5、传递参数(Passing parameters into raw())<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>如果需要执行参数化查询,您可以使用params参数原始()<br style="word-wrap: break-word; "/><ignore_js_op style="word-wrap: break-word; "><p><img id="aimg_79" aid="79" src="http://www.djangochina.cn/data/attachment/forum/201305/27/123618uff54ov5hv55hnfk.png" zoomfile="data/attachment/forum/201305/27/123618uff54ov5hv55hnfk.png" file="data/attachment/forum/201305/27/123618uff54ov5hv55hnfk.png" class="zoom" width="600" inpost="1" lazyloaded="true" _load="1" initialized="true" style="word-wrap: break-word; cursor: pointer; "/></p></ignore_js_op><br style="word-wrap: break-word; "/>注意两点：<br style="word-wrap: break-word; "/>（1）、<br style="word-wrap: break-word; "/><ignore_js_op style="word-wrap: break-word; "><p><img id="aimg_80" aid="80" src="http://www.djangochina.cn/data/attachment/forum/201305/27/123715vw5oj3uuwf7uzdnu.png" zoomfile="data/attachment/forum/201305/27/123715vw5oj3uuwf7uzdnu.png" file="data/attachment/forum/201305/27/123715vw5oj3uuwf7uzdnu.png" class="zoom" width="502" inpost="1" lazyloaded="true" _load="1" initialized="true" style="word-wrap: break-word; cursor: pointer; "/></p></ignore_js_op><br style="word-wrap: break-word; "/>（2）、必须使用[参数]，否则出错：<br style="word-wrap: break-word; "/><ignore_js_op style="word-wrap: break-word; "><p><img id="aimg_81" aid="81" src="http://www.djangochina.cn/data/attachment/forum/201305/27/123735pnsgg0wgzgnlsw05.png" zoomfile="data/attachment/forum/201305/27/123735pnsgg0wgzgnlsw05.png" file="data/attachment/forum/201305/27/123735pnsgg0wgzgnlsw05.png" class="zoom" width="479" inpost="1" lazyloaded="true" _load="1" style="word-wrap: break-word; cursor: pointer; "/></p></ignore_js_op><br style="word-wrap: break-word; "/>（3）、这种方式不对：<ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>Error:<br style="word-wrap: break-word; "/></p></li><li><p>&gt;&gt;&gt; query = &#39;SELECT * FROM myapp_person WHERE last_name = %s&#39; % lname<br style="word-wrap: break-word; "/></p></li><li><p>&gt;&gt;&gt; Person.objects.raw(query)</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p><span style="word-wrap: break-word; font-weight: 700; ">直接执行自定义SQL</span><br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>Manager.raw()远远不够，可直接执行自定义SQL，directly execute UPDATE, INSERT, or DELETE queries.<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>django.db.connection：代表默认的数据库连接<br style="word-wrap: break-word; "/>django.db.transaction：代表默认数据库事务（transaction）<br style="word-wrap: break-word; "/>用database connection调用connection.cursor() 得到一个游标(cursor)对象。<br style="word-wrap: break-word; "/>然后调用cursor.execute(sql, [params])执行SQL<br style="word-wrap: break-word; "/>cursor.fetchone() 或者 cursor.fetchall()：返回结果行<br style="word-wrap: break-word; "/><br style="word-wrap: break-word; "/>如果执行修改操作，则调用transaction.commit_unless_managed()来保证你的更改提交到数据库。<ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>def my_custom_sql():<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; from django.db import connection, transaction<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; cursor = connection.cursor()<br style="word-wrap: break-word; "/></p></li><li><p><br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; # 数据修改操作——提交要求<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; cursor.execute(&quot;UPDATE bar SET foo = 1 WHERE baz = %s&quot;, [self.baz])<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; transaction.commit_unless_managed()<br style="word-wrap: break-word; "/></p></li><li><p><br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; # 数据检索操作,不需要提交<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; cursor.execute(&quot;SELECT foo FROM bar WHERE baz = %s&quot;, [self.baz])<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; row = cursor.fetchone()<br style="word-wrap: break-word; "/></p></li><li><p><br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; return row</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p>django.db.connections：针对使用多个数据库<ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>from django.db import connections<br style="word-wrap: break-word; "/></p></li><li><p>cursor = connections[&#39;my_db_alias&#39;].cursor()<br style="word-wrap: break-word; "/></p></li><li><p># Your code here...<br style="word-wrap: break-word; "/></p></li><li><p>transaction.commit_unless_managed(using=&#39;my_db_alias&#39;)</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p>通常我们不需要手动调用transaction.commit_unless_managed(),我们可以这样做：<ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>@commit_on_success<br style="word-wrap: break-word; "/></p></li><li><p>def my_custom_sql_view(request, value):<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; from django.db import connection, transaction<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; cursor = connection.cursor()<br style="word-wrap: break-word; "/></p></li><li><p><br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; # Data modifying operation<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; cursor.execute(&quot;UPDATE bar SET foo = 1 WHERE baz = %s&quot;, [value])<br style="word-wrap: break-word; "/></p></li><li><p><br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; # Since we modified data, mark the transaction as dirty<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; &lt;span style=&quot;color: #ff0000;&quot;&gt;transaction.set_dirty()&lt;/span&gt;<br style="word-wrap: break-word; "/></p></li><li><p><br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; # Data retrieval operation. This doesn&#39;t dirty the transaction,<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; # so no call to set_dirty() is required.<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; cursor.execute(&quot;SELECT foo FROM bar WHERE baz = %s&quot;, [value])<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&lt;span style=&quot;color: #ff0000;&quot;&gt; row = cursor.fetchone()&lt;/span&gt;<br style="word-wrap: break-word; "/></p></li><li><p><br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; &lt;span style=&quot;color: #ff0000;&quot;&gt;return render_to_response(&#39;template.html&#39;, {&#39;row&#39;: row})<br style="word-wrap: break-word; "/></p></li><li><p>&lt;/span&gt;</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p><span style="word-wrap: break-word; font-weight: 700; ">个人常用：</span><ol style="word-wrap: break-word; margin-left: 10px !important; padding: 0px !important;" class=" list-paddingleft-2"><li><p>def Message(request,msg_id):<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp; &nbsp; &nbsp; where=msg_id<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;sql=&#39;&#39;&#39;<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;select t.id, t.real_name, t2.* from auth_user t join (<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;select max(is_red) as is_red,add_user_id,task_id from oa_red_yellow_card 　　　　　　　where msg_id=%s GROUP BY task_id,add_user_id)<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;t2 ON t2.add_user_id=t.id<br style="word-wrap: break-word; "/></p></li><li><p><br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; &#39;&#39;&#39; %where&nbsp;<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;cursor = connection.cursor()<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;cursor.execute(sql)<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;fetchall = cursor.fetchall()<br style="word-wrap: break-word; "/></p></li><li><p><br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;red_yellow_card=[]<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;for obj in fetchall:<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; dic={}<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; dic[&#39;user_id&#39;]=obj[0]<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; dic[&#39;real_name&#39;]=obj[1]<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; dic[&#39;is_red&#39;]=obj[2]<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; dic[&#39;add_user&#39;]=obj[3]<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; dic[&#39;task_id&#39;]=obj[4]<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; red_yellow_card.append(dic)<br style="word-wrap: break-word; "/></p></li><li><p>&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;context[&#39;red_yellow_card&#39;]=red_yellow_card</p></li></ol><p><span style="word-wrap: break-word; margin-left: 43px; font-size: 12px; cursor: pointer; color: rgb(51, 102, 153) !important;">复制代码</span></p></td></tr></tbody></table><p><a title="如何" href="http://www.djangochina.cn/misc.php?mod=tag&amp;id=54" target="_blank" style="word-wrap: break-word; color: rgb(51, 102, 153); text-decoration: none; ">如何</a></p><p><br/></p>', '2013-06-22 01:14:40', 1, 0, 0, 0, 1, 2, 'uublog', 0, 0, 0, 1, 1, ''),
(4, 0, 0, 2, '中国联通ESS系统，读卡器插件异常，请确认插件是否正确安装', '', '', '中国联通ESS系统，读卡器插件异常，请确认插件是否正确安装', '<p><span style="color: rgb(68, 68, 68); font-family: &#39;Microsoft Yahei&#39;, Hei, Tahoma, SimHei, sans-serif; font-weight: bold; orphans: 2; text-align: -webkit-auto;  widows: 2; background-color: rgb(255, 255, 255);">中国联通ESS系统，读卡器插件异常，请确认插件是否正确安装</span></p>', '2013-06-22 01:15:25', 1, 0, 0, 0, 1, 2, 'uublog', 0, 0, 0, 1, 1, ''),
(5, 0, 0, 2, '：军队要形成团结友爱和谐纯洁的内部关系', '', '', '全军党的群众路线教育实践活动工作会议在京召开　　范长龙许其亮出席　　新华网北京6月21日电（记者李宣良）中共中央总书记、国家主席、中央军委主席习近平日前作出重要指示，强调军队开展党的群众路线教育实践活动，既要贯彻中央统一要求，又要体现自身特点和建设规律，着眼永葆人民军队性质、宗旨、本色，着眼形成和发展团结友爱和谐纯洁的内部关系，着眼促进军队各项工作和建设。要坚决反对形式主义、官僚主义、享乐主义和奢', '<p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;"><strong style="margin: 0px; padding: 0px; list-style: none; border: 0px;">全军党的群众路线教育实践活动工作会议在京召开</strong></p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;"><strong style="margin: 0px; padding: 0px; list-style: none; border: 0px;">　　范长龙许其亮出席</strong></p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　新华网北京6月21日电（记者李宣良）中共中央总书记、国家主席、中央军委主席习近平日前作出重要指示，强调军队开展党的群众路线教育实践活动，既要贯彻中央统一要求，又要体现自身特点和建设规律，着眼永葆人民军队性质、宗旨、本色，着眼形成和发展团结友爱和谐纯洁的内部关系，着眼促进军队各项工作和建设。要坚决反对形式主义、官僚主义、享乐主义和奢靡之风，着力在纠治官兵反映强烈的突出问题上见到成效，在解决深层次矛盾和问题上见到成效，在构建规范化、制度化的长效机制上见到成效，努力从思想上、组织上、作风上为实现党在新形势下的强军目标提供坚强保证。</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　经习主席批准，全军党的群众路线教育实践活动工作会议21日在京召开。会议主要任务是认真贯彻党中央的部署要求，坚决落实习主席和军委决策指示，对全军深入开展党的群众路线教育实践活动进行动员部署。中共中央政治局委员、中央军委副主席范长龙，中共中央政治局委员、中央军委副主席许其亮出席会议并讲话。中央军委委员常万全、房峰辉、赵克石、张又侠、吴胜利、马晓天、魏凤和出席，张阳主持。</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　范长龙强调，贯彻党中央、习主席的决策部署和重要指示，搞好军队的教育实践活动，进一步抓好作风建设，要围绕实现党在新形势下的强军目标，贯彻“照镜子、正衣冠、洗洗澡、治治病”的总要求，突出反对形式主义、官僚主义、享乐主义和奢靡之风这个重点，坚持领导带头、严字当头，标本兼治、综合施策，务求改进作风有新成效，官兵士气高，部队风气正，强军底气足，有效履行军队的使命任务。要深化思想认识，充分认清这次教育实践活动的重大意义，站在听党指挥的高度，树立走在前列的标准，打赢改作风这场硬仗。反对形式主义，要着重解决文山会海、贪图虚名、弄虚作假、工作不实的问题；反对官僚主义，要着重解决对广大官兵的根本态度问题；反对享乐主义，要着重克服贪图享受、及时行乐思想和精神懈怠、不思进取的现象；反对奢靡之风，要着重纠治铺张浪费、挥霍无度、骄奢淫逸的不良风气。要认真贯彻整风精神，敢于较真碰硬，抓正反两方面典型。要以具体管用的制度作保证，对于公务接待、军车管理、建房占房、选人用人、资源管理等，要一项一项研究。要把教育实践活动与部队正在开展的各项工作结合起来，与加强党委班子和干部队伍建设结合起来，聚焦到提高战斗力上，贯穿到以军事斗争准备为龙头的各项工作中，确保部队能经受各种考验，圆满完成各项任务。</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　许其亮指出，各级要坚持用党中央、习主席的决策指示统一思想，充分认清开展教育实践活动是永葆党的性质宗旨的内在要求、是传承我党我军优良传统和作风的现实需要、是推动实现中国梦强军梦的战略之举，切实以强烈的政治责任感，高标准抓好教育实践活动，确保取得党中央、习主席满意，人民群众和广大官兵满意的成效。要紧密结合军队特点和实际，着力增强开展教育实践活动的质量和实效。牢牢把握听党指挥、服务人民这一核心要求，突出抓好中国特色社会主义理论体系武装，抓好马克思主义群众观点和党的群众路线、我军性质宗旨和优良传统教育，强化官兵宗旨意识，从思想根源和灵魂深处坚定信念、铸牢军魂，确保部队绝对忠诚、绝对纯洁、绝对可靠，一切行动听从党中央、中央军委和习主席指挥。以整风精神解决作风上的突出问题，坚决贯彻“照镜子、正衣冠、洗洗澡、治治病”的总要求，突出“四反”整治，以解决问题的实际成效取信官兵。始终把提高战斗力作为根本出发点落脚点，促进军事斗争准备往深里抓往实里抓。构建规范化制度化的长效机制推动形成文化自觉，使为民务实清廉成为每个党员干部的信仰追求。要把开展教育实践活动作为重大政治任务，严格落实党委领导责任，尤其是领导干部要带头参加，勇于纠正自身问题。</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　张阳主持会议时指出，要把习主席和军委的决策指示学习领会好，结合实际把教育实践活动工作部署安排好，把教育实践活动与其他工作统筹兼顾好，把加强组织领导的各项要求认真落实好，推动教育实践活动深入发展。</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　会议以电视电话会议形式举行。四总部、驻京各大单位、军委办公厅领导和全军教育实践活动领导小组成员在主会场参加会议。全军和武警部队军以上单位党委常委、部门领导在分会场参加会议。</p><p><br/></p>', '2013-06-22 01:15:53', 0, 0, 0, 0, 1, 2, 'uublog', 0, 0, 0, 1, 1, ''),
(6, 0, 0, 2, '大火启示录：拯救命悬一线的劳动权益', '', '', '　截止至6月4日早7时30分，吉林省德惠市吉林宝源丰禽业有限公司火灾，已造成120人遇难，70人受伤，事故发生后，企业法人代表已被控制。伤者描述，事发时，车间总计有300余人，工人上班后，车间大多数门都会被锁上。（6月4日 新华社）　　火灾猛于虎——吉林大火，再一次让世人看到了这一点。120人死亡、70人受伤的残酷现实，让无数个家庭陷入地狱般的深渊。虽然当地政府已经成立工作组做好维稳及善后工作，但', '<p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　截止至6月4日早7时30分，吉林省德惠市吉林宝源丰禽业有限公司火灾，已造成120人遇难，70人受伤，事故发生后，企业法人代表已被控制。伤者描述，事发时，车间总计有300余人，工人上班后，车间大多数门都会被锁上。（6月4日 新华社）</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　火灾猛于虎——吉林大火，再一次让世人看到了这一点。120人死亡、70人受伤的残酷现实，让无数个家庭陷入地狱般的深渊。虽然当地政府已经成立工作组做好维稳及善后工作，但是逝去的亡灵不再复活，造成的伤痛无法在短期内抚平。</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　我们不妨来看一下遇难者的身份。虽然当地政府并没有给出火灾发生的具体理由，但是可以肯定，这场火灾发生在了生产车间，死亡者基本都是普通工人。在笔者看来，这样的一场大火，烧出了我国众多普通劳动者的工作常态——车间大门紧锁、工人缺乏逃生训练、现场消防条件乏善可陈、现场没有火灾警报系统、没有自动喷水消防系统……</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　表面上看来，这是防火意识、防火条件的问题。实际上，这反映了我国普通劳动者的生命权益无法受到尊重和保护的现实。1995年实施的《劳动法》第六章是关于“劳动安全卫生”的内容。第五十二条规定，“用人单位必须建立、健全劳动安全卫生制度，严格执行国家劳动安全卫生规程和标准，对劳动者进行劳动安全卫生教育，防止劳动过程中的事故”；第五十三条规定，“劳动安全卫生设施必须符合国家规定的标准。”因此，我们有必要问一问当地政府，这家企业为什么没有按这样的标准进行消防配备？为什么没有对劳动者进行“安全教育”？当地劳动部门有没有进行负责任的监管？</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　作为“世界工厂”，如果对于劳动密集产业的安全监管不够，对于劳动者的权益尤其是生命权利不够尊重，则难免会产生惨烈的事故。而出事之后，政府不仅要将企业负责人和政府监管者进行问责，要对受害人及其家属进行到位和及时的赔偿，更要从根本上提高劳动者的权益、尊严和地位，让他们不再工作于命悬一线的危险车间。</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　关于立法进行权益保护，美国的三角内衣大火或许能够给我们一些启示。1911年3月25日，是美国纽约市历史上最大的工业灾难——三角内衣工厂火灾，火灾导致146名服装工人被烧死或因被迫跳楼致死。这也是纽约市2001年911事件之前最严重的工作场所的灾难。灾难的发生，促进了美国《劳动法》的通过实施。在1912年的美国《劳动法》之中，我们看到了这样的详细规定：工作场所每3个月就必须进行一次防火训练；在7层以上超过200名工作人员的楼层，必须安装自动防火喷淋系统；雇员超过25名的工作场所，都必须安装自动报警系统……这些在100年前的美国《劳动法》就已经出现的劳动权益保护规定，值得我们学习。</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　生命的价值重于财富——这是以人为本时代里，最需要普及的常识性价值理念。流水线的劳动者，不是机器，而是人。而人的生命价值是无法衡量的，是最宝贵的。而维护生命的尊严，只处理企业相关责任人，或是问责负责安全生产监管和劳动权益保护的官员，都是不够的。只有从用法律的方式去规范企业和安全生产行为，才可能改变劳动者的弱势地位，让劳动者有尊严的工作，让劳动者的生命不再为草芥。</p><p><br/></p>', '2013-06-22 01:16:20', 1, 0, 0, 0, 1, 2, 'uublog', 0, 0, 0, 1, 1, '');
INSERT INTO `blog_article` (`id`, `channel1_id`, `channel2_id`, `category_id`, `title`, `pic`, `tags`, `summary`, `content`, `createtime`, `views`, `comments`, `goods`, `bads`, `status`, `user_id`, `username`, `ishome`, `isrecommend`, `istop`, `isoriginal`, `cancomment`, `password`) VALUES
(7, 2, 0, 2, '张东健安七炫朴海镇 来中国捞金的韩男星/图', '', '', '张东健曾是韩国第一小生　　张东健，韩国著名男演员，顶级韩流明星。1992年参加韩国MBC电视台第21期演员培训班出道。出道以来演出多部影视作品，并凭借电视剧《天桥风云》《夏娃的诱惑》等风靡全亚洲。2004年凭借电影《太极旗飘扬》获得韩国电影青龙奖最佳男主角奖，这还使他成为青龙奖有史以来得到男演员类所有奖项大满贯的第一人。2010年5月2日张东健与演员高素荣结婚，2010年10月4日张东健喜得贵子。', '<p style="text-align:center;; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;"><img alt="" src="http://pinglun.youth.cn/wywy/wysh/201306/W020130621373075210333.jpg" oldsrc="W020130621373075210333.jpg" style="margin: 0px; padding: 0px; list-style: none; border: 0px;"/></p><p style="text-align:center;; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">张东健曾是韩国第一小生</p><p style="; ; ; list-style: none; border: 0px; font-family: &#39;Times New Roman&#39;; font-size: 14px; line-height: 28px; color: rgb(51, 51, 51); orphans: 2; white-space: normal; widows: 2;">　　张东健，韩国著名男演员，顶级韩流明星。1992年参加韩国MBC电视台第21期演员培训班出道。出道以来演出多部影视作品，并凭借电视剧《天桥风云》《夏娃的诱惑》等风靡全亚洲。2004年凭借电影《太极旗飘扬》获得韩国电影青龙奖最佳男主角奖，这还使他成为青龙奖有史以来得到男演员类所有奖项大满贯的第一人。2010年5月2日张东健与演员高素荣结婚，2010年10月4日张东健喜得贵子。2012年时隔12年重返小银幕 ，以韩国SBS TV新剧《绅士的品格》中的&quot;毒舌&quot;金道振形象回归。</p><p><br/></p>', '2013-06-22 01:16:47', 4, 0, 0, 0, 1, 2, 'uublog', 0, 0, 0, 1, 1, ''),
(8, 2, 0, 2, 'Windows 8.1最新版Build 9428曝光', '', '', '今天，一张名为 Windows 8.1 Milestone Preview 的截图出现在网上，如果图片并非伪造，那它就可能是微软将于 6 月 26 日发布的 Windows 8.1 公开预览版（也就是 Beta 公测版）。　　从截图中可以看到，Windows 8.1 Milestone Preview 的具体版本为 Build 9428，编译于 6 月 12 日。早在 5 月份就有传言称，Wind', '<p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); font-family: Verdana, Arial, Helvetica, sans-serif;">今天，一张名为 Windows 8.1 Milestone Preview 的截图出现在网上，如果图片并非伪造，那它就可能是微软将于 6 月 26 日发布的 Windows 8.1 公开预览版（也就是 Beta 公测版）。</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160229-c9974ebdc8f14c61b1b6b67f23382c7c.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); font-family: Verdana, Arial, Helvetica, sans-serif;">　　从截图中可以看到，Windows 8.1 Milestone Preview 的具体版本为 Build 9428，编译于 6 月 12 日。早在 5 月份就有传言称，Windows 8.1 公开预览版将选定 Build 9428，若此截图为真，那么上述传言就比较可信了。</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160228-9b4743c8ac6f4f1ca12694b88e595d81.jpg" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　还有几张应用程序的截图：</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160229-96b626131d1848b18403ef2836433f81.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　天气</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160229-9ef9f093af4c45b8ac66cc8845a005cb.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　计算器</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160228-4a54f0238df743c3bceb6af065bf455b.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　Movie Moments 电影时光</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160229-7e0b08c652764ebab8586b189e99e8d1.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　录音</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160229-a8780936da844105936d150f37cfc239.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　录音</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160229-40268b0a3bd64df990c69fd99375232f.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　闹钟</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160229-2c92a647a39145dd8ab64f9a9993c15e.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　Windows Store</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160230-64c2edf1ffa74c7db809ca9fef07854a.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　Windows Store 中的 Skype</p><p style="text-align:center;word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64);  font-family: Verdana, Arial, Helvetica, sans-serif;"><img alt="Windows 8.1 最新版 Build 9428 曝光" src="http://images.cnitblog.com/news/66372/201306/19160230-1a0996eb73e24612b7cc2ddd73fe2fac.png" style="word-wrap: break-word; max-width: 620px; border-style: none; padding: 0px; margin: 0px; line-height: 1.5em;"/></p><p style="word-wrap: break-word; ; ; ; font-size: 14px; line-height: 25px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(250, 250, 250); color: rgb(64, 64, 64); text-align: center; font-family: Verdana, Arial, Helvetica, sans-serif;">　　Windows Store 中的 Skype</p><p><br/></p>', '2013-06-22 01:17:26', 7, 1, 0, 0, 1, 2, 'uublog', 0, 0, 0, 1, 1, ''),
(9, 1, 1, 2, '创造别人想要的东西（1）----创业的本质', '', '', '　创业的本质是从自己出发，从身边的朋友出发，深度了解用户，发现用户的潜需求，做出一款满足用户刚需的产品或者服务。　　一个创业公司想要成功，必要条件（甚至可以说是充要条件）是它能够为人们提供人们想要的东西。这听起来是一个显而易见，无需赘述的道理，但却是创业公司经常没有充分考虑的问题。大张旗鼓，轰轰烈烈的创业，最终却做出了一些没人想要的产品，这样的例子在中外都常见。　　举个例子，Webvan，1999', '<p style=";"><strong>　<span style="background-color: rgb(128, 0, 128); color: rgb(255, 255, 255); font-size: 18pt; ">创业的本质</span></strong><span style="font-size: 15px; ">是从自己出发，从身边的朋友出发，深度了解用户，发现用户的潜需求，做出一款满足用户刚需的产品或者服务。</span></p><p style=";"><span style="font-size: 15px; ">　　一个创业公司想要成功，必要条件（甚至可以说是充要条件）是它能够为人们提供人们想要的东西。这听起来是一个显而易见，无需赘述的道理，但却是创业公司经常没有充分考虑的问题。大张旗鼓，轰轰烈烈的创业，最终却做出了一些没人想要的产品，这样的例子在中外都常见。</span></p><p style=";"><span style="font-size: 15px; ">　　举个例子，Webvan，1999年在加州创立的线上杂货（grocery）销售网站，在融资额高达12亿美金之后，2001年宣告破产！这被证明<strong><span style="background-color: rgb(255, 255, 255); color: rgb(0, 0, 255); ">至少在当时不是一个人们需要的服务</span></strong>。</span></p><p style=";"><span style="font-size: 15px; ">　　创业是艰辛的，从产品设计，到技术实现，到上线，到运营，到营销，到融资，再到面对媒体。</span></p><p style=";"><span style="font-size: 15px; ">　　我以前在的公司就是一个例子，购物搜索，比价，情感挖掘，让用户更便捷的买到自己的宝贝，09年就萌发的想法，时间远远超前于一淘，涉及到技术也比较前沿，但最后成就了一款没用户量的产品，失败在哪里？我个人觉得是在运营。工作几年后发现，发现运营真心重要。</span></p><p style=";">&nbsp;</p><p style=";">　　<span style="font-size: 18pt; "><strong><span style="background-color: rgb(128, 0, 128); color: rgb(255, 255, 255); ">困难</span></strong></span><span style="font-size: 15px; ">是多重的，创造出别人需要的东西，不是一件简单的事情。单单从统计数字上看，大多数创业公司是失败的。华尔街日报曾有报道，3/4的创业公司连投资者的本钱都无法挣回来。找到别人生活中存在的某个问题或者某种需求，然后（用技术手段）创造一个产品或服务将其解决。很多创业者就是这么想的。但实际上，<span style="color: rgb(0, 0, 255); "><strong>发现一个真正的问题，是比找到解决方法，是更有难度的事情</strong></span>。创造新的东西本就是在摸索未知。一次一次的迭代想法，通过数据分析，通过调查，来改进自己的产品服务。</span></p><p style=";"><span style="font-size: 15px; ">　　<span style="color: rgb(0, 0, 255); "><strong>创造者面临的另一个困难是，而真正巨大的需求，往往因为我们所处时代的局限而不能够被察觉</strong></span>。试想我们回到5年前，调研当时的互联网用户，恐怕还没有人会觉得有接收来自不相识的人140个字微博的需求。回想06年左右，Youtube公司于2005年2月15日注册，世界最大的视频分享网站，表现你自己，show出你的风采，你很难理解发现几年后，视频行业这么火。淘宝网2003年成立，你也很难相信你可以在网上与不见面老板进行买卖，这种信用机制在当时很难想象，而现在一天一亿次的亲，也改变了用户的购物习惯。</span></p><p data-find="_9" style=";"><span data-find="_8" style="font-size: 15px; ">　　<strong><span style="color: rgb(0, 0, 255); ">雪上加霜的是</span></strong>，对于天朝互联网界来说，更有一个值得担忧的传统。天朝的互联网行业发展几十年，很长时间一直处在追赶美国的硅谷。形成了一个C2C (copy to China) 的传统。最早一批成功的互联网公司也往往是复制美国已经成型的模式，包括实时通信工具，到搜索引擎，到门户网站。C2C带来了快速成功的可能，但是培养了很多人的思考习惯：更多在关注其他市场的成功案例，而忽略了手边客户的需求。比如视频行业，优酷土豆爱奇艺56酷6模仿youtube，百度搜搜360模仿谷歌，花瓣美丽说蘑菇街模仿pinterest，腾腾讯模仿qicq，知乎模仿quora，人人网模仿facebook但越走越偏，等等，这就是中国的悲剧，从来都是一个没有创意的国度，而模仿能力超级强。让我想起了中国教育，爱国爱社会，从小的洗脑，学微积分却不知道到底有毛用，就tmd知道解题，现在还是不太懂它的来历它到底在那些方面实现了它的价值，从小的教育培养了独特变态的你，这是应试教育的悲哀！</span></p><p style=";"><span style="font-size: 15px; ">　　<span style="color: rgb(0, 0, 255); "><strong>要敢于革自己的命</strong></span>，敢于回避知道的风险赶紧业务转型，敢于不吃老底而一次次的迭代变革自己的产品，在变革中成就自己。想想曾经的暴风影音，现在远没有前几年火了，想想网际快车，不知道还有几个人记得？想想电驴，我已经很久没上电驴了。想想人人网，至少2年没登陆过了。曾经风光无限的开心网，正在被遗忘。还有猫扑，不上了不玩了。怎么让自己的产品接地气，怎么让在残酷的竞争中杀出一条血路。</span></p><p style=";"><span style="font-size: 15px; ">　　中国内互联网企业的厮杀也异常激烈，大企业瞬间复制模仿你，秒杀你，2004年9月，QQ游戏平台将联众赶下了中国第一休闲游戏门户的宝座。我记得那个时候室友还在上面玩游戏，现在联众早已被网民遗忘，以至于记得当时的新闻是，&quot;多年以后，在北京知春路的一家咖啡馆，联众创始人鲍岳桥谈起当年腾讯对联众的围剿和逼迫，仍然耿耿于怀。在两个小时的采访中，他连续抽了两包烟&quot;。2006年底，鲍岳桥离开了江河日下的联众，成为了一名天使投资人。他告诉记者，现在他做投资的原则之一就是：<span style="color: rgb(0, 0, 255); "><strong>只做腾讯不会做、不能做的项目，</strong></span><span style="color: rgb(0, 0, 255); "><strong>别让腾讯盯上</strong></span>。腾讯，都是山寨。</span><em><br/></em></p><p style=";">&nbsp;</p><p style=";">　　<span style="background-color: rgb(128, 0, 128); color: rgb(255, 255, 255); font-size: 18pt; "><strong>己之所欲，可施于人</strong></span><span style="font-size: 15px; ">，我想说的是“实践是检验真理的唯一标准”。一个产品或者服务，是否是人们所要的，唯有试了才知道。逻辑的分析，其他市场，其他人的成功，只能作为一个维度或者指标来评判对产品的一个估计。从你自己的需求出发，你可以保证至少这个需求是确实存在，而不是你臆想出来。你有的问题，很有可能很多人都有。所谓”己之所欲，可施于人“。很多伟大的公司都如此诞生：苹果公司是因为 Steve Wozniak 自己想要一台个人电脑，Dropbox是因为Drew Houston 厌烦了每天拿着优盘，hotmail是几位程序员需要更方便的查自己的邮箱，Ben Silbermann 为他的女朋友寻找订婚戒指之时。他发现了很多还算中意的戒指，但又需要反复比较，于是他就开发了 Pinterest，把它们随手贴在同一个页面上。</span></p><p style=";"><span style="font-size: 15px; ">　　仅仅作为一个尝试，想想你能够简单快速的做出什么来，满足你自己的需求，进而满足别人的需求。也许，下一个让用户疯狂的产品就在从你这里诞生！轻松自己，轻松世界，改变自我，影响世界。</span></p><p style=";">　　<span style="font-size: 15px; ">本文参考网易公开课百科青年第二期峰哥的文章进行润色整理，</span><span style="font-size: 15px; ">欢迎微博互粉<span style="background-color: rgb(255, 255, 255); color: rgb(255, 0, 0); ">&nbsp;<strong>@板栗小羊</strong></span></span></p><p style=";">　　<img src="http://images.cnitblog.com/blog/388574/201306/22122557-6d04810b636748779ec95c84406b9592.jpg" alt="" style="border-top-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px; border-style: initial; border-color: initial; border-image: initial; "/></p><p>分类:&nbsp;<a href="http://www.cnblogs.com/banli/category/479394.html" style="color: rgb(0, 102, 255); text-decoration: none; ">视野扩展</a></p><p><br/></p>', '2013-06-22 05:02:38', 9, 2, 0, 0, 1, 2, 'uublog', 0, 0, 0, 1, 1, ''),
(10, 2, 0, 1, '普林斯顿大学算法公开课（1）----介绍', '', '', '课程概况这个课程是什么？（1）中级研究课程。（2）编程解决问题。（3）算法：解决问题的思路方法。（4）数据结构：存储信息的方法。课程分为两个部分为什么学习算法？算法的影响力是宽广和深远的。影响的领域不完全列表如下。（1）网络。包括搜索，包路由，分布式共享文件。（2）生物。包括基因工程，蛋白质折叠。（3）计算机。电路草图，文件系统，编译器。（4）计算机图形图像。电影，电子游戏，虚拟现实。（5）安全。', '<p style=";"><span style="font-size: 14px; background-color: rgb(0, 51, 0); color: rgb(255, 255, 255); "><strong>课程概况</strong></span></p><p style=";"><strong><span style="font-size: 14px; ">这个课程是什么？</span></strong></p><p style=";"><span style="font-size: 14px; ">（1）中级研究课程。</span></p><p style=";"><span style="font-size: 14px; ">（2）编程解决问题。</span></p><p style=";"><span style="font-size: 14px; ">（3）算法：解决问题的思路方法。</span></p><p style=";"><span style="font-size: 14px; ">（4）数据结构：存储信息的方法。</span></p><p style=";"><strong><span style="font-size: 14px; ">课程分为两个部分</span></strong></p><p style=";"><span style="font-size: 14px; "><img src="http://images.cnitblog.com/blog/388574/201306/16184114-f1d82ba5e5a244d7862a413ed6a2a5a7.jpg" alt="" width="666" height="321" style="border-top-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px; border-style: initial; border-color: initial; border-image: initial; "/></span></p><p style=";"><span style="font-size: 14px; background-color: rgb(0, 51, 0); color: rgb(255, 255, 255); "><strong>为什么学习算法？</strong></span></p><p style=";"><strong><span style="font-size: 14px; ">算法的影响力是宽广和深远的。影响的领域不完全列表如下。</span></strong></p><p style=";"><span style="font-size: 14px; ">（1）网络。包括搜索，包路由，分布式共享文件。</span></p><p style=";"><span style="font-size: 14px; ">（2）生物。包括基因工程，蛋白质折叠。</span></p><p style=";"><span style="font-size: 14px; ">（3）计算机。电路草图，文件系统，编译器。</span></p><p style=";"><span style="font-size: 14px; ">（4）计算机图形图像。电影，电子游戏，虚拟现实。</span></p><p style=";"><span style="font-size: 14px; ">（5）安全。手机，电子商务，投票计算机。</span></p><p style=";"><span style="font-size: 14px; ">（6）多媒体。mp3，jpg，divx，hdtv，人脸识别。</span></p><p style=";"><span style="font-size: 14px; ">（7）社会网络。推荐系统，新闻feeding，广告学。</span></p><p style=";"><span style="font-size: 14px; ">（8）物理学。n体模拟，粒子碰撞模拟。</span></p><p style=";"><strong><span style="font-size: 14px; ">针对个人，公司，学习算法有什么好处？</span></strong></p><p style=";"><span style="font-size: 14px; ">（1）智力激发。</span></p><p style=";"><span style="font-size: 14px; ">（2）成为高效的程序员。</span></p><p style=";"><span style="font-size: 14px; ">（3）揭开宇宙中生活的秘密。</span></p><p style=";"><span style="font-size: 14px; ">（4）为了乐趣和利润。</span></p><p style=";"><span style="background-color: rgb(0, 51, 0); color: rgb(255, 255, 255); "><strong><span style="font-size: 14px; ">资源</span></strong></span></p><p style=";"><span style="font-size: 14px; ">textbook，<a href="http://pan.baidu.com/share/link?shareid=4082772650&amp;uk=2483086068" style="color: rgb(0, 102, 255); text-decoration: none; ">http://algs4.cs.princeton.edu/home/</a></span></p><p style=";"><span style="font-size: 14px; ">公开课的视频和课件可以从我的百度网盘下载，<a href="http://pan.baidu.com/share/link?shareid=4082772650&amp;uk=2483086068" style="color: rgb(0, 102, 255); text-decoration: none; ">http://pan.baidu.com/share/link?shareid=4082772650&amp;uk=2483086068</a></span></p><p style=";"><strong><span style="background-color: rgb(255, 0, 0); color: rgb(255, 255, 255); ">今天是父亲节，祝福所有的程序员爸爸和程序员的爸爸节日快乐！</span></strong></p><p style=";"><img src="http://images.cnitblog.com/blog/388574/201306/16191903-7ce1f92c0cc74dc6a41e8deb9daef5e1.jpg" alt="" style="border-top-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px; border-style: initial; border-color: initial; border-image: initial; "/>　</p><p>分类:&nbsp;<a href="http://www.cnblogs.com/banli/category/479395.html" style="color: rgb(0, 102, 255); text-decoration: none; ">算法研究</a></p><p><br/></p>', '2013-06-22 05:03:09', 3, 0, 0, 0, 1, 2, 'uublog', 1, 1, 0, 1, 1, ''),
(11, 1, 0, 2, '第一次当面试官', '', '', '　今天第一面试别人，感觉还行，大概80分钟的样子结束了我的第一次，其实还是蛮长。应该有80*60/12多雷。　　以前都是别人面试我，这次终于也当了一次面试官。这次才真正体会到，其实面试官有时候可能比求职者，要付出更多时间来准备面试。面试官要根据简历的情况，来准备面试题目，要在短短的几十分钟内，还是需要面试官根据面试情况来调整面试题目等，以最短的时间获得准确的信息，了解一个人，其实很多时候还是看感觉', '<p style=";"><span style="font-family: 宋体; font-size: 15px; ">　今天第一面试别人，感觉还行，大概80分钟的样子结束了我的第一次，其实还是蛮长。应该有80*60/12多雷。</span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; ">　　以前都是别人面试我，这次终于也当了一次面试官。这次才真正体会到，其实面试官有时候可能比求职者，要付出更多时间来准备面试。面试官要根据简历的情况，来准备面试题目，要在短短的几十分钟内，还是需要面试官根据面试情况来调整面试题目等，以最短的时间获得准确的信息，了解一个人，其实很多时候还是看感觉的。</span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; ">　　前几天看了下<span style="color: rgb(255, 0, 0); "><span style="color: rgb(0, 0, 255); ">@左耳朵耗子</span></span>博客上的关于面试的几篇文章，收获到很多干货。其实面试的目标是想获得下面三件事情：</span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; ">　　（1）<span style="line-height: 22px; background-color: rgb(255, 255, 255);">这个</span><span style="line-height: 22px; background-color: rgb(255, 255, 255);">程序员的是否够聪明？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（2）</span><span style="line-height: 22px; background-color: rgb(255, 255, 255);">这个程序员能否把事情搞定？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（3）</span><span style="line-height: 22px; background-color: rgb(255, 255, 255);">这个程序员能和我的团队在一起工作吗？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　我的处女面试大概分下面几个步骤：</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　<span style="color: rgb(255, 0, 0); ">　<strong>开场</strong></span></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　我是XX的工程师，很高兴由我来和你聊聊技术，聊聊项目等，其实我也是第一次面试别人，可能我比你还紧张，所以也不用太紧张太严肃。Ok，我们开始！</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　<strong><span style="color: rgb(255, 0, 0); ">针对简历上提到的项目经验</span></strong></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（1）根据详细问项目怎么做的，具体细节等，第一来考察求职者是不是真参与了这个项目。</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（2）明白项目的用途，场景，或者指标等，做这个项目，哪里没做好，那些地方还有优化之处。　</span></span></p><p style=";"><span style="color: rgb(255, 0, 0); font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　<strong>　针对简历上提到的技能</strong></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　这里针对“熟悉hadoop”来提的几个问题</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（1）<span style="color: rgb(0, 0, 0); line-height: normal;">setMapOutputKeyClass</span>和<span style="color: rgb(0, 0, 0); line-height: normal;">setOutputKeyClass</span>的区别？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（2）<span lang="EN-US" style="color: rgb(0, 0, 0); line-height: 26px;">Combiner</span><span style="color: rgb(0, 0, 0); line-height: 26px;">的作用？partition的作用？</span></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);"><span style="color: rgb(0, 0, 0); line-height: 26px;">　　（3）setup和cleanup函数的用途？</span></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; ">　　（4）mapreduce的流程？具体讲下shuffle的细节？</span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; ">　　（5）hadoop的二次排序，代码上大概应该怎么写？具体内部原理是什么？</span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　<span style="color: rgb(255, 0, 0); "><strong>　针对面试的职位</strong></span></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　针对面试的岗位需要的技能面试，这里会针对数据挖掘面试一些基本知识。</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（1）knn，k-means，svm关联规则等的一些知识。</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（2）tf-idf的概念。</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><strong><span style="color: rgb(255, 0, 0); "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　算法</span></span></strong></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　这里会出几个大数据的算法，几个可以引导求职者一起攻克的循环更新的面试题。</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（1）快速从几亿个宝贝中找出今天点击量最大的top100个宝贝。</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（2）hashmap的内部实现原理？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　<span style="color: rgb(255, 0, 0); "><strong>产品</strong></span></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);"><strong>　　</strong>（1）你觉得你现在做的产品那些地方，不管是ui，还是交互，还是算法上，有那些可以改进的？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（2）你觉得我们这的产品，那些地方设计的不够人性化，影响了用户体验的？哪些功能有些badcace？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（3）说一下你经常用的一个app中，优秀的设计和需要改进的地方？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　<span style="color: rgb(255, 0, 0); "><strong>工作态度</strong></span></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（1）为什么换工作？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（2）工作几年来，有什么心得感悟和恼火的经历？</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　<strong><span style="color: rgb(255, 0, 0); ">　面试者提问</span></strong></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（1）对我们团队，对我们公司，有什么需要，或者感兴趣想了解的？</span></span></p><p style=";"><span style="color: rgb(255, 0, 0); font-size: 15px; "><strong><span style="font-family: 宋体; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　结尾</span></span></strong></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　<span style="color: rgb(0, 0, 0); line-height: normal;">OK，那就先到这里，如果有后续面试的话，再通知你。拜拜。</span></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　<span style="color: rgb(255, 0, 0); "><strong>面试别人的收获总结：</strong></span></span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　（1）在面试的过程中，不断穿插聊天方式的打断，来easy求职者，使得整个面试不那么严肃，就像同事之间的聊天，一个问题的解决探讨，这样才能让面试者发挥正常，也能让面试官更全面容易的了解求职者。我现在穿插的方式问一些平常有什么爱好，玩游戏嘛，玩dota吗，我们这经常和老大一起玩，老家哪里的等。</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　我的第一次面试，还是很粗糙，需要完善的地方好多，希望自己和求职者一起进步！也希望其他<span style="color: rgb(0, 0, 255); ">博友</span>能给我一些建议和经验之谈。谢谢。</span></span></p><p style=";"><span style="font-family: 宋体; font-size: 15px; "><span style="line-height: 22px; background-color: rgb(255, 255, 255);">　　<img src="http://images.cnitblog.com/blog/388574/201305/13234303-25bbf3100b9443938d4f8f8c5d6adade.jpg" alt="" style="border-top-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px; border-style: initial; border-color: initial; border-image: initial; "/></span></span></p><p>分类:&nbsp;<a href="http://www.cnblogs.com/banli/category/479394.html" style="color: rgb(0, 102, 255); text-decoration: none; ">视野扩展</a></p><p><br/></p>', '2013-06-22 05:03:49', 37, 1, 0, 0, 1, 2, 'uublog', 1, 0, 0, 1, 1, '');
INSERT INTO `blog_article` (`id`, `channel1_id`, `channel2_id`, `category_id`, `title`, `pic`, `tags`, `summary`, `content`, `createtime`, `views`, `comments`, `goods`, `bads`, `status`, `user_id`, `username`, `ishome`, `isrecommend`, `istop`, `isoriginal`, `cancomment`, `password`) VALUES
(12, 1, 1, 2, 'Python的静态方法和类成员方法', '', '', 'Python的静态方法和类成员方法都可以被类或实例访问，两者概念不容易理清，但还是有区别的：1）静态方法无需传入self参数，类成员方法需传入代表本类的cls参数；2）从第1条，静态方法是无法访问实例变量的，而类成员方法也同样无法访问实例变量，但可以访问类变量；3）静态方法有点像函数工具库的作用，而类成员方法则更接近类似Java面向对象概念中的静态方法。&nbsp;实现静态方法和类方法的两种方式一', '<p>Python的静态方法和类成员方法都可以被类或实例访问，两者概念不容易理清，但还是有区别的：</p><p>1）静态方法无需传入self参数，类成员方法需传入代表本类的cls参数；</p><p>2）从第1条，静态方法是无法访问实例变量的，而类成员方法也同样无法访问实例变量，但可以访问类变量；</p><p>3）静态方法有点像函数工具库的作用，而类成员方法则更接近类似Java面向对象概念中的静态方法。</p><p>&nbsp;</p><p><strong style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; ">实现静态方法和类方法的两种方式</strong></p><p><strong style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; ">一、在Python 2.3及之前，用staticmethod和classmethod类型对象包装实现</strong></p><p>例子如下（注意print里的说明）：</p><p>class MyClass:<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&nbsp;&nbsp;&nbsp;&nbsp;val1 = &#39;Value 1&#39;<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&nbsp;&nbsp;&nbsp;&nbsp;def __init__(self):<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.val2 = &#39;Value 2&#39;<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&nbsp;&nbsp;&nbsp;&nbsp;def staticmd():<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print &#39;静态方法，无法访问val1和val2&#39;<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&nbsp;&nbsp;&nbsp;&nbsp;smd = staticmethod(staticmd)<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/><br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&nbsp;&nbsp;&nbsp;&nbsp;def classmd(cls):<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print &#39;类方法，类：&#39; + str(cls) + &#39;，val1：&#39; + cls.val1 + &#39;，无法访问val2的值&#39;<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&nbsp;&nbsp;&nbsp;&nbsp;cmd = classmethod(classmd)<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/><br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/></p><p><strong style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; ">执行：</strong></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&gt;&gt;&gt;&nbsp;mc = MyClass()<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&gt;&gt;&gt;&nbsp;mc.smd()<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&gt;&gt;&gt;&nbsp;mc.cmd()<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&gt;&gt;&gt;&nbsp;MyClass.smd()<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&gt;&gt;&gt;&nbsp;MyClass.cmd()</span></p><p>&nbsp;</p><p><strong style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; ">二、在Python 2.4及之后，用装饰器（decorators）实现</strong></p><p>装饰器使用@操作符，例子如下：</p><p>class MyClass:<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&nbsp;&nbsp;&nbsp;&nbsp;val1 = &#39;Value 1&#39;<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&nbsp;&nbsp;&nbsp;&nbsp;def __init__(self):<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.val2 = &#39;Value 2&#39;<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/><br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&nbsp;&nbsp;&nbsp;&nbsp;@staticmethod<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&nbsp;&nbsp;&nbsp;&nbsp;def staticmd():<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print &#39;静态方法，无法访问val1和val2&#39;<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/><br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&nbsp;&nbsp;&nbsp;&nbsp;@classmethod<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&nbsp;&nbsp;&nbsp;&nbsp;def classmd(cls):<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print &#39;类方法，类：&#39; + str(cls) + &#39;，val1：&#39; + cls.val1 + &#39;，无法访问val2的值&#39;<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/><br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/></p><p><strong style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; ">不管是以上两种方式中的哪一种，执行情况都是一样的，以方式二执行结果</strong><strong style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; ">为例</strong><strong style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; ">分析如下：</strong></p><p>执行：</p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&gt;&gt;&gt;&nbsp;mc = MyClass() &nbsp;# 实例化</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; "><br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&gt;&gt;&gt;&nbsp;mc.staticmd()&nbsp;&nbsp;# 实例调用静态方法，无法访问实例变量val1和val2</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&gt;&gt;&gt;&nbsp;<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>静态方法，无法访问val1和val2</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&nbsp;</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&gt;&gt;&gt;&nbsp;mc.classmd()&nbsp;&nbsp;# 实例调用类方法，注意，这里访问的是类MyClass的变量val1的值，不是实例化后mc的实例变量val1，这里容易混淆，往下看就会明白。val2一直是实例变量，所以无法访问</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&gt;&gt;&gt;&nbsp;</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">类方法，类：__main__.MyClass，val1：Value 1，无法访问val2的值<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/><br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/></span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&gt;&gt;&gt;&nbsp;MyClass.staticmd()&nbsp;&nbsp;# 类直接调用静态方法，结果同上面的实例调用，无论是类变量还是实例变量都无法访问</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&gt;&gt;&gt;&nbsp;<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>静态方法，无法访问val1和val2</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&nbsp;</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&gt;&gt;&gt;&nbsp;MyClass.classmd()&nbsp;&nbsp;# 类直接调用类方法，结果同上面的实例调用</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&gt;&gt;&gt;&nbsp;</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">类方法，类：__main__.MyClass，val1：Value 1，无法访问val2的值</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&nbsp;</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&gt;&gt;&gt;&nbsp;mc.val1 = &#39;Value changed&#39; &nbsp;# 改变实例变量val1的值<br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/><br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/></span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&gt;&gt;&gt;&nbsp;mc.classmd()&nbsp;&nbsp;# 实例调用类方法，注意到cls.val1的值没变，所以，这时的cls.val1是类变量val1，而非实例变量val1</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&gt;&gt;&gt;&nbsp;</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">类方法，类：__main__.MyClass，val1：Value 1，无法访问val2的值</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; "><br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&gt;&gt;&gt;&nbsp;MyClass.classmd() &nbsp;# 类直接调用类方法，结果同上面的实例调用</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&gt;&gt;&gt;&nbsp;</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">类方法，类：__main__.MyClass，val1：Value 1，无法访问val2的值</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&nbsp;</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&gt;&gt;&gt;&nbsp;MyClass.val1 = &#39;Class Value changed&#39;&nbsp;&nbsp;# 改变类变量val1的值</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; "><br style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; "/>&gt;&gt;&gt;&nbsp;mc.classmd()&nbsp;&nbsp;# 实例调用类方法，注意到cls.val1的值变了，所以，进一步证明了这时的cls.val1是类变量val1，而非实例变量val1</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&gt;&gt;&gt;&nbsp;</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">类方法，类：__main__.MyClass，val1：Class Value changed，无法访问val2的值</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&nbsp;</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&gt;&gt;&gt;&nbsp;MyClass.classmd()&nbsp;&nbsp;# 类直接调用类方法，结果同上面的实例调用</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">&gt;&gt;&gt;&nbsp;</span></p><p><span style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; color: rgb(120, 120, 120); line-height: 1.8em; ">类方法，类：__main__.MyClass，val1：Class Value changed，无法访问val2的值</span></p><p>&nbsp;</p><p><strong style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; ">结论</strong></p><p><strong style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; ">如果上述执行过程太复杂，记住以下两点就好了：</strong></p><p><strong style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; ">静态方法：</strong>无法访问类属性、实例属性，相当于一个相对独立的方法，跟类其实没什么关系，换个角度来讲，其实就是放在一个类的作用域里的函数而已。</p><p><strong style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; ">类成员方法：</strong>可以访问类属性，无法访问实例属性。上述的变量val1，在类里是类变量，在实例中又是实例变量，所以容易混淆。</p><p><br/></p>', '2013-06-28 02:17:33', 14, 0, 0, 0, 1, 2, 'uublog', 1, 0, 0, 1, 1, ''),
(13, 5, 5, 7, 'python中文编码转换与正确输出', '', '', 'Python代码中字符串的默认编码与代码文件本身的编码一致decode的作用是将其他编码的字符串转换成unicode编码encode的作用是将unicode编码转换成其他编码的字符串&gt;&gt;&gt; s=&quot;中文&quot;&gt;&gt;&gt; s&#39;xd6xd0xcexc4&#39;&gt;&gt;&gt; s.decode(&quot;gbk&quot;)u&#39;', '<p style="; ; ; line-height: 24px; font-family: serif; font-size: 14px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2;">Python代码中字符串的默认编码与代码文件本身的编码一致<br/>decode的作用是将其他编码的字符串转换成unicode编码<br/>encode的作用是将unicode编码转换成其他编码的字符串</p><p style="; ; ; line-height: 24px; font-family: serif; font-size: 14px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2;">&gt;&gt;&gt; s=&quot;中文&quot;<br/>&gt;&gt;&gt; s<br/>&#39;xd6xd0xcexc4&#39;<br/>&gt;&gt;&gt; s.decode(&quot;gbk&quot;)<br/>u&#39;u4e2du6587&#39;<br/>&gt;&gt;&gt; print s.decode(&quot;gbk&quot;)<br/>中文<br/>&gt;&gt;&gt; print s<br/>中文<br/>&gt;&gt;&gt; s.decode(&quot;gbk&quot;).encode(&quot;gbk&quot;)<br/>&#39;xd6xd0xcexc4&#39;<br/>&gt;&gt;&gt; print s.decode(&quot;gbk&quot;).encode(&quot;gbk&quot;)<br/>中文<br/>&gt;&gt;&gt;</p><p style="; ; ; line-height: 24px; font-family: serif; font-size: 14px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2;">&gt;&gt;&gt; a=&#39;中国人&#39;<br/>&gt;&gt;&gt; a<br/>&#39;xd6xd0xb9xfaxc8xcb&#39;<br/>&gt;&gt;&gt; b = unicode(a,&#39;gbk&#39;)<br/>&gt;&gt;&gt; b<br/>u&#39;u4e2du56fdu4eba&#39;<br/>&gt;&gt;&gt; a.find(&#39;中&#39;)<br/>0<br/>&gt;&gt;&gt; a.find(&#39;人&#39;)<br/>4<br/>&gt;&gt;&gt; b.find(&#39;人&#39;.decode(&#39;gbk&#39;))<br/>2<br/>&gt;&gt;&gt; print a<br/>中国人<br/>&gt;&gt;&gt; print b<br/>中国人</p><p style="; ; ; line-height: 24px; font-family: serif; font-size: 14px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2;">这里find函数查到的结果应该很好理解啦。b中的find必须decode一下，否则会出错。至于为什么print出来的是汉字，我还没有研究出来呢。请高手告知。</p><p style="; ; ; line-height: 24px; font-family: serif; font-size: 14px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2;">&gt;&gt;&gt; b.encode(&#39;gb18030&#39;)<br/>&#39;xd6xd0xb9xfaxc8xcb&#39;<br/>&gt;&gt;&gt; b.encode(&#39;cp936&#39;)<br/>&#39;xd6xd0xb9xfaxc8xcb&#39;<br/>&gt;&gt;&gt; b.encode(&#39;gbk&#39;)<br/>&#39;xd6xd0xb9xfaxc8xcb&#39;<br/>&gt;&gt;&gt; b.encode(&#39;utf-8&#39;)<br/>&#39;xe4xb8xadxe5x9bxbdxe4xbaxba&#39;</p><p style="; ; ; line-height: 24px; font-family: serif; font-size: 14px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2;">说明gb18030、gbk、gb2312以及cp936等都可以进行中文编码，并且结果还一致，utf-8也可以，只是编码方式不一样，所以结果不同而已。原理上他们都是一致的。</p><p style="; ; ; line-height: 24px; font-family: serif; font-size: 14px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2;">&gt;&gt;&gt; type(a)<br/>&lt;type &#39;str&#39;&gt;<br/>&gt;&gt;&gt; type(b)<br/>&lt;type &#39;unicode&#39;&gt;<br/>&gt;&gt;&gt; type(b.encode(&#39;utf-8&#39;))<br/>&lt;type &#39;str&#39;&gt;</p><p style="; ; ; line-height: 24px; font-family: serif; font-size: 14px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2;">说明python对字符串有两种编码方式，一种就是普通方式，另外一种就是unicode。注意utf-8也认为是普通的编码方式</p><p style="; ; ; line-height: 24px; font-family: serif; font-size: 14px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2;">下面提供了编辑转换</p><p style="; ; ; line-height: 24px; font-family: serif; font-size: 14px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2;">汉字转为html实体字符得了。<br/>&nbsp;echo mb_convert_encoding (&quot;重玩一次&quot;, &quot;HTML-ENTITIES&quot;, &quot;gb2312&quot;);</p><p style="; ; ; line-height: 24px; font-family: serif; font-size: 14px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2;">编码转换<br/>s = &quot;中文&quot;<br/>s1 = u&quot;中文&quot;</p><p style="; ; ; line-height: 24px; font-family: serif; font-size: 14px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2;">unicode -&gt; gbk<br/>&nbsp;s1.encode(&quot;gbk&quot;)<br/>unicode -&gt; utf-8<br/>&nbsp;s1.encode(&quot;UTF-8&quot;)<br/>gbk -&gt;unicode<br/>&nbsp;unicode(s, &quot;gbk&quot;)<br/>&nbsp;或者<br/>&nbsp;s.decode(&quot;gbk&quot;)</p><p><br/></p>', '2013-06-28 04:56:42', 2, 0, 0, 0, 1, 3, 'test5', 1, 0, 0, 1, 1, ''),
(14, 17, 17, 5, '雷政富受贿316万余元一审被判13年', '', '', '　　中新网重庆6月28日电 (记者 刘贤)原中共重庆北碚区委书记雷政富涉嫌受贿一案28日在重庆第一中级人民法院一审宣判。雷政富以受贿316万余元被判有期徒刑13年，剥夺政治权利3年，没收30万元财产，追缴316万余元受贿款上交国库；没收财产和受贿款在1个月内上交。', '<p><span style="color: rgb(51, 51, 51); font-family: 微软雅黑; font-size: 15px; letter-spacing: 1px; line-height: 26px; orphans: 2; text-align: -webkit-auto;  widows: 2; background-color: rgb(238, 242, 246);">　　</span><a target="_blank" href="http://www.chinanews.com/" style="text-decoration: none; font-family: 微软雅黑; font-size: 15px; letter-spacing: 1px; line-height: 26px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(238, 242, 246);">中新网</a><span style="color: rgb(51, 51, 51); font-family: 微软雅黑; font-size: 15px; letter-spacing: 1px; line-height: 26px; orphans: 2; text-align: -webkit-auto;  widows: 2; background-color: rgb(238, 242, 246);">重庆6月28日电 (记者 刘贤)原中共重庆北碚区委书记雷政富涉嫌受贿一案28日在重庆第一中级人民法院一审宣判。雷政富以受贿316万余元被判有期徒刑13年，剥夺政治权利3年，没收30万元财产，追缴316万余元受贿款上交国库；没收财产和受贿款在1个月内上交。</span></p>', '2013-06-28 04:57:48', 1, 0, 0, 0, 1, 3, 'test5', 1, 0, 0, 1, 1, ''),
(15, 1, 1, 7, '今天我们到摄影棚里面拍产品照，结果看见两个新娘进来拍照。', '', '', '今天我们到摄影棚里面拍产品照，结果看见两个新娘进来拍照。我们老大很惊奇地问，这是怎么回事呢？新郎呢？然后摄影师说，她们拍得是闺蜜照。好吧，好吧，是我们想歪了。呵呵(~o~)！', '<p><span style="color: rgb(69, 69, 69); font-family: tahoma, helvetica, arial; font-size: 14px; line-height: 21px; orphans: 2; text-align: -webkit-auto;  widows: 2; background-color: rgb(255, 255, 255);">今天我们到摄影棚里面拍产品照，结果看见两个新娘进来拍照。</span><br style="color: rgb(69, 69, 69); font-family: tahoma, helvetica, arial; font-size: 14px; line-height: 21px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(255, 255, 255);"/><span style="color: rgb(69, 69, 69); font-family: tahoma, helvetica, arial; font-size: 14px; line-height: 21px; orphans: 2; text-align: -webkit-auto;  widows: 2; background-color: rgb(255, 255, 255);">我们老大很惊奇地问，这是怎么回事呢？新郎呢？</span><br style="color: rgb(69, 69, 69); font-family: tahoma, helvetica, arial; font-size: 14px; line-height: 21px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(255, 255, 255);"/><span style="color: rgb(69, 69, 69); font-family: tahoma, helvetica, arial; font-size: 14px; line-height: 21px; orphans: 2; text-align: -webkit-auto;  widows: 2; background-color: rgb(255, 255, 255);">然后摄影师说，她们拍得是闺蜜照。</span><br style="color: rgb(69, 69, 69); font-family: tahoma, helvetica, arial; font-size: 14px; line-height: 21px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(255, 255, 255);"/><span style="color: rgb(69, 69, 69); font-family: tahoma, helvetica, arial; font-size: 14px; line-height: 21px; orphans: 2; text-align: -webkit-auto;  widows: 2; background-color: rgb(255, 255, 255);">好吧，好吧，是我们想歪了。呵呵(~o~)！</span></p>', '2013-06-28 04:58:37', 15, 2, 0, 0, 1, 3, 'test5', 1, 0, 0, 1, 1, ''),
(16, 15, 15, 1, '我拿着彩票看双色球开奖', '', '', '.昨天晚上，我拿着彩票看双色球开奖。摇出前五个时全对上了，正要出第六个突然停电了。我一激动吧茶几踹碎了。今早到彩票站一看，我中了200元。默默地去家具城买个茶几，花了350元。', '<p><span style="color: rgb(51, 51, 51); font-family: 宋体, &#39;Helvetica Neue&#39;, Helvetica, Arial, sans-serif; font-size: 14px; line-height: 24px; orphans: 2;  widows: 2; background-color: rgb(255, 255, 255);">.昨天晚上，我拿着彩票看双色球开奖。摇出前五个时全对上了，正要出第六个突然停电了。我一激动吧茶几踹碎了。今早到彩票站一看，我中了200元。默默地去家具城买个茶几，花了350元。</span></p>', '2013-06-28 07:06:46', 2, 0, 0, 0, 1, 4, 'test6', 1, 0, 0, 1, 1, ''),
(17, 26, 26, 1, '藏獒频繁伤人、咬死人，社会不能继续沉默 ', '', '', '藏獒频繁伤人、咬死人，社会不能继续沉默6月27日19时许，河北省邯郸市人王某领其3岁半的女儿李某到大连高新园区梁家沟内一工地的小卖店内购买水喝，母女二人刚进入到商店的院内，突然从围挡的院内蹿出一条黑色藏獒，将李某的脖子左侧咬住，孩子母亲等人急忙用砖头、木棍驱打，藏獒被打跑后，商店服务员马上联系商店主人的哥哥驾车将李某送到大连附属第二医院，李某经抢救无效死亡。（6月28日《新华网》）6月28日，完全', '<p style="text-align:center;; ; border: 0px; list-style: none; word-wrap: normal; word-break: normal; line-height: 21px; color: rgb(50, 62, 50); font-family: simsun; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(107, 131, 102); text-indent: 2em;"><span style="word-wrap: normal; word-break: normal; line-height: 30px; font-size: 20px; "><strong>藏獒频繁伤人、咬死人，社会不能继续沉默</strong></span></p><p style="; ; border: 0px; list-style: none; word-wrap: normal; word-break: normal; line-height: 21px; color: rgb(50, 62, 50); font-family: simsun; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(107, 131, 102); text-indent: 2em;"><span style="word-wrap: normal; word-break: normal; line-height: 30px; font-size: 20px; ">6月27日19时许，河北省邯郸市人王某领其3岁半的女儿李某到大连高新园区梁家沟内一工地的小卖店内购买水喝，母女二人刚进入到商店的院内，突然从围挡的院内蹿出一条黑色藏獒，将李某的脖子左侧咬住，孩子母亲等人急忙用砖头、木棍驱打，藏獒被打跑后，商店服务员马上联系商店主人的哥哥驾车将李某送到大连附属第二医院，李某经抢救无效死亡。（6月28日《新华网》）</span></p><p style="; ; border: 0px; list-style: none; word-wrap: normal; word-break: normal; line-height: 21px; color: rgb(50, 62, 50); font-family: simsun; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(107, 131, 102); text-indent: 2em;"><span style="word-wrap: normal; word-break: normal; line-height: 30px; font-size: 20px; "><strong><img align="right" src="http://a.cvimg.cn/UploadFile/MiniBlog/2013/6-28/587d9ef9-bbd7-46c0-b04c-37b419827d39_Big.jpg" real_src="http://a.cvimg.cn/UploadFile/MiniBlog/2013/6-28/587d9ef9-bbd7-46c0-b04c-37b419827d39_Big.jpg" alt="藏獒频繁伤人、咬死人，社会不能继续沉默" title="藏獒频繁伤人、咬死人，社会不能继续沉默" style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; border-top-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px; border-style: initial; border-color: initial; border-image: initial; list-style-type: none; list-style-position: initial; list-style-image: initial; "/>6</strong><strong>月</strong><strong>28</strong><strong>日，完全可以被称为“中国藏獒伤人报道日”。</strong>就在这一天，媒体除了报道大连这名3岁半女孩被藏獒咬死之外，还有另外5起藏獒伤人事件的报道：</span></p><p style="; ; border: 0px; list-style: none; word-wrap: normal; word-break: normal; line-height: 21px; color: rgb(50, 62, 50); font-family: simsun; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(107, 131, 102); text-indent: 2em;"><span style="word-wrap: normal; word-break: normal; line-height: 30px; font-size: 20px; ">一大早，从题为《山西运城村民藏獒口中勇救小女孩》的视频中，看到一名不到10岁的小女孩在路口与一条藏獒相遇，被藏獒扑倒在地的小女孩试图反抗，但很快就被拖到一旁，挣扎了几秒钟就不再反抗，辛亏一名骑电动车的成人快速冲向这条伤人的藏獒，用电动车猛撞藏獒，再用木棍打击藏獒，最终救下小女孩。</span></p><p style="; ; border: 0px; list-style: none; word-wrap: normal; word-break: normal; line-height: 21px; color: rgb(50, 62, 50); font-family: simsun; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(107, 131, 102); text-indent: 2em;"><span style="word-wrap: normal; word-break: normal; line-height: 30px; font-size: 20px; ">还是发生在大连，一只重达150多斤的藏獒在辽宁省庄河市兴一条街上见人就咬，多人被咬伤。一名90岁老妇因躲避不及，被发狂的藏獒咬穿胳膊，周围居民拨打110报警求助。</span></p><p style="; ; border: 0px; list-style: none; word-wrap: normal; word-break: normal; line-height: 21px; color: rgb(50, 62, 50); font-family: simsun; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(107, 131, 102); text-indent: 2em;"><span style="word-wrap: normal; word-break: normal; line-height: 30px; font-size: 20px; ">今日清晨，一条体重近百斤的藏獒在四川泸州城区将一名妇女咬伤。为防止藏獒再次伤人，警方果断将其击毙。</span></p><p style="; ; border: 0px; list-style: none; word-wrap: normal; word-break: normal; line-height: 21px; color: rgb(50, 62, 50); font-family: simsun; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(107, 131, 102); text-indent: 2em;"><span style="word-wrap: normal; word-break: normal; line-height: 30px; font-size: 20px; ">6月24日清晨，两只藏獒犬突然从某公司院内蹿出，在位于昌平区邓庄村附近的马路边上，将3名路人咬伤。</span></p><p style="; ; border: 0px; list-style: none; word-wrap: normal; word-break: normal; line-height: 21px; color: rgb(50, 62, 50); font-family: simsun; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(107, 131, 102); text-indent: 2em;"><span style="word-wrap: normal; word-break: normal; line-height: 30px; font-size: 20px; ">6月27日10时许，平谷区公安分局接群众报警，称在马坊镇英城物流园区有2人被狗咬伤，一人被咬腿部，一人被咬肩部，伤者已被送往医院。</span></p><p style="; ; border: 0px; list-style: none; word-wrap: normal; word-break: normal; line-height: 21px; color: rgb(50, 62, 50); font-family: simsun; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(107, 131, 102); text-indent: 2em;"><span style="word-wrap: normal; word-break: normal; line-height: 30px; font-size: 20px; "><strong>藏獒伤人、咬死人事件如此频繁，兼简是骇人听闻。这些藏獒，动辄上百万甚至上千万，无非是富人的玩物。可富人玩物享受，总不该漠视他人生命啊。</strong></span></p><p style="; ; border: 0px; list-style: none; word-wrap: normal; word-break: normal; line-height: 21px; color: rgb(50, 62, 50); font-family: simsun; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(107, 131, 102); text-indent: 2em;"><span style="word-wrap: normal; word-break: normal; line-height: 30px; font-size: 20px; ">养藏獒的主人，之所以不把他人的生命当回事，应该和中国法律对恶犬主人的处罚过轻有关。5月30日美国洛杉矶也发生斗牛犬咬死人事件，犬主人杰克逊被以“谋杀罪”逮捕，洛杉矶县地区检察院发言人说，如果被定罪，杰克逊将面临终身监禁。而在中国，一般会以“过失杀人罪”，狗主人最多也就被判7年有期徒刑。</span></p><p style="; ; border: 0px; list-style: none; word-wrap: normal; word-break: normal; line-height: 21px; color: rgb(50, 62, 50); font-family: simsun; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(107, 131, 102); text-indent: 2em;"><span style="word-wrap: normal; word-break: normal; line-height: 30px; font-size: 20px; "><strong>此外，对犬只管理制度落实不够，也是造成恶犬频繁伤人的重要原因。</strong>从目前的城市管理看，如藏獒这样的大型犬、烈性犬，绝大多数城市都是禁养的，但我们在大街上还能不时地看到大型犬、烈性犬，而随处可见的宠物犬则基本上没有狗牌。</span></p><p style="; ; border: 0px; list-style: none; word-wrap: normal; word-break: normal; line-height: 21px; color: rgb(50, 62, 50); font-family: simsun; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(107, 131, 102); text-indent: 2em;"><span style="word-wrap: normal; word-break: normal; line-height: 30px; font-size: 20px; ">遵义恶犬咬死晨练老人事件发生之后，各地对犬只的管理力度得到了一定的加强。月初，北京市公安机关开始在全市各主要社区内张贴早年出台的《北京市公安局关于重点管理区禁止饲养大型犬烈性犬的通告》，要求在东城、西城、朝阳、海淀、丰台、石景山区这六个重点管理区开查大型犬和烈性犬。上述犬只一经查获，将由公安机关予以没收，并可对养犬单位处1万元罚款，对养犬人处5000元罚款。</span></p><p style="; ; border: 0px; list-style: none; word-wrap: normal; word-break: normal; line-height: 21px; color: rgb(50, 62, 50); font-family: simsun; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(107, 131, 102); text-indent: 2em;"><span style="word-wrap: normal; word-break: normal; line-height: 30px; font-size: 20px; ">因为昌平、平谷两区不属于重点管理区，估计此轮整治后六个重点管理区的大型犬、烈性犬改投昌平、平谷等区县了，因此上面两起藏獒伤人事故，仅是该地恶犬频繁伤人事故的开始，如果当地政府不能强化管理，更严重的惨剧将不可避免地要在近期发生。</span></p><p style="; ; border: 0px; list-style: none; word-wrap: normal; word-break: normal; line-height: 21px; color: rgb(50, 62, 50); font-family: simsun; font-size: 14px; orphans: 2; white-space: normal; widows: 2; background-color: rgb(107, 131, 102); text-indent: 2em;"><span style="word-wrap: normal; word-break: normal; line-height: 30px; font-size: 20px; "><strong>面对频繁发生的藏獒及其他犬类伤人、咬死人事件，社会不能再沉默下去了。政府有责任保护居民人身安全不受犬类的威胁，“禁犬”规定不能得到落实，就是政府失职、渎职。</strong>一些“伪动物保护主义者”，对部分城市捕杀大型犬、烈性犬举动横加指责，孰不知人的生命价值远高于犬类，远高于无论多么名贵的藏獒。那些“人不如狗”的思维，其实是将自己的价值贬低至犬类之下，理应遭到社会的唾弃。</span></p><p><br/></p>', '2013-06-29 06:58:18', 2, 0, 0, 0, 1, 4, 'test6', 0, 0, 0, 1, 1, ''),
(21, 10, 10, 9, '机器人总动员 WALL·E (2008)', '', '', '机器人总动员的剧情简介', '<p>机器人总动员的剧情简介</p>', '2013-06-29 13:28:59', 5, 0, 0, 0, 1, 5, 'xiaohuang', 1, 0, 0, 1, 1, '');
INSERT INTO `blog_article` (`id`, `channel1_id`, `channel2_id`, `category_id`, `title`, `pic`, `tags`, `summary`, `content`, `createtime`, `views`, `comments`, `goods`, `bads`, `status`, `user_id`, `username`, `ishome`, `isrecommend`, `istop`, `isoriginal`, `cancomment`, `password`) VALUES
(22, 3, 0, 13, '习近平强调:建设一支宏大高素质干部队伍', '', '', '&nbsp;&nbsp;&nbsp; 6月28日，中共中央总书记、国家主席、中央军委主席习近平在全国组织工作会议上发表重要讲话。新华社记者 鞠鹏 摄&nbsp;&nbsp;&nbsp;&nbsp;新华网北京６月２９日电（记者徐京跃　周英峰）全国组织工作会议２８日至２９日在北京召开。中共中央总书记、国家主席、中央军委主席习近平出席会议并发表重要讲话。他强调，面对复杂多变的国际形势和艰巨繁重的国内改革', '<p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px"><img id="{D13EED3E-F12F-44A9-8576-54EEC582C19C}" title="" style="BORDER-LEFT-WIDTH: 0px; HEIGHT: 600px; BORDER-RIGHT-WIDTH: 0px; BORDER-BOTTOM-WIDTH: 0px; PADDING-BOTTOM: 0px; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; WIDTH: 500px; border-image: initial" border="0" align="center" src="http://news.xinhuanet.com/politics/2013-06/29/116339948_11n.jpg" sourcename="本地文件" sourcedescription="编辑提供的本地文件"/></p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px"><span style="FONT-FAMILY: 楷体; COLOR: navy">&nbsp;&nbsp;&nbsp; 6月28日，中共中央总书记、国家主席、中央军委主席习近平在全国组织工作会议上发表重要讲话。新华社记者 鞠鹏 摄</span></p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">&nbsp;&nbsp;&nbsp;&nbsp;新华网北京６月２９日电（记者徐京跃　周英峰）全国组织工作会议２８日至２９日在北京召开。中共中央总书记、国家主席、中央军委主席习近平出席会议并发表重要讲话。他强调，面对复杂多变的国际形势和艰巨繁重的国内改革发展任务，实现党的十八大确定的各项目标任务，进行具有许多新的历史特点的伟大斗争，关键在党，关键在人。关键在党，就要确保党在发展中国特色社会主义历史进程中始终成为坚强领导核心。关键在人，就要建设一支宏大的高素质干部队伍。</p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">&nbsp;&nbsp;&nbsp;&nbsp;中共中央政治局常委、中央书记处书记刘云山在会议上讲话。中共中央政治局常委、中央纪委书记王岐山出席会议。</p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">&nbsp;&nbsp;&nbsp;&nbsp;习近平在讲话中首先代表党中央，在即将迎来中国共产党成立９２周年之际，向全国各级党组织和广大共产党员致以节日的问候。</p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">&nbsp;&nbsp;&nbsp;&nbsp;习近平指出，我们党历来高度重视选贤任能，始终把选人用人作为关系党和人民事业的关键性、根本性问题来抓。好干部要做到信念坚定、为民服务、勤政务实、敢于担当、清正廉洁。党的干部必须坚定共产主义远大理想、真诚信仰马克思主义、矢志不渝为中国特色社会主义而奋斗，全心全意为人民服务，求真务实、真抓实干，坚持原则、认真负责，敬畏权力、慎用权力，保持拒腐蚀、永不沾的政治本色，创造出经得起实践、人民、历史检验的实绩。</p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">&nbsp;&nbsp;&nbsp;&nbsp;习近平强调，好干部不会自然而然产生。成长为一个好干部，一靠自身努力，二靠组织培养。干部的党性修养、思想觉悟、道德水平不会随着党龄的积累而自然提高，也不会随着职务的升迁而自然提高，而需要终生努力。成为好干部，就要不断改造主观世界、加强党性修养、加强品格陶冶，时刻用党章、用共产党员标准要求自己，时刻自重自省自警自励，老老实实做人，踏踏实实干事，清清白白为官。干部要勤于学、敏于思，认真学习马克思主义理论特别是中国特色社会主义理论体系，丰富知识储备，完善知识结构，打牢履职尽责的知识基础。干部要深入基层、深入实际、深入群众，在改革发展的主战场、维护稳定的第一线、服务群众的最前沿砥砺品质、提高本领。</p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">&nbsp;&nbsp;&nbsp;&nbsp;习近平指出，用一贤人则群贤毕至，见贤思齐就蔚然成风。选什么人就是风向标，就有什么样的干部作风，乃至就有什么样的党风。各级党委及组织部门要坚持党管干部原则，坚持正确用人导向，坚持德才兼备、以德为先，努力做到选贤任能、用当其时，知人善任、人尽其才，把好干部及时发现出来、合理使用起来。要坚持全面、历史、辩证看干部，注重一贯表现和全部工作。要改进考核方法手段，既看发展又看基础，既看显绩又看潜绩，把民生改善、社会进步、生态效益等指标和实绩作为重要考核内容，再也不能简单以国内生产总值增长率来论英雄了。要树立强烈的人才意识，寻觅人才求贤若渴，发现人才如获至宝，举荐人才不拘一格，使用人才各尽其能。</p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">&nbsp;&nbsp;&nbsp;&nbsp;习近平指出，把好干部选用起来，需要科学有效的选人用人机制。要紧密结合干部工作实际，认真总结，深入研究，不断改进，努力形成系统完备、科学规范、有效管用、简便易行的制度机制。要特别注意研究新情况新问题。要把加强党的领导和充分发扬民主结合起来，发挥党组织在干部选拔任用工作中的领导和把关作用。要完善工作机制，推进干部工作公开，坚决制止简单以票取人的做法，确保民主推荐、民主测评风清气正。</p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">&nbsp;&nbsp;&nbsp;&nbsp;习近平强调，培养选拔年轻干部，事关党的事业薪火相传，事关国家长治久安。加强和改进年轻干部工作，要下大气力抓好培养工作。对那些看得准、有潜力、有发展前途的年轻干部，要敢于给他们压担子，有计划安排他们去经受锻炼。</p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">&nbsp;&nbsp;&nbsp;&nbsp;习近平指出，党要管党，才能管好党；从严治党，才能治好党。对我们这样一个拥有８５００多万党员、在一个１３亿人口大国长期执政的党，管党治党一刻不能松懈。组织工作必须认真贯彻党要管党、从严治党方针。党要管党，首先是管好干部；从严治党，关键是从严治吏。要把从严管理干部贯彻落实到干部队伍建设全过程，坚持从严教育、从严管理、从严监督，让每一个干部都深刻懂得，当干部就必须付出更多辛劳、接受更严格的约束。各级领导机关和领导干部，尤其是中央机关和中央国家机关、高级领导干部要强化带头意识，时时处处严要求、作表率。</p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">&nbsp;&nbsp;&nbsp;&nbsp;习近平强调，党员是党的肌体的细胞。党的先进性和纯洁性要靠千千万万党员的先进性和纯洁性来体现，党的执政使命要靠千千万万党员卓有成效的工作来完成，党要管党、从严治党必须落实到党员队伍的管理中去。党组织要严格把关，把政治标准放在首位，确保政治合格。要重视从青年工人、农民、知识分子中发展党员。要严格党员日常教育和管理，使广大党员平常时候看得出来、关键时刻站得出来、危急关头豁得出来，充分发挥先锋模范作用。</p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">&nbsp;&nbsp;&nbsp;&nbsp;习近平指出，贯彻党要管党、从严治党方针，必须扎实做好抓基层、打基础的工作，使每个基层党组织都成为坚强战斗堡垒。党的十八大提出了加强基层服务型党组织建设的重大任务。当前和今后一个时期，要以此来指导党的基层组织建设。各级都要重视基层、关心基层、支持基层，加强带头人队伍建设，确保基层党组织有资源、有能力为群众服务。对广大基层干部要充分理解、充分信任，格外关心、格外爱护，多为他们办一些雪中送炭的事情。</p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">&nbsp;&nbsp;&nbsp;&nbsp;习近平指出，严肃的党内生活，是解决党内自身问题的重要途径。要健全和认真落实民主集中制的各项具体制度，促使全党同志按照民主集中制办事，促使各级领导干部特别是主要领导干部带头执行民主集中制。要严明党的组织纪律和政治纪律，教育引导党员、干部自觉维护中央权威，始终在思想上政治上行动上同党中央保持高度一致，维护党的团结统一。</p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">&nbsp;&nbsp;&nbsp;&nbsp;习近平强调，组织部门作为管党治党的重要职能部门，必须带头改进作风，继承发扬组织部门优良传统和作风，树立和维护组织部门良好形象。组织部门改进作风，最核心的是坚持公道正派。要着眼于党的事业发展需要选人用人，公道对待干部，公平评价干部，公正使用干部，敢于坚持原则，让好干部真正受尊重、受重用，让那些阿谀逢迎、弄虚作假、不干实事、会跑会要的干部真正没市场、受惩戒。要严明组织人事纪律，对违反组织人事纪律的坚决不放过，对跑官要官、买官卖官的决不姑息，发现一起，查处一起。</p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">&nbsp;&nbsp;&nbsp;&nbsp;习近平指出，在党的群众路线教育实践活动中，组织部门担负着抓好自身活动和参与组织指导整个活动的双重责任，要自觉走在活动前列，努力把各级组织部门建设成为讲政治、重公道、业务精、作风好的模范部门。</p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">&nbsp;&nbsp;&nbsp;&nbsp;刘云山在讲话中指出，习近平总书记的重要讲话从统筹伟大事业伟大工程、实现党的新的历史使命的战略高度，深刻回答了关系党的建设和组织工作全局的重大理论和现实问题，为今后工作指明了方向、提供了遵循。要切实用讲话精神统一思想、指导实践，在新的起点上开创工作新局面。</p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">&nbsp;&nbsp;&nbsp;&nbsp;刘云山说，做好新形势下组织工作，要深入贯彻党的十八大部署和习近平总书记重要讲话精神，以党的执政能力建设、先进性和纯洁性建设为主线，以培养选拔更多党和人民需要的好干部为重点，体现从严、创新、务实的要求，着力提升党员干部思想政治素养，着力弘扬党的优良作风，着力形成科学有效的选人用人机制，着力增强各级党组织的发展活力，全面提高党的建设科学化水平。要抓好思想理论建设这个根本，教育引导党员干部坚定理想信念，做中国特色社会主义的坚定信仰者和忠实践行者。大力加强作风建设，深入开展群众路线教育实践活动，聚焦“四风”问题，务求取得实效。认真贯彻民主集中制，严肃党内生活，严肃政治纪律，保障党员民主权利，维护党的团结统一。深化干部人事制度改革，切实完善干部提名推荐、考核评价、选拔任用、管理监督等方面的措施办法，提高选人用人公信度，建设高素质干部队伍和人才队伍。创新基层党建工作，扩大组织覆盖和工作覆盖，深入推进基层服务型党组织建设。加强党对组织工作的领导，围绕公道正派这个核心加强组织部门作风建设，树立和维护组工干部的良好形象。</p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">&nbsp;&nbsp;&nbsp;&nbsp;中央组织部部长赵乐际在总结讲话中指出，要深入学习贯彻党的十八大精神、习近平总书记重要讲话和刘云山同志重要报告精神，深刻领会党要管党、从严治党的思想，锐意进取、改革创新的思想，改进工作作风、密切联系群众的思想，恪守“四个坚持”、选好执政骨干的思想，重心在基层、基层在服务的思想，强化制度约束、完善制度体系的思想，扎实推进组织工作各项任务落实。要坚持从严治部、从严律己、从严带队伍，带头改进作风，努力建设讲政治、重公道、业务精、作风好的模范部门。</p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">&nbsp;&nbsp;&nbsp;&nbsp;部分在京中共中央政治局委员、书记处书记出席会议。</p><p style="BORDER-LEFT-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px; WHITE-SPACE: normal; BORDER-BOTTOM-WIDTH: 0px; TEXT-TRANSFORM: none; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: left; PADDING-TOP: 0px; FONT: 16px/28px 宋体; PADDING-LEFT: 0px; MARGIN: 1em 0px; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BORDER-TOP-WIDTH: 0px; BACKGROUND-COLOR: rgb(255,255,255); TEXT-INDENT: 0px; border-image: initial; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">&nbsp;&nbsp;&nbsp;&nbsp;这次会议研究部署了今后５年党的建设和组织工作。中央党的建设工作领导小组成员，中央和国家机关各部委主要负责人，各省区市和副省级城市、新疆生产建设兵团党委组织部长，中央和国家机关各部委、各人民团体干部（人事）司（局）长，中央管理的金融企业、国有重要骨干企业和高校党委（党组）分管组织人事工作的负责人，解放军总政治部干部部和组织部、武警总部政治部负责人等参加会议。</p><p>&nbsp;</p>', '2013-06-30 12:50:06', 1, 0, 0, 0, 1, 6, 'dd', 1, 0, 0, 1, 1, ''),
(23, 18, 18, 17, '朴槿惠清华演讲：中国梦与韩国梦是一致的', '', '', '昨日，韩国总统朴槿惠在清华演讲。清华大学向朴槿惠赠送冯友兰先生书法。记者 周岗峰 摄原题：朴槿惠：中国梦与韩国梦是一致的韩国总统朴槿惠清华演讲引用古诗词展现中文功底，首次提出“韩国梦”昨日上午，清华大学主楼报告厅，身着紫色外套的韩国总统朴槿惠发表演讲。在一群黑色西装中间，这一抹紫色迎来了在场数百名大学生的阵阵掌声。朴槿惠在演讲开头和结尾都使用了中文。', '<p style="WORD-WRAP: break-word; WHITE-SPACE: normal; TEXT-TRANSFORM: none; WORD-BREAK: break-all; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; FONT: 14px/25px 宋体; PADDING-LEFT: 0px; MARGIN: 10px auto; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BACKGROUND-COLOR: rgb(250,252,255); TEXT-INDENT: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px"><a style="COLOR: rgb(0,0,0); TEXT-DECORATION: none" href="http://hb.people.com.cn/n/2013/0630/c192237-18966994-2.html"><img style="BORDER-TOP-STYLE: none; BORDER-LEFT-STYLE: none; BORDER-BOTTOM-STYLE: none; BORDER-RIGHT-STYLE: none; border-image: initial" alt="朴槿惠清华演讲：中国梦与韩国梦是一致的" src="http://www.people.com.cn/mediafile/pic/20130630/54/12625814107738192854.jpg"/></a></p><p style="WORD-WRAP: break-word; WHITE-SPACE: normal; TEXT-TRANSFORM: none; WORD-BREAK: break-all; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; FONT: 14px/25px 宋体; PADDING-LEFT: 0px; MARGIN: 10px auto; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BACKGROUND-COLOR: rgb(250,252,255); TEXT-INDENT: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">昨日，韩国总统朴槿惠在清华演讲。清华大学向朴槿惠赠送冯友兰先生书法。记者 周岗峰 摄</p><p class="pictext" style="WORD-WRAP: break-word; WHITE-SPACE: normal; TEXT-TRANSFORM: none; WORD-BREAK: break-all; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; PADDING-TOP: 0px; FONT: 14px/25px 宋体; PADDING-LEFT: 0px; MARGIN: 10px auto; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BACKGROUND-COLOR: rgb(250,252,255); TEXT-INDENT: 2em; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">原题：朴槿惠：中国梦与韩国梦是一致的</p><p class="pictext" style="WORD-WRAP: break-word; WHITE-SPACE: normal; TEXT-TRANSFORM: none; WORD-BREAK: break-all; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; PADDING-TOP: 0px; FONT: 14px/25px 宋体; PADDING-LEFT: 0px; MARGIN: 10px auto; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BACKGROUND-COLOR: rgb(250,252,255); TEXT-INDENT: 2em; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">韩国总统朴槿惠清华演讲引用古诗词展现中文功底，首次提出“韩国梦”</p><p style="WORD-WRAP: break-word; WHITE-SPACE: normal; TEXT-TRANSFORM: none; WORD-BREAK: break-all; WORD-SPACING: 0px; COLOR: rgb(0,0,0); PADDING-BOTTOM: 0px; PADDING-TOP: 0px; FONT: 14px/25px 宋体; PADDING-LEFT: 0px; MARGIN: 10px auto; ORPHANS: 2; WIDOWS: 2; LETTER-SPACING: normal; PADDING-RIGHT: 0px; BACKGROUND-COLOR: rgb(250,252,255); TEXT-INDENT: 2em; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px">昨日上午，清华大学主楼报告厅，身着紫色外套的韩国总统朴槿惠发表演讲。在一群黑色西装中间，这一抹紫色迎来了在场数百名大学生的阵阵掌声。朴槿惠在演讲开头和结尾都使用了中文。</p><p></p>', '2013-06-30 12:58:26', 2, 0, 0, 0, 1, 10, 'kongjian4', 1, 0, 0, 1, 0, ''),
(24, 2, 2, 19, '我区公安机关查处19起网上编造传播谣言行为 ', '', '', '新疆日报讯 近日，有个别网民在网上编造、传播谣言，引发社会恐慌，被公安机关依法查处。　　公安机关查明，近日网民孙某等利用手机和互联网，在微博、微信、QQ群、短信等平台编造、传播所谓“新疆各地暴乱”等谣言，产生了恶劣社会影响。我区各地公安机关迅速展开调查，并依据有关法律法规，对孙某、陈某等19名涉事人员予以行政拘留并处罚款。　　6月26日，乌鲁木齐市孙某（网名“494064074”）在QQ群妄称：“', '<p><strong>新疆日报讯</strong> 近日，有个别网民在网上编造、传播谣言，引发社会恐慌，被公安机关依法查处。</p><p>　　公安机关查明，近日网民孙某等利用手机和互联网，在微博、微信、QQ群、短信等平台编造、传播所谓“新疆各地暴乱”等谣言，产生了恶劣社会影响。我区各地公安机关迅速展开调查，并依据有关法律法规，对孙某、陈某等19名涉事人员予以行政拘留并处罚款。</p><p>　　6月26日，乌鲁木齐市孙某（网名“494064074”）在QQ群妄称：“我叫王桥军，家住新疆鄯善县鲁克沁镇10号，吐鲁番事件源自强行拆迁。”乌鲁木齐市公安局根据《中华人民共和国治安管理处罚法》相关规定对孙某作出行政拘留处罚。</p><p>　　6月27日，乌鲁木齐市陈某(网名“顺峰电子有限公司”)微博散布虚假信息称：新疆喀什市今日发生暴力恐怖事件，8人死亡。乌鲁木齐市公安局根据《中华人民共和国治安管理处罚法》相关规定对陈某作出行政拘留处罚。</p><p>　　6月28日，阿克苏市徐某道听途说自编短信散布谣言：有内部消息，今晚和明晚有暴乱。阿克苏市公安局根据《中华人民共和国治安管理处罚法》相关规定对徐某作出行政拘留处罚，并处罚款。</p><p>　　自治区公安厅有关负责人表示，公安机关将依法、从严查处利用手机、互联网编造传播谣言，严重扰乱社会秩序、影响社会稳定，危害社会安全的行为。希望广大网民自觉遵守国家法律法规，不信谣、不传谣，发现谣言及时举报，共同维护健康的网络环境和良好的社会秩序。</p><p></p>', '2013-06-30 13:08:00', 3, 1, 0, 0, 1, 11, 'qiqi', 1, 0, 0, 1, 1, ''),
(25, 16, 16, 22, '截访官员：警察不打人 那警察是养来干嘛的', '', '', '视频截图官员：“警察不打人 那警察是养来干嘛的&quot;近日，苏州某小区业主控诉无良开发商，上访至市信访局时遭遇阻拦，与相关领导沟通时，领导说：“警察不打人，那养警察干嘛？”此语一出，现场顿时一片哗然。有网友拍到一名地方官员对群众说：警察不打人，那警察养来干嘛的。现场顿时一片哗然。该官员身份目前正在核实中。', '<p style="TEXT-ALIGN: center"><img style="HEIGHT: 254px; WIDTH: 486px" alt="官员" src="http://china.haiwainet.cn/NMediaFile/2013/0630/LOCAL201306301907000488098129794.jpg" desc="视频截图"/></p><p class="desc" style="TEXT-ALIGN: center">视频截图</p><p style="TEXT-INDENT: 2em">官员：“警察不打人 那警察是养来干嘛的&quot;</p><p style="TEXT-INDENT: 2em">近日，苏州某小区业主控诉无良开发商，上访至市信访局时遭遇阻拦，与相关领导沟通时，领导说：“警察不打人，那养警察干嘛？”此语一出，现场顿时一片哗然。</p><p style="TEXT-INDENT: 2em">有网友拍到一名地方官员对群众说：警察不打人，那警察养来干嘛的。现场顿时一片哗然。该官员身份目前正在核实中。</p><p></p>', '2013-06-30 13:11:02', 2, 0, 0, 0, 1, 7, 'kongjian1', 1, 0, 0, 1, 1, ''),
(26, 1, 1, 23, '[原创]（原创）爱狗人士岂能沦为与恶狗同类', '', '', '&nbsp;因为在微博上发表反对养狗言论，积水潭医院一名烧伤科医生竟被两名爱狗女士堵在医院殴打，造成该医生手臂多处受伤，目前在家休养。话说微博名为“烧伤超人阿宝”的网友，在6月29日零点32分，发布了一条关于反对养狗的微博，言辞带有辱骂字眼，该条微博在发布之后遭到大量爱狗人士的谴责。当天早晨7点左右，一名微博名为“Aaaabbbbdddhhh”的网友留言称：今天会有人对“阿宝”泼硫酸并表示已经准备', '<p><span style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto;  widows: 2; background-color: rgb(220, 236, 237);">&nbsp;因为在微博上发表反对养狗言论，积水潭医院一名烧伤科医生竟被两名爱狗女士堵在医院殴打，造成该医生手臂多处受伤，目前在家休养。话说微博名为“烧伤超人阿宝”的网友，在6月29日零点32分，发布了一条关于反对养狗的微博，言辞带有辱骂字眼，该条微博在发布之后遭到大量爱狗人士的谴责。当天早晨7点左右，一名微博名为“Aaaabbbbdddhhh”的网友留言称：今天会有人对“阿宝”泼硫酸并表示已经准备好队伍，同时提醒“阿宝”如果不幸被烧伤，注意自己急救。据其称，两名爱狗女士昨天下午来到积水潭医院，对“阿宝”进行了殴打造成其多处受伤。大约半个小时后，双方都被警方带进派出所，随后大批的爱狗人士也很快赶到派出所。（长城网-燕赵都市报6月30日）</span><br style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(220, 236, 237);"/><br style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(220, 236, 237);"/><span style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto;  widows: 2; background-color: rgb(220, 236, 237);">&nbsp;&nbsp;&nbsp;&nbsp;感觉那些所谓的爱狗人士仿佛有组织群狼似的，不仅仅经常在公路上对合法贩运的商户干拦路抢劫的勾当，不仅司空见惯的在网上用最恶毒的语言群攻对手，这次竟然还对线上网民言论发展到线下组织暴力活动围殴网民，这不禁让人想起了最近频繁发生的恶狗伤人事件，也让人自然而然的将恶狗与爱狗人士的言行联想在一起，恶狗都是人养的，纵容恶狗的也是人，莫非一向自诩博爱的爱狗人士也同样沦落到与恶狗为伍了吗？</span><br style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(220, 236, 237);"/><br style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(220, 236, 237);"/><span style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto;  widows: 2; background-color: rgb(220, 236, 237);">&nbsp;&nbsp;&nbsp;&nbsp;其实网络本身只是一个开放的公共信息平台，每个人都有发表不同意见的权力，有人赞成养狗，自然也有人反对，赞成也好、反对也罢，不过是个人的观感，大不了有人养、有人不养，毕竟狗狗们仍然还会一如既往的过去被人类驯化的千百年来一样存在于人类社会和生活之中。爱狗人士何苦如此激动，人类养狗的历史证明，狗在东西方的文化中确实有着不同的地位，但并不妨碍人类与狗的交流。反对养狗的人也不过是个人观点而已，你不养照样有人养，大把的爱狗人士不用说了，更多平常心态的老百姓也会养；狗咬人、随地大小便成了社会问题，甚至社会公害，但问题似乎并不是狗，还是人的问题，是那些养狗的人的公民素质问题，这里就包括大量口口声声有爱心的爱狗人士、狗粉们，在恶狗不断伤人、狗占公交座位、狗与人争公共资源污染环境等问题上，狗粉们总是不吱声，仿佛什么也看不见，一但听说哪里有国人吃狗肉了，有人贩运狗了，他们立即就闪亮登场，大呼小叫，跟死了亲娘一样，典型的双重标准。</span><br style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(220, 236, 237);"/><br style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(220, 236, 237);"/><span style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto;  widows: 2; background-color: rgb(220, 236, 237);">&nbsp;&nbsp;&nbsp;&nbsp;狗就是狗，人就是人，狗是人驯化出来的动物，当狗成了人的宠物，或者说玩物的时候，有很多人就自然将狗当成了生命中的朋友，狗通人性，这似乎在其它同样被驯化的动物里，显得比较突出。但狗同样也有野性的时候，也就是我们所说的温驯的狗和恶狗之区别。要知道恶狗是会咬人的，甚至会咬死人，即使非恶狗，很多狗也成为传播狂犬病的源头，狗在中国社会泛滥成灾是不争的事实，并已经成为威胁社会安全的隐患。如果不采取日常化的规范监管，总是在出了问题后进行运动式打狗，且不说社会争议不断，也让人觉得政府有不作为的恶习。</span><br style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(220, 236, 237);"/><br style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(220, 236, 237);"/><span style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto;  widows: 2; background-color: rgb(220, 236, 237);">&nbsp;&nbsp;&nbsp;&nbsp;最近频繁发生的恶狗伤人事件已经让人触目惊心，6月13日庄河市兴达街道后炮台村李某家圈养的藏獒从饲养笼中跑到街面咬伤多人，居民拨打110求助。警方赶到后，将凶犬击毙。 6月3日山西运城盐湖区龙居镇赵村，一名8岁的小女孩街边玩耍的时候被一条凶猛的藏獒撕咬。5月28日贵州遵义红花岗区康海花园小区后山道路上，一位老人晨练时，被路边一苗圃蹿出的两只杜高犬咬伤致死，拖行10余米远。两只咬人恶犬和狗主人被警方控制。6月25日9时40分左右，在乌鲁木齐市西山路新疆标准件厂家属院里，一名5岁女孩突然被一只拴着的大狗扑倒并咬住右小腿不放，母亲拼力相救，还伸出右脚让狗咬，女儿才终于脱险。6月28日大连6岁女孩被烈犬咬断脖子惨死；据之前采访中有相关负责人介绍称，大型犬，尤其是烈性犬，在大连市内四区，旅顺地区的得胜街道、光荣街道、登峰街道都严禁饲养。</span><br style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(220, 236, 237);"/><br style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(220, 236, 237);"/><span style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto;  widows: 2; background-color: rgb(220, 236, 237);">&nbsp;&nbsp;&nbsp;&nbsp;类似恶狗伤人新闻不胜枚举，这还不包括那些污染公共环境的现象，狗成了社会公害，其实问题还是在人，尤其是那些假惺惺的爱狗人士，恶狗咬人嘛，那是畜生动物，而象这次北京医生发表反对养狗言论被2女子堵在医院殴打，还威胁要泼硫酸，则证明了中国的某些狗粉们已经沦落到了与恶狗为伍的地步，本来狗只是通人性的动物，爱狗人士总喜欢以狗对主人忠诚而将狗比作比人类还高尚，但狗忠诚主人并不意味着它们不咬别人，这种高尚就算成立也是自私的。相反目前一些狗粉们动辄极端的个人言行却彰显出确实比狗还低劣，谩骂加暴力，与西方在对待狗的态度上崇尚的爱心可谓南辕北辙。</span><br style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(220, 236, 237);"/><br style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(220, 236, 237);"/><span style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto;  widows: 2; background-color: rgb(220, 236, 237);">&nbsp;&nbsp;&nbsp;&nbsp;狗是人类的朋友，其实很多动物都是，人类总是从自身的功利性出发设定自我感觉良好的事物认定标准，其中就包括西方对狗的社会标准引入东亚包括中国社会后，也成为一部分狗粉狂热的追求，西方基督教文明中不吃狗，就象伊斯兰教不吃猪、印度教不吃牛一个道理，中国老百姓吃了几千年狗肉，你能说东方文化是野蛮文化？可这些狗粉就有那么执着，如果狗粉真的想彰显爱心与文明的话，对不同意见动辄粗痞相向甚至暴力威胁，就与恶狗无异了，只能是亵渎爱心。</span><br style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(220, 236, 237);"/><br style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto; white-space: normal; widows: 2; background-color: rgb(220, 236, 237);"/><span style="color: rgb(5, 17, 26); font-family: 宋体; font-size: 15px; line-height: 22px; orphans: 2; text-align: -webkit-auto;  widows: 2; background-color: rgb(220, 236, 237);">&nbsp;&nbsp;&nbsp;&nbsp;所以目前的根本问题根本就不是什么要不要养狗的问题，而是如何加强对养狗的管理、尤其是对养狗人的管理上进行规范，严格监管。没有人会真正干涉那些爱狗人士的狗道主义，同样也没有人能指责那些对狗害心存防范的市民，双方在权利上是平等的。在当前城市养狗泛滥成灾的情况下，如何减少狗患对人类正常生活的威胁、如何让人与狗和谐相处，其实考验的是城市管理者的能力。</span></p>', '2013-07-01 05:13:49', 37, 4, 0, 0, 1, 12, 'didi', 1, 0, 0, 1, 1, ''),
(27, 2, 2, 24, 'aa', '', '', 'bb', '<p>cc</p>', '2013-07-05 05:20:14', 1, 0, 0, 0, 1, 2, 'uublog', 1, 0, 0, 1, 1, ''),
(28, 2, 2, 24, '巴基斯坦总理北京坐地铁 希望以后自己国家也建(图)', '', '', '午，拥挤的北京地铁六号线迎来了一群特殊客人：巴基斯坦总理纳瓦兹·谢里夫及其随行人员。领导人首访中国是巴外交传统从3日开始，谢里夫开启了为期六天的访华行程。这是谢里夫上月开始新一任总理任期后首次出访，距离中国总理李克强访问巴基斯坦仅一个半月，两国新政府成立之初迅速实现高层互访，也被认为是中巴两国特殊友情的体现。“从中巴之间这样密切的关系和全天候的朋友来讲，这并不奇怪。”中国前驻伊朗、阿联酋、荷兰大使', '<p style="; ; ; ; ; ; line-height: 30px; font-family: SimSun; font-size: 14px; white-space: normal; text-indent: 2em; ">午，拥挤的北京地铁六号线迎来了一群特殊客人：巴基斯坦总理纳瓦兹·谢里夫及其随行人员。</p><p style="; ; ; ; ; ; line-height: 30px; font-family: SimSun; font-size: 14px; white-space: normal; text-indent: 2em; "><strong>领导人首访中国是巴外交传统</strong></p><p style="; ; ; ; ; ; line-height: 30px; font-family: SimSun; font-size: 14px; white-space: normal; text-indent: 2em; ">从3日开始，谢里夫开启了为期六天的访华行程。这是谢里夫上月开始新一任总理任期后首次出访，距离中国总理李克强访问巴基斯坦仅一个半月，两国新政府成立之初迅速实现高层互访，也被认为是中巴两国特殊友情的体现。</p><p style="; ; ; ; ; ; line-height: 30px; font-family: SimSun; font-size: 14px; white-space: normal; text-indent: 2em; ">“从中巴之间这样密切的关系和全天候的朋友来讲，这并不奇怪。”中国前驻伊朗、阿联酋、荷兰大使华黎明告诉记者，自上世纪六十年代以来，巴基斯坦历届总统或总理就任后首访的目</p><p><br/></p>', '2013-07-05 05:22:06', 3, 1, 0, 0, 1, 2, 'uublog', 1, 0, 0, 1, 1, ''),
(29, 3, 3, 2, '西安日系车主被砸成重伤案宣判 主犯获刑10年(图)', '', '', '打砸现场。来源：北京青年报嫌犯。来源：北京青年报　　原标题：西安集中宣判九起故意伤害、寻衅滋事案　　日前，陕西省西安市莲湖区、碑林区、雁塔区、长安区人民法院集中宣判去年9月15日发生的九起故意伤害、寻衅滋事案，十二名被告人分别被判处有期徒刑。　　莲湖区人民法院审理查明：2012年9月15日13时许，被告人蔡洋、寻建奎在西安市玉祥门盗取路边摩托车U型锁，打砸日系车辆。15时40分许，被害人李建利驾驶', '<p><img src="http://www.chinanews.com/fz/2013/07-05/U303P4T8D5009435F107DT20130705161559.jpg" alt="西安日系车主被砸成重伤案宣判主犯获刑10年（图）" style="border-top-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px; border-style: initial; border-color: initial; border-image: initial; "/></p><p>打砸现场。来源：北京青年报</p><p><img src="http://www.chinanews.com/fz/2013/07-05/U303P4T8D5009435F116DT20130705161752.jpg" style="border-top-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px; border-style: initial; border-color: initial; border-image: initial; "/></p><p>嫌犯。来源：北京青年报</p><p style="; ; ; ; ; ; color: rgb(51, 51, 51); letter-spacing: 1px; "><strong>　　原标题：西安集中宣判九起故意伤害、寻衅滋事案</strong></p><p style="; ; ; ; ; ; color: rgb(51, 51, 51); letter-spacing: 1px; ">　　日前，陕西省西安市莲湖区、碑林区、雁塔区、长安区人民法院集中宣判去年9月15日发生的九起故意伤害、寻衅滋事案，十二名被告人分别被判处有期徒刑。</p><p style="; ; ; ; ; ; color: rgb(51, 51, 51); letter-spacing: 1px; ">　　莲湖区人民法院审理查明：2012年9月15日13时许，被告人蔡洋、寻建奎在西安市玉祥门盗取路边摩托车U型锁，打砸日系车辆。15时40分许，被害人李建利驾驶陕A10J00号丰田卡罗拉轿车经过环城西路，被告人寻建奎持砖头砸该车前风挡玻璃和后视镜，李建利阻拦并夺下砖头。被告人蔡洋持U型锁砸前风挡玻璃时，李建利上前阻拦并用砖头砸伤蔡洋头部，蔡洋即用U型锁猛击李建利头部左侧四下，致李建利重伤并五级伤残，被砸车辆维修费7562元。次日，寻建奎向公安机关主动投案。莲湖区人民法院以犯故意伤害罪判处蔡洋有期徒刑九年；犯寻衅滋事罪判处有期徒刑一年零六个月；合并执行有期徒刑十年；并判决赔偿被害人经济损失人民币258860.06元。同案被告人寻建奎因犯寻衅滋事罪，被判处有期徒刑一年。</p><p style="; ; ; ; ; ; color: rgb(51, 51, 51); letter-spacing: 1px; ">　　碑林区人民法院宣判四起案件，对在2012年9月15日发生寻衅滋事行为的五名被告人，分别以犯寻衅滋事罪判处了相应刑罚。判处参与打砸、掀翻5辆日系轿车的被告人李强有期徒刑一年零九个月；判处参与打砸、掀翻4辆日系轿车的被告人胡健利有期徒刑一年零六个月；判处参与在陕西省人大常委会机关大院打砸1辆日系越野车的被告人冯崟有期徒刑一年零二个月；判处参与打砸1辆日系越野车的被告人唐东有期徒刑一年；判处在本市钟楼饭店门前广场打伤执勤武警的被告人王某某(未成年)有期徒刑一年。</p><p><br/></p>', '2013-07-05 05:22:30', 0, 0, 0, 0, 1, 2, 'uublog', 1, 1, 0, 1, 1, '');
INSERT INTO `blog_article` (`id`, `channel1_id`, `channel2_id`, `category_id`, `title`, `pic`, `tags`, `summary`, `content`, `createtime`, `views`, `comments`, `goods`, `bads`, `status`, `user_id`, `username`, `ishome`, `isrecommend`, `istop`, `isoriginal`, `cancomment`, `password`) VALUES
(30, 3, 3, 2, '新疆已有犯罪人员自首 群众上交近千把管制刀具', '', '', '原标题：新疆收缴管制刀具群众已上交近千把　　京华时报讯新疆维吾尔自治区公安厅有关负责人日前表示，收缴管制刀具等物品的通告发布以来，已经收到了群众主动上交的近千把管制刀具，已有违法犯罪人员主动投案自首。　　7月1日至2日，新疆维吾尔自治区公安厅先后发布了《关于检举揭发暴力恐怖犯罪活动的通告》、《关于收缴管制刀具、危爆物品、涉恐涉暴宣传品的通告》和《新疆维吾尔自治区公安厅公告》（通缉令）。公安厅有关负', '<p style="; ; ; ; ; ; font-family: 宋体; font-size: 18px; line-height: 34px; word-wrap: break-word; text-align: left; white-space: normal; -webkit-text-size-adjust: none; ">原标题：新疆收缴管制刀具群众已上交近千把</p><p style="; ; ; ; ; ; font-family: 宋体; font-size: 18px; line-height: 34px; word-wrap: break-word; text-align: left; white-space: normal; -webkit-text-size-adjust: none; ">　　京华时报讯新疆维吾尔自治区公安厅有关负责人日前表示，收缴管制刀具等物品的通告发布以来，已经收到了群众主动上交的近千把管制刀具，已有违法犯罪人员主动投案自首。</p><p style="; ; ; ; ; ; font-family: 宋体; font-size: 18px; line-height: 34px; word-wrap: break-word; text-align: left; white-space: normal; -webkit-text-size-adjust: none; ">　　7月1日至2日，新疆维吾尔自治区公安厅先后发布了《关于检举揭发暴力恐怖犯罪活动的通告》、《关于收缴管制刀具、危爆物品、涉恐涉暴宣传品的通告》和《新疆维吾尔自治区公安厅公告》（通缉令）。公安厅有关负责人接受记者采访时表示，两个《通告》和《公告》发布后，社会反应强烈，各族人民群众积极参与，公安部门已经接到了一些涉恐涉暴违法犯罪线索的举报，收到了群众主动上交的近千把管制刀具，已有违法犯罪人员主动投案自首。（据天山网）</p><p style="; ; ; ; ; ; font-family: 宋体; font-size: 18px; line-height: 34px; word-wrap: break-word; white-space: normal; -webkit-text-size-adjust: none; text-align: center; "><object id="_v_p_913" name="_v_p_913" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=10,1,85,3" width="548" height="411" classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"><embed name="_v_p_913" width="548" height="411" src="http://tv.people.com.cn/img/2011ptv2/playerByOsmfnb.swf?0.7933613189961761" wmode="Window" allowfullscreen="true" allowscriptaccess="always" pluginspage="http://www.adobe.com/shockwave/download/download.cgi?P1_Prod_Version=ShockwaveFlash" flashvars="id=/pvservice/xml/2013/7/2/321d4d20-6af1-430c-a66a-5246bab8e845.xml&amp;noad=1&amp;norecomm=1&amp;skin=2&amp;height=411&amp;width=548&amp;cdn=100%2C0%2C0%2C0&amp;sl=5&amp;ism=1&amp;key=" type="application/x-shockwave-flash"/></object></p><p style="; ; ; ; ; ; font-family: 宋体; font-size: 18px; line-height: 34px; word-wrap: break-word; text-align: left; white-space: normal; -webkit-text-size-adjust: none; ">&nbsp;</p><p><a href="http://tv.people.com.cn/n/2013/0703/c150716-22056453.html" target="_blank" style="color: rgb(0, 0, 0); text-decoration: none; ">新疆维吾尔自治区公安厅关于收缴管制刀具 危爆物品 涉恐涉暴宣传品的通告</a></p><p><br/></p>', '2013-07-05 12:46:55', 1, 0, 0, 0, 1, 2, 'uublog', 1, 1, 0, 1, 1, '');

-- --------------------------------------------------------

--
-- 表的结构 `blog_blog`
--

CREATE TABLE IF NOT EXISTS `blog_blog` (
  `id` int(11) NOT NULL,
  `avatar` varchar(80) DEFAULT ' ',
  `domain` varchar(200) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` varchar(200) NOT NULL,
  `keywords` varchar(200) NOT NULL,
  `about` varchar(500) NOT NULL,
  `announcement` varchar(500) NOT NULL,
  `types` varchar(200) DEFAULT '',
  `listenchannels` varchar(200) DEFAULT '',
  `modules` varchar(1000) NOT NULL,
  `template` varchar(50) NOT NULL,
  `css` varchar(500) NOT NULL,
  `headhtml` varchar(500) NOT NULL,
  `footerhtml` varchar(500) NOT NULL,
  `follows` int(11) DEFAULT '0',
  `todayviews` int(11) NOT NULL,
  `totalviews` int(11) NOT NULL,
  `articles` int(11) NOT NULL,
  `comments` int(11) NOT NULL,
  `suggestes` int(11) DEFAULT '0',
  `lastsuggesttime` datetime DEFAULT NULL,
  `createtime` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

--
-- 转存表中的数据 `blog_blog`
--

INSERT INTO `blog_blog` (`id`, `avatar`, `domain`, `title`, `description`, `keywords`, `about`, `announcement`, `types`, `listenchannels`, `modules`, `template`, `css`, `headhtml`, `footerhtml`, `follows`, `todayviews`, `totalviews`, `articles`, `comments`, `suggestes`, `lastsuggesttime`, `createtime`) VALUES
(1, ' ', '', 'admin的博客', '', '', '', '', '', '', 'profile,hotarticlelist,hotcommentlist', 'default', '', '', '', 3, 10, 10, 0, 0, 0, NULL, '2013-06-21 06:34:56'),
(2, 'blog/avatar/000/00/02.jpg', 'daaa', 'uublog的博客a', 'aa', 'bb', 'cc', 'dd', '2,3,', '', 'profile,category,search,hotuserlist,newuserlist,hotarticlelist,followbloglist,hotcommentlist,badarticlelist,befollowbloglist,goodcommentlist,archive,newarticlelist,newcommentlist,goodarticlelist,bevisitbloglist,badcommentlist,tags,', 'default', 'av', 'bv', 'cv', 2, 252, 252, 16, 6, 2, '2013-07-04 04:35:36', '2013-06-21 06:47:09'),
(3, 'blog/avatar/000/00/03.jpg', '', 'test5的博客', 'test5的博客test5的博客test5的博客test5的博客', '', '', '', '1,8,18,', '8,10,13,', 'profile,hotcommentlist,hotarticlelist,followbloglist,befollowbloglist', 'default', '', '', '', 4, 75, 75, 3, 2, 4, '2013-07-06 12:15:29', '2013-06-28 04:55:23'),
(4, 'blog/avatar/000/00/04.gif', '', 'test6的博客', '', '', '', '', '1,3,11,17,23,', '', 'profile,hotarticlelist,hotcommentlist', 'default', '', '', '', 3, 46, 46, 2, 0, 1, '2013-07-03 12:25:39', '2013-06-28 06:21:42'),
(5, 'blog/avatar/000/00/05.jpg', '', 'xiaohuang的博客', '', '', '', '', '1,5,13,24,', '1,2,', 'profile,category,befollowbloglist,hotarticlelist,hotcommentlist,followbloglist', 'default', '', '', '', 2, 78, 78, 1, 0, 0, NULL, '2013-06-29 10:37:36'),
(6, 'blog/avatar/000/00/06.jpg', '', 'dd的博客', '', '', '', '', '1,6,19,', '', 'profile,category,hotcommentlist,hotarticlelist,followbloglist,bevisitbloglist,', 'default', '', '', '', 4, 69, 69, 1, 0, 0, NULL, '2013-06-30 12:46:42'),
(7, 'blog/avatar/000/00/07.jpg', '', 'kongjian1的博客', '欢迎来我的博客', '', '', '', '1,18,', '67,', 'profile,befollowbloglist,hotcommentlist,hotarticlelist,bevisitbloglist,', 'default', '', '', '', 3, 38, 38, 1, 0, 0, NULL, '2013-06-30 12:55:25'),
(8, '', '', 'kongjian2的博客', '', '', '', '', '', '', 'profile,hotarticlelist,hotcommentlist', 'default', '', '', '', 2, 8, 8, 0, 0, 2, '2013-07-02 05:19:51', '2013-06-30 12:55:35'),
(9, '', '', 'kongjian3的博客', '', '', '', '', '', '', 'profile,hotarticlelist,hotcommentlist', 'default', '', '', '', 2, 0, 0, 0, 0, 0, NULL, '2013-06-30 12:55:45'),
(10, 'blog/avatar/000/00/10.jpg', '', 'kongjian4的博客', '', '', '', '', '2,6,21,', '', 'profile,category,hotcommentlist,hotarticlelist,followbloglist', 'default', '', '', '', 6, 73, 73, 1, 0, 5, '2013-07-02 12:29:09', '2013-06-30 12:55:55'),
(11, 'blog/avatar/000/00/11.jpg', '', 'qiqi的博客', '', '', '', '', '1,4,17,', '', 'profile,category,hotarticlelist,hotcommentlist,followbloglist', 'default', '', '', '', 2, 16, 16, 1, 1, 1, '2013-07-02 04:21:38', '2013-06-30 13:06:58'),
(12, 'blog/avatar/000/00/12.jpg', '', 'didi的博客', 'ddddd', 'asdf', 'aaa', 'dddd', '1,19,', '', 'profile,category,befollowbloglist,hotarticlelist,followbloglist,hotcommentlist,goodarticlelist,bevisitbloglist,', 'default', '', '', '', 4, 112, 112, 1, 6, 5, '2013-07-03 12:46:00', '2013-07-01 04:49:44'),
(14, '', '', 'ddd的博客', '', '', '', '', '', '', 'profile,category,hotarticlelist,hotcommentlist,followbloglist', 'default', '', '', '', 0, 1, 1, 0, 0, 0, '2013-07-02 15:34:16', '2013-07-02 15:34:17'),
(15, '', '', 'ccc的博客', '', '', '', '', '', '', 'profile,category,hotarticlelist,hotcommentlist,followbloglist', 'default', '', '', '', 1, 18, 18, 0, 0, 0, '2013-07-03 01:10:44', '2013-07-03 01:11:03'),
(16, '', '', 'ttt的博客', 'ttt的博客ttt的博客', '', '', '', '', '', 'profile,category,hotarticlelist,hotcommentlist,followbloglist', 'default', '', '', '', 0, 84, 84, 0, 0, 0, '2013-07-03 12:19:23', '2013-07-03 12:20:06'),
(17, '', '', 'aaa的博客', '', '', '', '', '', '', 'profile,category,hotarticlelist,hotcommentlist,followbloglist', 'default', '', '', '', 0, 3, 3, 0, 0, 0, '2013-07-06 12:07:34', '2013-07-06 12:08:33'),
(18, 'blog/avatar/000/00/18.png', '', 'night的博客', '欢迎来night的博客', '', '', '', '2,3,', '', 'profile,category,hotarticlelist,hotcommentlist,followbloglist', 'default', '', '', '', 0, 15, 15, 0, 0, 0, '2013-07-06 14:38:15', '2013-07-06 14:46:00');

-- --------------------------------------------------------

--
-- 表的结构 `blog_blogtype`
--

CREATE TABLE IF NOT EXISTS `blog_blogtype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `blog_id` int(11) DEFAULT NULL,
  `type_id` int(11) DEFAULT NULL,
  `isrecommend` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=43 ;

--
-- 转存表中的数据 `blog_blogtype`
--

INSERT INTO `blog_blogtype` (`id`, `blog_id`, `type_id`, `isrecommend`) VALUES
(1, 3, 1, 1),
(2, 3, 6, 1),
(3, 3, 11, 1),
(4, 4, 15, 1),
(5, 4, 1, 1),
(6, 4, 2, 1),
(7, 4, 3, 1),
(8, 4, 6, 1),
(9, 4, 4, 1),
(10, 4, 18, 1),
(11, 2, 1, 1),
(12, 2, 14, 1),
(16, 2, 18, 1),
(18, 2, 12, 1),
(21, 2, 6, 1),
(22, 2, 10, 1),
(25, 2, 11, 1),
(27, 2, 17, 1),
(29, 2, 24, 1),
(30, 2, 26, 1),
(31, 2, 22, 1),
(32, 2, 20, 1),
(33, 2, 23, 1),
(34, 2, 19, 1),
(35, 2, 25, 1),
(36, 3, 12, 1),
(37, 3, 20, 1),
(38, 3, 26, 1),
(39, 3, 5, 1),
(40, 3, 21, 1),
(41, 3, 22, 1),
(42, 3, 25, 1);

-- --------------------------------------------------------

--
-- 表的结构 `blog_category`
--

CREATE TABLE IF NOT EXISTS `blog_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `sortnum` int(11) NOT NULL,
  `articles` int(11) NOT NULL,
  `isnav` int(11) DEFAULT '0',
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=31 ;

--
-- 转存表中的数据 `blog_category`
--

INSERT INTO `blog_category` (`id`, `name`, `sortnum`, `articles`, `isnav`, `user_id`) VALUES
(1, '未分类', -1, -1, 0, -1),
(2, '明星', 1, 12, 0, 2),
(3, '分类1', 1, 0, 0, 3),
(4, '分类2', 2, 0, 0, 3),
(5, '分类3', 3, 1, 0, 3),
(6, '分类4', 4, 0, 0, 3),
(7, '分类5', 5, 2, 0, 3),
(8, '个人', 1, 0, 0, 5),
(9, '工作', 4, 1, 0, 5),
(10, 'wuwu', 1, 0, 0, 6),
(11, '电影', 2, 0, 0, 6),
(12, '电视', 4, 0, 0, 6),
(13, '音乐', 5, 1, 0, 6),
(14, 'tttt', 1, 0, 0, 10),
(15, 'eee', 3, 0, 0, 10),
(16, 'asfd', 3, 0, 0, 10),
(17, 'asdfddd6', 5, 1, 0, 10),
(18, 'ddd', 2, 0, 0, 11),
(19, 'ttt', 5, 1, 0, 11),
(20, 'hjhhhh', 7, 0, 0, 11),
(21, 'oooo', 1, 0, 0, 7),
(22, 'yyyy', 8, 1, 0, 7),
(23, '自然', 2, 1, 0, 12),
(24, '式', 3, 2, 0, 2),
(25, 'aa', 2, 0, 0, 2),
(28, 'aa', 3, 0, 1, 18),
(29, 'eee', 2, 0, 0, 18),
(30, 'afdas', 4, 0, 1, 18);

-- --------------------------------------------------------

--
-- 表的结构 `blog_channel`
--

CREATE TABLE IF NOT EXISTS `blog_channel` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=68 ;

--
-- 转存表中的数据 `blog_channel`
--

INSERT INTO `blog_channel` (`id`, `parent_id`, `name`, `sortnum`, `articles`, `users`, `user_id`, `username`, `isenable`) VALUES
(1, 0, '摄影', 0, 6, 0, 0, '', 1),
(2, 0, '旅游', 0, 6, 0, 0, '', 1),
(3, 0, '美食', 0, 5, 0, 0, '', 1),
(4, 0, '宠物', 0, 0, 0, 0, '', 1),
(5, 0, '家居', 0, 2, 0, 0, '', 1),
(6, 0, '时尚', 0, 0, 0, 0, '', 1),
(7, 0, '文学', 0, 2, 0, 0, '', 1),
(8, 0, '艺术', 0, 0, 0, 0, '', 1),
(9, 0, '创意', 0, 0, 0, 0, '', 1),
(10, 0, '影视', 0, 2, 0, 0, '', 1),
(11, 0, '美女', 0, 0, 0, 0, '', 1),
(12, 0, '音乐', 0, 0, 0, 0, '', 1),
(13, 0, '游戏', 0, 0, 0, 0, '', 1),
(14, 0, '动漫', 0, 0, 0, 0, '', 1),
(15, 0, '搞笑', 0, 2, 0, 0, '', 1),
(16, 0, '星座', 0, 2, 0, 0, '', 1),
(17, 0, '恋物', 0, 2, 0, 0, '', 1),
(18, 0, '体育', 0, 4, 0, 0, '', 1),
(19, 0, '数码', 0, 0, 0, 0, '', 1),
(20, 0, '科学', 0, 0, 0, 0, '', 1),
(21, 0, '育儿', 0, 0, 0, 0, '', 1),
(22, 0, '心情', 0, 0, 0, 0, '', 1),
(23, 0, '自然', 0, 0, 0, 0, '', 1),
(24, 0, '插画', 0, 0, 0, 0, '', 1),
(25, 0, '明星', 0, 0, 0, 0, '', 1),
(26, 0, '资讯', 0, 2, 0, 0, '', 1),
(27, 0, '生活', 0, 0, 0, 0, '', 1),
(29, 15, '笑话百科', 0, 0, 0, 0, '', 1),
(30, 15, '各种萌', 0, 0, 0, 0, '', 1),
(31, 15, '调侃趣多多', 0, 0, 0, 0, '', 1),
(32, 15, '其他搞笑', 0, 0, 0, 0, '', 1),
(33, 6, '服饰搭配', 0, 0, 0, 0, '', 1),
(34, 6, '鞋包配饰', 0, 0, 0, 0, '', 1),
(35, 6, '奢侈品', 0, 0, 0, 0, '', 1),
(36, 6, '美容美发', 0, 0, 0, 0, '', 1),
(37, 6, '美体瘦身', 0, 0, 0, 0, '', 1),
(38, 6, '购物社区', 0, 0, 0, 0, '', 1),
(39, 6, '其他时尚', 0, 0, 0, 0, '', 1),
(40, 26, '热点资讯', 0, 0, 0, 0, '', 1),
(41, 26, '时事', 0, 0, 0, 0, '', 1),
(42, 26, '军事', 0, 0, 0, 0, '', 1),
(43, 26, '科技数码', 0, 0, 0, 0, '', 1),
(44, 26, '汽车', 0, 0, 0, 0, '', 1),
(45, 26, '体育', 0, 0, 0, 0, '', 1),
(46, 26, '财经', 0, 0, 0, 0, '', 1),
(47, 26, '其他资讯', 0, 0, 0, 0, '', 1),
(48, 2, '国内游', 0, 0, 0, 0, '', 1),
(49, 2, '国外游', 0, 0, 0, 0, '', 1),
(50, 2, '主题游', 0, 0, 0, 0, '', 1),
(51, 2, '人在旅途', 0, 0, 0, 0, '', 1),
(52, 2, '其他旅行', 0, 0, 0, 0, '', 1),
(53, 3, '美味食谱', 0, 0, 0, 0, '', 1),
(54, 3, '烘焙甜品', 0, 0, 0, 0, '', 1),
(55, 3, '美酒饮品', 0, 0, 0, 0, '', 1),
(56, 3, '天下吃货', 0, 0, 0, 0, '', 1),
(57, 3, '其他美食', 0, 0, 0, 0, '', 1),
(58, 10, '电影', 0, 0, 0, 0, '', 1),
(59, 10, '热播剧', 0, 0, 0, 0, '', 1),
(60, 10, '视频', 0, 0, 0, 0, '', 1),
(61, 10, '游戏', 0, 0, 0, 0, '', 1),
(62, 10, '啪啪·唱吧', 0, 0, 0, 0, '', 1),
(63, 10, '音乐', 0, 0, 0, 0, '', 1),
(64, 10, '其他娱乐', 0, 0, 0, 0, '', 1),
(65, 14, '动漫名作', 0, 0, 0, 0, '', 1),
(66, 14, '动漫风格', 0, 0, 0, 0, '', 1),
(67, 14, '动漫达人', 0, 0, 0, 0, '', 1);

-- --------------------------------------------------------

--
-- 表的结构 `blog_comment`
--

CREATE TABLE IF NOT EXISTS `blog_comment` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=16 ;

--
-- 转存表中的数据 `blog_comment`
--

INSERT INTO `blog_comment` (`id`, `article_id`, `user_id`, `username`, `content`, `createtime`, `goods`, `bads`, `reply_id`) VALUES
(1, 1, 2, 'uublog', 'asdfafds', '2013-06-21 09:38:51', 0, 0, 0),
(2, 9, 2, 'uublog', '残酷的竞争中杀出一条血路。\r\n　　中国内互联网企业的厮杀也异常激烈，大企业瞬间复制模仿你，秒杀你，2004年9月，QQ游戏平台将联众赶下了中国第一休闲游戏门户的宝座。我记得那个时候室友还在上面玩游戏，现在联众早已被网民遗忘，以至于记得当时的新闻是，"多年以后，在北京知春路的一家咖啡馆，联众创始人鲍岳桥谈起当年腾讯对联众的围剿和逼迫，仍然耿耿于怀。在两个小时的采访中，他连续抽了两包烟"。20', '2013-06-22 05:24:02', 0, 0, 0),
(3, 26, 2, 'uublog', 'gggg', '2013-07-02 12:29:56', 0, 0, 0),
(4, 26, 2, 'uublog', 'gggg', '2013-07-02 12:30:10', 0, 0, 0),
(5, 9, 2, 'uublog', 'FFFF', '2013-07-02 12:39:47', 0, 0, 0),
(6, 15, 16, 'ttt', '磊', '2013-07-03 13:12:44', 0, 0, 0),
(7, 26, 15, 'username', 'content', '2013-07-04 14:03:58', 0, 0, 0),
(8, 26, 15, 'username', 'content', '2013-07-04 14:04:18', 0, 0, 0),
(9, 26, 2, 'uublog', 'adfsadeee', '2013-07-05 08:54:40', 0, 0, 0),
(10, 26, 2, 'uublog', '胁要泼硫酸，则证明了中国的某些狗粉们已经沦落到了与恶狗为伍的地步，本来狗只是通人性的动物，爱狗人士总喜欢以狗对主人忠诚而将狗比作比人类还高尚，但狗忠诚主人并不意味着它们不咬别人，这种高尚就算成立也是自私的。相反目前一些狗粉们动辄极端的个人言行却彰显出确实比狗还低劣，谩骂加暴力，与西方在对待狗的态度上崇尚的爱心可谓南辕北辙。\r\n', '2013-07-05 08:56:07', 0, 0, 0),
(11, 15, 2, 'uublog', '里面拍产品照，结果看见两个新娘进来拍照。\r\n我们老大很惊奇地问，这是怎么回事呢？新郎呢？\r\n然后摄影师说，她们拍得是闺蜜', '2013-07-05 08:58:30', 0, 0, 0),
(12, 24, 2, 'uublog', '面试我，这次终于也当了一次面试官。这次才真正体会到，其实面试官有时候可能比求职者，要付出更多时间来准', '2013-07-05 09:01:08', 0, 0, 0),
(13, 28, 2, 'uublog', '近平会见西班牙众议长', '2013-07-06 02:54:13', 0, 0, 0),
(14, 11, 2, 'uublog', '者提问\r\n　　（1）对我们团队，对我们公司，有什么需要，或者感兴趣想了解的？\r\n　　结尾\r\n　　OK，那就先到这里，如果有后续面试的话，再通知你。拜拜。\r\n　　面试别人的收获总结：\r\n　　（1）在面试的过', '2013-07-06 03:29:06', 0, 0, 0),
(15, 8, 2, 'uublog', 'stone Preview 的截图出现在网上，如果图片并非伪造，那它就可能是微软将于 6 月 26 日发布的 Windows 8.1 公开预览版（也就是 Beta 公测版）。', '2013-07-06 03:30:03', 0, 0, 0);

-- --------------------------------------------------------

--
-- 表的结构 `blog_follow`
--

CREATE TABLE IF NOT EXISTS `blog_follow` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `blog_id` int(11) DEFAULT NULL,
  `follow_blog_id` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=90 ;

--
-- 转存表中的数据 `blog_follow`
--

INSERT INTO `blog_follow` (`id`, `blog_id`, `follow_blog_id`) VALUES
(43, 5, 3),
(44, 5, 2),
(45, 5, 5),
(46, 3, 2),
(47, 6, 3),
(48, 6, 2),
(49, 6, 5),
(50, 10, 3),
(51, 7, 2),
(52, 7, 6),
(53, 7, 3),
(54, 7, 7),
(55, 7, 5),
(56, 7, 4),
(57, 5, 6),
(58, 7, 12),
(59, 7, 10),
(60, 7, 1),
(61, 3, 10),
(62, 3, 8),
(63, 12, 6),
(64, 12, 11),
(65, 12, 8),
(66, 12, 10),
(67, 12, 1),
(68, 12, 3),
(69, 2, 12),
(70, 2, 10),
(71, 6, 10),
(72, 12, 7),
(73, 12, 2),
(74, 12, 4),
(75, 12, 9),
(76, 12, 9),
(77, 3, 12),
(78, 16, 4),
(79, 16, 3),
(80, 16, 10),
(81, 16, 12),
(82, 16, 1),
(83, 16, 2),
(84, 16, 11),
(85, 16, 15),
(86, 16, 6),
(87, 16, 7),
(88, 12, 5),
(89, 17, 3);

-- --------------------------------------------------------

--
-- 表的结构 `blog_suggest`
--

CREATE TABLE IF NOT EXISTS `blog_suggest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `blog_id` int(11) DEFAULT NULL,
  `suggest_blog_id` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=79 ;

--
-- 转存表中的数据 `blog_suggest`
--

INSERT INTO `blog_suggest` (`id`, `blog_id`, `suggest_blog_id`) VALUES
(48, 6, 2),
(50, 10, 3),
(55, 7, 5),
(60, 7, 10),
(61, 7, 3),
(62, 3, 10),
(63, 3, 8),
(64, 12, 11),
(65, 12, 10),
(66, 12, 8),
(67, 12, 3),
(68, 2, 12),
(69, 2, 12),
(70, 2, 12),
(71, 2, 10),
(72, 2, 12),
(73, 16, 4),
(74, 16, 12),
(75, 16, 3),
(76, 16, 2),
(77, 12, 2),
(78, 17, 3);

-- --------------------------------------------------------

--
-- 表的结构 `blog_type`
--

CREATE TABLE IF NOT EXISTS `blog_type` (
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
-- 转存表中的数据 `blog_type`
--

INSERT INTO `blog_type` (`id`, `parent_id`, `name`, `sortnum`, `articles`, `users`, `user_id`, `username`, `isenable`) VALUES
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
-- 表的结构 `blog_visit`
--

CREATE TABLE IF NOT EXISTS `blog_visit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `blog_id` int(11) DEFAULT NULL,
  `visit_blog_id` int(11) DEFAULT '0',
  `lastvisittime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=49 ;

--
-- 转存表中的数据 `blog_visit`
--

INSERT INTO `blog_visit` (`id`, `blog_id`, `visit_blog_id`, `lastvisittime`) VALUES
(1, 12, 11, '2013-07-02 09:09:20'),
(2, 7, 11, '2013-07-02 09:09:20'),
(3, 7, 7, '2013-07-02 09:09:20'),
(4, 12, 7, '2013-07-02 09:09:20'),
(5, 7, 3, '2013-07-02 09:09:20'),
(6, 12, 6, '2013-07-02 09:14:07'),
(7, 7, 6, '2013-07-02 09:15:03'),
(8, 6, 6, '2013-07-02 09:15:44'),
(9, 2, 10, '2013-07-02 12:00:48'),
(10, 2, 12, '2013-07-02 12:22:54'),
(11, 2, 7, '2013-07-02 12:32:08'),
(12, 12, 4, '2013-07-02 13:26:40'),
(13, 12, 3, '2013-07-02 13:26:47'),
(14, 6, 12, '2013-07-02 15:15:55'),
(15, 12, 15, '2013-07-03 04:28:41'),
(16, 12, 8, '2013-07-03 04:29:00'),
(17, 12, 10, '2013-07-03 04:29:13'),
(18, 3, 6, '2013-07-03 06:16:36'),
(19, 12, 5, '2013-07-03 09:07:17'),
(20, 16, 4, '2013-07-03 12:21:14'),
(21, 16, 3, '2013-07-03 12:26:26'),
(22, 16, 10, '2013-07-03 12:29:42'),
(23, 16, 12, '2013-07-03 12:47:22'),
(24, 16, 6, '2013-07-03 13:11:01'),
(25, 3, 10, '2013-07-03 13:46:40'),
(26, 16, 7, '2013-07-03 14:07:20'),
(27, 16, 2, '2013-07-03 14:08:31'),
(28, 12, 2, '2013-07-04 04:35:33'),
(29, 15, 2, '2013-07-04 08:02:38'),
(30, 15, 10, '2013-07-04 12:38:40'),
(31, 15, 7, '2013-07-04 12:49:31'),
(32, 15, 12, '2013-07-04 13:03:34'),
(33, 2, 5, '2013-07-05 07:58:53'),
(34, 2, 3, '2013-07-05 08:58:24'),
(35, 2, 11, '2013-07-05 09:01:03'),
(36, 2, 16, '2013-07-06 03:16:47'),
(37, 2, 1, '2013-07-06 03:16:54'),
(38, 2, 8, '2013-07-06 03:16:57'),
(39, 2, 4, '2013-07-06 03:37:25'),
(40, 2, 14, '2013-07-06 04:38:12'),
(41, 17, 2, '2013-07-06 12:09:57'),
(42, 17, 6, '2013-07-06 12:10:00'),
(43, 17, 3, '2013-07-06 12:15:22'),
(44, 18, 12, '2013-07-07 00:53:51'),
(45, 18, 6, '2013-07-07 00:54:22'),
(46, 18, 3, '2013-07-07 03:52:03'),
(47, 18, 5, '2013-07-07 03:52:26'),
(48, 18, 11, '2013-07-07 07:21:49');

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
) ENGINE=InnoDB  DEFAULT CHARSET=gbk AUTO_INCREMENT=16 ;

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
(14, 'blog', 'UUBlog', 'blog'),
(15, 'user profile', 'Accounts', 'userprofile');

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
('0cwoelnb1xzo3ntbrx9zfwh2si1aji8f', 'N2FkMWY0OGJiNzQ5YjZlNGQxZDJmYjZlMmUwODY4YTMwNDI0OGQ5MTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQN1Lg==', '2013-07-14 00:16:29'),
('6s0cippj3s07mnn2vrz182zvvacz3nl0', 'MDU0MzZjYWUzMDQ0ZjJhNzhlNGIwMWE3NzI1YWU0MThiOWNlYmEwNDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARJ1Lg==', '2013-07-20 14:46:16'),
('d8swek4p9m80laudzamwfqr5c72bw6kn', 'MjNmODE5Y2U3MDRkNGQyNzAxMDNjNTJjYmFlNTVmYWRjNjcxMWZjYTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARB1Lg==', '2013-07-17 12:20:20'),
('i1nhm8yddl36q9ls0yih3esy62whyw5p', 'N2FkMWY0OGJiNzQ5YjZlNGQxZDJmYjZlMmUwODY4YTMwNDI0OGQ5MTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQN1Lg==', '2013-07-12 15:08:14'),
('jyrrjd6zxrgfydeobz0daltcsxyzoyyt', 'ODdmNTA3M2M4YTc1MWIwMTI4M2E1ZGViOTA2YzJhY2ZjZmFiNGNhMzqAAn1xAS4=', '2013-07-12 13:24:48'),
('l555d99wbp9cgv1tlj1krq3kby1r1o0b', 'ODdmNTA3M2M4YTc1MWIwMTI4M2E1ZGViOTA2YzJhY2ZjZmFiNGNhMzqAAn1xAS4=', '2013-07-20 12:05:38'),
('oyodyswrpzc5ajylw6o2wy9l8jbuwab7', 'NDg1MWI3YjZmYjg2OTc2Y2Q0ZjdhN2RhOWEyM2MxNjM0NDk4YTU1MTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQx1Lg==', '2013-07-15 04:49:52');

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
