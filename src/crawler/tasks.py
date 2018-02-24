import os
import sys
import json
import urllib.request

test_search_string_list = ['홈', '베이킹', '쿠킹']
test_search_exclude_list = ['소다']


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
	request.add_header("X-Naver-Client-Id", client_id)
	request.add_header("X-Naver-Client-Secret", client_secret)

	response = urllib.request.urlopen(request)
	rescode = response.getcode()
	if(rescode == 200):
		#print(response.read().decode('utf-8'))
		return json.loads(response.read().decode('utf-8')) 
	else:
		#print("Error Code: " + rescode)
		return False

## main code
return_val = search_on_naver(test_search_string_list,test_search_exclude_list, 11, False)
if(return_val == False):
	print("error")
else:
	print(return_val)
	print(return_val['items'][0]['title'])
