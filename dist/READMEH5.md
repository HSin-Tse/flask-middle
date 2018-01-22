<!-- ![Markdown](http://m1.app111.com/attchment2/AppImg/160x160/2014/10/12/9207009201451665870576.jpg) -->
#  H5数据埋点服务

# 统计接口设计规划v1
参见word文档(https://ajmide-my.sharepoint.cn/personal/linchaoqun_ajmide_com/_layouts/15/onedrive.aspx?FolderCTID=0x012000F633E83BBC69EC43A66B854F5FDA562D&View=%7BBE987567-1CF5-452A-B579-CEC7D97C2365%7D&AjaxDelta=1&isStartPlt1=1498713159751&id=%2Fpersonal%2Flinchaoqun_ajmide_com%2FDocuments%2F%E6%95%B0%E6%8D%AE%2F%E6%95%B0%E6%8D%AE%E5%9F%8B%E7%82%B9)

# 统计接口设计规划v2

## 目的
为了方便产品，客户端，数据组 高度合作。需要一份可共同维护的文档体系。产品可以建立产品业务，数据组依此建立埋点体系。客户端容易实作。

## 概览
该文档规定了统计日志（stat.php）的接口设计标准， 目的是记录用户操作阿基米德FM客户端的行为和状态

### 设计准则
1. 参数固定为七种级别(0~1)
2. 参数必须传值不可为空，前六种为string,最后一种为jason。如果客户端取不到值则传ept(empty)
3. 有鉴于业务需要，如可传pid,tid ,phid 则设计成必传，遇到可选如播放开关则用/区分。ex:play/stop。选填 play or stop 。
4. 客户端 ios/android 返回必须一致



埋点主要参数:
================

级别 | 参数      | 全称    | 意义     | 必要| 型别| 可填值| 
----|----------|---------|---------|-----|----|-------|-
0   | t1       | touch   | 行为动作 | 必要| str  | click,scroll,swich(依触发动作分类)
1   | ctl(lv1) | control | 业务集合 | 必要| str  | commu,live,home,person,detail,player(依业务主要模块分类)
2   | pg(lv2)  | page    | 主要分页 | 必要| str  | 依详细业务列举
3   | blk(lv3) | block   | 页面组件 | 必要| str  | 依详细业务列举
4   | bt(lv4)  | button  | 确切按钮 | 必要| str  | 依详细业务列举
5   | goto     | goto    | 跳转去向 | 必要| str  | 依详细业务列举
6   | vlu      | value   | 附加参数 | 必要| jason| 依详细业务列举



##级别0参数可填值对照名词以及意义

1. cli click: 点击事件
2. scl scroll: 上下滑动列表
3. swc swich:左右滑动分页
4. drag drag:拖动

##级别1参数可填值对照名词以及意义

1. commu:社区首页
2. live: 直播间
3. home:app首页
4. person:个人页面
5. detail:帖子详情
6. plbar:播放条
7. fullplay:全屏播放器
8. knife:前刀
9. editknife:前刀编辑页面
10. car:驾车模式
11. comment:评论页面
12. keyboard ：选择发布内容
13. mstore:社区米店主页
14. mtotalorder:米店全部订单
14. msubmitorder:米店提交订单
15. mmine:米店
16. mproduct:米店商品详情
17. photo:照片墙
18. maddress:米店选择收货地址
19. morderdetail:M店订单详情
20. mycutmusic:我的音频(剪辑）

##常见通用参数可填值对照名词以及意义
1. ept empty: 不传
2. back back: 自身消失结束
3. play     :播放
4. stop     :停止播放
5. open     :开
6. close    :关
7. pid      :节目id
8. phid     :音频id
9. tid     :帖子id
10. ttype   :帖子类型
11. list : 表达为一种列表
12. sub : 标题(subject)
13. nav:导航栏
14. head:app头部页面
15. plpo:当前播放列表位置

## useragent格式
###  app_name/app_version (os os_version; device_type; id; channel; idfa)

#### 目前appn内部ua示例
ajmd/2.2.5 (ios 10.3.3; iPhone6,2; 8dbf64db3467bd4d6b2f00f952aac9754bd4e78e; AppStore; 36EC3819-6F6E-48CF-8552-7BCCE5770067)
#### 微信小程序ua示例
ajmd-wp/1.0 (ios 10.3.3; iPhone6,2; 12345; AppStore; 36EC3819-6F6E-48CF-8552-7BCCE5770067)
#### 微信分享页ua示例
ajmd-wx/1.0 (ios 10.3.3; iPhone6,2; 12345; AppStore; 36EC3819-6F6E-48CF-8552-7BCCE5770067)

* * *

业务分类:
================


## 社区M店首页


### M店:导航

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1   |1.返回   | click |mstore |nav    | bar   |back   |close  |productid,pid


### M店首页操作

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1   |1.分享     | click |mstore | first  |bar   |share    |sharepop    |storeId,pid
2.2.1   |1.今日热卖<-->去购买    | click |mstore | first  |bar   |gobuy    |mproduct    |storeId,pid
2.2.5   |1.消息中心     | click |mstore | first  |bar   |message    |message    |storeId,pid
2.2.1   |1.关注社区     | click |mstore | first  |bar   |like/dislike    |etp    |storeId,pid
2.2.5   |1.米票入口     | click |mstore | first  |bar   |mticket    |mticket    |storeId,pid,mticketId


### ~~M店首页头图~~  --duplicated

 ~~M店首页头图~~

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1   |1.轮播图     | click |mstore | head  |pager   |image    |mproduct    |productId,pos,pid

    *   [pos]: 页面位置

### M店优品推荐操作
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1   |1.优品推荐     | click |mstore | third  |bar   |product  |mproduct  |storeId,productId,pid,pos
2.2.1   |1.主播推荐     | click |mstore | middle  |bar   |product  |mproduct  |storeId,productId,pid,pos

### M店首页推荐栏
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1   |1.推荐单位| click |mstore | second  |bar   |comment |mproduct    |productId,pos,pid

### M店底部操作栏

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|------- |-------|-------|-------
2.1.1   |1.首页| click |mstore | foot  |bar   |home    |mproduct  |pos,pid
2.1.1   |1.订单| click |mstore | foot  |bar   |order   |mtotalorder  |pos,pid
2.1.1   |1.我的| click |mstore | foot  |bar   |my      |mmine  |pos,pid



## 米票中心
### 导航
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.5   |1.分享   | click |mticket |nav    | bar   |share   |close  |pid

###  操作
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.5   |1.使用规则   | click |mticket |first    | bar   |rule   | rule |pid
2.2.5   |1.免费领取   | click |mticket |first    | bar   |get   |getTicket  |pid,mticketId
2.2.5   |1.转发      | click |mticket |first    | bar   |send   |commupop  |pid,mticketId

### 领取成功
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.5   |1.立即使用   | click |mticket-get |first    | bar   |mproduct   | mproduct |pid,mticketId,productId
2.2.5   |1.分享给好友   | click |mticket-get |first    | bar   |share        |share  |pid,mticketId

### 微信分享领取
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.5   |1.立即使用   | click |mticket-get-w |first    | bar   |mproduct   | mproduct |pid,mticketId,productId
2.2.5   |1.分享给好友   | click |mticket-get-w |first    | bar   |share        |share  |pid,mticketId

### 主播转发领取
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.5   |1.立即使用   | click |mticket-get-p |first    | bar   |mproduct   | mproduct |pid,mticketId,productId
2.2.5   |1.分享给好友   | click |mticket-get-p |first    | bar   |share        |share  |pid,mticketId
2.2.5   |1.更多米票领取   | click |mticket-get-p |first    | bar   |get        |mticket  |pid,mticketId

### 转发社区选择弹窗
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.5   |1.转发社区选择   | click |mticket |list    | pop   |ept   | tips |pid,mticketId
2.2.5   |1.转发社区成功   | click |mticket |list    | pop   |commu   | commu |pid,mticketId

## 领取米票
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.5   |1.立即使用   | click |getTicket |use    | now   |mproduct   | mproduct |pid,mticketId,productId

## 底部导航
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.5   |1.我的米票 | click |getTicket |foor    | bar   |myMticket   | myMticket |pid,mticketId

## 我的米票
## 我的米票内容

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.5   |1.使用规则   | click |mticket-my |first    | bar   |rule   | rule |mticketId
2.2.5   |1.米票列表   | click |mticket-my |first    | list   |ticket   | MTicketDetail |mticketId



## 米票详情
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.5   |1.立即使用   | click |MTicketDetail |center    | bar   |mproduct   | useNow |pid,mticketId,productId
2.2.5   |1.分享好友   | click |MTicketDetail |center    | bar   |share   | useNow |pid



## M店我的订单:
### M店我的订单:导航

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1   |1.返回   | click |morder |nav    | bar   |back   |close  |productid,pid

### M店我的订单:订单标题

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1   |1.查看全部订单   | click |morder |second    | bar   |orders   |mtotalorder  |productid,pid


### M店我的订单:订单操作栏

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1   |1.待付款   | click |morder |third    | block   |waitpay      |mtotalorder  |productid,pid,position
2.1.1   |2.待发货   | click |morder |third    | block   |waitgood     |mtotalorder  |productid,pid,position
2.1.1   |3.待付款   | click |morder |third    | block   |alreadygood  |mtotalorder  |productid,pid,position
2.1.1   |4.退款售后 | click |morder |third    | block   |service      |mtotalorder  |productid,pid,position


    *   [position]: 待付款 0, 待发货 1,2,3

### M店我的订单:信息列表

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1   |1.收藏商品   | click |morder |list    | block   |like      |mlikelist  |productid,pid
2.1.1   |2.收货地址   | click |morder |list    | block   |address   |maddress   |productid,pid
2.1.1   |3.联系客服   | click |morder |list    | block   |call      |phone      |productid,pid

## M店商品详情

### M店详情导航

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1   |1.返回   | click |mproduct |nav | bar   |back          |close    |productid,pid
2.1.1   |2.关注   | click |mproduct |nav | bar   |like/dislike  | ept     |pid,productid
2.2.0   |2.消息中心   | click |mproduct |nav | bar   |message  | message     |pid,productid



### M店详情头图

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1   |1.轮播图  | click |mproduct |head |pager   |image    |photo    |storeId,productid,pos,pid

    *   [pos]: 页面位置 ex:0(第一页),1,2


### M店详情操作栏

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1   |1.收藏     | click |mproduct | first  |bar   |collec/discollec| ept    |storeId,productid,pid,storeid
2.2.1   |2.在线客服     | click |mproduct | first  |bar   |callline            |call    |storeId,productid,pid,storeid
2.2.1   |2.电话谘询     | click |mproduct | first  |bar   |callphone            |call    |storeId,productid,pid,storeid
2.2.1   |2.客服     | click |mproduct | first  |bar   |callpop            |callpop    |storeId,productid,pid,storeid
2.1.1   |3.分享     | click |mproduct | first  |bar   |share           |sharepop|storeId,productid,pid,storeid
2.2.1   |3.首页     | click |mproduct | first  |bar   |home           |mstore|storeId,productid,pid,storeid
2.2.7   |3.立即领取米票    | click |mproduct | first  |bar   |mticket           |ept|storeId,productid,pid,storeid
2.2.5   |3.已领取米票    | click |mproduct | first  |bar   |mticket           |MTicketDetail|storeId,productid,pid,storeid


### M店社区信息
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1   |1.跳转社区  | click |mproduct |second |bar   |commu    |commu    |storeId,productid,pid
2.1.1   |1.猜你喜欢| click |mproduct | second  |bar   |guess    |mproduct    |storeId,productId,pos,pid

### 快速导航

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------   |-------|-------|-------|-------|-------
2.1.1   |1.首页   | click |mproduct | right  |float   |home| mstore    |productid,pid @@废弃
2.1.1   |1.首页   | click |mproduct | right  |float   |commu| commu    |productid,pid  @@ 跳转社区
2.1.1   |2.订单   | click |mproduct | right  |float   |mtotalorder  |mtotalorder  |productid,pid


### M店详情信息
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1   |1.商品底部大图  | click |mproduct |second |block   |image    |photo    |productid,pid
2.1.1   |1.返回顶舖      | click |mproduct |second |block   |totop    |ept    |productid,pid

###  M店多规格

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------   |-------|-------|-------|-------|-------
2.1.1   |1.多规格货品 | click |mproduct |third |block   |goods    |goods    |storeId,productid,pid


### M店详情操作栏

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|------- |-------|-------|-------
2.1.1   |1.立即购买| click |mproduct | foot  |bar   |buynow    |mbuying  |productid,pid,mTicketId


## M店提交订单

### 导航

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1 |1.返回     | click | msubmitorder| nav  |block   |back    |close    |productid,pid

### 地址

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1 |1.地址     | click | msubmitorder| top  |block   |address    |maddress    |productid,pid

### 信息栏

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1 |1.购买数量  | click | msubmitorder| detail  |block   |add/less    |ept    |number
2.1.1 |1.发票需要  | click | msubmitorder| detail  |block   |invoiceY/invoiceN     |ept   |ept
2.1.1 |1.发票详情  | click | msubmitorder| detail  |block   |invoiceDetail     |invoiceDetail   |ept
2.1.1 |1.买家留言  | click | msubmitorder| detail  |block   |message     |keyboard    |ept

    *   [number]: 购买数量 ex:0
### M店提交订单:确认支付
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.6 |1.确认支付     | click | msubmitorder| foot  |block   |pay    |msubmitorder    |productid,pid,paytype,mTicketId
2.2.5 |1.米票选择弹窗     | click | msubmitorder| foot  |block   |ticket    |mticketdetail    |productid,pid,mTicketId
2.2.5 |1.使用米票     | click | msubmitorder| foot  |block   |ticket    |mticketdetail    |productid,pid,mTicketId,pos
2.2.5 |1.不使用米票     | click | msubmitorder| foot  |block   |ticket    |mticketdetail    |productid,pid,mTicketId

    *   [paytype]: 支付方法 :wechat ,alipay

## 发票信息
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1 |1.开票须知 | click | invoiceDetail| title  |block   |invoQ  |invoQ    |productid,pid
2.1.1 |1.确定    | click | invoiceDetail| foot  |block   |ok    |msubmitorder    |productid,pid

## M店选择收货地址
### 导航

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1 |1.返回     | click | maddress| nav  |block   |back    |close    |productid,pid

### 地址列表
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1   |1.选择     | click | maddress| list  |block   |check    |etp    |productid,pid
2.1.1   |1.编辑     | click | maddress| list  |block   |edit    |meditaddress    |productid,pid
2.1.1   |1.删除     | click | maddress| list  |block   |dele    |etp    |productid,pid
2.1.1   |1.增加新地址| click | maddress| list  |block   |add    |meditaddress    |productid,pid



## M店全部订单
### 导航

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1 |1.返回     | click | mtotalorder| nav  |block   |back    |close    |productid,pid,orderid
### 订单tabs
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1 |1.返回     | click | mtotalorder| bar  |tabs  |odertype|close    |productid,pid,orderid

    *   [odertype]:ex=0 : 0,1,2,3,=全部,代付款,带发货...


### 订单信息

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1 |1.取消订单    | click | mtotalorder|  list |  odertype  |cancel    |ept    |productid,pid,orderid
2.1.1 |2.付款       | click | mtotalorder|  list |  odertype  |pay    |msubmitorder    |productid,pid,orderid,paytype
2.1.1 |3.商品信息    | click | mtotalorder|  list |  odertype  |subject    |morderdetail    |productid,pid,orderid



## M店订单详情
### 导航
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1 |1.返回     | click | mtotalorder| nav  |block   |back    |close    |productid,pid,orderid

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1 |1.取消订单    | click | mtotalorder|  list |  odertype  |cancel    |ept    |productid,pid,orderid
2.1.1 |1.商品信息    | click | mtotalorder|  list |  odertype  |subject    |mproductdetail    |productid,pid,orderid


## M生活
### M生活导航
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5 |1.返回     | click | mlive| nav  |block   |back    |close    |productid,pid,orderid
2.1.5 |1.我的订单  | click | mlive| nav  |block   |back    |morder    |productid,pid,orderid



### M生活轮播图

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.轮播图     | click |mlive | head  |pager   |image    |url    |productid,pos,pid


### M生活tabs
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.推荐   | click |mlive | bar  |block   |recommend |ept    |pos
2.1.5   |1.优品   | click |mlive | bar  |block   |great    |ept    |pos
2.1.5   |1.福利   | click |mlive | bar  |block   |bonus    |ept    |pos

### M生活推荐
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.推荐   | click |mlive | recommend  |list   |infor |mliveproduct    |productid,pos,pid

### M生活优品
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.优品   | click |mlive | great  |list   |infor |mliveproduct    |productid,pos,pid
### M生活福利
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.福利   | click |mlive | bonus  |list   |infor |topicdetail    |pos,pid,bonusid


## M生活内容详情
### 导航
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1 |1.返回     | click | mliveproduct| nav  |block   |back    |close    |productid
2.1.1 |1.返回顶部     | click | mliveproduct| nav  |totop   |ept     |close    |productid
2.1.1   |2.关注   | click |mliveproduct |nav | bar   |like/dislike  | ept     |productid
2.2.1   |2.进M生活主页   | click |mliveproduct |nav | bar   |gomlive | mlive     |productid


### 工具栏
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.分享        | click |mliveproduct | bar  |block   |share        |sharebar    |pos,productId,pid
2.1.5   |1.推荐给主播   | click |mliveproduct | bar  |block   |recommend    |recommendpop    |pos,productId,pid
2.2.0   |1.去购买   | click |mliveproduct | bar  |block   |gobuy    |recommendpop    |pos,productId,pid
2.2.0   |1.换一换  | click |mliveproduct | bar  |block   |change    |ept    |pos,productId,pid
2.2.0   |1.播放(待开发)  | click |mliveproduct | bar  |block   |play    |ept    |pos,productId,pid

### 跳转m店详情
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.跳转m店详情   | click |mliveproduct | ept  |list   |circle    |mstore   |pos,productId,pid

### 看了又看
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.看了又看   | click |mliveproduct | look  |list   |rec    |mstore   |pos,productId


### 推荐给主播弹窗
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.推荐给主播        | click |mliveproduct | recommendpop  |list   |commu        |back   |pos,pid

### 推荐进入以下社区M店购买
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.0   |1.推荐购买  | click |mliveproduct | recommendbuypop  |list   |gobuy        |mproduct   |pos,pid

# 统一整合模块
## 分享弹窗
埋点版本 |埋点业务   | t1    |ctl         | pg   | blk   | bt     | goto      | vlu
--------|--------  |-------|-----------|------|-------|---------|-----------|-------
2.2.6   |1.分享弹窗 | click  | h5-sharepop | add  |list  |share     | sdk     | fromUrl,target,pos,shareUrl


    *   target=0  :wechat
    *   target=1  :friend
    *   target=2  :weibo
    *   target=3  :qqzone
    *   target=4  :qq
    *   fromUrl=当前页面url

活动:
======
## 广播年货节
### 米票红包
#### 领红包
埋点版本 |埋点业务   | t1    |ctl                | pg   | blk   | bt     | goto      | vlu
--------|--------  |-------|-------------------|------|-------|---------|-----------|-------
2.2.7   |1.弹出红包 | show  | h5-activity-year  | yearpop  |block  |show     | show     | activityId
2.2.7   |1.开红包   | click  | h5-activity-year | yearpop  |block  |open     | h5-acitvity-getyear     | activityId
2.2.7   |1.关闭弹窗 | click  | h5-activity-year | yearpop  |block  |close    | close     | activityId
#### 打开红包
埋点版本 |埋点业务              | t1    |ctl                    | pg         | blk   | bt     | goto      | vlu
--------|-------------------  |-------|-------------------   |--------------|-------|---------|-----------|-------
2.2.7   |1.米票列表中奖             | show  | h5-activity-getyear  | getyearpop  |list  |usenow     | mproduct     | activityId
2.2.7   |1.米票列表             | click  | h5-activity-getyear  | getyearpop  |list  |usenow     | mproduct     | activityId,pos,mticketId
2.2.7   |1.查看我的米票          | click  | h5-activity-getyear | getyearpop  |block  |mticket-my    | mticket-my     | activityId
2.2.7   |1.年货节主页-米票中心   | click  | h5-activity-getyear | getyearpop  |block  |mticket     | mticket     | activityId
2.2.7   |1.关闭弹窗             | click  | h5-activity-getyear | getyearpop  |block  |close    | close     | activityId


客户端交互:
======
## 客户端交互请求

### 登入

埋点版本 |埋点业务 | t1    |action       | url  | data
--------|--------|-------|-------|-------|-------
2.1.2 |1.登入    | client | login   |{url}    |ept


H5页面流转:
=======
## 页面流转
埋点版本 |埋点业务 | pg    |refer       | h5nm
--------|--------|-------|-------|-------
2.1.2 |1.页面流转    | {pg}  | {refer}   |{h5nm}



    *   [pg]:http://m.ajmide.com/touch/pages/shopping/life/recommend.htm?id=120
    *   [refer]:http://m.ajmide.com/touch/pages/shopping/life/index.htm (从ＡＰＰ跳转传undefined)
    *   [h5nm]:M店推荐详
    *


#### Ex1: http://stat.ajmide.com/m.gif?pg=http://m.ajmide.com/touch/pages/shopping/life/recommend.htm?id=120&refer=http://m.ajmide.com/touch/pages/shopping/life/index.htm&h5nm=M店推荐详情
#### Ex2: m.gif?pg=http%3A%2F%2Fm.ajmide.com%2Ftouch%2Fpages%2Fshopping%2Flife%2Findex.htm%3Fver%3D2.1.7&refer=undefined&h5nm=M%E7%94%9F%E6%B4%BB%E9%A6%96%E9%A1%B5


wechat端:
========

## 健康小测试
### 开始测试
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.开始测试 | click |health| first  |center   |start    |healq   |ept

### 答题页面
埋点版本 |埋点业务    | t1    |ctl     | pg    | blk   | bt    | goto      | vlu
--------|----------|-------|--------|--------|-------|-------|-----------|-------
2.1.5   |1.答题页面1 | click |health-0| first  |center |start  |health-1   |qid,aid
2.1.5   |1.答题页面2 | click |health-1| first  |center |start  |health-2   |qid,aid
2.1.5   |1.答题页面3 | click |health-2| first  |center |start  |health-end |qid,aid

### 测试结果
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|---------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.分享朋友| click |health-end| bottom  |list   |share    |share   |grade
2.1.5   |1.节目推荐| click |health-end| bottom  |list   |start    |app     |grade,pos.pid




## 分享音频
### 顶图
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.播放  | click |ctl |share |head   |play/stop  |ept   | phid/vedioid,pid

### 功能列表
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.好评 | click |ctl| first  | center|like     |ept   |phid/vedioid
2.1.5   |1.评论 | click |ctl| first  |center |comment  |ept   |phid/vedioid
2.1.5   |1.发送评论 | click |ctl| first  |center |send  |ept   |phid/vedioid

### 社区信息
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.跳转社区 | click |ctl| second  |center |commu  |commu   |pid,phid/vedioid

### 音频列表
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.播放| click |ctl |third |list   |play/stop  |ept   | phid,pid/vedioid
2.1.5   |1.跳转| click |ctl|third |list   |detail  |w-music   | phid,pid/vedioid

### 二维码
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.qrcode | click |ctl| bottom  |qrcode |qrcode  |ept   |pid,phid/vedioid

    *   [ctl ]:依照产品以下分类 https://pro.modao.cc/app/c059b467bcd1654c7ebb5f4435492f63fe89bf80#screen=s24C35123FB1511935308572
    *   [w-sound-share ]:声音分享页
    *   [w-knife-share ]:前刀分享页
    *   [w-album-share ]:专辑分享页
    *   [w-veg-share ]:菠菜回听分享页
    *   [w-live-share ]:直拨回听分享页


## 全部评论
### 顶图
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.4   |1.播放  | click |w-allComment |share |head   |play/stop  |ept   | phid/vedioid,pid
2.2.4   |1.返回     | click |w-allComment| nav  |block   |back    |close    |productid
2.2.4   |1.查看全部评论  | click |w-allComment| nav  |block   |see    |ept    |productid

### 功能列表
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.评论我也聊两句 | click |w-allComment| first  |center |comment  |ept   |phid
2.1.5   |1.发送评论 | click |w-allComment| first  |center |send  |ept   |phid

### 社区信息
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.跳转社区 | click |w-allComment| second  |center |commu  |commu   |pid,phid


## 分享帖子
### 顶图

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.播放  | click |w-topic |top |head   |play/stop  |ept   | videoId,pid,tid,ttype

### 声音列表
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.播放  | click |w-topic |sound |list   |play/stop  |ept   | phid,pid,tid,ttype,pos
2.1.5   |1.前往阿基米德FM  | click |w-topic |sound |list   |detail |app   | phid,pid,tid,ttype,pos

### 专辑列表
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.播放| click |w-t |third |list   |play/stop  |ept   | phid,pid,tid,ttype
2.1.5   |1.跳转| click |w-t|third |list   |play/stop  |w-music   | phid,pid,tid,ttype

### 功能列表
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.好评 | click |w-topic| first  | center|like     |ept   |tid
2.1.5   |1.评论 | click |w-topic| first  |center |comment  |ept   |tid
2.1.5   |1.发送评论 | click |w-topic| first  |center |send  |ept   |tid

### 评论功能列表
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.4   |1.查看全部评论  | click |w-t| first  |center   |see    |ept    |tid,ttype
2.2.4   |1.去阿基米德ＦＭ  | click |w-t| first  |center   |see    |app    |tid,ttype

### 社区信息
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.跳转社区 | click |w-t| second  |center |commu  |commu   |pid,tid,ttype



### 精选推荐
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.推荐   | click |w-t | recommend  |list   |infor |w-t    |tid,pos,pid


###  福利列表
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.福利列表   | click |w-t | bonus  |list   |infor |w-t    |tid,pos,pid


### 二维码
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |1.qrcode | click |w-t| bottom  |qrcode |qrcode  |ept   |pid,tid,ttype



    * 产品原型 https://pro.modao.cc/app/c059b467bcd1654c7ebb5f4435492f63fe89bf80#screen=s24C35123FB1511935308572
    * 帖子类型 topic_type http://dev.ajmide.com/wiki/doku.php?id=dev:api:topic
    * 0:普通贴
    * 1:直播贴
    * 2:福利贴
    * 3:新闻头条
    * 4:热点新闻
    * 5:投票帖
    * 6:沉底贴
    * 7:往期节目回听
    * 8:精彩点播（后台上传音频）
    * 9:广告贴
    * 10:专题贴


wechat M店小程序:
=============
## 底部导航
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.22   |首页    | click |w-ms-home    | bottom |tab |home     |w-ms-home   |ept
2.1.22   |米票    | click  |w-ms-home   | bottom |tab |mticket  |w-ms-mticket |ept
2.1.22   |个人中心 | click |w-ms-home    | bottom |tab |me      |w-ms-me    |ept

## 好店推荐
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.22   |首页    | click |w-ms-home    | second |list   |commu     |w-ms-mstore   |pid,pos

## 好物推荐
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.22   |好物推荐tabs    | click |w-ms-home    | third |tabs   |commu     |ept   |pos,recommedId
2.1.22   |好物推荐列表    | click |w-ms-home    | third |list   |w-ms-product-detail     |ept   |pos,recommedId,productId


## 米票M店小程序中心
### 导航
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.5   |1.分享   | click |w-ms-mticket |nav    | bar   |share   |close  |pid

###  操作
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.5   |1.使用规则   | click |w-ms-mticket |first    | bar   |rule   | rule |pid
2.2.5   |1.免费领取   | click |w-ms-mticket |first    | bar   |get   |w-ms-getTicket  |pid,mticketId
2.2.5   |1.转发      | click |w-ms-mticket |first    | bar   |send   |commupop  |pid,mticketId

### 领取成功
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.5   |1.立即使用   | click |w-ms-mticket-get |first    | bar   |mproduct   | mproduct |pid,mticketId,productId
2.2.5   |1.分享给好友   | click |w-ms-mticket-get |first    | bar   |share        |share  |pid,mticketId
2.2.5   |1.更多米票领取   | click |w-ms-mticket-get |first    | bar   |get        |mticket  |pid,mticketId



### 底部导航
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.5   |1.我的米票 | click |w-ms-mticket |foor    | bar   |myMticket   | w-ms-mticket-my |pid,mticketId

## 我的米票
## 我的米票内容

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.5   |1.使用规则   | click |w-ms-mticket-my |first    | bar   |rule   | rule |mticketId
2.2.5   |1.米票列表   | click |w-ms-mticket-my |first    | list   |ticket   | MTicketDetail |mticketId



## 米票详情
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.5   |1.立即使用   | click |w-ms-mTicketDetail |center    | bar   |mproduct   | useNow |pid,mticketId,productId
2.2.5   |1.分享好友   | click |w-ms-mTicketDetail |center    | bar   |share   | useNow |pid


## M店小程序商品详情

### M店详情导航

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1   |1.返回   | click |w-ms-mproduct |nav | bar |back |close    |productid,pid



### M店详情头图

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1   |1.轮播图  | click |w-ms-mproduct |head |pager   |image    |photo    |storeId,productid,pos,pid

    *   [pos]: 页面位置 ex:0(第一页),1,2


### M店详情操作栏

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1   |1.收藏       | click |w-ms-mproduct | first  |bar   |collec/discollec   | ept              |storeId,productid,pid,storeid
2.2.1   |2.客服       | click |w-ms-mproduct | first  |bar   |callpop            |ept                |storeId,productid,pid,storeid
2.1.1   |3.分享       | click |w-ms-mproduct | first  |bar   |share              |w-ms-sharepop      |storeId,productid,pid,storeid
2.2.1   |3.主页       | click |w-ms-mproduct | first  |bar   |home               |w-ms-mstore        |storeId,productid,pid,storeid
2.2.7   |3.立即领取米票| click |w-ms-mproduct | first  |bar   |mticket            |ept                |storeId,productid,pid,storeid
2.2.5   |3.已领取米票  | click |w-ms-mproduct | first  |bar   |mticket            |w-ms-MTicketDetail|storeId,productid,pid,storeid
2.1.1   |1.立即购买    | click |w-ms-mproduct | foot  |bar   |buynow              |w-ms-mbuying      |productid,pid,mTicketId



### 快速导航

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------   |-------|-------|-------|-------|-------
2.1.1   |2.订单   | click |w-ms-mproduct | right  |float   |w-ms-mtotalorder  |w-ms-me  |productid,pid



###  M店多规格

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------   |-------|-------|-------|-------|-------
2.1.1   |1.多规格货品 | click |w-ms-mproduct |third |block   |goods    |goods    |storeId,productid,pid




## M小程序店提交订单

### 导航

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1 |1.返回     | click | w-ms-msubmitorder| nav  |block   |back    |close    |productid,pid

### 地址

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1 |1.地址     | click | w-ms-msubmitorder| top  |block   |address    |w-ms-maddress    |productid,pid

### 信息栏

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.1 |1.购买数量  | click | w-ms-msubmitorder| detail  |block   |add/less           |ept             |number
2.1.1 |1.发票需要  | click | w-ms-msubmitorder| detail  |block   |invoiceY/invoiceN  |ept             |ept
2.1.1 |1.发票详情  | click | w-ms-msubmitorder| detail  |block   |invoiceDetail      |invoiceDetail   |ept
2.1.1 |1.买家留言  | click | w-ms-msubmitorder| detail  |block   |message            |keyboard        |ept

    *   [number]: 购买数量 ex:0
### M店提交订单:确认支付
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.2.6 |1.确认支付        | click | w-ms-msubmitorder| foot  |block   |pay    |w-ms-msubmitorder    |productid,pid,paytype,mTicketId
2.2.5 |1.米票选择弹窗     | click | w-ms-msubmitorder| foot  |block   |ticket    |w-ms-mticketdetail    |productid,pid,mTicketId
2.2.5 |1.使用米票         | click | w-ms-msubmitorder| foot  |block   |ticket    |w-ms-mticketdetail    |productid,pid,mTicketId,pos
2.2.5 |1.不使用米票       | click | w-ms-msubmitorder| foot  |block   |noticket    |w-ms-mticketdetail    |productid,pid,mTicketId
2.2.5 |1.同意ajmd协议       | click | w-ms-msubmitorder| foot  |block   |iknonw    |w-ms-mticketdetail    |productid,pid,mTicketId

    *   [paytype]: 支付方法 :wechat

wechat 小程序:
===========
## 播放页面
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |点占    | click |w-s-play    | top |hot |good     |more   |pid,pos,phid
2.1.5   |分享    | click  |w-s-play    | foot |hot |share     |detail |pid,pos,phid
2.1.5   |播放    | click |w-s-play    | foot |hot |play/stop   |ept    |pid,pos,phid

## 首页
### 推荐
#### 热播节目
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |热播节目 | click |w-s-re    | recommend |hot |play/stop     |ept   |pid,pos,phid
### 子模块 (健康,情感,音乐)

埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |查看更多 | click |w-s-re    | recommend |hot |panelhead     |more   |pid,pos,phid,panelpos,tag
2.1.5   |跳转    | click  |w-s-re    | recommend |hot |panelbody        |detail   |pid,pos,phid,panelpos,tag
2.1.5   |播放    | click |w-s-re    | recommend |hot |play/stop      |ept   |pid,pos,phid,panelpos,tag

### 直播
### 节目


## 更多
埋点版本 |埋点业务 | t1    |ctl     | pg    | blk   | bt    | goto  | vlu
--------|--------|-------|-------|-------|-------|-------|-------|-------
2.1.5   |播放   | click |w-s-more    | list |block |play/stop      |ept   |pid,pos,phid,panelpos,tag
2.1.5   |跳转    | click  |w-s-more    | list |block |panelbody    |detail   |pid,pos,phid,panelpos,tag

    * tag:(健康,情感,音乐)

<h1 id="editer">any question find tse</h1>
