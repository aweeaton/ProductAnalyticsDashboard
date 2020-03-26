from flask import Flask
from flask import render_template
import boto3

from user_definition import *

application = Flask(__name__)


def read_s3_obj(bucket, filename):
    """ Read from s3 bucket"""
    try:
        s3 = boto3.client('s3')
        obj = s3.get_object(Bucket=bucket, Key=filename)
        body = obj['Body'].read().decode('utf-8')
        return body
    except:
        return ""


@application.route('/', methods=['GET', 'POST'])
def homepage():
    """ homepage page -- shown on the beginning """
    body = read_s3_obj(bucket_name, filename)
    print(body)
    return render_template('homepage.html', output=body)


if __name__ == '__main__':
    application.jinja_env.auto_reload = True
    application.config['TEMPLATES_AUTO_RELOAD'] = True
    application.debug = True
    application.run()
