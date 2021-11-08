import pandas as pd


class Data:

    def __init__(self):
        self.columns = [str(i) for i in list(range(27))]
        self.job_df = pd.read_csv("./dataset/job_mbti_learn.csv")  # LDA 데이터 입력 예정


    def merge_rating_mbti(self, rating):  # [cb] 사용자 평점 별 mbti 지표값 데이터

        merge_df = pd.merge(rating, self.job_df)  # 사용자 평점 정보

        for i in self.columns:
            merge_df[i] = merge_df[i] * merge_df['rating'] * 0.2

        return merge_df


    def make_job_mbti(self, rating):  # [cb] 직종 별 mbti수치 계산 (21.11.02)
        input_df = rating
        data_list = []

        for i in self.job_df['sub_code'].values:
            df = input_df[input_df['sub_code'] == i][self.columns]
            df = df.sum() / len(df)
            data_list.append([i] + df.values.tolist())

        job_result_df = pd.DataFrame(data=data_list, columns=['sub_code', 'E', 'I', 'S', 'N', 'T', 'F', 'J', 'P']).fillna(0)
        #     job_result_df.to_csv("./dataset/job_mbti_values.csv", index=False, encoding='utf-8')

        return job_result_df


    def make_user_mbti(self, rating, user):  # 한 사용자의 mbti 수치 계산
        input_df = rating

        df = input_df[input_df['user_id'] == user][self.columns]
        df = df.sum() / len(df)
        print('make_user : ', df.values.tolist())

        return df.values.tolist()