import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def cb(userid=0):
    column = ['E', 'S', 'T', 'J', 'I', 'N', 'F', 'P']
    result_df = pd.read_csv("./dataset/mbti_to_column_result.csv")

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

    uesr_profile = pd.DataFrame([intercept, *coef], index=['intercept'] + column, columns=['score'])

    print(uesr_profile)

if __name__=="__main__":
    cb()
