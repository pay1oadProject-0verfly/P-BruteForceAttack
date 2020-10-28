'''
pay1oad 프로젝트 팀 0verfly.
Brute_Force_Attack 프로젝트.
주석은 필수, 변수명은 목적에 따라,
모르는 내용은 다같이 회의해봅시다!

'''

#리턴 값을 어떻게 하실건지, 미리 적어주세요!

import zipfile  #zip파일 읽기 및 압축 해제 기능이 포함된 모듈.
import os
def zipfile_check():
    import zipfile
    import os

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