echo -e "3\nFactNews\nY\n1\nN\nn\n" | eb init -i
eb create FactNews-web
aws codepipeline create-pipeline --cli-input-json file://pipeline.json
