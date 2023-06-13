from utils.http_methods import Http_methods

"""Методы для тестирования Google_Maps_API"""

base_url = "https://rahulshettyacademy.com/" #Базовая URL  
key = "?key=qaclick123" #Ключ-параметр для всех запросов

class Google_Maps_API():

    """Метод для создания новой локации"""
    @staticmethod
    def create_new_place():

        json_post = {
            "location": { 
            "lat": -38.383494, 
            "lng": 33.427362 
            }, "accuracy": 50, 
            "name": "Frontline house", 
            "phone_number": "(+91) 983 893 3937", 
            "address": "29, side layout, cohen 09", 
            "types": [
            "shoe park", 
            "shop"

            ],
            "website": "http://google.com", 
            "language": "French-IN"
     
        }

        post_resource = "maps/api/place/add/json" #POST-ресурс 
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = Http_methods.post(post_url, json_post)
        # print(result_post.text)
        return result_post
    
    """Метод для проверки новой локации"""
    @staticmethod
    def check_location(place_id):
        get_resource = "maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        # print(result_get.text)
        return result_get
    
    """Метод для изменения локации"""
    @staticmethod
    def change_location(place_id):
        put_resource = "maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)

        json_put = { 

            "place_id": place_id,
            "address":"10 Lenina street, RU", 
            "key":"qaclick123" 

            }
        result_put = Http_methods.put(put_url, json_put)
        # print(result_put.text)
        return result_put

    """Метод удаления локации"""
    @staticmethod
    def delete_location(place_id):
        delete_resource = "maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)

        json_delete = {

            "place_id": place_id

            }
        
        result_delete = Http_methods.delete(delete_url, json_delete)
        # print(result_delete.text)
        return result_delete

    
    



