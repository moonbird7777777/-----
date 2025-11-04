import streamlit as st
import random
import time

# 设置页面配置
st.set_page_config(
    page_title="moonbird的炫酷祝福",
    page_icon="🎉",
    layout="centered"
)

# 极致炫酷的CSS样式
st.markdown("""
<style>
.blessing {
    position: fixed;
    padding: 15px 25px;
    border-radius: 20px;
    font-family: 'SimHei', 'Microsoft YaHei', sans-serif;
    font-size: 20px;
    font-weight: bold;
    z-index: 1000;
    box-shadow: 0 10px 40px rgba(0,0,0,0.5);
    border: 4px solid rgba(255,255,255,0.8);
    min-width: 120px;
    text-align: center;
    animation: superBounce 1s ease-out;
    backdrop-filter: blur(10px);
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

@keyframes superBounce {
    0% { 
        opacity: 0; 
        transform: translateY(-100px) scale(0.2) rotate(-30deg);
        filter: blur(20px);
    }
    30% { 
        opacity: 0.8; 
        transform: translateY(30px) scale(1.3) rotate(15deg);
        filter: blur(5px);
    }
    50% { 
        transform: translateY(-20px) scale(1.1) rotate(-10deg);
    }
    70% { 
        transform: translateY(10px) scale(1.05) rotate(5deg);
    }
    100% { 
        opacity: 1; 
        transform: translateY(0) scale(1) rotate(0);
        filter: blur(0);
    }
}

.blessing:hover {
    animation: megaGlow 0.6s ease-in-out infinite alternate, float 3s ease-in-out infinite;
    transform: scale(1.2) rotate(5deg);
    z-index: 1001;
}

@keyframes megaGlow {
    0% { 
        box-shadow: 0 10px 40px rgba(0,0,0,0.5), 
                   0 0 20px currentColor,
                   0 0 40px currentColor;
        transform: scale(1.15);
    }
    100% { 
        box-shadow: 0 15px 50px rgba(0,0,0,0.6), 
                   0 0 30px currentColor,
                   0 0 60px currentColor,
                   0 0 80px rgba(255,255,255,0.5);
        transform: scale(1.25);
    }
}

@keyframes float {
    0%, 100% { transform: translateY(0px) rotate(5deg); }
    50% { transform: translateY(-10px) rotate(-5deg); }
}

/* 粒子效果 */
.particle {
    position: fixed;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    pointer-events: none;
    z-index: 999;
    animation: particleFloat 3s ease-in-out infinite;
}

@keyframes particleFloat {
    0% { 
        opacity: 0;
        transform: translateY(0) rotate(0deg) scale(0);
    }
    10% { 
        opacity: 1;
        transform: translateY(-20px) rotate(180deg) scale(1);
    }
    90% { 
        opacity: 0.8;
        transform: translateY(-100px) rotate(720deg) scale(1.2);
    }
    100% { 
        opacity: 0;
        transform: translateY(-150px) rotate(900deg) scale(0);
    }
}

/* 超炫背景 */
body {
    background: 
        radial-gradient(circle at 20% 80%, rgba(255,107,107,0.3) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(255,217,61,0.3) 0%, transparent 50%),
        radial-gradient(circle at 40% 40%, rgba(107,207,127,0.3) 0%, transparent 50%),
        radial-gradient(circle at 60% 60%, rgba(77,150,255,0.3) 0%, transparent 50%),
        linear-gradient(135deg, #FF6B6B 0%, #FFD93D 25%, #6BCF7F 50%, #4D96FF 75%, #9D4BFF 100%);
    background-size: 400% 400%;
    animation: cosmicShift 20s ease infinite;
    min-height: 100vh;
}

@keyframes cosmicShift {
    0% { 
        background-position: 0% 50%;
        filter: hue-rotate(0deg);
    }
    25% { 
        background-position: 100% 50%;
        filter: hue-rotate(90deg);
    }
    50% { 
        background-position: 50% 100%;
        filter: hue-rotate(180deg);
    }
    75% { 
        background-position: 0% 50%;
        filter: hue-rotate(270deg);
    }
    100% { 
        background-position: 50% 0%;
        filter: hue-rotate(360deg);
    }
}

/* 标题特效 */
.title-container {
    text-align: center;
    padding: 30px;
    background: rgba(255,255,255,0.15);
    border-radius: 30px;
    backdrop-filter: blur(20px);
    margin-bottom: 30px;
    border: 3px solid rgba(255,255,255,0.4);
    box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    animation: titleGlow 4s ease-in-out infinite alternate;
}

@keyframes titleGlow {
    0% { 
        box-shadow: 0 15px 35px rgba(0,0,0,0.3),
                   0 0 30px rgba(255,107,107,0.5);
        transform: scale(1);
    }
    100% { 
        box-shadow: 0 20px 45px rgba(0,0,0,0.4),
                   0 0 50px rgba(255,217,61,0.6),
                   0 0 70px rgba(107,207,127,0.4);
        transform: scale(1.02);
    }
}

.title-text {
    font-size: 4em;
    font-weight: bold;
    background: linear-gradient(45deg, #FF6B6B, #FFD93D, #6BCF7F, #4D96FF, #9D4BFF, #FF6B6B);
    background-size: 400% 400%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: rainbowFlow 6s ease infinite, textShake 3s ease-in-out infinite;
    text-shadow: 3px 3px 8px rgba(0,0,0,0.2);
}

@keyframes rainbowFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes textShake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-2px); }
    75% { transform: translateX(2px); }
}

.subtitle {
    font-size: 1.5em;
    color: white;
    margin-top: 15px;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
    animation: subtitlePulse 2s ease-in-out infinite;
}

@keyframes subtitlePulse {
    0%, 100% { opacity: 0.8; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.05); }
}

/* 超级按钮 */
.super-button {
    background: linear-gradient(45deg, #FF6B6B, #FFD93D, #6BCF7F, #4D96FF);
    background-size: 400% 400%;
    animation: buttonFlow 3s ease infinite, buttonPulse 2s ease-in-out infinite;
    color: white;
    border: none;
    padding: 25px 50px;
    border-radius: 35px;
    font-size: 1.8em;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 12px 35px rgba(0,0,0,0.4);
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    position: relative;
    overflow: hidden;
}

.super-button::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(45deg, transparent, rgba(255,255,255,0.3), transparent);
    transform: rotate(45deg);
    animation: buttonShine 3s ease-in-out infinite;
}

@keyframes buttonShine {
    0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
    100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
}

@keyframes buttonFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes buttonPulse {
    0%, 100% { transform: scale(1); box-shadow: 0 12px 35px rgba(0,0,0,0.4); }
    50% { transform: scale(1.08); box-shadow: 0 15px 45px rgba(0,0,0,0.6), 0 0 30px rgba(255,255,255,0.3); }
}

.super-button:hover {
    animation: buttonFlow 1s ease infinite, buttonPulse 0.5s ease-in-out infinite;
    transform: scale(1.1);
}

/* 进度条美化 */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #FF6B6B, #FFD93D, #6BCF7F, #4D96FF, #9D4BFF);
    background-size: 300% 300%;
    animation: gradientFlow 2s ease infinite;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(255,255,255,0.5);
}

/* 隐藏Streamlit元素 */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

# 扩展的祝福语和颜色
wordslist = [
    '早睡💤', '工作顺利📚', '要开心呀！😊', '天天快乐🎈', '心想事成✨',
    '身体健康💪', '万事如意🌟', '笑口常开😄', '平安喜乐🕊️', '好运连连🍀',
    '梦想成真🌈', '前程似锦🎓', '友谊长存👫', '幸福美满❤️', '活力满满⚡',
    '聪明伶俐🎯', '勇敢坚强🛡️', '温柔善良🌸', '自信美丽🌟', '无忧无虑🎵',
    '收获满满📦', '灵感不断💡', '光芒四射☀️', '温暖如春🌺', '财源滚滚💰',
    '事业腾飞🚀', '爱情甜蜜💑', '家庭和睦🏠', '青春永驻🌹', '能量爆棚⚡',
    '幸运爆棚🎯', '快乐加倍😆', '好运爆棚🎊', '奇迹发生🌟', '心想事成🎁'
]

colors = [
    '#FF6B6B', '#FFD93D', '#6BCF7F', '#4D96FF', '#9D4BFF',
    '#FF8E8E', '#FFE066', '#8CE08C', '#6BA8FF', '#B366FF',
    '#FF5252', '#FFEB3B', '#4CAF50', '#2196F3', '#9C27B0',
    '#FF4081', '#FF9800', '#00E676', '#00B0FF', '#E040FB',
    '#FF1744', '#FFC107', '#00C853', '#0091EA', '#D500F9'
]

def create_particles():
    """创建粒子效果"""
    particles_html = ""
    for i in range(20):  # 创建20个粒子
        color = random.choice(colors)
        left = random.randint(0, 100)
        delay = random.uniform(0, 5)
        duration = random.uniform(2, 4)
        
        particles_html += f'''
        <div class="particle" style="
            left: {left}vw;
            background-color: {color};
            animation-delay: {delay}s;
            animation-duration: {duration}s;
        "></div>
        '''
    return particles_html

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
    
    # 添加粒子效果
    particles_html = create_particles()
    st.markdown(particles_html, unsafe_allow_html=True)
    
    for i in range(total_blessings):
        progress = (i + 1) / total_blessings
        progress_bar.progress(progress)
        status_text.text(f'✨ 超炫祝福发送中... {i+1}/{total_blessings}')
        
        text = random.choice(wordslist)
        color = random.choice(colors)
        left = random.randint(1, 95)
        top = random.randint(3, 90)
        font_size = random.randint(20, 28)
        
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
    
    status_text.success('🎊 超炫祝福发送完成！视觉效果爆炸！')
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button('🚀 再来一次超炫体验！', type='primary', use_container_width=True):
            for key in ['blessing_count', 'blessings_shown']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

def main():
    # 超炫标题
    st.markdown("""
    <div class="title-container">
        <div class="title-text">moonbird的炫酷祝福</div>
        <div class="subtitle">视觉盛宴 • 极致体验 • 祝福满屏</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 特效说明
    st.info("""
    🌟 **特效说明**：
    - 💫 悬浮粒子背景
    - 🌈 彩虹渐变流动
    - ✨ 3D弹跳动画
    - 🔥 发光悬浮效果
    - 🎭 色彩变幻魔法
    """)
    
    if 'blessing_count' not in st.session_state or st.session_state.blessing_count == 0:
        st.markdown("<br><br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            if st.button('🎆 开启视觉盛宴！', type='primary', use_container_width=True):
                st.session_state.blessing_count = 1
                st.rerun()
    
    if 'blessing_count' in st.session_state and st.session_state.blessing_count > 0:
        show_blessings_one_by_one()

if __name__ == '__main__':
    main()
