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
	
# 新增區塊改用st.form
with st.form(key = "add_task_form", clear_on_submit = True):
	# clear_on_submit = True 會自動清空輸入框
	col1, col2 = st.columns([4, 1]) # 切版：輸入框寬一點，按鈕窄一點

with col1:
	new_task = st.text_input("今天想做什麼？")

with col2:
	# 為了排版好看，加個空行讓按鈕往下移對齊
	st.write("") 
	st.write("")
	# 改用st.form
	submit_btn = st.form_submit_button("新增")

if submit_btn and new_task: # 按鈕被按下+有輸入文字 才執行
	st.session_state.tasks.append(new_task)
	st.rerun() # 馬上更新清單
	
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
		st.info(f"{index+1}. {task}", icon="📌")
	with c2:
		# del button
		if st.button("❌", key = f"delete_{index}"): 
			# key=f"delete_{index}" 讓每個按鈕的 ID 會變成 delete_0, delete_1...
			st.session_state.tasks.pop(index) # 立即更新網頁
			st.rerun()

# st.write(st.session_state)
