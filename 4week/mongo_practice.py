from pymongo import MongoClient
client = MongoClient("localhost", 27017)
db = client.dbsparta

def question1():
    # 어벤져스: 엔드게임 의 평점을 가져오자
    movie = db.movies.find_one(
        {"title": "어벤져스: 엔드게임"}
    )
    print(movie["star"])

if __name__ == "__main__":
    question1()
