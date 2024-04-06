FROM python:3.9-slim-buster

# イメージ内のディレクトリ
WORKDIR /app

# 必要なライブラリのインストール
RUN pip install streamlit


# SSL証明書のコピー
COPY cert.crt /etc/ssl/certs/
COPY private.key /etc/ssl/private/

# Streamlitアプリのコピー
COPY dbsearch.py /app

# カレントディレクトリからrequirements.txtをコピー
COPY requirements.txt .

# SQLiteデータベースファイルをコピー
COPY /Careerup.db /app/Careerup.db

# Dockerが外部に公開するポート
EXPOSE 8501



# コンテナが起動した際に実行
# ENTRYPOINTでStreamlitを起動するように指定し、
# CMDで実行するPythonファイルを指定
ENTRYPOINT []
CMD ["streamlit", "run","dbsearch.py", "--server.enableCORS=false", "--server.enableXsrfProtection=false", "--server.address=0.0.0.0", "--server.port=8501", "--server.baseUrlPath", "/"]

