# cfg

BASIC Group存放所有通用配置

## `MEAN`

图像预处理减去的均值（格式为 *[R, G, B]* ）

### 默认值

[104.008, 116.669, 122.675]

<br/>
<br/>

## `STD`

图像预处理所除的标准差（格式为 *[R, G, B]* ）

### 默认值

[1.000, 1.000, 1.000]

<br/>
<br/>

## `EVAL_CROP_SIZE`

评估时所对图片裁剪的大小（格式为 *[宽, 高]* ）

### 默认值

无（需要用户自己填写）

### 注意事项
* 裁剪的大小不能小于原图，请将该字段的值填写为评估数据中最长的宽和高

<br/>
<br/>

## `TRAIN_CROP_SIZE`

训练时所对图片裁剪的大小（格式为 *[宽, 高]* ）

### 默认值

无（需要用户自己填写）

<br/>
<br/>

## `BATCH_SIZE`

训练、评估、可视化时所用的BATCH大小

### 默认值

1（需要根据实际需求填写）

### 注意事项

* 当指定了多卡运行时，PaddleSeg会将数据平分到每张卡上运行，因此每张卡单次运行的数量为 BATCH_SIZE // dev_count

* 多卡运行时，请确保BATCH_SIZE可被dev_count整除

* 增大BATCH_SIZE有利于模型训练时的收敛速度，但是会带来显存的开销。请根据实际情况评估后填写合适的值

<br/>
<br/>