import random
from job_code import job_code
import pandas as pd
import os

def make_sample(user_cnt=100, rating_max_cnt=50):

    # job code
    sub_code_list = []
    for key, value in job_code.items():
        for index, sub_code in value.items():
            sub_code_list.append(sub_code)

    total_rate = []

    for i in range(user_cnt):
        rating_cnt = random.randint(1, rating_max_cnt)
        sub_code = random.sample(sub_code_list, rating_cnt)
        temp_rating = []
        for sc in sub_code:
            total_rate.append([i, sc, random.randint(1, 15)])

    rating_df = pd.DataFrame(data=total_rate, columns=['user_id', 'sub_code', 'rating'])
    rating_df.to_csv("./dataset/random_user_rating.csv", index=False, encoding='utf-8')


if __name__ == "__main__":

    path = "./dataset"
    if not os.path.isdir(path):
        os.mkdir(path)

    make_sample(100, 10)
