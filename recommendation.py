import pandas as pd
from job_code import sub_code_list

from cb_data_preprocessing import Data
from cb_contents_rec import *
from cf_item_rec import Item
from cf_user_rec import User


class Recommendation:

    def __init__(self):
        self.code_list = sub_code_list()

        self.rating_df = pd.read_csv('./dataset/random_user_rating.csv')

        self.user_list = self.rating_df['user_id'].drop_duplicates().values


    def recommendation(self, algorithm, user, rec_num=5):

        global rating, job, rec_list

        if algorithm == 'cb':
            topic = 29
            job = pd.read_csv("./dataset/job-topic_29_1.csv")
            data = Data(job, topic)
            rating = data.merge_rating_topic(self.rating_df)
            user_model = data.make_user_mbti(rating, user)

            rec_list = contents_based_rec(user_model, job, topic, rec_num)  # 추천 리스트

        elif algorithm == 'cf_i':
            item_cf = Item(self.rating_df)
            sim = item_cf.calc_item_simmularity()
            # sim_df = pd.read_csv("./dataset/item_simmularity.csv")

            rec_list = item_cf.item_based_rec(sim)

        elif algorithm == 'cf_u':
            user_cf = User(self.rating_df)
            sim = user_cf.calc_user_simmularity()
            # sim_df = pd.read_csv("./dataset/user_simmularity.csv")

            rec_list = user_cf.user_based_rec(sim)

        return rec_list


if __name__ == "__main__":
    rec = Recommendation()

    print(rec.recommendation('cb', 0, rec_num=5))