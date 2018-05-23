# scrapyForLearn
python爬虫(Scrapy)学习日志


## 2018-05-23
下午粗略的将简书首页的文章列表信息抓成json格式

比如，假设你想提取在 <div> 元素中的所有 <p> 元素。首先，你将先得到所有的 <div> 元素:

``` python
>>> divs = response.xpath('//div') 
```
开始时，你可能会尝试使用下面的错误的方法，因为它其实是从整篇文档中，而不仅仅是从那些 <div> 元素内部提取所有的 <p> 元素:

``` python
>>> for p in divs.xpath('//p'):  # this is wrong - gets all <p> from the whole document
...     print p.extract() 
```
下面是比较合适的处理方法(注意 .//p XPath的点前缀):

``` python
>>> for p in divs.xpath('.//p'):  # extracts all <p> inside
...     print p.extract() 
```
另一种常见的情况将是提取所有直系 <p> 的结果:

``` python
>>> for p in divs.xpath('p'):
...     print p.extract() 
```

###今天看到使用选择器的 使用EXSLT扩展
https://scrapy-chs.readthedocs.io/zh_CN/latest/topics/selectors.html#exslt
