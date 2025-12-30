import streamlit as st

st.title("📝 瓜的待辦清單")

# initialize
if 'tasks' not in st.session_state:
	st.session_state.tasks = []  # create new list 'tasks'

# callback
def add_task():
	task_content = st.session_state.new_task_input # 從輸入框(new_task_input)抓取文字
	if task_content:  # 如果真的有寫字
		st.session_state.tasks.append(task_content) # 1. 加進清單
		st.session_state.new_task_input = ""        # 2. 把輸入框歸零！
	
# 輸入框與按鈕
col1, col2 = st.columns([4, 1]) # 切版：輸入框寬一點，按鈕窄一點

with col1:
	# new_task = st.text_input("想做什麼？", placeholder="例如：寫完 Python 作業")
	st.text_input("今天想做什麼？", key="new_task_input", on_change=add_task)
	# key="new_task_input" -> 幫這個輸入框取個 ID，讓小幫手找得到它
	# on_change=add_task   -> 當使用者在框框按 enter 時，也呼叫小幫手

with col2:
	# 為了排版好看，加個空行讓按鈕往下移對齊
	st.write("") 
	st.write("")
	# add_btn = st.button("新增")
	st.button("新增", on_click=add_task) # on_click=add_task -> 當按鈕被按下去時，呼叫小幫手

# show list rn
st.divider() # 分隔線
st.subheader("待辦事項：")

# 把背包裡的每一項任務拿出來印在螢幕上 + 刪除按鈕
# enumerate 是為了拿到index，start from 1
for index, task in enumerate(st.session_state.tasks):
	# 每一行都切成兩欄：左邊放字，右邊放按鈕
	c1, c2 = st.columns([5, 1])

	with c1:
		# show num+task
		st.write(f"{index+1}. {task}")
	with c2:
		# del button
		if st.button("❌", key = f"delete_{index}"): 
			# key=f"delete_{index}" 讓每個按鈕的 ID 會變成 delete_0, delete_1...
			st.session_state.tasks.pop(index) # 立即更新網頁
			st.rerun()

# st.write(st.session_state)
