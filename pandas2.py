import os, re
import pandas as pd
os.chdir(r"C:\Users\tmdgu\OneDrive\바탕 화면\github\git_start01")
df2 = pd.read_csv('survey.csv')
print(df2.head()) #자료 열어보는 것
print(df2.mean()) #평균
print(df2.income.mean()) #특정 값만의 평균
print(df2.income.sum()) #특정 값만의 합
print(df2.median()) #행별 중앙값
print(df2.sex.value_counts()) #변수의 빈도 구하기
print(df2.groupby(df2.sex).mean()) #두 그룹의 평균을 구해 비교하기
#ctrl + F5누르면 파이썬 코드가 실행됨
