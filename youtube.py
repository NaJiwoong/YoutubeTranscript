from youtube_transcript_api import YouTubeTranscriptApi
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class YoutubeTranscript(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', type=str)
        args = parser.parse_args()
        url = args['url']
        myTrans = YouTubeTranscriptApi.get_transcript(url)
        print(myTrans)
        return str(myTrans)

api.add_resource(YoutubeTranscript, '/youTrans')

if __name__ == '__main__':
    app.run(debug=True)