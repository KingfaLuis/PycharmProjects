import pymysql
import json
from image_match.goldberg import ImageSignature
import hashlib
import time
from tkinter import _flatten
from collections import Counter
import copy


# cursor.execute("select  id,product_group_new from product_info")
# products = cursor.fetchall()
# for item in products:
#     mysql_update('product_info', "product_group_copy = '{}'".format(item[1]), 'id = {}'.format(item[0]))



def drop_multi_idsort():
    #找出重复的product_id并删掉只保留一个
    while True:
        sql = "SELECT id,product_id FROM product_info WHERE \
                product_id IN (SELECT product_id FROM product_info \
                    GROUP BY product_id HAVING count(product_id) > 1 )"
        cursor.execute(sql)
        results1 = cursor.fetchall()
        if len(results1) == 0:
            print('无重复...')
            break
        else:
            print('存在重复，清除...')
        rm_dict = {}
        for item in results1:
            rm_dict[item[1]] = item[0]
        for id in rm_dict.values():
            cursor.execute("delete  from product_info where id = {}".format(id))
            db.commit()

def mysql_delete():
    #删除某个字段为null的记录
    cursor.execute("delete from product_info where avg_sales_3d is null")
    db.commit()

def mysql_config():
    print('连接mysql...', end='')
    db = pymysql.connect(host='localhost', port=3306, user='wwj',passwd='Shalou-2018', db='vvic', charset='utf8')
    cursor = db.cursor()
    # 开始程序先配置，使能用group by
    cursor.execute("set global sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';")
    db.commit()
    cursor.execute("set session sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';")
    db.commit()
    print('连接成功')
    return db,cursor

def mysql_select(what, table, where):
    cursor.execute("select {} from {} where {}".format(what, table, where))
    results = cursor.fetchall()
    return results

def mysql_insert(table, field, value):
    cursor.execute("insert into {}({}) values({})".format(table, field,value))
    db.commit()

def mysql_update(table, field_value, where):
    cursor.execute("update {} set {} where {}".format(table,field_value,where))
    db.commit()

def vvic_tranf_hash():
    print("Three steps, don't close the window and the computer")
    print('-------------------step1--------------------------------')
    print('加载vvic_daily_product_info的新纪录')
    t1 = time.time()
    results = mysql_select('id,images','vvic_daily_product_info','hashcode is null')
    t5 = time.time()
    print('新记录数：{} time:{:.4f}'.format(len(results),t5 - t1))
    gis = ImageSignature()
    for item in results:
        t2 = time.time()
        hashcode = []
        print('新纪录ID:',item[0], ' 正转换至vvic_matching...',end='')
        urls = json.loads(item[1])
        for url in urls:
            try:
                feature = gis.generate_signature('https:' + url).tolist()
            except:
                print(' err...',end='')
                continue
            feature_str = json.dumps(feature)
            feature_md5 = hashlib.new('md5', feature_str.encode('utf-8')).hexdigest()
            mysql_insert('vvic_matching', 'table_id, hashcode', "'{}','{}'".format('D'+str(item[0]),feature_md5))
            print(' ok...',end='')
            hashcode.append(feature)
        print('向vvic_daily_product_info备份hashcode...')
        hashcode = json.dumps(hashcode)
        mysql_update('vvic_daily_product_info', "vvic_daily_product_info.hashcode = '{}'".format(hashcode), 'id= {}'.format(item[0]))
        t3 = time.time()
        print('ok...time:{:.4f}'.format(t3-t2))
    t4 = time.time()
    print('step 1用时：{:.4f}'.format(t4 - t1))

def id_resort():
    cursor.execute("ALTER  TABLE  product_info DROP id")
    db.commit()
    cursor.execute("ALTER  TABLE  product_info ADD id int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT FIRST")
    db.commit()
    print('已重新排序...')

def tb_tranf_hash(MODE):
    '''
    用product_info记录更新本记录hashcode字段/用tb_product_info group by的记录处理插入product_info
    :param MODE: #'tb_productInsert'/'productUpdate'
    :return:
    '''
    gis = ImageSignature()
    if MODE == 'tb_productInsert':
        feilds = ['shop_name', 'shop_id', 'product_id', 'name', 'current_price','product_publish_time', 'month_sales_count', 'stores_count', 'url', 'images']
        cursor.execute("select {} from tb_product_info where product_id not in "
                       "(select product_id from product_info) group by product_id".format(','.join(feilds)))
    else:
        cursor.execute("select product_id,images from product_info where hashcode is  null")
        cursor.execute("select product_id,images from product_info")
    product_select = cursor.fetchall()
    profuct_num = len(product_select)
    profuct_cnt = 0
    if MODE == 'tb_productInsert':
        for item in product_select:  # 处理每个商品
            t1 = time.time()
            profuct_cnt += 1
            data = dict(zip(feilds, item))
            print('[{}/{}] mode:{} product:{} '.format(profuct_cnt,profuct_num,MODE,data['product_id']),end='')

            # 处理价格,2个pride字段
            print('price...', end='')
            prices = data['current_price'].split('-')
            if len(prices) == 1:
                data['current_price'] = prices[0]
                data['current_price_max'] = prices[0]
            else:
                data['current_price'] = prices[0]
                data['current_price_max'] = prices[1]

            # 处理图片链接和vvic_matching作匹配，vvic_id字段
            images_url = json.loads(data['images'])
            images_url = [x['image_url'] for x in images_url]
            hashcode = []
            sql_match = []
            for url in images_url:
                try:
                    feature = gis.generate_signature(url).tolist()
                    print('img_ok...', end='')
                except:
                    print('img_err...', end='')
                    continue
                feature_str = json.dumps(feature)
                feature_md5 = hashlib.new('md5', feature_str.encode('utf-8')).hexdigest()
                mysql_insert('tb_matching', 'product_id, hashcode', "{},'{}'".format(data['product_id'], feature_md5))
                hashcode.append(feature)
                sql_match.append("'" + feature_md5 + "' or")

            #匹配VVIC
            print('vvic_matching...', end='')
            cursor.execute('select table_id from vvic_matching where hashcode like {}'.format(
                ' hashcode like '.join(sql_match)[:-3]))
            results = cursor.fetchall()
            results1 = [x[0] for x in results]
            results1 = list(set(results1))
            data['vvic_id'] = ','.join(results1)
            print('matched...', end='')

            data['hashcode'] = json.dumps(hashcode)
            mysql_insert('product_info', '{},{}'.format('product_id', 'shop_id'),'{},{}'.format(data['product_id'], data['shop_id']))
            sql_data = ','.join(['product_info.' + key + ' = ' + "'" + value + "'" for key, value in data.items() if key != 'product_id' and key != 'shop_id'])
            mysql_update('product_info', sql_data, 'product_id = {}'.format(data['product_id']))
            t2 = time.time()
            print('...ok time:{:.4f}'.format(t2 - t1))

    else:
        for item in product_select:
            t1 = time.time()
            profuct_cnt += 1
            print('[{}/{}] mode:{} product:{} '.format(MODE,profuct_cnt,profuct_num,item[0]),end='')
            images_url = [x['image_url'] for x in json.loads(item[1])]
            hashcode = []
            sql_match = []
            for url in images_url:
                # feature = gis.generate_signature(url).tolist()
                try:
                    feature = gis.generate_signature(url).tolist()
                    print('img_ok...',end='')
                except:
                    print('img_err...',end='')
                    continue
                feature_str = json.dumps(feature)
                feature_md5 = hashlib.new('md5', feature_str.encode('utf-8')).hexdigest()
                mysql_insert('tb_matching', 'product_id, hashcode', "{},'{}'".format(item[0], feature_md5))
                hashcode.append(feature)
                sql_match.append("'" + feature_md5 + "' or")
            hashcode = json.dumps(hashcode)
            mysql_update('product_info', "product_info.hashcode = '{}'".format(hashcode),
                         'product_id= {}'.format(item[0]))
            t2 = time.time()
            print('...ok time:{:.4f}'.format(t2-t1))

def tb_match():
    '''
    淘宝数据之间的匹配
    :return:
    '''
    #step1
    cursor.execute("select product_id from product_info")
    products = cursor.fetchall()
    products_num = len(products)
    products_cnt = 0
    for item in products:
        #对应在tb_matching的记录
        cursor.execute("select hashcode from tb_matching where product_id = {}".format(item[0]))
        products_hash_h5 = cursor.fetchall()
        cursor.execute('select product_id from tb_matching where {}'.format(' or '.join(["hashcode='{}'".format(x[0]) for x in products_hash_h5])))
        products_matched = cursor.fetchall()
        products_matched = list(set([str(x[0]) for x in products_matched]))
        mysql_update('product_info', "product_group_new = '{}'".format(','.join(products_matched)), 'product_id = {}'.format(item[0]))
        products_cnt += 1
        print('[{}/{}] product_id:{} matched_num:{}'.format(products_cnt,products_num,item[0],len(products_matched)))

    #step2 对step1形成的group再次整合
    cursor.execute("select  product_id,product_group_new from product_info")
    products = cursor.fetchall()
    products_num = len(products)
    products_cnt = 0
    for item in products:
        product_id = item[0]
        product_group = item[1].split(',')
        cursor.execute("select product_group_new from product_info where {}".format(' or '.join(["find_in_set('{}',product_group_new)".format(x) for x in product_group])))
        products_group_all = cursor.fetchall()
        products_group_all = [x[0].split(',') for x in products_group_all]
        products_group_all = list(_flatten(products_group_all))
        products_matched = list(set(products_group_all))
        products_matched = sorted(products_matched)
        mysql_update('product_info', "product_group_new = '{}'".format(','.join(products_matched)), 'product_id = {}'.format(product_id))
        products_cnt += 1
        print('[{}/{}] product_id:{} matched_num:{}'.format(products_cnt,products_num,product_id,len(products_matched)))

    #step3 对step2形成的group处理出上下架标志
    # cursor.execute("select distinct product_group_new from product_info")
    cursor.execute("select product_group_new from product_info group by product_group_new")
    product_groups = cursor.fetchall()
    group_num = len(product_groups)
    group_cnt = 0
    for item in product_groups:
        products_id_from_group = [x for x in item[0].split(',')]
        cursor.execute("select product_id,shop_id from product_info where {}".format(' or '.join(['product_id ={}'.format(x) for x in products_id_from_group])))
        result = cursor.fetchall()
        product_ids = [x[0] for x in result]
        shop_ids = [x[1] for x in result]
        #先标记频率为1的shop_id为上架状态
        sf = Counter(shop_ids)
        product_ids_up = []
        for shop_id, times in dict(sf).items():
            if times == 1:
                index = shop_ids.index(shop_id)
                product_id_up = product_ids[index]
                product_ids_up.append(product_id_up)
                mysql_update('product_info', 'product_state = 1','product_id = {}'.format(product_id_up))
            else:#shop_id重复，商品ID不一样但是商品是重复的
                products_id_more_time = [product_ids[i] for (i,j) in enumerate(shop_ids) if j == shop_id]
                cursor.execute("select product_id,__time from tb_product_info where {}".format(' or '.join(['product_id ={}'.format(x) for x in products_id_more_time])))
                craw_time = cursor.fetchall()
                products_id_tmp = [x[0] for x in craw_time]
                craw_time_tmp = [x[1] for x in craw_time]
                craw_time_newest = sorted(craw_time_tmp)[-1]
                products_id_newest = products_id_tmp[craw_time_tmp.index(craw_time_newest)]
                product_ids_up.append(products_id_newest)
                mysql_update('product_info', "product_state = 0", '{}'.format(' or '.join(['product_id ={}'.format(x) for x in products_id_more_time])))#先批量标记为下架
                mysql_update('product_info', "product_state = 1", 'product_id = {}'.format(products_id_newest))#再标记最新的products_id为上架
        mysql_update('product_info', "product_group_up = '{}'".format(','.join([str(x) for x in product_ids_up])),
                     '{}'.format(' or '.join(['product_id ={}'.format(x) for x in products_id_from_group])))
        group_cnt += 1
        print('[{}/{}] group_up_dw_judge...'.format(group_cnt, group_num))



def analysis():
    # step 1计算日均销量和日均收藏
    product_match_dict = {}
    cursor.execute("select product_id,product_group_up from product_info")
    results = cursor.fetchall()
    for item in results:
        product_match_dict[item[0]] = [int(x) for x in item[1].split(',')]

    # 核心算法区
    import numpy as np
    import pandas as pd
    def group_by_list(results):
        results = [list(x) for x in results]
        results.sort(key=lambda x: x[3])
        group_by_col = [x[2] for x in results]
        group_by_col_element = list(dict(Counter(group_by_col)).keys())
        group_by_out = []
        for element in group_by_col_element:
            group_by_out.append([results[i] for (i, j) in enumerate(group_by_col) if j == element])
        return group_by_out

    products_cnt = 0
    products_num = len(product_match_dict)
    #遍历该商品ID和对应的组
    for product_id, group in product_match_dict.items():
        products_cnt += 1
        print('[{}/{}] analysis product:{}'.format(products_cnt,products_num,product_id))
        # if products_cnt<6300:
        #     continue
        matched_pd_dict = {}
        #遍历组里的每个商品ID
        for matched_pd in group:
            cursor.execute("select month_sales_count,stores_count,FROM_UNIXTIME(__time,'%j'),FROM_UNIXTIME(__time,'%T'),product_publish_time from tb_product_info where product_id = {}".format(matched_pd))
            results = cursor.fetchall()
            product_publish_time = [x[4] for x in results]
            results = [(x[0],x[1],x[2],x[3]) for x in results]
            results_gb = group_by_list(results)#按照特定列group_by一个列表
            results_np = [np.array(day) for day in results_gb]
            try:#results_np里会存在''，以至于不能转成int
                results_tm = [x[:,0:2].astype(int) for x in results_np]
            except:#删除掉''的行
                results_tm = []
                err_loc = [np.where(x == '')[0].tolist() for x in results_np]
                for item in zip(results_np,err_loc):
                    if len(item[1])==0:#正常
                        results_tm.append(item[0][:,0:2].astype(int))
                    else:#异常
                        temp = np.delete(item[0], item[1], axis=0)[:, 0:2].astype(int)
                        if len(temp.tolist()) != 0:#判断删掉之后ndarray是否为空
                            results_tm.append(temp)
            #求梯度（剔除负数）之和
            # results_daily = np.array([[x[:,0].max()-x[0,0],x[:,1].max()-x[0,1]]  for x in results_tm])
            results_daily = []
            for day_data in  results_tm:
                try:#至少两条记录才能求梯度，必会出错
                    dif = np.gradient(day_data,axis=0).T.tolist()
                except:
                    dif = [[0],[0]]
                day_sale = np.array([x for x in dif[0] if x >=0]).sum()
                day_store = np.array([x for x in dif[1] if x >= 0]).sum()
                results_daily.append([day_sale,day_store])
            results_daily = np.array(results_daily)
            #3.5.7天平均
            avg_sales_7d = np.mean(results_daily[-7:, 0])
            avg_sales_5d = np.mean(results_daily[-5:, 0])
            avg_sales_3d = np.mean(results_daily[-3:, 0])
            avg_store_3d = np.mean(results_daily[-7:, 1])
            avg_store_5d = np.mean(results_daily[-5:, 1])
            avg_store_7d = np.mean(results_daily[-3:, 1])

            # # 写入该product_id
            # cursor.execute("update product_info set "
            #                "product_info.avg_sales_3d={},"
            #                "product_info.avg_sales_5d={},"
            #                "product_info.avg_sales_7d={},"
            #                "product_info.avg_store_3d={},"
            #                "product_info.avg_store_5d={},"
            #                "product_info.avg_store_7d={} "
            #                "where product_id = '{}'".format(avg_sales_3d, avg_sales_5d, avg_sales_7d,
            #                                                 avg_store_3d, avg_store_5d, avg_store_7d, product_id))

            #收集到一个组的字典里
            matched_pd_dict[matched_pd] = {'avg_sales_7d': avg_sales_7d, 'avg_store_7d': avg_store_7d,
                                           'avg_sales_5d': avg_sales_5d, 'avg_store_5d': avg_store_5d,
                                           'avg_sales_3d': avg_sales_3d, 'avg_store_3d': avg_store_3d,
                                           'product_publish_time':product_publish_time[-1]}
        #对组的结果进行分析
        matched_pd = pd.DataFrame(matched_pd_dict)
        #找出组内最早和最新发布时间写入该product_id
        product_publish_time_newst = matched_pd.ix['product_publish_time', :].max()
        product_publish_time_oldst = matched_pd.ix['product_publish_time', :].min()
        cursor.execute("update product_info set product_info.product_publish_time_newst = '{}',product_info.product_publish_time_oldst = '{}' where product_id = {}"
                       "".format(product_publish_time_newst,product_publish_time_oldst, product_id))
        db.commit()

        #标记该product_id在组内是 0：销量收藏都不是最优  1：收藏最优  2：销量最优  3：销量收藏同时最优（含组里只有自己的情况）
        avg_xx_xd = [['avg_sales_3d', 'avg_store_3d'], ['avg_sales_5d', 'avg_store_5d'],
                     ['avg_sales_7d', 'avg_store_7d']]
        group_analysis_xds = ['group_analysis_3d', 'group_analysis_5d', 'group_analysis_7d']
        for item in avg_xx_xd:
            res_tem1 = 0
            res_tem2 = 0
            # 计算出一个group_analysis_result
            if matched_pd.ix[item[0], :].idxmax() == product_id: res_tem1 = 1  # 3天 均收藏
            if matched_pd.ix[item[1], :].idxmax() == product_id: res_tem2 = 1  # 3天 均销量
            # 产生标志
            if res_tem1 == 1 and res_tem2 == 1: flag = 3
            if res_tem1 == 0 and res_tem2 == 1: flag = 2;;
            if res_tem1 == 1 and res_tem2 == 0: flag = 1;
            if res_tem1 == 0 and res_tem2 == 0: flag = 0;
            group_analysis_xd = group_analysis_xds[avg_xx_xd.index(item)]
            cursor.execute("update product_info set product_info.{} = '{}' where product_id = {}".format(group_analysis_xd,str(flag), product_id))
            db.commit()





db, cursor = mysql_config()
if __name__ == '__main__':
    vvic_tranf_hash()
    tb_tranf_hash('tb_productInsert')#'productUpdate'
    tb_match()
    analysis()

###################################常用的工具######################################################
# #选择性地更新product_info的某一个字段
# cursor.execute("select product_id,product_publish_time  from tb_product_info group by product_id")
# results = cursor.fetchall()
# for item in results:
#     cursor.execute("update product_info set product_info.product_publish_time='{}' where product_id = {}".format(str(item[1]),item[0]))
#     db.commit()
