# REST_API_wtih_MachineLearning

### REST API

#### Recommend requirements

- python3
- flask
- flask_restful

#### Run Flask web server

```buildoutcfg
$ python3 restapi.py
``` 

#### 1. Search API

search options : Index, Type

If sucess, return result API

If fail, return valid options

- terminal

```
$ curl -X POST http://127.0.0.1:5000/search?options=index
/result/index
```

- Postman 

![alt text](/image/postman.png "cover_image")

```buildoutcfg
/result/index
```


#### 2. Result API

- terminal

```
$ curl -X GET http://127.0.0.1:5000/result/index
1
```

- Postman 

![alt text](/image/postman2.png "cover_image")

```buildoutcfg
1
```


### comming soon

- Elasticsearch
- Machine Learning
    - Image Classification
    - NLP
        - word2vec
        - TF IDF (Term Frequency Inverse Document Frequency)
        - Korean POS Tag (Part of Speech Tag)
        



