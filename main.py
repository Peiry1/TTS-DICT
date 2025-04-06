import dict_process as dp
import tts as tts
import UI as ui

class MainProcess:
    def __init__(self):
        self.dict_path = 'ECDICT/stardict.db'
        self.dict_srcpath = 'ECDICT/stardict.csv'
        self.dict_manager = dp.DictionaryManager(self.dict_path, self.dict_srcpath)
        self.tts = tts.TTS()  # 初始化 TTS 模块

    def word_search(self, word):
        """查词并输出结果"""
        self.dict_manager.check_dictionary()
        match_result = self.dict_manager.search_word(word)  # 使用字典管理器的 search_word 方法
        
        # 如果没有找到结果
        if not match_result:
            return "未找到相关结果"
            
        # 如果是模糊匹配（多个结果）
        detailed_list  = []
        for _, matched_word in match_result:
            # 对每个匹配的单词进行详细查询
            detailed  = self.dict_manager.query_word(matched_word)
            if detailed:
                detailed_list.append(detailed)
                
        return detailed_list

    def start_ui(self):
        """启动 UI 界面"""
        ui_instance = ui.UI(self)  # 创建 UI 实例，传入 MainProcess 实例
        ui_instance.run()

        
if __name__ == "__main__":
    try:
        dict_manager = dp.DictionaryManager('ECDICT/stardict.db', 'ECDICT/stardict.csv')
        dict_manager.check_dictionary()

        main = MainProcess()
        main.start_ui()  # 启动 UI 界面
    except FileNotFoundError as e:
        print(e)