# 读取用户数据
try:
    with open(self.USER_DATA_FILE, 'r', encoding='utf-8') as f:  # 打开文件,以只读模式读取
        user_data = json.load(f)  # 将文件中的json数据解析为python对象
except FileNotFoundError:  # 若出现异常，建立空字典
    user_data = {} # 创建一个新字典

# 创建账户类
class Account:
    def __init__(self, username, password, game_times , win_times, winning_percentage):
        self.username = username
        self.password = password
        self.game_times = game_times
        self.win_times = win_times
        self.winning_percentage = winning_percentage

    def to_dict(self):  # 用于将Account对象的username和password等属性打包为一个字典并返回
        return {"username": self.username,  # 便于将用户的信息写入文件或先从文件中读取出来
                "password": self.password,
                "game_times": self.game_times,
                "win_times": self.win_times,
                "winning_percentage": self.winning_percentage}

# 完善用户注册/账号创建信息
def register(self):
    """处理用户注册。"""
    username = self.entry_username.get()  # 获取用户名
    password = self.entry_password.get()  # 获取密码
    game_times = 0 # 初始化游戏次数
    win_times = 0 # 初始化胜利次数
    winning_percentage = win_times / game_times * 100 # 计算胜率

    # 检查用户名和密码是否为空
    if not username or not password:
        messagebox.showwarning("输入错误", "用户名和密码不能为空！")
        return

    # 读取用户数据
    with open(self.USER_DATA_FILE, 'r') as f:
        user_data = json.load(f)

    # 检查用户名是否已存在
    if username in user_data:
        messagebox.showwarning("注册失败", "用户名已存在！")
    else:
        # 将新用户信息保存到文件
        user_data[username] = {
            "password": password,
            "game_times": game_times,
            "win_times": win_times,
            "winning_percentage": winning_percentage
        }
        with open(self.USER_DATA_FILE, 'w') as f:
            json.dump(user_data, f)

        messagebox.showinfo("注册成功", "注册成功，请登录！")  # 显示注册成功消息
        self.entry_username.delete(0, tk.END)  # 清空输入框
        self.entry_password.delete(0, tk.END)  # 清空输入框

# 查询用户信息
def view_user_info():
    if not username in user_data: # 用户名输入错误
        messagebox.showwarning("输入错误", "用户名不存在！")
    else:
        # 格式化标题行
        title_row = "{:<10} {:<10} {:<10} {:<10} {:<10}".format(
        '用户名', '密码', '游戏次数', '胜利次数', '胜率（%）')

        # 格式化用户数据行
        data_row = "{:<10} {:<10} {:<10} {:<10} {:<10}".format(
        user_data["username"], user_data["password"], user_data["game_times"], user_data["win_times"], user_data["winning_percentage"])

        # 将标题行和数据行合并为一个单一的字符串消息
        message = title_row + "\n" + data_row

        # 输出用户信息
        messagebox.showinfo("用户信息", message)

