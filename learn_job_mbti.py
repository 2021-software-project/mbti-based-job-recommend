import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

def learn_job_mbti():
    column = ['E', 'S', 'T', 'J', 'I', 'N', 'F', 'P']

    result_df = pd.read_csv("./dataset/subcode_mbti.csv")
    return_df = pd.read_csv("./dataset/job_mbti_split.csv")

    for sub_code in result_df['sub_code'].drop_duplicates() :
        target_df = result_df.loc[result_df['sub_code'] == sub_code]

        if target_df.empty or len(target_df) == 1:
            # 수집 자료 중 해당 직종에 대한 평점이 1개 이하인 경우, 기존 MBTI 정보 그대로 사용
            continue
            
        else : 
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

            user_profile = user_profile.reshape(8,).tolist()
            list = [sub_code]
            list += user_profile
            return_df[return_df['sub_code']==sub_code] = list

    pd.DataFrame(return_df).to_csv('./dataset/job_mbti_learn.csv', index=False, encoding='utf-8')
    
    
if __name__=="__main__":
    
    learn_job_mbti()