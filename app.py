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

# 自定义CSS样式 - 鲜艳活泼配色
st.markdown("""
<style>
.blessing {
    position: fixed;
    padding: 12px 20px;
    border-radius: 15px;
    font-family: 'SimHei', 'Microsoft YaHei', sans-serif;
    font-size: 18px;
    font-weight: bold;
    z-index: 1000;
    box-shadow: 0 6px 25px rgba(0,0,0,0.3);
    border: 3px solid rgba(255,255,255,0.9);
    min-width: 100px;
    text-align: center;
    animation: bounceIn 0.8s ease-out;
}

@keyframes bounceIn {
    0% { 
        opacity: 0; 
        transform: translateY(-50px) scale(0.3) rotate(-15deg);
    }
    50% { 
        opacity: 0.9; 
        transform: translateY(15px) scale(1.2) rotate(8deg);
    }
    70% { 
        transform: translateY(-8px) scale(0.95) rotate(-3deg);
    }
    100% { 
        opacity: 1; 
        transform: translateY(0) scale(1) rotate(0);
    }
}

.blessing:hover {
    animation: heartbeat 0.5s ease-in-out, glow 1s infinite alternate;
    transform: scale(1.05);
}

@keyframes heartbeat {
    0% { transform: scale(1.05); }
    25% { transform: scale(1.15); }
    50% { transform: scale(1.05); }
    75% { transform: scale(1.1); }
    100% { transform: scale(1.05); }
}

@keyframes glow {
    from { box-shadow: 0 6px 25px rgba(0,0,0,0.3), 0 0 10px currentColor; }
    to { box-shadow: 0 6px 25px rgba(0,0,0,0.3), 0 0 20px currentColor; }
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.main .block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

/* 鲜艳的渐变背景 */
body {
    background: linear-gradient(135deg, 
        #FF6B6B 0%, 
        #FFD93D 25%, 
        #6BCF7F 50%, 
        #4D96FF 75%, 
        #9D4BFF 100%);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* 标题样式 */
.title-container {
    text-align: center;
    padding: 20px;
    background: rgba(255,255,255,0.1);
    border-radius: 20px;
    backdrop-filter: blur(10px);
    margin-bottom: 20px;
    border: 2px solid rgba(255,255,255,0.3);
}

.title-text {
    font-size: 3em;
    font-weight: bold;
    background: linear-gradient(45deg, #FF6B6B, #FFD93D, #6BCF7F, #4D96FF, #9D4BFF);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradientFlow 4s ease infinite;
    text-shadow: 3px 3px 6px rgba(0,0,0,0.2);
}

@keyframes gradientFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.subtitle {
    font-size: 1.2em;
    color: white;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    margin-top: 10px;
}

/* 开始按钮样式 */
.start-button {
    background: linear-gradient(45deg, #FF6B6B, #FFD93D, #6BCF7F, #4D96FF);
    background-size: 300% 300%;
    animation: gradientFlow 3s ease infinite;
    color: white;
    border: none;
    padding: 20px 40px;
    border-radius: 30px;
    font-size: 1.5em;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.start-button:hover {
    transform: scale(1.1);
    box-shadow: 0 12px 35px rgba(0,0,0,0.4);
}

/* 进度条样式 */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #FF6B6B, #FFD93D, #6BCF7F, #4D96FF, #9D4BFF);
    background-size: 300% 300%;
    animation: gradientFlow 2s ease infinite;
}

/* 音效提示 */
.sound-tip {
    background: rgba(255,255,255,0.9);
    padding: 10px 15px;
    border-radius: 20px;
    font-size: 14px;
    text-align: center;
    margin: 10px 0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# 更鲜艳的祝福语和颜色
wordslist = [
    '早睡💤', '工作顺利📚', '要开心呀！😊', '天天快乐🎈', '心想事成✨',
    '身体健康💪', '万事如意🌟', '笑口常开😄', '平安喜乐🕊️', '好运连连🍀',
    '梦想成真🌈', '前程似锦🎓', '友谊长存👫', '幸福美满❤️', '活力满满⚡',
    '聪明伶俐🎯', '勇敢坚强🛡️', '温柔善良🌸', '自信美丽🌟', '无忧无虑🎵',
    '收获满满📦', '灵感不断💡', '心想事成🎯', '光芒四射☀️', '温暖如春🌺',
    '财源滚滚💰', '事业腾飞🚀', '爱情甜蜜💑', '家庭和睦🏠', '青春永驻🌹',
    '能量爆棚⚡', '幸运爆棚🎯', '快乐加倍😆', '好运爆棚🎊', '奇迹发生🌟'
]

# 更鲜艳活泼的颜色
colors = [
    '#FF6B6B', '#FFD93D', '#6BCF7F', '#4D96FF', '#9D4BFF',
    '#FF8E8E', '#FFE066', '#8CE08C', '#6BA8FF', '#B366FF',
    '#FF5252', '#FFEB3B', '#4CAF50', '#2196F3', '#9C27B0',
    '#FF4081', '#FF9800', '#00E676', '#00B0FF', '#E040FB',
    '#FF1744', '#FFC107', '#00C853', '#0091EA', '#D500F9',
    '#F44336', '#FFEB3B', '#4CAF50', '#03A9F4', '#9C27B0'
]

def play_simple_sound():
    """使用Streamlit的audio组件播放简单音效"""
    # 创建一个简单的提示音（使用base64编码的短音频）
    # 这里使用一个非常简短的beep声
    audio_base64 = "SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjU4Ljc2LjEwMAAAAAAAAAAAAAAA//tQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWGluZwAAAA8AAAABAAACcQCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8AAABQTEFNRTMuMTAwBKkAAAAAAAAAADUgJAOHQQAB9AAACHDURWIvAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//sQZAAP8AAAaQAAAAgAAA0gAAABAAABpAAAACAAADSAAAAETEFNRTMuMTAwVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV"
    
    # 隐藏的音频播放
    st.audio(audio_base64, format="audio/wav", start_time=0, autoplay=True)

def show_blessings_one_by_one():
    """一个个显示祝福"""
    placeholder = st.empty()
    
    if 'blessing_count' not in st.session_state:
        st.session_state.blessing_count = 0
    if 'blessings_shown' not in st.session_state:
        st.session_state.blessings_shown = []
    
    total_blessings = 80
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    blessings_container = st.empty()
    
    # 显示音效提示
    with st.empty():
        st.markdown('<div class="sound-tip">🎵 音效播放中...</div>', unsafe_allow_html=True)
        time.sleep(2)
    
    for i in range(total_blessings):
        progress = (i + 1) / total_blessings
        progress_bar.progress(progress)
        status_text.text(f'✨ 正在发送祝福... {i+1}/{total_blessings}')
        
        text = random.choice(wordslist)
        color = random.choice(colors)
        left = random.randint(1, 95)
        top = random.randint(3, 90)
        font_size = random.randint(18, 26)
        padding_h = random.randint(12, 20)
        padding_v = random.randint(10, 16)
        rotation = random.randint(-8, 8)
        animation_delay = random.uniform(0, 0.3)
        
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
        blessings_container.markdown(''.join(st.session_state.blessings_shown), unsafe_allow_html=True)
        
        # 每10个祝福尝试播放一次音效
        if i % 10 == 0:
            try:
                play_simple_sound()
            except:
                pass  # 如果音效失败，静默继续
        
        time.sleep(0.15)
    
    # 播放完成音效
    try:
        play_simple_sound()
    except:
        pass
    
    status_text.success('🎊 所有祝福发送完成！满屏都是对你的祝福！')
    
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button('🎉 再来一次！', type='primary', use_container_width=True):
            for key in ['blessing_count', 'blessings_shown']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

def main():
    # 使用新的标题样式
    st.markdown("""
    <div class="title-container">
        <div class="title-text">moonbird的祝福</div>
        <div class="subtitle">点击下方按钮，接收满满的惊喜祝福！</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 音效说明
    st.markdown("""
    <div class="sound-tip">
        🎵 温馨提示：为确保最佳体验，请确保设备音量已开启
    </div>
    """, unsafe_allow_html=True)
    
    if 'blessing_count' not in st.session_state or st.session_state.blessing_count == 0:
        st.markdown("<br><br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            if st.button('🎁 开启祝福礼包 ✨', type='primary', use_container_width=True):
                st.session_state.blessing_count = 1
                st.rerun()
    
    if 'blessing_count' in st.session_state and st.session_state.blessing_count > 0:
        show_blessings_one_by_one()

if __name__ == '__main__':
    main()
