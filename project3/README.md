특정 조건에 따라 social network 에 노출되는 광고 제품 구매 여부 예측 서비스

ML Model 을 바탕으로 Flask 를 이용하여 가상의 서비스를 제공하는 데이터 파이프라인을 구축

Using data : Social_Network_Ads.csv 
Info  : User_ID(int), Gender(str), Age(int), EstimatedSalary(int), Purchased(int)
데이터셋 출처 - Social_Network_Ads.csv https://www.kaggle.com/jahnveenarang/c vdcvd-vd


ML Model
데이터 전처리  : 원핫인코딩, 불필요한 칼럼 삭제, 수지형 데이터 정규화
데이터 셋 생성 : train set, test set split
모델 구축        : KNeighborsClassifier, LogisticRegression, DecisionTreeClassifier, 
                 GradientBoostingClassifier, RandomForestClassifier
모델별 성능 평가 
진행 및 비교    : 높은 학습, 검증 정확도, 과적합 발생 유무
모델 선정        : GradientBoostingClassifier


Pipeline deployment in Flask 
데이터 저장 : 관계형 데이터베이스 저장(sqlite)
API 서비스 개발 : localhost API 로 개발 후 Proof-of-Concept 진행


