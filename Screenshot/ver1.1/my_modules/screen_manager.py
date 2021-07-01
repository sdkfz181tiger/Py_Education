# coding: utf-8

import datetime
import os
import sys
import sqlite3
import time
import chromedriver_binary # For Mac
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

# MainManager
class MainManager:

	def __init__(self, prefix):
		print("MainManager:%s" % (prefix))
		# Make directory
		self.dir_path = os.path.join("images", prefix, self.get_dir_name())
		os.makedirs(self.dir_path, exist_ok=True)

	def browse(self, db_name, url, match):
		print("Browse URL:%s" % (url))
		
		# Launch browser
		driver = webdriver.Chrome(options=self.get_options())
		driver.set_window_size(1400, 2000)
		driver.get(url)# Get
		time.sleep(5)# Sleep

		# Read more(For Note)
		try:
			driver.find_element_by_class_name("o-timelineHome__more").find_element_by_tag_name("button").click()
			time.sleep(2)
			for n in range(10):
				driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				time.sleep(1)
		except Exception as e:
			print(e)
		time.sleep(1)# Sleep
		
		# Searching...
		alinks = driver.find_elements_by_tag_name("a")
		for alink in alinks:
			url = str(alink.get_attribute("href"))
			if(len(str(alink.text)) <= 0): continue# Length
			if(match not in str(url)): continue# Match
			if(0 < self.check(db_name, url)): continue# DB
			self.save(url)# Save

		time.sleep(1)# Sleep
		driver.quit()# Quit

	def save(self, url):
		print("Save URL:%s" % (url))

		# arr = [u for u in url.split("/") if "http" not in u and len(u) < 10 ]
		# file_url = "-".join(arr)
		# file_name = "{}_{}.png".format(file_url, alink.text)
		# file_path = os.path.join(self.dir_path, file_name)
		
		# Launch browser
		driver = webdriver.Chrome(options=self.get_options())
		driver.set_window_size(1400, 2000)
		driver.get(url)# Get
		time.sleep(5)# Sleep

		# File title(For Note)
		try:
			title = driver.find_element_by_class_name("o-noteContentText__title")
			print("Title:%s" % (title.text))
		except Exception as e:
			print(e)
		time.sleep(1)# Sleep

		try:
			date = driver.find_element_by_class_name("o-noteContentHeader__date")
			print("Date:%s" % (date.text))
		except Exception as e:
			print(e)
		time.sleep(1)# Sleep

		# for title in titles:
		# 	# name = str(dtime.get_attribute("href"))
		# 	print("Title:%s" % (title.text))

		# dtimes = driver.find_elements_by_tag_name("h1")
		# for dtime in dtimes:
		# 	# name = str(dtime.get_attribute("href"))
		# 	print("Time:%s" % (dtime.text))
		
		# Read more(For Hatena)
		# try:
		# 	driver.find_element_by_class_name("read-more-comments").find_element_by_tag_name("a").click()
		# except Exception as e:
		# 	print(e)
		# time.sleep(1)# Sleep
		
		# w = driver.execute_script("return document.body.scrollWidth;")
		# h = driver.execute_script("return document.body.scrollHeight;")
		# driver.set_window_size(w, h)
		# driver.save_screenshot(file_path)# Screen shot
		time.sleep(1)# Sleep
		driver.quit()# Quit

	def check(self, db_name, url):
		print("Check DB:%s URL:%s" % (db_name, url))
		
		# Sqlite3
		db_connect = sqlite3.connect(db_name)
		db_cursor = db_connect.cursor()
		db_cursor.execute("CREATE TABLE IF NOT EXISTS tbl_screenshot(id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT)")
		db_select = db_cursor.execute("SELECT * FROM tbl_screenshot WHERE url='{}'".format(url))
		# Count
		cnt = len(db_select.fetchall())
		if(cnt <= 0):
			db_cursor.execute("INSERT INTO tbl_screenshot(url) VALUES('{}')".format(url))
			db_connect.commit()
		db_cursor.close()
		db_connect.close()
		return cnt

	def get_dir_name(self):
		# Directory name
		d_obj   = datetime.datetime.now()
		s_year  = str(d_obj.year).zfill(4)
		s_month = str(d_obj.month).zfill(2)
		s_day   = str(d_obj.day).zfill(2)
		return "{}{}{}".format(s_year, s_month, s_day)

	def get_file_name(self):
		# File name
		d_obj   = datetime.datetime.now()
		s_hour  = str(d_obj.hour).zfill(2)
		s_min   = str(d_obj.minute).zfill(2)
		s_sec   = str(d_obj.second).zfill(2)
		return "{}{}{}".format(s_hour, s_min, s_sec)

	def get_options(self):
		# Options
		options = webdriver.ChromeOptions()
		options.add_argument("start-maximized")
		options.add_argument("enable-automation")
		options.add_argument("--headless")
		options.add_argument("--no-sandbox")
		options.add_argument("--disable-infobars")
		options.add_argument('--disable-extensions')
		options.add_argument("--disable-dev-shm-usage")
		options.add_argument("--disable-browser-side-navigation")
		options.add_argument("--disable-gpu")
		options.add_argument('--ignore-certificate-errors')
		options.add_argument('--ignore-ssl-errors')
		prefs = {"profile.default_content_setting_values.notifications" : 2}
		options.add_experimental_option("prefs", prefs)
		return options

# HatenaManager
class HatenaManager(MainManager):

	def __init__(self, prefix):
		super().__init__(prefix)
		print("HatenaManager")

#QiitaManager
class QiitaManager(MainManager):

	def __init__(self, prefix):
		super().__init__(prefix)
		print("QiitaManager")

#NoteManager
class NoteManager(MainManager):

	def __init__(self, prefix):
		super().__init__(prefix)
		print("NoteManager")
		
