FROM python:3.11

WORKDIR /app

# Оновлюємо список пакетів і встановлюємо залежності
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    libnss3 \
    libgconf-2-4 \
    libfontconfig \
    libx11-dev \
    libxss1 \
    libappindicator3-1 \
    libasound2 \
    xvfb \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*

# Додаємо репозиторій для Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update

# Встановлюємо останню доступну стабільну версію Google Chrome
RUN apt-get install -y google-chrome-stable

# Перевіряємо, чи встановлений Google Chrome
RUN google-chrome --version || echo "Google Chrome installation failed"

# Копіюємо chromedriver в контейнер
COPY chromedriver /app/chromedriver

# Додаємо права на виконання для chromedriver
RUN chmod +x /app/chromedriver

# Копіюємо файли проекту
COPY requirements.txt .
COPY .env .
COPY . .

# Встановлюємо Python залежності
RUN pip install --no-cache-dir -r requirements.txt

# Встановлюємо змінні середовища
ENV DISPLAY=:99
ENV PATH="/usr/local/bin:${PATH}"

CMD ["python", "main.py"]
