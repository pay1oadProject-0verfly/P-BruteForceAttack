'''
pay1oad 프로젝트 팀 0verfly.
Brute_Force_Attack 프로젝트.
주석은 필수, 변수명은 목적에 따라,
모르는 내용은 다같이 회의해봅시다!

'''

#리턴 값을 어떻게 하실건지, 미리 적어주세요!

import zipfile  #zip파일 읽기 및 압축 해제 기능이 포함된 모듈.
import os
import itertools
def zipfile_check():
  #1번 파트, 해독할 파일 경로 찾기 및 zip파일 판정하기.
	#김민주, 김정윤
    while True:
        file_path = input("파일 경로를 입력하세요: ")  # 파일 경로 입력받기

        if (os.path.exists(file_path) == True):  # 파일 경로가 존재하는지 확인 > True일시 if문 진행
            dir, file = os.path.split(file_path)  # 경로 중 디렉토리명과 파일명을 나누어 얻기
            os.chdir(dir)  # 작업 디렉토리를 file path로 변경.
            if (zipfile.is_zipfile(file) == True):  # 파일이 zip파일인지 확인
                print("zip 파일이 맞습니다.")  # 맞을경우 zip파일이 맞습니다 출력 > return 파일 경로 해야함 ...
                return(os.path.abspath(file_path))# 절대경로를 반환

            else:
                print("zip 파일이 아닙니다.")  # zip파일이 아닐 경우 zip파일이 아닙니다 출력
        else:
            print("존재하지 않는 파일입니다.")  # 경로 내에 해당 파일이 존재하지 않을경우 존재하지 않는 파일입니다 입력경우 존재하지 않는 파일입니다 입력

#문자열의 조건 설정.
def make_string():
    # 2번 파트, 문자열 생성
    # 박승민, 심승민
    global recieve
    global minimum
    global maximum

    string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    print('현재 모든 숫자와 모든 알파벳이 준비되어있습니다.')
    answer = input('시간절약을 위한 문자열을 다시 입력하겠습니까? [Y/N]')
    if answer == 'Y' or answer == 'y':
        string = input("매칭에 사용할 문자열을 입력해주세요.")

    elif answer == 'N' or answer == 'n':
        pass

    else:
        print('ERROR')

    # 문자열의 길이 설정. (minimum, maximum)
    minimum = input("문자열의 최소길이를 입력해주세요.")
    if minimum <= 0:
        print('ERROR')
    else:
        pass
    maximum = input("문자열의 최대길이를 입력해주세요.")
    if maximum >= minimum:
        pass
    else:
        print('ERROR')


'''
string_input과 연계하여 움직이는 def.
틀릴시엔 while문을 돌아야 하기 때문에
string_input으로부터의 Fasle값 받기 필수.
'''


def matching_string()
    while recieve == False:  # string_input에서 recieve를 통한 False값 받음.
        for len in range(minimum, maximum):
            endTrying = itertools.product(string, repeat=len)
            for trying in endTrying:
                password = ''.join(trying)
                return password




def string_input():
	#3번 파트, 생성 된 문자열 입력 및 T/F판정
	#최지혁, 윤성우
	z = zipfile.ZipFile(zipfile_check())			#test.zip파일 암호는 6
	made_key = ['1', '2', '3', '4', '5', '6', '7', '8', '9']		#임시로 테스트
	for i in made_key:			#나중에 make_string에서 for문쓸지 여기서 for문쓸지 정하기
		try:
			z.extractall(pwd=bytes(i, 'utf-8'))			#pwd를 그냥 입력하면 오류가 걸려 bytes 취해주기
		except Exception:
			pass




def main():
    path = zipfile_check()
    make_string()

if __name__ == "__main__":
	main()
