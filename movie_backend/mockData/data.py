
class MockData():

    @classmethod
    def data_post(cls):
        return {
            "genre": "drama",
            "title": "last blood",
            "link" : "https://www.youtube.com/watch?v=4vWg5yJuWfs",
            "image": "https://en.wikipedia.org/wiki/Rambo:_Last_Blood#/media/File:Rambo_-_Last_Blood_official_theatrical_poster.jpg",
            "detail": "syvester stallon movie"
        }
    @classmethod
    def data_update(cls):
        return {
            "pk":1,
            "genre":"action",
            "title" :"last blood",
            "link" : "https://www.youtube.com/watch?v=4vWg5yJuWfs",
            "image" : "https://en.wikipedia.org/wiki/Rambo:_Last_Blood#/media/File:Rambo_-_Last_Blood_official_theatrical_poster.jpg",
            "detail" : "syvester stallon movie"
        }

    @classmethod
    def set_up(cls):
        return {
            "id":1,
            "genre":"drama",
            "title" :"last blood",
            "link" : "https://www.youtube.com/watch?v=4vWg5yJuWfs",
            "image" : "https://en.wikipedia.org/wiki/Rambo:_Last_Blood#/media/File:Rambo_-_Last_Blood_official_theatrical_poster.jpg",
            "detail" : "syvester stallon movie"
        }
