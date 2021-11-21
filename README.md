# weather-bot

企业微信天气信息推送 bot

## 示例

### 1. 创建 workflow

在你的任意一个 GitHub 仓库 `.github/workflows/` 文件夹下创建一个 `.yml` 文件，如 `cc.yml`，内容如下：

```yml
name: qweather-bot

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:

jobs:
  checkin:
    runs-on: ubuntu-latest
    steps:
      - uses: hongyiheng/weather-bot@v0.0.2
        with:
          email: ${{ secrets.CITY_CODE }}
          passwd: ${{ secrets.WEBHOOK }}
```

### 2. 配置 secrets 参数

在 GitHub 仓库的 `Settings -> Secrets` 路径下配置好 `CITY_CODE` 与 `WEBHOOK`

参数获取：

- CITY_CODE： [城市代码查询](https://where.qweather.com/index.html)

- WEBHOOK： [企业微信群机器人WEBHOOK](https://zhuanlan.zhihu.com/p/370006823)
