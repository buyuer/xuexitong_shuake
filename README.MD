# 说明
    注意：此程序只限技术交流学习使用，不要用于任何不正当用途，否则后果自负


    具备的功能：
    Android学习通APP：
    1、自动播放下一条视频
    2、自动点击重试
    3、自动选择视频中的选择题
    
    使用说明：
    此程序使用Opencv+Python+ADB实现，可在windows和linux上运行
    
    以Ubuntu为例：
    
        一、安装python
            sudo apt install python3
        
        二、安装Opencv
            sudo python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-contrib-python
       
        三、安装ADB
            sudo apt-get install android-tools-adb
        
        四、手机开启调试模式，并在终端中输入
            adb devices
            检查是否手机已连接
        
        五、修改main.py中的adb_path,和cache_path:
            adb_path = "adb"
            cache_path = "~/"
            (如果adb没添加到path中，就将adb_path设置成adb的完整路径)
            
        Windows系统类似，adb需要自己去官网下载
        网址：https://developer.android.google.cn/studio
        
        六、目前只适应了1920X1080的分辨率，其他分辨率可能会出现识别不准的问题，需要自己适配。主要是重新截一下Resource中的图片
    
    
