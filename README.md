# 作者 Author
罗世明 Shiming Luo shl666@ucsd.edu

# 动机 Motion

人在国外，约国内的面试，跟HR折腾算预约时间的这个时差啊，因为算对了时刻算错了日期错过面试啊。都是不想回首的痛苦记忆...

经过事实多次论证，我是一个时差计算恐惧者。我可以手推神经网络的反传播，可以求解拉格朗日对偶，可以对着三四行的损失函数耗一下午。但是我不得不承认，我对这个北京时间和洛杉矶时间之间的相互倒腾。。。**相！当！无！力**

而且！市面上的竟然找不到一款解决我需求的APP（T_T）

APP Store里，大多与时差相关的程序，只会给出当前时刻的世界时间。当你想算一下特定时间，比如：北京时间2018年12月28日中午11点对应的洛杉矶时间是啥时候？这样的问题的时候，乖乖掰手指头吧。+16 hours

I don't wanna translate the part above, too long for me and useless for you.

# 环境要求 Requirement
Python 3.6

pytz (一个python包／a python module)

# 使用方法 Usage
首次使用需要给shell文件权限 <br>
Run the following code for the first time of using...
```bash
$ chmod +x ./run.sh 
```

在*run.shell*中要设置三个参数， 分别是 -tz1（待转换时区）-tz2（目标时区）-tz1_time（待转换时间）。三个参数都是str格式的，照着样例改就行了。然后运行shell文件即可<br>
Three parameters in the *run.shell* file: -tz1(time zone that need to be converted), -tz2(target time zone), -tz1_time(time that need to be converted). Plz follow the example to set your own data. Then run it.
```bash
$ ./run.sh 
```

样例 example：
```bash
$ ./run.sh 
2018-12-27 13:01:00 PST-0800 Thursday
```

# 未完成列表 to do list
1. UI设计
1. 发布APP
1. 成立母公司（就叫Time Lag？）
1. 出任CEO
1. 风投／融资
1. 纳斯达克上市
1. 给自己买台装了GPU的Mac...
