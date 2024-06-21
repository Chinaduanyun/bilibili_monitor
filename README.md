 ```markdown
# bilibili_monitor

## 简介
`bilibili_monitor` 是一个用于实时监控Bilibili视频播放量的工具。当播放量达到特定阈值时，它会自动发送邮件通知。用户可以自定义邮件发送服务器和报告频率。

## 功能特性
- **实时监控**：持续监控指定Bilibili视频的播放量。
- **邮件通知**：当播放量达到设定阈值时，自动发送邮件通知。
- **自定义配置**：支持自定义邮件发送服务器和报告频率。

## 安装
1. **克隆仓库**：
   ```bash
   git clone https://github.com/Chinaduanyun/bilibili_monitor.git
   cd bilibili_monitor
   ```

2. **安装依赖**：
 

## 配置
按照以下格式进行配置：

[Email]
smtp_server = smtp.example.com
smtp_port = 587
sender_email = your_email@example.com
sender_password = your_password
receiver_email = recipient_email@example.com

[Bilibili]
video_url = https://www.bilibili.com/video/BV*****
```

## 使用
1. **运行脚本**：
   ```bash
   python bilibili_monitor.py
   ```


## 自定义报告频率
默认情况下，脚本每分钟检查一次播放量。你可以在 `bilibili_monitor.py` 中修改 `time.sleep(60)` 的值来调整检查频率。

## 贡献
欢迎贡献代码、提出问题或建议。请在GitHub上提交Issue或Pull Request。

## 许可证
本项目采用 [MIT 许可证](LICENSE)。
```

这个 `README.md` 文件提供了项目的简介、功能特性、安装步骤、配置方法、使用说明、自定义报告频率的说明、贡献指南以及许可证信息。希望这能帮助用户更好地理解和使用 `bilibili_monitor` 项目。
