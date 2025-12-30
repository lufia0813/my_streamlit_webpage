import streamlit as st

st.title("📝 瓜的待辦清單")

# step 1: initialize
if 'tasks' not in st.session_state:
	st.session_state.tasks = []  # create new list 'tasks'

# step 2: 建立輸入框與按鈕
col1, col2 = st.columns([4, 1]) # 切版：輸入框寬一點，按鈕窄一點

with col1:
    new_task = st.text_input("想做什麼？", placeholder="例如：寫完 Python 作業")

with col2:
    # 為了排版好看，加個空行讓按鈕往下移對齊
    st.write("") 
    st.write("")
    add_btn = st.button("新增")

# step 3: 寫入資料與顯示
if add_btn:
    if new_task: # ensure使用者真的有打字，不是空的
        # 把新任務 append 丟進 tasks 清單
        st.session_state.tasks.append(new_task)
    else:
        st.warning("請先輸入內容喔！")

# show list rn
st.divider() # 分隔線
st.subheader("待辦事項：")

# 把背包裡的每一項任務拿出來印在螢幕上
# enumerate 是為了拿到index，sstart from 1
for index, task in enumerate(st.session_state.tasks, start=1):
    st.write(f"{index}. {task}")

st.write(st.session_state)
