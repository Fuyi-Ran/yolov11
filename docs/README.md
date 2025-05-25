# Yolov11轻量化改进

通过融合 MutilBackbone-MSGA 模块和 bifpn 模块对 Yolo 人脸识别进行了轻量化改造，改进后的程序能够在半小时内完成包含两万余张图片数据集的 100 轮训练，且模型平均精度 mAP50稳定在 0.99 以上(租用RTX4090显卡)。

![训练参数](https://github.com/user-attachments/assets/db5e1657-2ef4-4fbc-bf1c-0d1fa591ab95)
![模型精度](https://github.com/user-attachments/assets/0445d561-f7dc-48b9-82dd-4dfe7f1a5219)

**配置环境**：

**PyTorch** 1.11.0

**Python** 3.8

**CUDA** 11.3

*常规yolov11运行环境即可*

**常见问题**：

1. 报错：没有pywt模块

此时只需要在环境中下载该模块即可

```python
#先激活配置环境(我的环境名为yolov11,使用时应替换为自己的环境名)
conda activate yolov11
#然后再安装该模块
pip install PyWavelets
```

2. 使用代码需要将代码中涉及到的文件路径全部改为自己的文件所在地，主要涉及两个文件(两个文件均在根目录下)：一个是`train.py`，需要注意`data.yaml`文件的路径替换。另一个是`data.yaml`文件中训练数据集的路径替换。所有路径**最好都使用绝对路径**，不使用相对路径，避免出现文件找不到的情况。
3. 要使用本项目来训练自己的数据集，需要将根目录下的`datasets`文件夹按照格式换为自己的数据集（核心部分是`images`文件夹和`labels`文件夹中的`train`，`test`和`val`文件夹要划分正确）。

# Yolov11 lightweight improvements

By fusing the MutilBackbone-MSGA module and the bifpn module, Yolo face recognition has been changed to a light-weight model, and the improved program can complete 100 rounds of training with a dataset of more than 20,000 images in half an hour, and the average accuracy of the model mAP50 is stable at more than 0.99 (renting RTX4090 graphics card).

**Configuration Environment**:

**PyTorch** 1.11.0

**Python** 3.8

**CUDA** 11.3

*Regular yolov11 operating environment is sufficient*

**Frequently asked questions**:

1. Error: There is no pywt module.

At this point, you only need to download the module in the environment.

```python
#Activate the configuration environment first (My environment name is yolov11, you should replace it with your environment name when using it)
conda activate yolov11
#Then install the module
pip install PyWavelets
```

2. To use the code, you need to change all the file paths involved in the code to the location of your files, mainly involving two files (both files are in the root directory): one is `train.py`, you need to pay attention to the path replacement of the `data.yaml` file. The other is the path substitution of the training dataset in the `data.yaml` file. **It is best to use absolute paths for all paths**, not relative paths, to avoid the situation where the file cannot be found.

3. To use this project to train your dataset, you need to replace the `datasets` folder in the root directory with your dataset according to the format (the core part is the `train`, `test`, and `val` folders in the `images` folder and `labels` folder to be divided correctly).
