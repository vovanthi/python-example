# やりたいこと
1. Azure IoT Hubダイレクトメソッド動作検証
2. IoT HubのコンソールからEdgeデバイスにあるメソッドを実行する
3. 呼び出されたメソッドがDockerのビルドを実行する。
4. Dockerビルドはベースのイメージから始め、Git上にあるコード、Storageにあるファイルを取得しデプロイする。

# IoT Hub Python Module Installation
下記を参照してください。WindowsとLinuxでは異なる点があります。<br/>
https://github.com/Azure/azure-iot-sdk-python/blob/master/device/doc/package-readme.md

# IoT Hub Python Module on Windows OS
* Python3.5

```
# create python3.5 env
python3.5 -m venv env

# active env
.\env\Script\activate

# install python library
python -m pip install -r requement.txt
```

# IoT Hub Python Module on Ubuntu
* Python3.5
```
# install libboost-all-dev
apt-get install libboost-all-dev

# install libcurl4-openssl-dev
apt-get install libcurl4-openssl-dev

# create python3.5 env
python3.5 -m venv env

# active env
.\env\Script\activate

# install python library
python -m pip install -r requement.txt

```

# 実行

```
# run sample
python direct-method.py
```

# 課題
Linux、Docker環境上に動作しない

# 参考（ほぼコピー）
[Edge側実装](
https://docs.microsoft.com/ja-jp/azure/iot-hub/iot-hub-python-python-device-management-get-started#create-a-simulated-device-app)

