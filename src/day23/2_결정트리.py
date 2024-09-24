# 어종 데이터셋: https://raw.githubusercontent.com/rickiepark/hg-mldl/master/fish.csv
# 주제: 여러 특성들을 바탕으로 어종명 예측하기
# species: 어종명 , diagonal: 대각선길이

# [1] 데이터 셋
import pandas as pd
data=pd.read_csv('https://raw.githubusercontent.com/rickiepark/hg-mldl/master/fish.csv')
#print(data.head()) # 확인
x=data[['Weight','Length','Diagonal','Height','Width']]
#print(x)
y=data['Species']
#print(y)
# [2] 7:3 비율로 훈련용과 테스트용으로 분리하기
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(random_state=156)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

# [3] 결정트리 모델로 훈련용 데이터 피팅 하기
model.fit(x_train,y_train)

# [4] 훈련된 모델 기반으로 테스트용 데이터 예측하고 정확도 확인하기
y_pred=model.predict(x_test)
#print(y_pred)
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,y_pred)
print(accuracy)
# 출력예시: 개선 전 결정트리모델 정확도: 0.625

# [5] 최적의 하이퍼 파라미터 찾기 # params={'max_depth':[2,6,10,14], 'min_samples_split':[2,4,6,8]}
params={'max_depth':[2,6,10,14], 'min_samples_split':[2,4,6,8]}
from sklearn.model_selection import GridSearchCV
grid_cv=GridSearchCV(model,param_grid=params,scoring='accuracy',cv=5,return_train_score=True)
grid_cv.fit(x_train,y_train)
print(grid_cv.best_score_,grid_cv.best_params_)
# 출력예시: 평균 정확도: x.xxxxxx, 최적 하이퍼파라미터:{'max_depth':xx,'min_samples_split':x}

# [6] 최적의 하이퍼 파라미터 기반으로 모델 개선 후 테스트용 데이터 예측하고 예측 정확도 확인하기 # 시각화하기
model2=DecisionTreeClassifier(max_depth=10,min_samples_split=2)
model2.fit(x_train,y_train)
y_pred2=model2.predict(x_test)
accuracy2=accuracy_score(y_test,y_pred2)
print(accuracy2)

import matplotlib.pyplot as plt
from sklearn import tree
tree.plot_tree(model2,feature_names=['Weight','Length','Diagonal','Height','Width'],class_names=['Bream','Roach','Whitefish','Parkki','Perch','Pike','Smelt'])
plt.show()