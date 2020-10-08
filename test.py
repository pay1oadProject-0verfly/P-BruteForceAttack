import zipfile
import os

file_path = input("파일 경로를 입력하세요: ") #파일 경로 입력받기
file_name = input("이름을 입력하세요: ") #파일 이름 입력받기

if(os.path.exists(file_path)==True): #파일 경로가 존재하는지 확인 > True일시 if문 진행
	os.chdir(file_path)
	if (zipfile.is_zipfile(file_name)==True): #파일이 zip파일인지 확인
		print("zip 파일이 맞습니다.") #맞을경우 zip파일이 맞습니다 출력 > return 파일 경로 해야함 ...
	else:
		print("zip 파일이 아닙니다.") #zip파일이 아닐 경우 zip파일이 아닙니다 출력
else:
	print("존재하지 않는 파일입니다.") #경로 내에 해당 파일이 존재하지 않을경우 존재하지 않는 파일입니다 입력 
