#选择框的左上角点位置
x0_ratio = 2/8 #可以更改
y0_ratio = 4/8 #可以更改
#选择框的右下角点位置
x1_ratio = 7/8 #可以更改
y1_ratio = 8/9 #可以更改
#获取线性公式设置为Flase，获取识别结果设置为True
con_detect =True #可以更改
#获取线性公式时，需要手动输入浓度值，个数一定严格和比色皿数量比配
con_list = [30.7, 10, 50.9, 80, 1, 100, 120] #可以更改
b_avg_list = []


# 原始照片存放位置： C:\Users\李肖夏\Desktop\Peng\Peng\custom\detectImg\Peng
# 线性公式存放位置： C:\Users\李肖夏\Desktop\Peng\Peng\custom\detectImg\formula
# 识别照片生成位置： C:\Users\李肖夏\Desktop\Peng\Peng\runs\detect