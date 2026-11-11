# 候鸟巡护数据的授权字段采集

这个 Python 项目保存采集侧的来源读取工具和合成资料。代码位于 app，示例输入位于 fixtures，现有读取工具的回归位于 tests。示例不代表任何真实单位的业务记录。

## 数据与接口

Partner 是接口替身，只执行请求投影，不实现客户端授权判断。grant 返回用途下的指定授权修订；page 的 violate=True 模拟服务方违反投影返回完整行。grants.json 内 public 的第二修订收紧字段。所有经纬度都是与保护区无关的合成坐标，note 用作受限字段泄漏检查。

## 本地使用

使用 Python 3.12 或更新版本，当前工具仅依赖标准库。从项目根目录执行：

```sh
python3 -m app.inspect
python3 -m unittest discover -s tests -v
python3 -m compileall -q app tests
```

读取命令输出当前素材的结构或单次读取结果。运行过程中产生的文件放在 runtime 中，与原始素材分开。公开示例仅使用 .invalid 域名，网络适配时应替换为已授权的来源。
