from flask import Flask
from flask import render_template
import boto3

from user_definition import *

application = Flask(__name__)

def read_s3_obj(bucket_name):
    """ Read from s3 bucket"""
    try:
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket_name)
        for obj in bucket.objects.all():
            body = obj.get()['Body'].read().decode('utf-8')
        return body
    except:
        ""


@application.route('/', methods=['GET', 'POST'])
def homepage():
    """ homepage page -- shown on the beginning """
    body = read_s3_obj(bucket_name)
    print(body)
    return render_template('homepage.html', output=body)


if __name__ == '__main__':
    application.jinja_env.auto_reload = True
    application.config['TEMPLATES_AUTO_RELOAD'] = True
    application.debug = True
    application.run()
