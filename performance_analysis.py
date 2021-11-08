import pandas as pd
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics

from job_code import sub_code_list
from data_preprocessing import Data
from contents_based_rec import *


class Analysis:

    def __init__(self):
        self.code_list = sub_code_list()

        rating_df = pd.read_csv("./dataset/random_user_rating.csv")  # 학습 데이터 셋 = 사용자 평점 정보
        self.train_df, self.test_df = train_test_split(rating_df, test_size=0.3, shuffle=True, random_state=121)
        self.test_df = self.test_df[self.test_df['rating'] >= 4]

        self.user_list = self.train_df['user_id'].drop_duplicates().values

        self.data = Data()


    def performance_analysis(self, algorithm, rec_num=5):

        global rating, job, rec_list


        if algorithm == 'cb':
            rating = self.data.merge_rating_mbti(self.train_df)
            job = self.data.make_job_mbti(rating)
            print("if문 cb완료")

        k = rec_num  # 추천받을 직종 개수

        indicator = [0, 0, 0, 0]  # accuracy, precision, recall, f1score
        for user in self.user_list:
            print("사용자 ", user, "시작")
            if algorithm == 'cb':
                user_model = self.data.make_user_mbti(rating, user)
                rec_list = contents_based_rec(user_model, job, k)  # 추천 리스트

            y_pred = pd.DataFrame(columns=self.code_list)
            y_pred.loc[len(y_pred)] = [0 for i in range(150)]  # 초기화
            y_pred[rec_list] = y_pred[rec_list].replace([0], 1)
            y_pred = y_pred.values.tolist()[0]

            real_list = self.test_df[self.test_df['user_id'] == user]['sub_code'].values.tolist()
            y_true = pd.DataFrame(columns=self.code_list)
            y_true.loc[len(y_true)] = [0 for i in range(150)]  # 초기화
            y_true[real_list] = y_true[real_list].replace([0], 1)
            y_true = y_true.values.tolist()[0]

            indicator[0] += metrics.accuracy_score(y_true, y_pred)
            indicator[1] += metrics.precision_score(y_true, y_pred)
            indicator[2] += metrics.recall_score(y_true, y_pred)
            indicator[3] += metrics.f1_score(y_true, y_pred)

        #         metrics.classification_report(y_true, y_pred)
        #         metrics.confusion_matrix(y_true, y_pred)

        print("accuracy : ", indicator[0] / len(self.user_list))
        print("precision : ", indicator[1] / len(self.user_list))
        print("recall : ", indicator[2] / len(self.user_list))
        print("f1 score : ", indicator[3] / len(self.user_list))


if __name__ == "__main__":
    ana = Analysis()

    ana.performance_analysis('cb', 10)
