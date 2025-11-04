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

/* 隐藏音频但确保播放 */
.audio-player {
    position: fixed;
    top: 0;
    left: 0;
    width: 100px;
    height: 50px;
    opacity: 0.01;
    z-index: 9999;
    pointer-events: none;
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

def play_background_music():
    """播放背景音乐 - 使用base64编码的音频数据"""
    # 这是一个简短的欢快音乐片段（base64编码）
    audio_base64 = """
    UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQoGAACBhYqFbF1fdJivrJBh
    AAAAk7G2l2U8AACPtLqXaDgAAI2yuZdmOAAAjLC5l2Y3AACLr7qXZjcAAIquu5dmNwAAia27l2Y3
    AACIq7uXZjcAAIequpdmNwAAhqi6l2Y3AACFp7mXZjcAAISmuJdmNwAAg6W3l2Y3AACCpLaXZjcA
    AIGjtZdmNwAAgKK0l2Y3AAB/oLOXZjcAAH6fsZdmNwAAfZ6vl2Y3AAB8nK2XZjcAAHuaq5dmNwAA
    epipl2Y3AAB4l6iXZjcAAHaVppdmNwAAdJOk
    """
    
    # 创建音频播放器
    audio_html = f"""
    <div class="audio-player">
        <audio id="bgMusic" autoplay loop>
            <source src="data:audio/wav;base64,{audio_base64}" type="audio/wav">
        </audio>
    </div>
    <script>
        // 确保音乐播放
        function playMusic() {{
            const audio = document.getElementById('bgMusic');
            if (audio) {{
                audio.volume = 0.3;
                const playPromise = audio.play();
                if (playPromise !== undefined) {{
                    playPromise.then(_ => {{
                        console.log('音乐开始播放');
                    }}).catch(error => {{
                        console.log('自动播放被阻止');
                        // 显示播放按钮
                        showPlayButton();
                    }});
                }}
            }}
        }}
        
        function showPlayButton() {{
            const btn = document.createElement('button');
            btn.innerHTML = '🎵 点击播放音乐';
            btn.style.cssText = `
                position: fixed;
                top: 10px;
                right: 10px;
                background: #FF6B6B;
                color: white;
                border: none;
                padding: 10px 15px;
                border-radius: 20px;
                cursor: pointer;
                z-index: 10000;
                font-size: 14px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.3);
            `;
            btn.onclick = function() {{
                document.getElementById('bgMusic').play();
                this.remove();
            }};
            document.body.appendChild(btn);
        }}
        
        // 页面加载后尝试播放
        window.addEventListener('load', function() {{
            setTimeout(playMusic, 500);
        }});
        
        // 用户交互时也尝试播放
        document.addEventListener('click', function() {{
            playMusic();
        }});
    </script>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

def show_blessings_one_by_one():
    """一个个显示祝福"""
    placeholder = st.empty()
    
    if 'blessing_count' not in st.session_state:
        st.session_state.blessing_count = 0
    if 'blessings_shown' not in st.session_state:
        st.session_state.blessings_shown = []
    
    total_blessings = 50
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    blessings_container = st.empty()
    
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
        time.sleep(0.1)
    
    status_text.success('🎊 祝福发送完成！')
    
    if st.button('🔄 再来一次'):
        for key in ['blessing_count', 'blessings_shown']:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

def main():
    # 立即开始播放音乐
    play_background_music()
    
    # 标题
    st.markdown("""
    <div class="title-container">
        <div class="title-text">moonbird的祝福</div>
        <div class="subtitle">音乐自动播放中... 🎵</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 音乐状态提示
    st.info("💡 如果音乐没有自动播放，请点击页面任意位置或刷新页面")
    
    if 'blessing_count' not in st.session_state or st.session_state.blessing_count == 0:
        if st.button('🎁 开始祝福', type='primary', use_container_width=True):
            st.session_state.blessing_count = 1
            st.rerun()
    
    if 'blessing_count' in st.session_state and st.session_state.blessing_count > 0:
        show_blessings_one_by_one()

if __name__ == '__main__':
    main()
