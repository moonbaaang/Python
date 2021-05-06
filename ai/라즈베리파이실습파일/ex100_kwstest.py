'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example 1: GiGA Genie Keyword Spotting"""

from __future__ import print_function

import audioop
from ctypes import *
import RPi.GPIO as GPIO
import ktkws # KWS
import MicrophoneStream as MS
KWSID = ['기가지니', '지니야', '친구야', '자기야']
RATE = 16000
CHUNK = 512

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(31, GPIO.OUT)
btn_status = False

def callback(channel):  
	print("falling edge detected from pin {}".format(channel))
	global btn_status
	btn_status = True
	print(btn_status)

GPIO.add_event_detect(29, GPIO.FALLING, callback=callback, bouncetime=10)

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
def py_error_handler(filename, line, function, err, fmt):
  dummy_var = 0
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
asound = cdll.LoadLibrary('libasound.so')
asound.snd_lib_error_set_handler(c_error_handler)


def detect():
	cnt = 0
	with MS.MicrophoneStream(RATE, CHUNK) as stream:
		audio_generator = stream.generator()

		for content in audio_generator:
			cnt += 1
			rc = ktkws.detect(content)
			rms = audioop.rms(content,2)
			#print('audio rms = %d' % (rms))
			print('detect=>' ,rc, ":", cnt)
			if (rc == 1):
				MS.play_file("../data/sample_sound.wav")
				return 200
			elif(rc==0 and cnt>100):
				return 404
			

def btn_detect():
	global btn_status
	with MS.MicrophoneStream(RATE, CHUNK) as stream:
		audio_generator = stream.generator()

		for content in audio_generator:
			GPIO.output(31, GPIO.HIGH)
			rc = ktkws.detect(content)
			rms = audioop.rms(content,2)
			#print('audio rms = %d' % (rms))
			GPIO.output(31, GPIO.LOW)
			if (btn_status == True):
				rc = 1
				btn_status = False			
			if (rc == 1):
				GPIO.output(31, GPIO.HIGH)
				MS.play_file("../data/sample_sound.wav")
				return 200

def test(key_word = '기가지니'):
	rc = ktkws.init("../data/kwsmodel.pack")
	print ('init rc = %d' % (rc))
	rc = ktkws.start()
	print ('start rc = %d' % (rc))
	print ('\n호출어를 불러보세요~\n')
	#ktkws.set_keyword(KWSID.index(key_word))
	for k in KWSID:
		if k == key_word:
			#print(k)
			ktkws.set_keyword(KWSID.index(key_word))
			rc=detect()
			break
		else:
			rc=404

	print ('detect rc = %d' % (rc))
	if(rc==200):
		print ('\n\n호출어가 정상적으로 인식되었습니다.\n\n')
	else:
		print ('\n\n호출어가 비정상적으로 인식되었습니다.\n\n')
	ktkws.stop()
	result_test(keyword, rc)
	return rc

def btn_test(key_word = '기가지니'):
	global btn_status
	rc = ktkws.init("../data/kwsmodel.pack")
	print ('init rc = %d' % (rc))
	rc = ktkws.start()
	print ('start rc = %d' % (rc))
	print ('\n버튼을 눌러보세요~\n')
	ktkws.set_keyword(KWSID.index(key_word))
	rc = btn_detect()
	print ('detect rc = %d' % (rc))
	print ('\n\n호출어가 정상적으로 인식되었습니다.\n\n')
	ktkws.stop()
	result_test(key_word, rc)
	return rc
'''
def result_test(key_word, rc):
	import datetime as dt
	now = dt.datetime.now()
	now.strtime('%Y-%m-%d %H:%M:%S')

	# 시간 키워드 단어 응답 1줄로 result.txt 에 저장
	# 현재시간 설정, result.txt file open
	file = open('result.txt', 'a')
	file.write(now + "," + key_word + "," + str(rc) +"\n")
	file.close()

def result_read_test():
	file = open('result.txt' , 'r')
	time_list = []
	keyword_list = []
	response_list = []

	file_dict = {}

	for line in file:
                linedata_list = line.rstrip().split(',')	
		time_list.append(linedata_list[0])
		keyword_list.append(linedata_list[1])
		response_list.append(linedata_list[2])
	file_dict['time'] = time_list
	file_dict['keyword'] = keyword_list
	file_dict['response'] = response_list

	file.close()

	print(file_dict)

	#result.txt file read list, dict
	#읽은 파일 내용 출력
	# time keyword response 를 제목이 되도록
	# -------------------------- 이후 내용들 출력

	for i in file_dict.keys():
		print(i, end=" ")
	print()
	
	for i in range(0, len(file_dict['time']), 1):
		for k in file_dict.keys():
			print(file_dict[k][i], end=" ")
		print()

	# 키워드 기가지니 몇번 호출
	print(file_dict['keyword'].count('기가지니'))
	
	# 200번 응답 몇번 출력 
	print(file_dict['response'].count('200'))	

	# 오늘  호출이 몇번인지 출력
	import datetime as dt
	now = dt.datetime.now()
	now = now.strftime("%Y-%m-%d")
	
	today_call = 0
	for t in file_dict['time']:
		if(t[:10]==now):
			today_call +=1
	
	print("today call = ", today_call)	

	#파일 내용을 다 읽어서 저장한 리스트, 딕셔너리, 문자열 리턴 
	return file_dict	



def result_graph_test():
	file_dict = result_read_test()	
	
	import matplotlib.pyplot as plt
	import matplotlib.font_manager as fm
	
	for f in fm.fontManager.ttflist:
		print(f.name)
		

	# 각 키워드 4개마다 호출 횟수 히스토그램으로 그림
	
	plt.title('키워드 빈도수')
	plt.hist(file_dict['keyword']) #y축은 키워드 등장횟수를 자동으로 계나
	plt.xlabel('keyword')
	plt.ylabel('response')
	plt.rcParams['font.family'] = 'NanumGothic'
	plt.plot(file_dict)
	plt.savefig('kwstest.gif')
	plt.show()	

	#response - plt.barh() > 202 404 / 10, 20
	print(file_dict['response'])
	print(set(file_dict['response']))

        response_cnt_dict = {}
	for k in set(file_dict['response']):
                response_cnt_dict[k] = file_dict['response'].count(k);

        print(response_cnt_dict)

        k_list = []
        v_list = []
        for k, v in response_cnt_dict.items():
                k_list.append(k)
                v_list.append(v)


	plt.barh(k_list, v_list)
	plt.title('응답 코드 빈도수')
        plt.ylabel('응답 코드')
        plt.xlabel('등장 횟수')
        plt.savefig('response.png')
        plt.show()

def result_server_test():
        # http://192.168.137.132:9091/fileupload - post
        # result.txt, response.png 파일 업로드
        # 터미널 pop3 install requests

        import requests
        textfile = open('result.txt', 'r')
        graphfile = open('response.png', 'rb')

        response = requests.post("http://192.168.137.132:9091/fileupload",
        data= {"name":"라즈베리", "description":"uploadtest"},
        files= {"file1":"textfile", "file2":"graphfile"} )
        print(response.status_code)
        print(response.text)

def main():
	#test()
# import ex1_kwstest
# ex1_kestest.test()
	#test('지니야')
	#test('친구야')
	#test('자기야')
	
	#result_read_test()
	#result_graph_test()
        result_server_test()
if __name__ == '__main__':
	main()

