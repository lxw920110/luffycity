# from django.test import TestCase
#
# # Create your tests here.
import redis
#
# # 字符串操作
#
#
# # 设置值
conn = redis.Redis(host='192.168.11.180',port =6379)



import redis
#
# # ############### 字符串操作
# # # 设置值
# # conn.set('wupeiqi_name','于超')
# #
# # # 获取值
# # val = conn.get('wupeiqi_name').decode('utf-8')
# # ##############  字典操作
# """
# {
#     xx:{
#         k1:'于超',
#         k2:'彭静',
#     }
# }
#
# """
# # hset操作字典
# conn.hset('xx','k1','于超')
# conn.hset('xx','k2','彭静')
#
# n1 = conn.hget('xx','k1').decode('utf-8')
# n2 = conn.hget('xx','k2').decode('utf-8')
# print(n1,n2)
#
# # conn.flushall()
# import json
# print(conn.keys('shopping_car_1*'))
# print(conn.hget('shopping_car_1_1','id').decode('utf-8'))
# print(conn.hget('shopping_car_1_1','name').decode('utf-8'))
# print(conn.hget('shopping_car_1_1','img').decode('utf-8'))
# print(conn.hget('shopping_car_1_1','default_price_id').decode('utf-8'))
# print(json.loads(conn.hget('shopping_car_1_1','price_policy_dict').decode('utf-8')))
#
#
# print(conn.hget('shopping_car_1_2','id').decode('utf-8'))
# print(conn.hget('shopping_car_1_2','name').decode('utf-8'))
# print(conn.hget('shopping_car_1_2','img').decode('utf-8'))
# print(conn.hget('shopping_car_1_2','default_price_id').decode('utf-8'))
# print(json.loads(conn.hget('shopping_car_1_2','price_policy_dict').decode('utf-8')))
#
#
# conn.set('kkkkkkkkkkkk',123,ex=10)
# print(conn.get('kkkkkkkkkkkk'))
#
# conn.hset('xxxxxxxxxx','k1',123)
# conn.hset('xxxxxxxxxx','k2',567)
# print(conn.keys())
# conn.expire('xxxxxxxxxx',10)
#
# print(conn.keys())
# print(conn.keys('shopping_car_1_1'))
# print(conn.hget('shopping_car_1_1','id').decode('utf-8'))
# print(conn.hget('shopping_car_1_1','name').decode('utf-8'))
# print(conn.hget('shopping_car_1_1','img').decode('utf-8'))
# print(conn.hget('shopping_car_1_1','default_price_id').decode('utf-8'))
#
# vals = conn.hgetall('shopping_car_1_1')
# print(vals)

# temp = {
#     'id': CONN.hget(key, 'id').decode('utf-8'),
#     'name': CONN.hget(key, 'name').decode('utf-8'),
#     'img': CONN.hget(key, 'img').decode('utf-8'),
#     'default_price_id': CONN.hget(key, 'default_price_id').decode('utf-8'),
#     'price_policy_dict': json.loads(CONN.hget(key, 'price_policy_dict').decode('utf-8'))
# }

#
# conn.hmset('shopping_car_1_1',{'id':1,'name':'xxxx'})

conn.hmset('shopping_car_1_1',{'id':1,'name':'python全栈','img':'美图','default_price_id':'1','price_policy_dict':'1'})

conn.hgetall('shopping_car_1_1')





