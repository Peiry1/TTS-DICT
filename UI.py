import tkinter as tk

class UI:
    def __init__(self, main_process):
        self.main_process = main_process
        self.root = tk.Tk()
        self.root.title("TTS 词典查询")
        self._center_window()  # 窗口居中
        self._setup_ui()

    def _center_window(self):
        """让窗口居中显示"""
        window_width = 800  # 窗口宽度
        window_height = 600  # 窗口高度

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def _setup_ui(self):
        """初始化 UI 组件"""
        # 主容器，用于布局
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # TTS 发音按钮
        self.tts_button = tk.Button(main_frame, text="TTS发音", command=self.on_tts, font=("Arial", 14))
        self.tts_button.pack(pady=10)

        # 输入框
        self.entry = tk.Entry(main_frame, font=("Arial", 14), fg='grey')
        self.entry.pack(fill=tk.X, pady=10)
        self.entry.insert(0, "请输入...")
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.add_placeholder)

        # 查询结果显示区域
        self.result_text = tk.Text(main_frame, font=("Arial", 12))
        self.result_text.pack(fill=tk.BOTH, expand=True, pady=10)

        # 在所有组件初始化完成后再设置 trace
        self.entry_var = tk.StringVar()
        self.entry_var.trace("w", self.on_entry_change)
        self.entry.config(textvariable=self.entry_var)

    def clear_placeholder(self, event):
        """清除提示文字"""
        if self.entry.get() == "请输入...":
            self.entry.delete(0, tk.END)
            self.entry.config(fg='black')

    def add_placeholder(self, event):
        """添加提示文字"""
        if not self.entry.get():
            self.entry.insert(0, "请输入...")
            self.entry.config(fg='grey')

    def on_entry_change(self, *args):
        """处理输入框内容变化事件"""
        if not hasattr(self, 'result_text'):  # 防御性检查
            return
            
        word = self.entry_var.get()
        if word and word != "请输入...":  # 只有当输入框不为空且不是提示文字时才查询
            result = self.main_process.word_search(word)
            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete(1.0, tk.END)
    
            for item in result:
                w = item.get('word','')
                p = item.get('phonetic','')
                t = item.get('translation','')
                # 插入单词信息
                self.result_text.insert(tk.END, f"单词: {w}\n音标: {p}\n释义: {t}\n")
                
                # 在每个单词后插入发音按钮
                btn = tk.Button(self.result_text, text="🔊", 
                              command=lambda w=w: self.main_process.tts.speak(w))
                self.result_text.window_create(tk.END, window=btn)
                self.result_text.insert(tk.END, "\n" + "-"*40 + "\n\n")
            
            self.result_text.config(state=tk.DISABLED)  # 设置为只读模式

        # 设置窗口大小变化时的行为
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    # def on_search(self):  #未使用
    #     """处理查询事件"""
    #     word = self.entry.get()
    #     result = self.main_process.word_search(word)  # 获取查询结果
    #     self.result_text.delete(1.0, tk.END)  # 清空之前的查询结果
    #     self.result_text.insert(tk.END, result)  # 显示查询结果

    def on_tts(self):
        """处理 TTS 发音事件"""
        word = self.entry.get()
        self.main_process.tts.speak(word)

    def run(self):
        """启动 UI"""
        self.root.mainloop()

    # def display_results(self, results): #未使用
    #     """显示查询结果"""
    #     self.result_text.delete(1.0, tk.END)
        
    #     # 存储所有单词
    #     self.words = []
        
    #     for result in results.split("----------------------------------------"):
    #         if not result.strip():
    #             continue
                
    #         # 添加结果文本
    #         self.result_text.insert(tk.END, result.strip() + "\n")
            
    #         # 提取单词
    #         word = result.split("\n")[0].replace("单词: ", "").strip()
    #         self.words.append(word)
            
    #         # 添加发音按钮
    #         tts_button = tk.Button(self.result_text, text="🔊", 
    #                              command=lambda w=word: self.main_process.tts.speak(w))
    #         self.result_text.window_create(tk.END, window=tts_button)
    #         self.result_text.insert(tk.END, "\n\n")
            
    #     # 绑定回车键
    #     self.root.bind('<Return>', self.on_enter_key)
    #     self.result_text.config(state=tk.DISABLED)

    # def on_enter_key(self, event):
    #     """处理回车键事件"""
    #     # 获取当前光标位置
    #     index = self.result_text.index(tk.INSERT)
        
    #     # 查找最近的单词
    #     for i, word in enumerate(self.words):
    #         line_start = f"{i*3 + 1}.0"
    #         line_end = f"{i*3 + 3}.0"
    #         if self.result_text.compare(line_start, '<=', index) and \
    #            self.result_text.compare(index, '<', line_end):
    #             self.main_process.tts.speak(word)
    #             break