# scrapyForLearn
python爬虫(Scrapy)学习日志


## 2018-05-23
下午粗略的将简书首页的文章列表信息抓成json格式

比如，假设你想提取在 \<div> 元素中的所有 \<p> 元素。首先，你将先得到所有的 \<div> 元素:

``` python
>>> divs = response.xpath('//div') 
```
开始时，你可能会尝试使用下面的错误的方法，因为它其实是从整篇文档中，而不仅仅是从那些 \<div> 元素内部提取所有的 \<p> 元素:

``` python
>>> for p in divs.xpath('//p'):  # this is wrong - gets all <p> from the whole document
...     print p.extract() 
```
下面是比较合适的处理方法(注意 .//p XPath的点前缀):

``` python
>>> for p in divs.xpath('.//p'):  # extracts all <p> inside
...     print p.extract() 
```
另一种常见的情况将是提取所有直系 \<p> 的结果:

``` python
>>> for p in divs.xpath('p'):
...     print p.extract() 
```

###今天看到使用选择器的 使用EXSLT扩展
https://scrapy-chs.readthedocs.io/zh_CN/latest/topics/selectors.html#exslt


## 2018-05-24

### Item Loaders
Item Loaders提供了一种便捷的方式填充抓取到的 Items 。 虽然Items可以使用自带的类字典形式API填充，但是Items Loaders提供了更便捷的API， 可以分析原始数据并对Item进行赋值。

大概就是为Item原生数据过滤格式的

### Item Pipeline

当Item在Spider中被收集之后，它将会被传递到Item Pipeline，一些组件会按照一定的顺序执行对Item的处理。

可以做到去重、写入JSON文件、写入mongoDB等等

启用一个Item Pipeline组件
为了启用一个Item Pipeline组件，你必须将它的类添加到 ITEM_PIPELINES 配置，就像下面这个例子:
```python
ITEM_PIPELINES = {
    'myproject.pipelines.PricePipeline': 300,
    'myproject.pipelines.JsonWriterPipeline': 800,
}
```
分配给每个类的整型值，确定了他们运行的顺序，item按数字从低到高的顺序，通过pipeline，通常将这些数字定义在0-1000范围内。

###Feed exports
实现爬虫时最经常提到的需求就是能合适的保存爬取到的数据，或者说，生成一个带有爬取数据的”输出文件”(通常叫做”输出feed”)，来供其他系统使用。

其自带支持的类型有:JSON ,JSON lines,CSV,XML ,也可以通过 FEED_EXPORTERS 设置扩展支持的属性。


###看到有点头痛先看到这 https://scrapy-chs.readthedocs.io/zh_CN/master/topics/broad-crawls.html