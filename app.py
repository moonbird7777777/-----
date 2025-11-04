import streamlit as st
import random
import time

# 设置页面配置
st.set_page_config(
    page_title="来自moonbird的祝福",
    page_icon="🎉",
    layout="centered"
)

# 自定义CSS样式
st.markdown("""
<style>
.blessing {
    position: fixed;
    padding: 15px 25px;
    border-radius: 10px;
    font-family: 'SimHei', 'Microsoft YaHei', sans-serif;
    font-size: 20px;
    font-weight: bold;
    z-index: 1000;
    box-shadow: 3px 3px 15px rgba(0,0,0,0.2);
    border: 2px solid white;
    animation: fadeIn 0.5s;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* 隐藏Streamlit默认元素 */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 祝福语和颜色
wordslist = ['早睡💤', '工作顺利📚', '要开心呀！😊', '天天快乐🎈', '心想事成✨','身体健康✨']
colors = ['#FFB6C1', '#87CEFA', '#FFFACD', '#98FB98', '#DDA0DD']

def main():
    st.title('🎉 moonbird的祝福')
    st.write('点击下面的按钮，接收满满的祝福吧！')
    
    if st.button('开始祝福 ✨', type='primary'):
        # 创建放置祝福的容器
        placeholder = st.empty()
        
        # 清空之前的内容
        placeholder.empty()
        
        # 创建多个祝福弹窗
        blessing_elements = []
        for i in range(30):  # 数量适中，避免太卡
            text = random.choice(wordslist)
            color = random.choice(colors)
            
            # 随机位置（使用vw/vh单位适应不同屏幕）
            left = random.randint(5, 85)
            top = random.randint(10, 80)
            
            blessing_html = f'''
            <div class="blessing" style="
                left: {left}vw; 
                top: {top}vh;
                background-color: {color};
                color: #333;
            ">{text}</div>
            '''
            blessing_elements.append(blessing_html)
        
        # 一次性显示所有祝福
        placeholder.markdown(''.join(blessing_elements), unsafe_allow_html=True)
        
        st.success('祝福发送完成！🎊')
        
        # 添加重新开始按钮
        if st.button('再来一次 🔄'):
            st.rerun()

if __name__ == '__main__':
    main()
