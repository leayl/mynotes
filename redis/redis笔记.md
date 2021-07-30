## redis运行

服务端：redis-server

客户端：redis-cli [-h ip -p port -a password]

## redis配置

配置文件：redis.windows.conf

命令格式：CONFIG GET 配置名

1. 查看所有配置项：CONFIG GET *

设置配置：CONFIG SET 配置名 配置值

![image-20210417220044816](.\redis笔记\image-20210417220044816.png)

![image-20210417220158811](.\redis笔记\image-20210417220158811.png)

![image-20210417220215066](.\redis笔记\image-20210417220215066.png)

![image-20210417220331598](.\redis笔记\image-20210417220331598.png)

![image-20210417220419748](.\redis笔记\image-20210417220419748.png)

![image-20210417220500432](.\redis笔记\image-20210417220500432.png)

## redis keys 命令

语法：COMMAND KEY_NAME

设置：SET keyname key_value

删除：DEL keyname，执行成功返回1，否则0

命令：https://www.runoob.com/redis/redis-keys.html

| 序号 | 命令                                       | 用法                                                         |
| ---- | ------------------------------------------ | :----------------------------------------------------------- |
| 1    | DEL key                                    | key存在时删除key                                             |
| 2    | DUMP key                                   | 序列化给定 key ，并返回被序列化的值                          |
| 3    | EXISTS key                                 | 检查给定 key 是否存在                                        |
| 4    | EXPIRE key sedonds                         | 为给定 key 设置过期时间，以秒计                              |
| 5    | EXPIREAT key timestamp                     | EXPIREAT 的作用和 EXPIRE 类似，都用于为 key 设置过期时间。 不同在于 EXPIREAT 命令接受的时间参数是 UNIX 时间戳(unix timestamp) |
| 6    | EXPIREAT key milliseconds                  | 设置 key 过期时间的时间戳(unix timestamp) 以毫秒计           |
| 7    | PEXPIREAT key milliseconds-timestamp       | 设置 key 过期时间的时间戳(unix timestamp) 以毫秒计           |
| 8    | KEYS pattern                               | 查找所有符合给定模式( pattern)的 key                         |
| 9    | MOVE key db                                | 将当前数据库的 key 移动到给定的数据库 db 当中                |
| 10   | PERSIST key                                | 移除 key 的过期时间，key 将持久保持                          |
| 11   | PTTL key                                   | 以毫秒为单位返回 key 的剩余的过期时间                        |
| 12   | TTL key                                    | 以秒为单位，返回给定 key 的剩余生存时间(TTL, time to live)   |
| 13   | RANDOMKEY                                  | 从当前数据库中随机返回一个 key                               |
| 14   | RENAME key newkey                          | 修改 key 的名称                                              |
| 15   | RENAMEX key newkey                         | 仅当 newkey 不存在时，将 key 改名为 newkey                   |
| 16   | SCAN cursor [MATCH pattern\] [COUNT count] | 迭代数据库中的数据库键                                       |
| 17   | TYPE key                                   | 返回 key 所储存的值的类型                                    |



## redis数据类型

### String（字符串）

string类型是二进制安全的，可以包含任何数据。比如jpg图片或者序列化的对象。

string 类型是 Redis 最基本的数据类型，string 类型的值最大能存储 512MB。

`SET testkey "例子字符"`

`GET testkey`

`"例子字符"`

String命令

![image-20210417230450451](.\redis笔记\image-20210417230450451.png)

![image-20210417230553215](.\redis笔记\image-20210417230553215.png)

### Hash（哈希）

Redis hash 是一个键值(key=>value)对集合。

Redis hash 是一个 string 类型的 field 和 value 的映射表，hash 特别适合用于存储对象。

Redis 中每个 hash 可以存储 2^32 - 1 键值对（40多亿）

HMSET test_hash name 'yl' age '25'

```
127.0.0.1:6379> HMSET test_hash name 'yl' age '25'
OK
127.0.0.1:6379> HGETALL test_hash
1) "name"
2) "yl"
3) "age"
4) "25"
127.0.0.1:6379> HGET test_hash name
"yl"
127.0.0.1:6379> HMGET test_hash name
1) "yl"
127.0.0.1:6379> HMGET test_hash name age
1) "yl"
2) "25"
```

Hash命令

![image-20210417233352287](.\redis笔记\image-20210417233352287.png)

![image-20210417233411349](.\redis笔记\image-20210417233411349.png)

### List（列表）

Redis列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）

一个列表最多可以包含 2^32 - 1 个元素 (4294967295, 每个列表超过40亿个元素)

```
127.0.0.1:6379> LPUSH test_list 1
(integer) 1
127.0.0.1:6379> LPUSH test_list 2 3 4
(integer) 4
127.0.0.1:6379> LRANGE test_list 0 -1
1) "4"
2) "3"
3) "2"
4) "1"
```

List命令

![image-20210417233747892](.\redis笔记\image-20210417233747892.png)

![image-20210417233807584](.\redis笔记\image-20210417233807584.png)

### Set（集合）

Redis 的 Set 是 String 类型的无序集合。集合成员是唯一的，这就意味着集合中不能出现重复的数据。

Redis 中集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。

集合中最大的成员数为 2^32 - 1 (4294967295, 每个集合可存储40多亿个成员)。

```
127.0.0.1:6379> SADD test_set 1 2 3 1
(integer) 3
127.0.0.1:6379> SMEMBERS test_set
1) "1"
2) "2"
3) "3"
```

Set命令

![image-20210417234047370](.\redis笔记\image-20210417234047370.png)

![image-20210417234109951](D:\study\mynotes\redis\redis笔记\image-20210417234109951.png)

### zset（sorted set：有序集合）

Redis 有序集合和集合一样也是 string 类型元素的集合,且不允许重复的成员。

不同的是每个元素都会关联一个 **double 类型的分数**。redis 正是通过分数来为集合中的成员进行从小到大的排序。

有序集合的成员是唯一的,但**分数(score)却可以重复**。

集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。 集合中最大的成员数为 2**32 - 1 (4294967295, 每个集合可存储40多亿个成员)。

语法：COMMAND setkeyname score member

```
127.0.0.1:6379> ZADD test_zset 1 yl 2 dl 1 dll
(integer) 3
127.0.0.1:6379> ZRANGE test_zset 0 -1
1) "dll"
2) "yl"
3) "dl"
127.0.0.1:6379> ZRANGE test_zset 0 -1 WITHSCORES
1) "dll"
2) "1"
3) "yl"
4) "1"
5) "dl"
6) "2"
```

zset命令

![image-20210417234827910](.\redis笔记\image-20210417234827910.png)

![image-20210417234850929](.\redis笔记\image-20210417234850929.png)

