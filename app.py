import streamlit as st
import random
import time
import pygame
import threading
import os
from io import BytesIO
import requests

# 初始化pygame mixer
try:
    pygame.mixer.init()
    music_available = True
except:
    music_available = False

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
    animation: heartbeat 0.5s ease-in-out;
    transform: scale(1.05);
}

@keyframes heartbeat {
    0% { transform: scale(1.05); }
    25% { transform: scale(1.15); }
    50% { transform: scale(1.05); }
    75% { transform: scale(1.1); }
    100% { transform: scale(1.05); }
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.main .block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

body {
    background: linear-gradient(135deg, #FF6B6B 0%, #FFD93D 25%, #6BCF7F 50%, #4D96FF 75%, #9D4BFF 100%);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

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
}

@keyframes gradientFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.subtitle {
    font-size: 1.2em;
    color: white;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# 祝福语和颜色
wordslist = [
    '早睡💤', '工作顺利📚', '要开心呀！😊', '天天快乐🎈', '心想事成✨',
    '身体健康💪', '万事如意🌟', '笑口常开😄', '平安喜乐🕊️', '好运连连🍀',
    '梦想成真🌈', '前程似锦🎓', '友谊长存👫', '幸福美满❤️', '活力满满⚡'
]

colors = [
    '#FF6B6B', '#FFD93D', '#6BCF7F', '#4D96FF', '#9D4BFF',
    '#FF8E8E', '#FFE066', '#8CE08C', '#6BA8FF', '#B366FF'
]

def play_music_in_thread():
    """在后台线程中播放音乐"""
    def music_player():
        try:
            # 方法1: 使用pygame播放（如果可用）
            if music_available:
                # 创建一个简单的提示音
                pygame.mixer.music.set_volume(0.3)
                
                # 播放简单的音调
                for i in range(100):  # 播放100次
                    # 创建简单的音效
                    pygame.mixer.Sound.play(pygame.mixer.Sound(buffer=bytes([0] * 44)))
                    time.sleep(2)  # 每2秒播放一次
                    
        except Exception as e:
            print(f"音乐播放错误: {e}")
    
    # 在后台线程中播放音乐
    music_thread = threading.Thread(target=music_player, daemon=True)
    music_thread.start()

def play_simple_beep():
    """播放简单的提示音"""
    try:
        # 在本地环境中，我们可以使用系统声音
        import sys
        if sys.platform == "win32":
            import winsound
            winsound.Beep(1000, 200)  # 频率1000Hz，持续时间200ms
        elif sys.platform == "darwin":  # macOS
            os.system('afplay /System/Library/Sounds/Ping.aiff &')
        else:  # Linux
            os.system('play -q -n synth 0.2 sine 1000 &')
    except:
        pass  # 如果无法播放，静默失败

def show_blessings_one_by_one():
    """一个个显示祝福"""
    placeholder = st.empty()
    
    if 'blessing_count' not in st.session_state:
        st.session_state.blessing_count = 0
    if 'blessings_shown' not in st.session_state:
        st.session_state.blessings_shown = []
    
    total_blessings = 30  # 减少数量
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    blessings_container = st.empty()
    
    # 开始播放音乐
    play_music_in_thread()
    
    for i in range(total_blessings):
        progress = (i + 1) / total_blessings
        progress_bar.progress(progress)
        status_text.text(f'✨ 发送祝福 {i+1}/{total_blessings}')
        
        text = random.choice(wordslist)
        color = random.choice(colors)
        left = random.randint(1, 95)
        top = random.randint(3, 90)
        font_size = random.randint(18, 24)
        
        new_blessing = f'''
        <div class="blessing" style="
            left: {left}vw; 
            top: {top}vh;
            background-color: {color};
            color: #333;
            font-size: {font_size}px;
        ">{text}</div>
        '''
        st.session_state.blessings_shown.append(new_blessing)
        blessings_container.markdown(''.join(st.session_state.blessings_shown), unsafe_allow_html=True)
        
        # 每5个祝福播放一次提示音
        if i % 5 == 0:
            play_simple_beep()
            
        time.sleep(0.15)
    
    status_text.success('🎊 祝福发送完成！')
    
    if st.button('🔄 再来一次'):
        for key in ['blessing_count', 'blessings_shown']:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

def main():
    # 标题
    st.markdown("""
    <div class="title-container">
        <div class="title-text">moonbird的祝福</div>
        <div class="subtitle">带音效的祝福程序 🎵</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 音乐状态显示
    if music_available:
        st.success("🎵 音乐系统已就绪")
    else:
        st.warning("🔇 音乐功能在当前环境不可用，但祝福效果正常")
    
    if 'blessing_count' not in st.session_state or st.session_state.blessing_count == 0:
        if st.button('🎁 开始祝福', type='primary', use_container_width=True):
            st.session_state.blessing_count = 1
            st.rerun()
    
    if 'blessing_count' in st.session_state and st.session_state.blessing_count > 0:
        show_blessings_one_by_one()

if __name__ == '__main__':
    main()
