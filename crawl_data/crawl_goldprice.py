import yfinance as yf
gold_1d = yf.download("GC=F", period="5y", interval="1d")

gold_1d.to_csv("gold_5y_1d_aaaa.csv")

# tại thời điểm này là crawl data từ 29/7/2020 - 25/7/2025