#!/usr/bin/python
# -*- coding:utf-8 -*-
# refrence: https://redis-py.readthedocs.io/en/latest/
# pip install redis 之后要记得将redis-cli/server做个软链到/usr/bin/redis-cli/server
# 也可以wget安装 #
# 密码设置 #

import redis

# 连接 redis # 两种方式 # 直接连接和连接池 #
#1) 直接连接
r = redis.Redis(host='localhost', port=6379, db=0)
#2) 连接池 可以将连接返回池，多次利用 # 节约连接时间 # 如果出现多次连接，可以这样搞 #
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
#
# redis支持的存储类型 # #
#1) string
print "########### string ##########"
if r.exists('string_col'):
	print r.get('string_col')
else:
	r.set('string_col', 'xiaoming')
	print r.get('string_col')
#2) 集合
print "########### set #############"
r.sadd('list_name', 'list_cont1')
r.sadd('list_name', 'list_cont2')
r.sadd('list_name', 'list_cont3')
r.sadd('list_name2','list_cont1' )
r.sadd('list_name2','list_cont11')
print r.smembers('list_name') # 获取集合内容 
print r.sinter('list_name', 'list_name2') # 获取集合的相同的值 #
print r.sunion('list_name', 'list_name2') # 获取并集 #
#3) hash
print "########### hash ############"
r.hset('hash_name', 'name', 'xiaoming')
r.hset('hash_name', 'gender', 'male')
r.hgetall('hash_name') # 所有key
r.hkeys('hash_name') # 所有 value
if r.hexists('myhash', 'name'):
	print r.hget('myhash', 'name')
print z
#r.delete('myhash')

# 数据传输 # TCP协议 #
