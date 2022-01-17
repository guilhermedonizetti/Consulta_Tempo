from requests import get
from json import loads

def buscar_dados(codigo):
    x = get("https://api.hgbrasil.com/weather?woeid={}&key=chave".format(codigo))
    x = x.content.decode("utf-8")
    x = loads(x)



    return x['results']['forecast']


#ESTRUTURA DO RETORNO DA API

# {
#     "by":"woeid",
#     "valid_key":false,
#     "results":
#     {
#         "temp":23,
#         "date":"16/01/2022",
#         "time":"18:21",
#         "condition_code":"45",
#         "description":"Chuva",
#         "currently":"dia",
#         "cid":"",
#         "city":"Queluz, SP",
#         "img_id":"45",
#         "humidity":97,
#         "wind_speedy":"0.3 km/h",
#         "sunrise":"05:28 am",
#         "sunset":"06:49 pm",
#         "condition_slug":"rain",
#         "city_name":"Queluz",
#         "forecast":[
#             {
#                 "date":"16/01",
#                 "weekday":"Dom",
#                 "max":30,
#                 "min":20,
#                 "description":"Chuva",
#                 "condition":"rain"
#             },
#             {
#                 "date":"17/01",
#                 "weekday":"Seg",
#                 "max":30,
#                 "min":19,
#                 "description":"Chuvas esparsas",
#                 "condition":"rain"
#             },
#             {
#                 "date":"18/01",
#                 "weekday":"Ter",
#                 "max":31,
#                 "min":20,
#                 "description":"Chuva",
#                 "condition":"rain"
#             },
#             {
#                 "date":"19/01",
#                 "weekday":"Qua",
#                 "max":31,
#                 "min":20,
#                 "description":"Chuva",
#                 "condition":"rain"
#             },
#             {
#                 "date":"20/01",
#                 "weekday":"Qui",
#                 "max":29,
#                 "min":19,
#                 "description":"Chuva",
#                 "condition":"rain"
#             },
#             {
#                 "date":"21/01",
#                 "weekday":"Sex",
#                 "max":30,
#                 "min":19,
#                 "description":"Chuva",
#                 "condition":"rain"
#             },
#             {
#                 "date":"22/01",
#                 "weekday":"Sáb",
#                 "max":30,
#                 "min":20,
#                 "description":"Chuva",
#                 "condition":"rain"
#             },
#             {
#                 "date":"23/01",
#                 "weekday":"Dom",
#                 "max":30,
#                 "min":20,
#                 "description":"Chuvas esparsas",
#                 "condition":"rain"
#             },
#             {
#                 "date":"24/01",
#                 "weekday":"Seg",
#                 "max":32,
#                 "min":20,
#                 "description":"Chuvas esparsas",
#                 "condition":"rain"
#             },
#             {
#                 "date":"25/01",
#                 "weekday":"Ter",
#                 "max":30,
#                 "min":20,
#                 "description":"Chuvas esparsas",
#                 "condition":"rain"
#             }
#         ]
#     },
#     "execution_time":0.0,
#     "from_cache":true
# }