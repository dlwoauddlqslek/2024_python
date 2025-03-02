# 결정트리: 결정트리(다중분류) vs 로지스틱 회귀(이진분류)
# 모델 생성하고 예측
# [1] 데이터 수집 # 데이터셋 찾는 과정
# 스마트폰으로 수집한 사람의 움직임 데이터


import numpy as np
import pandas as pd

# 피처 이름 파일 읽어오기
feature_name_df=pd.read_csv('features.txt',sep='\s+',header=None,names=['index','feature_name'],engine="python")
    # 1. sep='\\s+' : 공백으로 구분된 형식 파일
    # 2. header=None: 제목이 없는 파일
    # 3. names=[열이름]
#print(feature_name_df.head())
#print(feature_name_df.shape)

# index 제거하고, feature_name만 리스트로 저장
feature_name=feature_name_df.iloc[:,1].values.tolist()
    # 데이터프레임객체.iloc[행 슬라이싱]
    # 데이터프레임객체.iloc[행 슬라이싱, 열번호]
    # feature_name_df.iloc[:] : 모든 행
    # feature_name_df.iloc[:,1]: 모든 행의 두번째 열(첫번째 열 제외)
    # .value 값 추출 # .tolist() 리스트로 반환 함수
print(feature_name)

# 훈련용, 테스트용 파일 읽어오기
x_train=pd.read_csv('train/X_train.txt',delim_whitespace=True,header=None,encoding='latin-1')
x_train.columns=feature_name
x_test=pd.read_csv('test/X_test.txt',delim_whitespace=True,header=None,encoding='latin-1')
x_test.columns=feature_name
y_train=pd.read_csv('train/y_train.txt',sep='\s+',header=None,names=['action'],engine='python')
y_test=pd.read_csv('test/y_test.txt',sep='\s+',header=None,names=['action'],engine='python')
#print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)
#print(x_train.head())
#print(y_train['action'].value_counts())

# 종속변수의 데이터 레이블 파일 가져오기
label_name_df=pd.read_csv('activity_labels.txt',sep='\s+',header=None,names=['index','label'],engine='python')

# index 제거하고, label_name만 리스트로 저장
label_name=label_name_df.iloc[:,1].values.tolist()
print(label_name)

# 데이터 수집 정리
'''
    1. activity_labels.txt: 클래스(종속변수) 값에 따른 분류 값
    2. features.txt: 피처(독립변수) 값에 따른 필드(열) 이름
    3. 분류된 데이터 제공 vs train_test_split
        1. 훈련용
            1. x_train.txt
            2. y_train.txt
        2. 테스트용
            1. x_test.txt
            2. y_test.txt
    - 변수
        1. x_train   : 독립변수 데이터프레임(훈련용)
        2. y_train   : 종속변수 데이터프레임
        3. x_test    : 독립변수 데이터프레임(테스트용)
        4. y_test    : 종속변수 데이터프레임
        5. label_name: 종속변수 값에 따른 분류 값, 1(걷기)
'''

# 결정트리 모델 구축하기
from sklearn.tree import DecisionTreeClassifier # 모듈 호출
# 결정 트리 분류 분석: 모델 생성
dt_HAR=DecisionTreeClassifier(random_state=156)
# 결정 트리 분류 분석: 모델 훈련
dt_HAR.fit(x_train,y_train)
# 결정 트리 분류 분석: 평가 데이터에 예측 수행 -> 예측 결과로 y_predict 구하기
y_predict=dt_HAR.predict(x_test) # 피팅된 모델이  새로운 데이터의 독립변수를 가지고 종속변수를 예측한다
print(y_predict)
# 테스트 데이터를 이용한 모델 예측 정확도 확인
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,y_predict) # 정확도 확인 # 실제 값(y_test), 예측 값(y_preidct)
print(accuracy) # 0.8547675602307431 # 1에 가까울 수록 예측을 잘 하고 있다.  # 실행때마다 오차가 존재한다.



# 최적의 하이퍼 매개변수 찾기 # 정확도가 높은 트리 찾기 # 정확도가 가장 높았을 대의 매개변수를 찾아보자.
print('결정 트리의 현재 하이퍼 매개변수: \n',dt_HAR.get_params())
    # depth: 트리의 깊이 # max_depth: 최대 트리의 깊이
    # criterion: 노드 결정 방식

# 최적의 하이퍼 매개변수를 찾을 설정값을 변수 만들기

params={
    'max_depth' : [6,8,10,12,16,20,24] # 다양한 트리의 최대 노드깊이를 설정
}

# 다양한 하이퍼 매개변수 조합을 시도해서 최적의 하이퍼매개변수를 찾는데 사용되는 모듈, 교차 검증 제공
from sklearn.model_selection import GridSearchCV
    # cv 객체 생성
    # 이미 설정한 'params'의 'max_depth' 라는 최대 노드깊이를 (5회)교차 검증하는 cv 객체
# grid_cv=GridSearchCV(dt_HAR,param_grid=params,scoring='accuracy',cv=5,return_train_score=True)
#     # GridSearchCV( 확인할 트리 모델객체, param_grid=테스트할 설정변수, scoring='정확도', cv=검증횟수
#         # scoring='accuracy': # 모델 평가 기준을 정확도 기준으로 하겟다는 뜻을 가진 속성
#         # cv=5 # 교차 검증 # 데이터를 5개로 나누어서 5번 반복해서 모델 학습
#         # return_train_score=True: 검증후 점수도 같이 반환 하겠다는 뜻을 가진 속성
#     # cv 객체 테스트
# grid_cv.fit(x_train,y_train)
#     # 결과 확인 # .cv_results_
# print(grid_cv.cv_results_)
#     # 검증 결과를 데이터프레임 객체로 변환
# cv_results_df=pd.DataFrame(grid_cv.cv_results_)
#     # 필요한 열(필드) 확인
# print(cv_results_df[['param_max_depth','mean_test_score','mean_train_score']])
#     # 최적의 정확도 # .best_score_, 최적의 하이퍼 매개변수 확인 # .best_params_)
# print(grid_cv.best_score_,grid_cv.best_params_)
#     # 사용처: 다음에 모델 만들 때 최적의 하이퍼 매개변수를 사용
#         # model= DecisionTreeClassfier

# (모델의 성능 개선) 최적의 하이퍼 파라미터 찾기2
params={
    'max_depth' : [8, 16, 20], # 트리의 최대 깊이로 검증하겟다.
    'min_samples_split':[8,16,24] # 노드를 분할 하기 위해 사용되는 최소 샘플수의 값들을 검증하겠다.
}
grid_cv=GridSearchCV(dt_HAR,param_grid=params,scoring='accuracy',cv=5, return_train_score=True)
grid_cv.fit(x_train,y_train)
#cv_results_df=pd.DataFrame(grid_cv.cv_results_)
#print(cv_results_df[['param_max_depth','param_min_samples_split','mean_test_score','mean_train_score']])
print(grid_cv.best_score_,grid_cv.best_params_) # 평균 정확도:0.8548794147162603 , {'max_depth': 8, 'min_samples_split': 16}
    # 예시) 모델 생성
dt_HAR2 = DecisionTreeClassifier(max_depth=8,min_samples_split=16)
dt_HAR2.fit(x_train,y_train) # 개선된 모델로 다시 피팅
    # 개선된 모델로 다시 테스트
y_predict2=dt_HAR2.predict(x_test)       # 예측
print(accuracy_score(y_test,y_predict2)) # 예측 정확도 확인

# best_dt_HAR=grid_cv.best_estimator_
# best_y_predict=best_dt_HAR.predict(x_test)
# best_accuracy=accuracy_score(y_test,best_y_predict)
# print(best_accuracy)

# 결정트리 모델 시각화
import matplotlib.pyplot as plt
from sklearn import tree # 결정트리 시각화 모듈
tree.plot_tree(dt_HAR2,feature_names=feature_name, class_names=label_name)
    # tree.plot_tree(결정트리모델객체,feature_names=[피처이름들], class_names=[클래스레이블들])
plt.show()

