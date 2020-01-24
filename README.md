ロボットシステム学　課題2

# led_ros

ROSでLEDを光らせるプログラム
[課題1](https://github.com/shotasoyama/led_teach_and_replay)のプログラムをROSで簡単に実行できるようにした

echo 0 > /dev/myled0 →　0 
echo 1 > /dev/myled0 →　1 
echo 2 > /dev/myled0 →　2 
echo 3 > /dev/myled0 →　3 
echo R > /dev/myled0 →　4 

[デモ動画](https://youtu.be)

## 動作環境

* ubuntu 18.04
* Raspberry Pi 3 Model B+
 * 接続ピン - GPIO16,20,21,GND
* LED 3つ 
* 抵抗 - 330[Ω]

## 準備

``` 
$ cd ~/catkin_wc/src
$ git clone https://github.com/shotasoyama/led_ros.git
$ cd ..
$ catkin_make
$ cd src/led_ros/driver/led_teach_and_replay
$ bash setup.bash
$ roslaunch led_ros led.launch
```

## 操作方法

### 教示

``` 
$ 0
$ 1
$ 2  
$ 3 
```

上記の4行から光らせたいLEDの番号を任意の順番で光らせます。

### リプレイ

以下を実行すると教示した動きが再現されます。

``` 
$ 4
```

### 終了

``` 
Ctrl + c
```
