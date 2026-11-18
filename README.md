# slots · 公共信息时段与受众测量交叉核对

使用 Python 3.11 标准库，不需要联网、第三方包或数据库。输入示例使用本地合成记录。

```sh
python3 -m slots offers data/sample.json
python3 -m unittest discover -s tests -v
```

输出为 UTF-8 JSON。输入文件不可读、业务引用无效或记录不符合口径时退出码为 2，同时报告原因。

## 记录口径

`groups` 给出受众组总体；`surveys` 中同一组内 `segment` 是可对照的来源测量区块，ID 不同不意味着人群互斥。`min/max` 为覆盖人数区间，`overlap` 是两区块已识别的共同人数范围；未调查不相当于零，区块重叠与汇总人口都以同组为范围。
`offers` 是时段报价，`window` 内同一 `network` 的同一 `slot` 只能购买一次，`path` 是联播依赖。同一 `outages` 情景中的失效路径同时失效。`orders` 是已购时段，`policy` 为预算、重点组下限及要纳入的情景。现有清单只列报价和逐项调查，未作去重估计。
