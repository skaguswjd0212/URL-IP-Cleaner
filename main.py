from flask import Flask, request, render_template
from markupsafe import Markup
import os
from threading import Timer
import webbrowser
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    result = ''
    
    if 'file' in request.files and request.files['file'].filename != '':
        file = request.files['file']
        content = file.read().decode('utf-8')  
        result = process_text(content) 
    elif 'content' in request.form and request.form['content'] != '':
        content = request.form['content']
        result = process_text(content)
    else:
        return 'No file or text provided'
     
    return render_template('index.html', result=Markup(result))

def process_text(text):
    # URL, IP 추출하여 텍스트로 변환
    lines = text.split('\n')
    processed_lines = [process_line(line) for line in lines]
    # 테이블 태그가 포함되어 있더라도 무시하고, 순수 텍스트만 출력
    return '\n'.join(filter(None, processed_lines))  


def process_line(line):
    # 비표준 프로토콜을 표준 프로토콜로 변환
    line = re.sub(r'h(x{2}|xs)p(s?)', r'http\2', line, flags=re.IGNORECASE)  # hxxp, hxxps, hxsp 변환
    line = re.sub(r'(https?)\[\:\]', r'\1:', line)  # http[:] -> http:
    line = re.sub(r'(https?)\[\:\/{1,2}\]', r'\1://', line)  # http[:/] 또는 http[://] -> http://
    line = line.replace('[.]', '.') # [.] -> .

    # 도메인 및 IP 주소의 포트 제거
    line = re.sub(r'(\d+\.\d+\.\d+\.\d+)\[\:\]\d+', r'\1', line)
    line = re.sub(r'(\d+\.\d+\.\d+\.\d+):\d+', r'\1', line)
    line = re.sub(r'([a-zA-Z0-9.-]+):\d+', r'\1', line) 


    pattern = r"""
        (?<![a-zA-Z0-9])https?://[^\s",]+|              # URL (http 또는 https) 
        \b(?:\d{1,3}\.){2,3}\d{1,3}\b|                  # IPv4 
        \b(?:[0-9a-fA-F]{1,4}:){1,7}[0-9a-fA-F]{1,4}\b| # IPv6 
        \b(?:[a-zA-Z0-9-]+\.){2,}[a-zA-Z]{2,}\b         # 도메인 필터링
    """
    urls_and_ips = re.findall(pattern, line, re.VERBOSE)

    return '\n'.join(urls_and_ips) if urls_and_ips else ''

if __name__ == '__main__':
    app.run()
