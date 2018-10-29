# 网络性能

## 裁剪测试结果

| net  | data | caffe deploy time(ms)/GPU memory(MB) | ssd_detect time(ms)/GPU memory(MB) | mAP  | car  | bicycle | motocycle | person | roadblock | speedbump |
| ---- | ---- | ------------------------------------ | ---------------------------------- | ---- | ---- | ------- | --------- | ------ | --------- | --------- |
| net1 |      |                                      |                                    |      |      |         |           |        |           |           |

## PX2测试结果

| net  | ssd_detect time(ms) |      |
| ---- | ------------------- | ---- |
|      | GPU0                | GPU1 |
|      |                     |      |
|      |                     |      |
|      |                     |      |

表中同一单元格中多个数字代表相同条件下的多次测量结果

## 服务器(GPU:P100)测试结果

### SAICParking-Selected数据集测试

| net                                           | data                 | caffe deploy time(ms)/GPU memory(MB) | ssd_detect time(ms)GPU memory(MB) | mAP   | car   | bicycle | motocycle | person | roadblock | speedbump |
| --------------------------------------------- | -------------------- | ------------------------------------ | --------------------------------- | ----- | ----- | ------- | --------- | ------ | --------- | --------- |
|                |  |                            |                   |   |  |    |      |   |      |      |

### COCO数据集训练结果

| method | data | backbone | mAP  | Avg. Rrecision. IoU: |      |      | Avg. Precision. Area: |      |      | Avg. Recall. Dets: |      |      | Avg. Recall. Area: |      |      |
| ------ | ---- | -------- | ---- | -------------------- | ---- | ---- | --------------------- | ---- | ---- | ------------------ | ---- | ---- | ------------------ | ---- | ---- |
|        |      |          |      |                      |      |      |                       |      |      |                    |      |      |                    |      |      |

## 表格说明

### 其它说明

caffe deploy time: 运行`$CAFFE_ROOT/build/tools/caffe time`进行网络运行时间测试, 默认使用`TRAIN phase`运行50次取平均

ssd_detect : 运行`ssd_detect`对若干图片进行检测, 只计算网络本身的运行时间, 且去除前面10次检测后的剩余检测时间取平均值

mAP: IoU=0.5, 11 point interption

### 预训练模型说明

网络名字上加‘*’代表不使用预训练模型

网络名字上加‘+’代表使用COCO预训练模型

#### MobileNet默认预训练模型

采用chuanqi的:

> I trained this model from a MobileNet classifier([caffemodel](https://drive.google.com/open?id=0B3gersZ2cHIxZi13UWF0OXBsZzA) and [prototxt](https://drive.google.com/open?id=0B3gersZ2cHIxWGEzbG5nSXpNQzA)) converted from [tensorflow](http://download.tensorflow.org/models/mobilenet_v1_1.0_224_2017_06_14.tar.gz). 

这句话的意思应该是他是从MobileNet  classifier这个预训练模型训练的

> I first trained the model on MS-COCO and then fine-tuned on VOC0712. 

这是他训练MobileNet-SSD的过程

chuanqi给出的预训练模型其实是MobileNet-SSD-VOC模型(训练自己的数据需要修改conf层名), 应该是它自己训练好的结果

#### VGG默认预训练模型 

采用的是VGG的预训练模型(应该是VGG-ImageNet), 不是VGG-SSD-COCO

### 网络说明

### data 说明

#### COCO2017

###### Images

2017 Train images [118K/18GB]
2017 Val images [5K/1GB]
2017 Test images [41K/6GB]

###### Annotations

2017 Train/Val annotations [241MB]
2017 Testing Image info [1MB]

- 各类别数目统计

```shell
('num_files:', 22562)
Counter({'car': 66221, 'roadblock': 4261, 'person': 3110, 'speedbump': 2260, 'motorcycle': 903, 'bicycle': 382})
('total_num:', 77137)
```

- 数据集划分

```shell
train:val:test=3:1:1
total_num=22562
trainval_num=18049
train_num=13536
val_num=4513
test_num=4513
```

## 
