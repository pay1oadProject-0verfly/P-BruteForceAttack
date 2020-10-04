'''
pay1oad 프로젝트 팀 0verfly.
Brute_Force_Attack 프로젝트.
주석은 필수, 변수명은 목적에 따라,
모르는 내용은 다같이 회의해봅시다!

'''

#리턴 값을 어떻게 하실건지, 미리 적어주세요!

import zipfile  #zip파일 읽기 및 압축 해제 기능이 포함된 모듈.

def zipfile_check():
	#1번 파트, 해독할 파일 경로 찾기 및 zip파일 판정하기.
	#김민주, 김정윤

def make_string():
	#2번 파트, 문자열 생성
	#박승민, 심승민

def string_input():
	#3번 파트, 생성 된 문자열 입력 및 T/F판정
	#최지혁, 윤성우
	'''
	make_string에서 만든 문자열을 made_key 변수에 저장.
	made_key 변수의 값을 zipfile_check에서 입력받은 경로의 zip파일 압축해제시 필요한 pwd 값에 대입.
	틀리면 다음 문자열로 변경, 맞으면 그 문자열 리턴.
	'''
	#사용할 함수 목록:
	#extractall('Zip_route', pwd = 'make_string()')
	#try/except
	#return
	#for
	z = zipfile.ZipFile('test.zip')			#test.zip파일 암호는 6
	made_key = ['1', '2', '3', '4', '5', '6', '7', '8', '9']		#임시로 테스트
	for i in made_key:			#나중에 make_string에서 for문쓸지 여기서 for문쓸지 정하기
		try:
			z.extractall(pwd=bytes(i, 'utf-8'))기			#pwd를 그냥 입력하면 오류가 걸려 bytes 취해주기
			print('성공! 암호는 ' + i)
			exit(0)			#나중에 return으로 바꾸
		except Exception:
			print('실패: ', i)
			pass



def main():
	
if __name__ == "__main__":
	main()
