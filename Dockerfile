FROM python:3.9-slim-buster

# イメージ内のディレクトリ
WORKDIR /app

# カレントディレクトリからrequirements.txtをコピー
COPY requirements.txt .

# SQLiteデータベースファイルをコピー
COPY /Careerup.db /app/Careerup.db

# Dockerが実行するコマンド
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y ffmpeg && \
    pip install -r requirements.txt

# Dockerが外部に公開するポート
EXPOSE 8501
#EXPOSE 443

# 
COPY . /app


# コンテナが起動した際に実行
# ENTRYPOINTでStreamlitを起動するように指定し、
# CMDで実行するPythonファイルを指定
ENTRYPOINT ["streamlit", "run"]
CMD ["DBsearch.py"]


# メモ 依存関係をインストール 
# メモ RUN pip install --no-cache-dir -r requirements.txt
# メモ CMD ["streamlit", "run", "DBsearch.py"]
