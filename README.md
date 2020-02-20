Python Django新闻网站
====================

目标
----
- [X] 新闻采集
- [X] 使用Django展示新闻
- [X] 后台管理新闻
- [X] 管理新闻模板

快速运行
-------
    $ pip install -r requirements.txt
    $ python web/manage.py runserver

管理员用户 admin 密码 admin

爬取
---
    $ cd scrape
    $ scrapy crawl netease

项目结构
-------
scrape/ 是一个scrapy项目,爬取网易新闻并保存到数据库
web/ 是一个django项目,展示和管理爬取到的新闻

注意事项
-------
scrapy在Windows下如果安装失败,最简单的解决方法是手动安装编译过的Twisted
