import os
import re
import time

def extract_from_resource_id(all_info, string):
	return all_info.partition(string)[0][::-1].partition('text="'[::-1])[0][::-1]

def grab_ui_automator():
	command = "adb pull $(adb shell uiautomator dump | grep -oP '[^ ]+.xml') /tmp/view.xml"
	os.system(command)
	time.sleep(.1)
	all_info = open("/tmp/view.xml").read()
	attention_val = extract_from_resource_id(all_info, '" resource-id="com.pwittchen.eeganalyzer:id/tv_attention"')
	meditation_val = extract_from_resource_id(all_info, '" resource-id="com.pwittchen.eeganalyzer:id/tv_meditation"')
	blink_val = extract_from_resource_id(all_info, '" resource-id="com.pwittchen.eeganalyzer:id/tv_blink"')
	raw_val = extract_from_resource_id(all_info, '" resource-id="com.pwittchen.eeganalyzer:id/tv_raw_data"')
	print("Attention Value: {}".format(attention_val))
	print("Meditation Value: {}".format(meditation_val))
	print("Blink Value: {}".format(blink_val))
	print("Raw Value: {}".format(raw_val))

if __name__ == '__main__':
	for i in range(100):
		grab_ui_automator()
