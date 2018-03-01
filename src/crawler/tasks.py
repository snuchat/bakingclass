import os
import sys
import json
import re
import urllib.request
import naver_secrets

test_search_string_list = ['홈', '베이킹', '쿠킹']
test_search_exclude_list = ['소다']

<<<<<<< HEAD
#clean up your tag
def remove_tags(text):
	TAG_RE = re.compile(r'<[^>]+>')
	return TAG_RE.sub('',text)

#clean up bloglink
#?Redirect=Log&amp;logNo=   ==> / change
def clean_up_bloglink(text):
	TAG_RE = re.compile(r'[?]Redirect=Log&amp;logNo[=]')
	return TAG_RE.sub('/', text)

=======
>>>>>>> 9746b6bc514cb24918ee230856224a6896db7352

def search_on_naver(search_text_list, exclude_text_list, num_of_search_display_option, sort_date_option):
	
	final_search_text = ""

	for search_text in search_text_list:
		if(final_search_text == ""):
			final_search_text = final_search_text + search_text
		else:
			final_search_text = final_search_text + "+" + search_text

	for exclude_text in exclude_text_list:
		if(final_search_text == ""):
			break
		else:
			final_search_text = final_search_text + "-" + exclude_text


	print(final_search_text)
	encText=urllib.parse.quote(final_search_text)
	url="https://openapi.naver.com/v1/search/blog?query="+encText #json result

	if (num_of_search_display_option > 10):
		url = url + "&display=" + str(num_of_search_display_option)

	if (sort_date_option):
		url = url + "&sort=date"

	print(url)

	request = urllib.request.Request(url)
	request.add_header("X-Naver-Client-Id", naver_secrets.client_id)
	request.add_header("X-Naver-Client-Secret", naver_secrets.client_secret)

	response = urllib.request.urlopen(request)
	rescode = response.getcode()
	if(rescode == 200):
		#print(response.read().decode('utf-8'))
		return json.loads(response.read().decode('utf-8')) 
	else:
		#print("Error Code: " + rescode)
		return False

def clean_json_data(json_input):
	# do we need backup for json_input?
	for i in range(0, len(json_input['items'])):
		json_input['items'][i]['title'] = remove_tags(json_input['items'][i]['title'])
		json_input['items'][i]['link'] = clean_up_bloglink(json_input['items'][i]['link'])
		json_input['items'][i]['description'] = remove_tags(json_input['items'][i]['description'])
	return json_input


## main code
return_val = search_on_naver(test_search_string_list,test_search_exclude_list, 11, True)
if(return_val == False):
	# if error happend send mail to owner
	# TODO 
	print("error")
else:
	print(return_val)
	print(return_val['items'][0]['description'])
	cleaned_data = clean_json_data(return_val)
	print(cleaned_data)
	print(cleaned_data['items'][0]['description'])

	# print(return_val['items'][0]['title'])
	# print(remove_tags(return_val['items'][0]['title']))
	# print(return_val['items'][0]['link'])
	# print(clean_up_bloglink(return_val['items'][0]['link']))
