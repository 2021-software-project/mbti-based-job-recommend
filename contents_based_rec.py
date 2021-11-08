import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def contents_based_rec(user_model, job, k=5):
    rec_num = k  # 추천받을 직종 개수
    user_model = user_model
    job = job

    i = 0  # range안에 총 직종 개수만큼 적어주기
    sim = [[0, 0.0] for x in range(150)]

    for index, row in job.iterrows():
        sim[i][0] = row[0]

        user_model = np.array(user_model).reshape(1, 8)
        row = row[1:].to_numpy().reshape(1, 8)
        sim[i][1] = cosine_similarity(user_model, row)[0][0]

        i += 1

    sim = sorted(sim, key=lambda x: x[1], reverse=True)
    # print(sim)

    # 이부분 수정할 것 (쓸데없음)
    rec_job = []
    for num in sim[:rec_num]:
        rec_job.append(num[0])

    return rec_job