# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DouBanItem(scrapy.Item):

    likes = scrapy.Field()  # 点赞数量
    title = scrapy.Field()  # 文章标题
    pic = scrapy.Field()  # 文章缩略图
    abstract = scrapy.Field()  # 文章摘要
    source = scrapy.Field()  # 源自什么小组
    pubtime = scrapy.Field()  # 发表时间

class JianShuItem(scrapy.Item):
    # author = scrapy.Field()  # 作者信息
    # avatar = scrapy.Field()  # 头像
    nickname = scrapy.Field()  # 作者昵称
    title = scrapy.Field()  # 文章标题
    createTime = scrapy.Field() #发表时间
    abstract = scrapy.Field()  # 文章摘要
    read = scrapy.Field()  # 浏览数量
    comments = scrapy.Field()  # 评论数量
    like = scrapy.Field()  # 点赞数量
    money = scrapy.Field()  # 打赏金额


class ZhiHuItem(scrapy.Item):
    # author = scrapy.Field()  # 作者信息
    avatar = scrapy.Field()  # 头像
    nickname = scrapy.Field()  # 作者昵称
    flag = scrapy.Field() #作者标签
    title = scrapy.Field()  # 文章标题
    abstract = scrapy.Field()  # 文章摘要
    comments = scrapy.Field()  # 评论数量
    like = scrapy.Field()  # 点赞数量