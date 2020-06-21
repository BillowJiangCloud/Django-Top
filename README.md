## 分数TOP

> 本Demo用到了redis缓存，前提安装好Redis。

#### 一、下载依赖

pip install -m yilai.txt

#### 二、数据库

数据库用Django框架自带的Sqlite3数据库。

数据来源：随机出10个用户，以及随机出1...10000000范围的分数。

#### 三、缓存

本Demo用到Redis缓存数据，提高效率。

#### 四、功能

登录、排行榜范围查询以及自身榜定位、登录用户上传分数；

每次查询的最后，都会附加上调用接口的客户端的排名。

##### 结尾：Demo下载后，安装完依赖即可正常运行。



**附加题：**

> 版本号比较。
>
> 比较两个版本号 version1 和 version2。
> 如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。

解题文件：version.py