import json
import xml.etree.ElementTree as ET
from pprint import pprint

def transform_json_into_list():
    with open('input/newsafr.json', encoding='utf-8') as file:
        data = json.load(file)
        data_list = data['rss']['channel']['items']
        news_discriptions = []
        for item in data_list:
            news_body = item['description']
            news_body = news_body.split(' ')
            news_discriptions.extend(news_body)
        # print(news_discriptions)
    return news_discriptions

def transform_xml_into_list():
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('input/newsafr.xml', parser)
    root = tree.getroot()
    discription = root.findall('channel/item/description')
    news_discriptions = []
    for item in discription:
        news_body = item.text
        news_body = news_body.split(' ')
        news_discriptions.extend(news_body)
    # print(news_discriptions)
    return news_discriptions

def sort_by_length(length,file_type):
    if file_type == 'xml':
        news_discriptions = transform_xml_into_list()
    elif file_type == 'json':
        news_discriptions = transform_json_into_list()
    else:
        print(f'Выберите формат: xml или json')
    sorted_news_discriptions = sorted(news_discriptions, key=len, reverse=True)
    for word in sorted_news_discriptions:
        if len(word) <= length:
            last_element = sorted_news_discriptions.index(word)
            break
    cut_news_discriptions = sorted_news_discriptions[:last_element]
    # print(cut_news_discriptions)
    return cut_news_discriptions

def top_popular_words(number, length, file_type):
    news_discription = sort_by_length(length, file_type)
    frequency_list = []
    temp_top_dict = {}
    for word in news_discription:
        if word in frequency_list:
            temp_top_dict[word] += 1
        else:
            temp_top_dict[word] = 1
        frequency_list.append(word)
    top_dict = sorted(temp_top_dict, key=lambda x: temp_top_dict[x], reverse=True)
    cut_top_dict = top_dict[:number]
    print(cut_top_dict)


top_popular_words(10, 6, 'json')
