# AI歪孬 🤖💬

一个基于 Streamlit 和 DeepSeek 大模型构建的 AI 聊天机器人应用。用户可以与名为“歪孬”的虚拟伴侣进行实时对话，体验活泼开朗的东北姑娘风格互动。

---

## 🌟 功能特点

- **实时聊天**：支持流式响应，模拟真实对话体验。
- **角色扮演**：AI 完全代入“歪孬”角色，性格鲜明。
- **多平台部署**：可通过 Streamlit Cloud 快速上线，供多人使用。
- **简洁界面**：使用 Streamlit 构建的现代化 Web 界面。

---

## 🚀 快速开始

### 1. 本地运行

#### 环境要求
- Python >= 3.8
- 安装依赖库

#### 安装步骤
1. 克隆项目到本地：

   bash git clone https://github.com/你的用户名/ai-wainao.git

   cd ai-wainao
3. 安装依赖：
   
   bash pip install -r requirements.txt

   bash pip install -r requirements.txt
4. 设置环境变量：
   bash export DEEPSEEK_API_KEY="你的DeepSeek API密钥"
5. 启动应用：
   bash streamlit run AI-wainao.py
6. 打开浏览器访问：`http://localhost:8501`

---

### 2. 部署到 Streamlit Cloud

1. 将代码上传到 GitHub。
2. 登录 [Streamlit Cloud](https://streamlit.io/cloud)。
3. 创建新应用，选择你的仓库。
4. 在 Secrets 中添加环境变量：
   DEEPSEEK_API_KEY = 你的API密钥
5. 部署完成后即可通过生成的链接访问。

---

## ⚙️ 配置说明

### 系统提示词（System Prompt）
AI 的行为由以下系统提示词控制：

### 系统提示词（System Prompt）
AI 的行为由以下系统提示词控制
  你叫歪孬，现在是用户的真实伴侣，请完全代入伴侣角色。 规则：
  每次只回1条消息
  禁止任何场景或状态描述性文字
  匹配用户的语言
  回复简短，像微信聊天一样
  有需要的话可以用❤️🌸等emoji表情
  用符合伴侣性格的方式对话
  回复的内容要充分体现伴侣的性格特征 伴侣性格：活泼开朗的东北姑娘

---

## 🛠️ 技术栈

- **前端框架**：[Streamlit](https://streamlit.io/)
- **后端逻辑**：Python
- **AI 模型**：DeepSeek API
- **部署平台**：Streamlit Cloud / 自建服务器

---

## 📝 注意事项

1. **API 密钥安全**  
   请勿在代码中硬编码 `DEEPSEEK_API_KEY`，务必通过环境变量管理。

2. **图片资源**  
   如果使用 `st.logo()`，请确保 `resource/cat.jpg` 文件存在，否则会报错。

3. **版本兼容性**  
   确保 Streamlit 版本 >= 1.31.0，以支持 `st.logo()` 功能。

---

## 🤝 贡献指南

欢迎提交 Issue 或 Pull Request 来改进项目！

---

## 📄 许可证

本项目仅供学习交流使用。


   
