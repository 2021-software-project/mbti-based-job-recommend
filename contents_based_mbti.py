import pandas as pd
import numpy as np
import math

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity


def predict_mbti(userid=0):
    column = ['E', 'S', 'T', 'J', 'I', 'N', 'F', 'P']
    result_df = pd.read_csv("./dataset/linear_sample_data.csv")

    userid = userid
    target_df = result_df.loc[result_df['user_id'] == userid]

    x_train, x_test, y_train, y_test = train_test_split(
        target_df[column],
        target_df['rating'],
        test_size=.2,
        random_state=121)

    reg = LinearRegression()

    # 학습
    reg.fit(x_train, y_train)

    intercept = reg.intercept_
    coef = reg.coef_

    user_profile = pd.DataFrame([*coef], column, columns=['score']) # 표준화를 위해 intercept 제거

    scaler = MinMaxScaler()
    user_profile = scaler.fit_transform(user_profile)

    return user_profile
  
    
def contents_based_rec(user_model, k = 5) :
    
    rec_num = k             # 추천받을 직종 개수
    
    mbti = pd.read_csv("./dataset/job_mbti_learn.csv", encoding='UTF-8')

    i = 0                           # range안에 총 직종 개수만큼 적어주기
    sim = [[0, 0.0] for x in range(150)]

    for index, row in mbti.iterrows():

        user_model = user_model.reshape(8,)
        row = row[1:].to_numpy()
        num = np.dot(user_model,row)
        dem = math.sqrt(sum(user_model))*math.sqrt(sum(user_model*user_model))

        sim[i][0] = i

        if dem == 0 :
            sim[i][1] = 0
        else :
            sim[i][1] = num / dem

        i += 1
        
    sim = sorted(sim, key=lambda x:x[1], reverse = True)
#     print(sim)
    rec_job = []
    for num in sim[:rec_num] :
        rec_job += mbti[mbti.index==num[0]].sub_code.tolist()
    
    return rec_job


if __name__=="__main__":
    
    model = predict_mbti(68)
    rec_job_list = contents_based_rec(model, 5)
    
    print(rec_job_list) 