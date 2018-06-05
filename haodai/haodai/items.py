# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field



class HaodaiItem(scrapy.Item):
    table_name = 'hdata'
    # 公司id(主键)
    cid = Field()
    # 公司放贷网址
    url = Field()
    # 获取公司名称
    name = Field()

    money = Field()
    # 期限
    timeran = Field()
    # 月供
    month_pay= Field()
    # 总费用
    sum_money = Field()
    # 费用说明
    description = Field()
    # 额度范围
    mon_range = Field()
    # 期限范围
    termtime_range = Field()
    # 还款方式
    pay_style = Field()
    # 放款时间
    loan_time = Field()
    # 申请人数量
    man_num = Field()
    # 申请条件
    man_condition = Field()
    # 所需材料
    material = Field()
    # 详细说明
    all_explain = Field()
    # 公司图标
    gongsi_img = Field()
    # 贷款方式
    loan_style = Field()
    # 星级评价
    evaluation = Field()
    # 贷款要求
    requirements = Field()
    # 公司特色
    charas = Field()
    # 公司特色图片
    charas_img = Field()



# 创建数据库表模型

class CompanyItem(scrapy.Item):
    table_name = 'daikuan'
    # 公司id(主键)
    cid = Field()
    # 公司放贷网址
    url = Field()
    # 获取公司名称
    company_name = Field()
    # 金额
    money = Field()
    # 期限
    limit_time = Field()
    # 月供
    month_supply = Field()
    # 总费用
    total_post = Field()
    # 费用说明
    expense_description = Field()
    # 额度范围
    limit_range = Field()
    # 期限范围
    term_range = Field()
    # 还款方式
    Repayment = Field()
    # 放款时间
    loan_time = Field()
    # 申请人数量
    applicant = Field()
    # 申请条件
    application_condition = Field()
    # 所需材料
    material = Field()
    # 详细说明
    detailed_description = Field()
    # 公司图标
    company_img = Field()
    # 贷款方式
    load_method = Field()
    # 星级评价
    evaluation = Field()
    # 贷款要求
    lender_requirements = Field()
    # 公司特色
    features = Field()
    # 公司特色图片
    features_img = Field()





