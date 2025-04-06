'''
功能：检测与调试部分接口函数
作者：星海
日期：2024-08-08
'''


import ECDICT.stardict as sd
import requests

# path='ECDICT/stardict.db'

# dictionary = sd.StarDict(path)

# # 查询单词并获取结果
# result = dictionary.query('insanely')

# # 打印查询结果
# print(result)

def query_word(word):
    """查询单词释义"""
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        return response.json()  # 返回JSON格式的结果
    except requests.exceptions.HTTPError as err:
        print(f"HTTP错误: {err}")
    except requests.exceptions.RequestException as err:
        print(f"请求错误: {err}")
    return None

def format_result(result):
    """格式化查询结果"""
    if not result:
        return "未找到相关结果"
    
    formatted = []
    for entry in result:
        word = entry.get('word', '')
        formatted.append(f"单词: {word}\n")
        
        # 处理释义
        for meaning in entry.get('meanings', []):
            part_of_speech = meaning.get('partOfSpeech', '')
            formatted.append(f"词性: {part_of_speech}\n")
            
            for definition in meaning.get('definitions', []):
                formatted.append(f"  - 释义: {definition.get('definition', '')}\n")
                if 'example' in definition:
                    formatted.append(f"    例句: {definition['example']}\n")
        
        # 处理来源
        if 'sourceUrls' in entry:
            formatted.append("\n来源:\n")
            for url in entry['sourceUrls']:
                formatted.append(f"  - {url}\n")
        
        formatted.append("\n----------------------------------------\n")
    
    return "".join(formatted)

# 示例用法
if __name__ == "__main__":
    word = "sensational"
    result = query_word(word)
    if result:
        print(format_result(result))