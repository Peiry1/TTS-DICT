import ECDICT.stardict as sd
import os
import sys

class DictionaryManager:
    def __init__(self, dict_path, dict_srcpath):
        # 处理开发环境和打包环境的路径
        if getattr(sys, 'frozen', False):
            # 运行在打包的 EXE 中
            base_path = os.path.dirname(sys.executable)
            self.dict_path = os.path.join(base_path, dict_path)
            self.dict_srcpath = os.path.join(base_path, dict_srcpath)
        else:
             # 运行在开发环境中
            self.dict_path = dict_path
            self.dict_srcpath = dict_srcpath
            
        self.dictionary = sd.StarDict(self.dict_path)

    def check_dictionary(self):
        """检查字典文件是否存在，必要时进行转换"""
        if os.path.exists(self.dict_path):
            return True
            
        if not os.path.exists(self.dict_srcpath):
            raise FileNotFoundError(f"词典文件 {self.dict_path} 和源文件 {self.dict_srcpath} 均不存在")
            
        sd.convert_dict(dstname=self.dict_path, srcname=self.dict_srcpath)
        
        if not os.path.exists(self.dict_path):
            raise RuntimeError(f"文件转换失败，未生成目标文件 {self.dict_path}")
            
        return True

    def search_word(self, word):
        """查询单词匹配"""
        return self.dictionary.match(word)

    def query_word(self, word):
        """查询单词详细释义"""
        return self.dictionary.query(word)

    def format_result(self, result):
        """格式化查询结果"""
        if not result:
            return "未找到相关结果"
        if isinstance(result, dict):
            return f"单词: {result['word']}\n音标: {result['phonetic']}\n释义: {result['translation']}"
        else:
            return "\n".join([f"{word}" for _, word in result])