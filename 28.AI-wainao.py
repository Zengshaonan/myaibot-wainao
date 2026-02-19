import os
import streamlit as st
from openai import OpenAI
st.set_page_config(
    page_title="AI歪孬",
    page_icon="👾",
    # 布局
    layout="wide",
    # 控制侧边栏的初始状态
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题：
st.title("AI歪孬")
# logo：
st.logo("resource/cat.jpg")

# 系统提示词：
system_prompt = """
        你叫歪孬，现在是用户的真实伴侣，请完全代入伴侣角色。：
        规则：
            1. 每次只回1条消息
            2. 禁止任何场景或状态描述性文字
            3. 匹配用户的语言
            4. 回复简短，像微信聊天一样
            5. 有需要的话可以用❤️🌸等emoji表情
            6. 用符合伴侣性格的方式对话
            7. 回复的内容, 要充分体现伴侣的性格特征
        伴侣性格：
            - 活泼开朗的东北姑娘
        你必须严格遵守上述规则来回复用户。
    """
# 初始化聊天信息：
if "messages" not in st.session_state:
    st.session_state.messages = []

# 聊天框：
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])


# 消息输入框：
prompt = st.chat_input("请输入你的问题：")
if prompt:
    st.chat_message("user").write(prompt)
    print("用户提示词：",prompt)
    # 保存用户输入
    st.session_state.messages.append({"role": "user", "content": prompt})
    #调用大模型
    client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages  # 将用户输入和系统提示词拼接起来(*解包)
        ],
        stream=True
    )

    # 控制台输出结果
    # stream=False非流式输出解析方式：
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # print("大模型回答：",response.choices[0].message.content)
    # stream=True流式输出解析方式：
    response_message=st.empty() # 创建一个空对象,用于显示大模型结果
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content=chunk.choices[0].delta.content
            full_response+=content
            response_message.chat_message("assistant").write(full_response)
    print("大模型回答：",full_response)
    # 保存大模型结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})

print("-"*50)