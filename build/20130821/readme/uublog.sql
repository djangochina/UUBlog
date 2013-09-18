-- phpMyAdmin SQL Dump
-- version 3.2.0.1
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2013 年 08 月 21 日 20:02
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
-- 表的结构 `blog_blog`
--

CREATE TABLE IF NOT EXISTS `blog_blog` (
  `id` int(11) NOT NULL,
  `avatar` varchar(80) CHARACTER SET utf8 DEFAULT ' ',
  `domain` varchar(200) CHARACTER SET utf8 NOT NULL,
  `title` varchar(200) CHARACTER SET utf8 NOT NULL,
  `description` varchar(200) CHARACTER SET utf8 NOT NULL,
  `keywords` varchar(200) CHARACTER SET utf8 NOT NULL,
  `about` varchar(500) CHARACTER SET utf8 NOT NULL,
  `announcement` varchar(500) CHARACTER SET utf8 NOT NULL,
  `types` varchar(200) CHARACTER SET utf8 DEFAULT NULL,
  `listenchannels` varchar(200) CHARACTER SET utf8 DEFAULT NULL,
  `modules` varchar(1000) CHARACTER SET utf8 NOT NULL,
  `template` varchar(50) CHARACTER SET utf8 NOT NULL,
  `css` varchar(500) CHARACTER SET utf8 NOT NULL,
  `headhtml` varchar(500) CHARACTER SET utf8 NOT NULL,
  `footerhtml` varchar(500) CHARACTER SET utf8 NOT NULL,
  `follows` int(11) DEFAULT '0' COMMENT '关注的人数',
  `befollows` int(11) DEFAULT '0' COMMENT '被关注数量（粉丝数）',
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

INSERT INTO `blog_blog` (`id`, `avatar`, `domain`, `title`, `description`, `keywords`, `about`, `announcement`, `types`, `listenchannels`, `modules`, `template`, `css`, `headhtml`, `footerhtml`, `follows`, `befollows`, `todayviews`, `totalviews`, `articles`, `comments`, `suggestes`, `lastsuggesttime`, `createtime`) VALUES
(1, 'blog/avatar/000/00/01.gif', '', 'admin的博客', 'dddaa', 'test', ' aaaa', 'aaaa', '1,12,13,', '', 'profile,hotarticlelist,hotcommentlist', 'default', '', '', '', 9, 0, 197, 197, 4, 0, 0, NULL, '2013-06-21 06:34:56'),
(2, 'blog/avatar/000/00/02.jpg', 'daaa', 'uublog的博客a', 'aa', 'bb', 'cc', 'dd', '2,3,', '', 'profile,category,search,hotuserlist,newuserlist,hotarticlelist,followbloglist,hotcommentlist,badarticlelist,befollowbloglist,goodcommentlist,archive,newarticlelist,newcommentlist,goodarticlelist,bevisitbloglist,badcommentlist,tags,', 'default', 'av', 'bv', 'cv', 2, 0, 284, 284, 16, 6, 2, '2013-07-04 04:35:36', '2013-06-21 06:47:09'),
(3, 'blog/avatar/000/00/03.jpg', '', 'test5的博客', 'test5的博客test5的博客test5的博客test5的博客', '', '', '', '1,8,18,', '8,10,13,', 'profile,hotcommentlist,hotarticlelist,followbloglist,befollowbloglist', 'default', '', '', '', 4, 0, 98, 98, 3, 2, 4, '2013-07-06 12:15:29', '2013-06-28 04:55:23'),
(4, 'blog/avatar/000/00/04.gif', '', 'test6的博客', '', '', '', '', '1,3,11,17,23,', '', 'profile,hotarticlelist,hotcommentlist', 'default', '', '', '', 3, 0, 52, 52, 2, 0, 1, '2013-07-03 12:25:39', '2013-06-28 06:21:42'),
(5, 'blog/avatar/000/00/05.jpg', '', 'xiaohuang的博客', '', '', '', '', '1,5,13,24,', '1,2,', 'profile,category,befollowbloglist,hotarticlelist,hotcommentlist,followbloglist', 'default', '', '', '', 2, 0, 81, 81, 1, 0, 0, NULL, '2013-06-29 10:37:36'),
(6, 'blog/avatar/000/00/06.jpg', '', 'dd的博客', '', '', '', '', '1,6,19,', '', 'profile,category,hotcommentlist,hotarticlelist,followbloglist,bevisitbloglist,', 'default', '', '', '', 4, 0, 75, 75, 1, 0, 0, NULL, '2013-06-30 12:46:42'),
(7, 'blog/avatar/000/00/07.jpg', '', 'kongjian1的博客', '欢迎来我的博客', '', '', '', '1,18,', '67,', 'profile,befollowbloglist,hotcommentlist,hotarticlelist,bevisitbloglist,', 'default', '', '', '', 3, 0, 47, 47, 2, 0, 0, NULL, '2013-06-30 12:55:25'),
(8, '', '', 'kongjian2的博客', '', '', '', '', '', '', 'profile,hotarticlelist,hotcommentlist', 'default', '', '', '', 2, 0, 16, 16, 2, 0, 2, '2013-07-02 05:19:51', '2013-06-30 12:55:35'),
(9, '', '', 'kongjian3的博客', '', '', '', '', '', '', 'profile,hotarticlelist,hotcommentlist', 'default', '', '', '', 2, 0, 16, 16, 5, 0, 0, NULL, '2013-06-30 12:55:45'),
(10, 'blog/avatar/000/00/10.jpg', '', 'kongjian4的博客', '', '', '', '', '2,6,21,', '', 'profile,category,hotcommentlist,hotarticlelist,followbloglist', 'default', '', '', '', 6, 2, 95, 95, 1, 0, 6, '2013-07-12 11:09:16', '2013-06-30 12:55:55'),
(11, 'blog/avatar/000/00/11.jpg', '', 'qiqi的博客', '', '', '', '', '1,4,17,', '', 'profile,category,hotarticlelist,hotcommentlist,followbloglist', 'default', '', '', '', 2, 0, 18, 18, 1, 1, 1, '2013-07-02 04:21:38', '2013-06-30 13:06:58'),
(12, 'blog/avatar/000/00/12.jpg', '', '悠悠闲云', '凤凰论坛高级写手。天涯名博', 'asdf', 'aaa', 'dddd', '1,19,', '', 'profile,category,befollowbloglist,hotarticlelist,followbloglist,hotcommentlist,goodarticlelist,bevisitbloglist,', 'default', '', '', '', 4, 4, 149, 149, 2, 6, 5, '2013-07-03 12:46:00', '2013-07-01 04:49:44'),
(14, '', '', 'ddd的博客', '', '', '', '', '', '', 'profile,category,hotarticlelist,hotcommentlist,followbloglist', 'default', '', '', '', 0, 1, 7, 7, 0, 0, 0, '2013-07-02 15:34:16', '2013-07-02 15:34:17'),
(15, '', '', 'ccc的博客', '', '', '', '', '', '', 'profile,category,hotarticlelist,hotcommentlist,followbloglist', 'default', '', '', '', 1, 0, 20, 20, 0, 0, 0, '2013-07-03 01:10:44', '2013-07-03 01:11:03'),
(16, '', '', 'ttt的博客', 'ttt的博客ttt的博客', '', '', '', '', '', 'profile,category,hotarticlelist,hotcommentlist,followbloglist', 'default', '', '', '', 0, 0, 87, 87, 0, 0, 0, '2013-07-03 12:19:23', '2013-07-03 12:20:06'),
(17, '', '', 'aaa的博客', '', '', '', '', '', '', 'profile,category,hotarticlelist,hotcommentlist,followbloglist', 'default', '', '', '', 0, 0, 7, 7, 0, 0, 0, '2013-07-06 12:07:34', '2013-07-06 12:08:33'),
(18, 'blog/avatar/000/00/18.png', '', 'night的博客', '欢迎来night的博客', '', '', '', '2,3,', '', 'profile,category,hotarticlelist,hotcommentlist,followbloglist', 'default', '', '', '', 1, 0, 22, 22, 0, 0, 0, '2013-07-06 14:38:15', '2013-07-06 14:46:00'),
(19, '', '', 'one的博客', '欢迎来one的博客', 'one', '', '', '1,2,', '', 'profile,category,hotarticlelist,hotcommentlist,followbloglist,bevisitbloglist', 'default', '', '', '', 1, 1, 72, 72, 8, 0, 1, '2013-07-16 09:37:23', '2013-07-08 06:23:16'),
(20, '', '', 'ni的博客', '欢迎来ni的博客', 'ni', '', '', '', '', 'profile,category,hotarticlelist,hotcommentlist,followbloglist,bevisitbloglist', 'default', '', '', '', 1, 0, 5, 5, 0, 0, 0, '2013-07-08 13:10:58', '2013-07-08 13:11:38'),
(22, '', '', 'gg的博客', '欢迎来gg的博客', 'gg', '', '', '', '', 'profile,category,hotarticlelist,hotcommentlist,followbloglist,bevisitbloglist', 'default', '', '', '', 0, 0, 2, 2, 0, 0, 0, '2013-07-09 12:41:35', '2013-07-09 12:48:55'),
(23, '', '', 'tt的博客', '欢迎来tt的博客', 'tt', '', '', '', '', 'profile,category,hotarticlelist,hotcommentlist,followbloglist,bevisitbloglist', 'default', '', '', '', 0, 0, 6, 6, 0, 0, 0, '2013-07-09 13:45:34', '2013-07-09 14:13:29'),
(28, '', '', 'aa的博客', '欢迎来aa的博客', 'aa', '', '', '', '', 'profile,category,hotarticlelist,hotcommentlist,followbloglist,bevisitbloglist', 'default', '', '', '', 0, 1, 4, 4, 0, 0, 0, '2013-07-10 04:59:34', '2013-07-10 05:06:42'),
(30, 'blog/avatar/000/00/30.jpg', 'aaa', 'aab的博客', '欢迎来aab的博客', 'aab', ' ', '', '1,2,19,', '', 'profile,category,hotarticlelist,hotcommentlist,followbloglist,bevisitbloglist', 'temp1', '', '', '', 4, 1, 259, 259, 45, 1, 0, '2013-07-10 05:12:23', '2013-07-10 06:45:16'),
(31, '', '', 'jianjian的博客', '欢迎来jianjian的博客', 'jianjian', '', '', '', '', 'profile,category,hotarticlelist,hotcommentlist,followbloglist,bevisitbloglist', 'default', '', '', '', 0, 1, 19, 19, 1, 0, 0, '2013-07-21 12:44:41', '2013-07-21 12:48:27');
