# mbti-based-job-recommend

# contents_based_rec.py 순서
1. make_sample.py 로 가상의 사용자 생성
2. mbti_to_columns.py 로 생성된 사용자 데이터를 가공
3. contents_based_rec.py 로 지정된 사용자에 맞는 EBTI 성향 점수로 


# 데이터 셋
1. random_user_rating.csv : 사용자 평점 정보 랜덤 생성
2. MBTI list.csv : 직종 별 MBTI 정보
3. mbti_to_column_result.csv : 랜덤 데이터에 MBTI정보 추가
4. subcode_mbti.csv : 설문조사로 수집한 사용자 평점정보에 사용자 기반 MBTI 지표 추가
5. job_mbti_split.csv : 직종별 MBTI 정보
6. job_mbti_learn.csv : 설문조사 결과를 반영한 직종별 MBTI 정보
7. linear_sample_data.csv : 설문조사로 수집한 사용자 평점정보에 직종 기반 MBTI 지표 추가


# 추천 알고리즘
1. learn_job_mbti()
    : 모든 사용자의 직종에 대한 평가를 기반으로 직종 별 mbti 정보 형성
    - 사용자의 MBTI 정보를 통해 각 직종의 MBTI 지표 값 예측

2. predict_mbti(사용자번호) 
    : 특정 사용자의 평가 정보를 기반으로 해당 사용자가 선호하는 콘텐츠 모형 형성
    - 사용자의 평점 정보만으로 해당 사용자의 MBTI 지표 값 예측

3. contents_based_rec(직종 모형) 
    : 1에서 형성한 콘텐츠 모형과 유사한 콘텐츠 추출 
    - 코사인 유사도를 사용하여 유사한 k개의 직종 추출