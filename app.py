import streamlit as st
import random
import time

# 设置页面配置
st.set_page_config(
    page_title="moonbird的祝福",
    page_icon="🎉",
    layout="centered"
)

# 自定义CSS样式
st.markdown("""
<style>
.blessing {
    position: fixed;
    padding: 12px 20px;
    border-radius: 8px;
    font-family: 'SimHei', 'Microsoft YaHei', sans-serif;
    font-size: 18px;
    font-weight: bold;
    z-index: 1000;
    box-shadow: 3px 3px 15px rgba(0,0,0,0.2);
    border: 2px solid white;
    animation: fadeIn 0.5s;
    min-width: 100px;
    text-align: center;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-20px) scale(0.8); }
    to { opacity: 1; transform: translateY(0) scale(1); }
}

/* 隐藏Streamlit默认元素 */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* 确保祝福显示在内容上方 */
.main .block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# 更多祝福语和颜色
wordslist = [
    '早睡💤', '工作顺利📚', '要开心呀！😊', '天天快乐🎈', '心想事成✨',
    '身体健康💪', '万事如意🌟', '笑口常开😄', '平安喜乐🕊️', '好运连连🍀',
    '梦想成真🌈', '前程似锦🎓', '友谊长存👫', '幸福美满❤️', '活力满满⚡',
    '聪明伶俐🎯', '勇敢坚强🛡️', '温柔善良🌸', '自信美丽🌟', '无忧无虑🎵',
    '收获满满📦', '灵感不断💡', '心想事成🎯', '光芒四射☀️', '温暖如春🌺'
]

colors = [
    '#FFB6C1', '#87CEFA', '#FFFACD', '#98FB98', '#DDA0DD',
    '#FFD700', '#FFA07A', '#20B2AA', '#DEB887', '#FF69B4',
    '#BA55D3', '#40E0D0', '#FF6347', '#7B68EE', '#00FA9A',
    '#FFDAB9', '#B0E0E6', '#FFA500', '#98F5FF', '#E0FFFF'
]

def show_blessings_one_by_one():
    """一个个显示祝福"""
    placeholder = st.empty()
    
    # 初始化session_state
    if 'blessing_count' not in st.session_state:
        st.session_state.blessing_count = 0
    if 'blessings_shown' not in st.session_state:
        st.session_state.blessings_shown = []
    
    total_blessings = 50  # 增加到50个祝福，让屏幕更满
    
    # 进度条
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # 创建祝福的容器
    blessings_container = st.empty()
    
    # 一个个显示祝福
    for i in range(total_blessings):
        # 更新进度
        progress = (i + 1) / total_blessings
        progress_bar.progress(progress)
        status_text.text(f'正在发送祝福... {i+1}/{total_blessings}')
        
        # 生成新的祝福 - 更密集的分布
        text = random.choice(wordslist)
        color = random.choice(colors)
        
        # 更密集的位置分布
        left = random.randint(2, 90)  # 从2%到90%，更靠边
        top = random.randint(5, 85)   # 从5%到85%，覆盖更多区域
        
        # 随机大小变化，让布局更自然
        font_size = random.randint(16, 22)
        padding_h = random.randint(10, 15)
        padding_v = random.randint(8, 12)
        
        # 添加到已显示的祝福列表
        new_blessing = f'''
        <div class="blessing" style="
            left: {left}vw; 
            top: {top}vh;
            background-color: {color};
            color: #333;
            font-size: {font_size}px;
            padding: {padding_v}px {padding_h}px;
        ">{text}</div>
        '''
        st.session_state.blessings_shown.append(new_blessing)
        
        # 显示所有已生成的祝福
        blessings_container.markdown(''.join(st.session_state.blessings_shown), unsafe_allow_html=True)
        
        # 等待一段时间再显示下一个 - 稍微加快速度
        time.sleep(0.2)  # 从0.3秒减少到0.2秒，显示更快
    
    # 完成后的消息
    status_text.success('🎊 所有祝福发送完成！满屏都是对你的祝福！')
    
    # 显示重新开始按钮
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button('再来一次 🔄', type='primary', use_container_width=True):
            # 清空状态，重新开始
            for key in ['blessing_count', 'blessings_shown']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

def main():
    st.title('🎉 moonbird的祝福')
    st.write('点击下面的按钮，满满的祝福会一个个出现，填满整个屏幕！')
    
    # 只有第一次点击或重新开始时显示按钮
    if 'blessing_count' not in st.session_state or st.session_state.blessing_count == 0:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button('开始祝福 ✨', type='primary', use_container_width=True):
                st.session_state.blessing_count = 1
                st.rerun()
    
    # 如果已经开始，显示祝福
    if 'blessing_count' in st.session_state and st.session_state.blessing_count > 0:
        show_blessings_one_by_one()

if __name__ == '__main__':
    main()
