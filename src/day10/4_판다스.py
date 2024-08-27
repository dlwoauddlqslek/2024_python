# - 테이블형태 다룰 수 있는 라이브러리
# 1차원 구조: Series, 2차원: DataFrame, 3차원: Panel
# -[설치]
# -[모듈] import pandas as pd # pd는 별칭
import pandas as pd
print(pd.__version__) # 2.2.2
print(type(pd)) # <class 'module'>
# [1] Series(리스트) : 1차원 자료구조 객체, 인덱스 0부터 시작
data1=[10,20,30,40,50] # 리스트 선언
sr1= pd.Series(data1) # Series 객체 생성, dtype: int64
print(sr1)
data2=['1반','2반','3반','4반','5반']
sr2=pd.Series(data2); print(sr2) # dtype: object

# [2]
sr3=pd.Series([101,102,103,104,105]); print(sr3)
sr4=pd.Series(['월','화','수','목','금']); print(sr4)

# [3] index 속성
sr5=pd.Series(data1,index=[1000,1001,1002,1003,1004]); print(sr5)
sr6=pd.Series(data1,index=data2); print(sr6)
sr7=pd.Series(data2,index=data1); print(sr7)
sr8=pd.Series(data2,index=sr4); print(sr8)

# [4] 인덱싱
#print(sr8[2]) # 3반 # 인덱스2 ->3행
# 경고: 인덱스를 0이아닌 다른 데이터를 사용하고 있으므로 인덱싱에서 경고, 해결방안 iloc
print(sr8.iloc[2]) # 3반
print(sr8['수']) # 3반
print(sr8.iloc[-1]) # 5반

# [5] 슬라이싱
print(sr8[0:4]) # [0:4] 0~3 인덱스만 추출 # 5반이 잘린다.

# [6] 인덱스 호출, 데이터 호출
print(sr8.index)
print(sr8.values)

# [7]
print(sr1+sr3) # 데이터가 숫자 타입이면 덧셈
print(sr4+sr2) # 데이터가 문자열 타입이면 연결된다

# [8] DataFrame: 2차원 자료구조 객체
data_dic={'year':[2018,2019,2020],'sales':[350,480,1099]}
# 딕셔너리를 이용한 생성
df1=pd.DataFrame(data_dic); print(df1)
# 2차원리스트를 이용한 생성
df2=pd.DataFrame([ [89.2,92.5,90.8],[92.8,89.9,95.2] ],index=['중간고사','기말고사'],columns=data2[0:3]); print(df2)

data_list= [['20201101','Hong', '90' , '95'], ['20201102','kim','93','94'],['20201103','Lee','87','97']]
df3=pd.DataFrame(data_list); print(df3)
# 컬럼 추가
df3.columns=['학번','이름','중간고사','기말고사']; print(df3)
# 조회
print(df3.head(2)) # 위에서부터 2개 행 조회
print(df3.tail(2)) # 아래에서부터 2개 행 조회
print(df3['이름']) # 컬럼 조회
# DataFrame을 CSV로 저장
df3.to_csv('score.csv',header='False') # df3 객체를 csv로 보내기
# CSV를 DataFrame 로 불러오기, index_cold=0: 첫번째 열을 DataFrame의 인덱스로 사용하겠다는 뜻, engine=파서엔진(c 또는 python)
df4=pd.read_csv('score.csv',encoding="utf-8",index_col=0,engine='c')
print(df4)

