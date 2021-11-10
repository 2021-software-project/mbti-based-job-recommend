import random
from job_code import sub_code_list
import pandas as pd
import os

def make_sample(user_cnt=100, rating_max_cnt=50):

    mbti_list = ['ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'ESTP',
                  'INFJ', 'INFP', 'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP']

    total_rate = []

    for i in range(user_cnt):
        mbti = random.sample(mbti_list, 1)[0]
        rating_cnt = random.randint(1, rating_max_cnt)
        sub_code = random.sample(sub_code_list(), rating_cnt)
        for sc in sub_code:
            total_rate.append([i, mbti, sc, random.randint(0, 5)])

    rating_df = pd.DataFrame(data=total_rate, columns=['user_id', 'mbti', 'sub_code', 'rating'])
    rating_df.to_csv("./dataset/random_user_rating.csv", index=False, encoding='utf-8')


if __name__ == "__main__":

    path = "./dataset"
    if not os.path.isdir(path):
        os.mkdir(path)

    make_sample(100, 10)


