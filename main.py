import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import threading

class BilibiliMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("B站视频播放量监控")
        self.root.geometry("400x300")

        self.url_label = tk.Label(root, text="视频URL:")
        self.url_label.pack()
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack()

        self.email_label = tk.Label(root, text="接收邮箱:")
        self.email_label.pack()
        self.email_entry = tk.Entry(root, width=50)
        self.email_entry.pack()

        self.start_button = tk.Button(root, text="开始监控", command=self.start_monitoring)
        self.start_button.pack()

    def get_play_count(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取播放量
        play_count_tag = soup.find('div', class_='view-text')
        if play_count_tag:
            play_count = play_count_tag.text.strip()
            return int(play_count)
        return None

    def send_email(self, subject, body):
        smtp_server = 'smtp.qq.com'
        smtp_port = 587
        sender_email = '*******'
        sender_password = '******'
        receiver_email = self.email_entry.get()

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())

    def monitor_loop(self):
        last_play_count = 0
        while True:
            play_count = self.get_play_count(self.url_entry.get())
            if play_count is not None:
                if play_count % 1 == 0 and play_count != last_play_count:
                    subject = f"B站视频播放量达到 {play_count}"
                    body = f"视频播放量已达到 {play_count}。"
                    self.send_email(subject, body)
                    last_play_count = play_count
            time.sleep(60)  # 每分钟检查一次

    def start_monitoring(self):
        monitor_thread = threading.Thread(target=self.monitor_loop)
        monitor_thread.daemon = True
        monitor_thread.start()
        messagebox.showinfo("提示", "监控已开始")

if __name__ == "__main__":
    root = tk.Tk()
    app = BilibiliMonitorApp(root)
    root.mainloop()
