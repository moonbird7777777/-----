import streamlit as st
import random
import time
import base64

# 设置页面配置
st.set_page_config(
    page_title="moonbird的祝福",
    page_icon="🎉",
    layout="centered"
)

# 自定义CSS样式 - 更欢快的动画效果
st.markdown("""
<style>
.blessing {
    position: fixed;
    padding: 12px 20px;
    border-radius: 12px;
    font-family: 'SimHei', 'Microsoft YaHei', sans-serif;
    font-size: 18px;
    font-weight: bold;
    z-index: 1000;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    border: 3px solid rgba(255,255,255,0.8);
    min-width: 100px;
    text-align: center;
    animation: bounceIn 0.8s ease-out;
}

@keyframes bounceIn {
    0% { 
        opacity: 0; 
        transform: translateY(-50px) scale(0.3) rotate(-10deg);
    }
    50% { 
        opacity: 0.8; 
        transform: translateY(10px) scale(1.1) rotate(5deg);
    }
    70% { 
        transform: translateY(-5px) scale(0.9) rotate(-2deg);
    }
    100% { 
        opacity: 1; 
        transform: translateY(0) scale(1) rotate(0);
    }
}

/* 心跳动画 */
.blessing:hover {
    animation: heartbeat 0.5s ease-in-out;
}

@keyframes heartbeat {
    0% { transform: scale(1); }
    25% { transform: scale(1.1); }
    50% { transform: scale(1); }
    75% { transform: scale(1.05); }
    100% { transform: scale(1); }
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

/* 背景装饰 */
body {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

/* 音乐播放器样式 */
.audio-player {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1001;
    background: rgba(255,255,255,0.9);
    padding: 10px;
    border-radius: 25px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# 更多祝福语和颜色
wordslist = [
    '早睡💤', '工作顺利📚', '要开心呀！😊', '天天快乐🎈', '心想事成✨',
    '身体健康💪', '万事如意🌟', '笑口常开😄', '平安喜乐🕊️', '好运连连🍀',
    '梦想成真🌈', '前程似锦🎓', '友谊长存👫', '幸福美满❤️', '活力满满⚡',
    '聪明伶俐🎯', '勇敢坚强🛡️', '温柔善良🌸', '自信美丽🌟', '无忧无虑🎵',
    '收获满满📦', '灵感不断💡', '心想事成🎯', '光芒四射☀️', '温暖如春🌺',
    '财源滚滚💰', '事业腾飞🚀', '爱情甜蜜💑', '家庭和睦🏠', '青春永驻🌹'
]

colors = [
    '#FFB6C1', '#87CEFA', '#FFFACD', '#98FB98', '#DDA0DD',
    '#FFD700', '#FFA07A', '#20B2AA', '#DEB887', '#FF69B4',
    '#BA55D3', '#40E0D0', '#FF6347', '#7B68EE', '#00FA9A',
    '#FFDAB9', '#B0E0E6', '#FFA500', '#98F5FF', '#E0FFFF',
    '#FFEC8B', '#FFBBFF', '#C1FFC1', '#BBFFFF', '#EEDD82'
]

# 背景音乐函数
def autoplay_audio(audio_file):
    with open(audio_file, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <div class="audio-player">
                <audio controls autoplay loop>
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
            </div>
        """
        st.markdown(md, unsafe_allow_html=True)

def show_blessings_one_by_one():
    """一个个显示祝福"""
    placeholder = st.empty()
    
    # 初始化session_state
    if 'blessing_count' not in st.session_state:
        st.session_state.blessing_count = 0
    if 'blessings_shown' not in st.session_state:
        st.session_state.blessings_shown = []
    
    total_blessings = 80  # 调整为80个，既满屏又不会太卡
    
    # 进度条
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # 创建祝福的容器
    blessings_container = st.empty()
    
    # 添加背景音乐（使用在线音乐链接）
    st.markdown("""
    <div class="audio-player">
        <audio controls autoplay loop>
            <source src="https://cdn.pixabay.com/download/audio/2022/03/15/audio_1e7b2f6d98.mp3?filename=happy-14585.mp3" type="audio/mp3">
        </audio>
    </div>
    """, unsafe_allow_html=True)
    
    # 一个个显示祝福
    for i in range(total_blessings):
        # 更新进度
        progress = (i + 1) / total_blessings
        progress_bar.progress(progress)
        status_text.text(f'✨ 正在发送祝福... {i+1}/{total_blessings}')
        
        # 生成新的祝福 - 更密集的分布
        text = random.choice(wordslist)
        color = random.choice(colors)
        
        # 更密集的位置分布
        left = random.randint(1, 95)  # 从1%到95%，更靠边
        top = random.randint(3, 90)   # 从3%到90%，覆盖更多区域
        
        # 随机大小和旋转变化，让布局更自然活泼
        font_size = random.randint(16, 24)
        padding_h = random.randint(10, 18)
        padding_v = random.randint(8, 15)
        rotation = random.randint(-5, 5)  # 轻微旋转
        
        # 随机动画延迟，让弹窗更有层次感
        animation_delay = random.uniform(0, 0.3)
        
        # 添加到已显示的祝福列表
        new_blessing = f'''
        <div class="blessing" style="
            left: {left}vw; 
            top: {top}vh;
            background-color: {color};
            color: #333;
            font-size: {font_size}px;
            padding: {padding_v}px {padding_h}px;
            transform: rotate({rotation}deg);
            animation-delay: {animation_delay}s;
        ">{text}</div>
        '''
        st.session_state.blessings_shown.append(new_blessing)
        
        # 显示所有已生成的祝福
        blessings_container.markdown(''.join(st.session_state.blessings_shown), unsafe_allow_html=True)
        
        # 等待一段时间再显示下一个 - 调整速度
        time.sleep(0.15)  # 加快显示速度
    
    # 完成后的消息
    status_text.success('🎊 所有祝福发送完成！满屏都是对你的祝福！')
    
    # 显示重新开始按钮
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button('🎉 再来一次！', type='primary', use_container_width=True):
            # 清空状态，重新开始
            for key in ['blessing_count', 'blessings_shown']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

def main():
    # 添加一些装饰性元素
    st.markdown("""
    <div style="text-align: center;">
        <h1 style="color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">🎉 moonbird的祝福 🎉</h1>
        <p style="color: white; font-size: 18px;">点击按钮，接收满满的惊喜祝福！</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 只有第一次点击或重新开始时显示按钮
    if 'blessing_count' not in st.session_state or st.session_state.blessing_count == 0:
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button('🎁 开启祝福礼包 ✨', type='primary', use_container_width=True):
                st.session_state.blessing_count = 1
                st.rerun()
    
    # 如果已经开始，显示祝福
    if 'blessing_count' in st.session_state and st.session_state.blessing_count > 0:
        show_blessings_one_by_one()

if __name__ == '__main__':
    main()
