# 測試引用相關套件
from urllib.request import urlopen
from bs4 import BeautifulSoup
import threading, queue, time, datetime, os, json, subprocess, fcntl

# <!-- For MAC電腦
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# -->
