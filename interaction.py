import os
import re

def extract_from_resource_id(all_info, string):
	return all_info.partition(string)[0][::-1].partition('text="'[::-1])[0][::-1]

def grab_ui_automator():
	command = "sudo adb pull $(adb shell uiautomator dump | grep -oP '[^ ]+.xml') info.xml"
	os.system(command)
	all_info = open("info.xml").read()
	attention_val = extract_from_resource_id(all_info, '" resource-id="com.pwittchen.eeganalyzer:id/tv_attention"')
	print attention_val

if __name__ == '__main__':
	grab_ui_automator()
