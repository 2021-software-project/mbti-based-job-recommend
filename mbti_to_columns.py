import pandas as pd


def mbti_to_col(data):
    d = [0 for _ in range(8)]
    for element in data:
        if (element == 'E'):
            d[0] = 1
        elif (element == 'S'):
            d[1] = 1
        elif (element == 'T'):
            d[2] = 1
        elif (element == 'J'):
            d[3] = 1
        elif (element == 'I'):
            d[4] = 1
        elif (element == 'N'):
            d[5] = 1
        elif (element == 'F'):
            d[6] = 1
        elif (element == 'P'):
            d[7] = 1
    return d

def mtc():
    column = ['E','S','T','J','I','N','F','P']

    df = pd.read_csv("./dataset/random_user_rating.csv",encoding='cp949')
    mbti_df = pd.read_csv("./dataset/MBTI list.csv",encoding='cp949')

    merge_df = pd.merge(df,mbti_df)
    temp = merge_df.mbti.apply(mbti_to_col)
    mbti_info = pd.DataFrame(temp.tolist(), columns=column)
    result_df = pd.concat([merge_df,mbti_info],axis=1).sort_values(by=['user_id','sub_code']).reset_index(drop=True)
    result_df.to_csv("./dataset/mbti_to_column_result.csv",index=False)


if __name__=="__main__":
    mtc()