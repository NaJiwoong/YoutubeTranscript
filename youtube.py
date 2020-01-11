from youtube_transcript_api import YouTubeTranscriptApi
from flask import Flask
from flask_restful import Resource, Api, reqparse, request
from flask_ngrok import run_with_ngrok


app = Flask(__name__)
run_with_ngrok(app)
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


@app.route('/Trans', methods=['POST'])
def trans():
    if request.method == 'POST':
        parser = reqparse.RequestParser()
        parser.add_argument('url', type=str)
        args = parser.parse_args()
        url = args['url']
        print("your url")
        print(url)
        print("your url")
        myTrans = YouTubeTranscriptApi.get_transcript(url)
        print(myTrans)
        return str(myTrans)


@app.route('/Trans/<url>')
def trans1(url):
    return str(YouTubeTranscriptApi.get_transcript(url))


api.add_resource(YoutubeTranscript, '/youTrans')

if __name__ == '__main__':
    app.run()