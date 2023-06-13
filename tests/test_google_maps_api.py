# from requests import Response -- Конструкцию Result_post: Response = ... устарела, можно без нее
import json
import sys 
sys.path.append("C:\\Users\\galov\\ED_auto\\ED_APItests_project")
from utils.checking import Checking
from utils.api import Google_Maps_API
import allure


"""Создание, изменение и удаление новой локации"""
@allure.epic("Test create new location")
class Test_create_place():

    @allure.description("Test create, update and delete location")
    def test_create_new_place(self):

        print("Метод POST")
        result_post = Google_Maps_API.create_new_place()
        check_place_id = result_post.json()
        place_id = check_place_id.get("place_id")
        print(place_id)
        Checking.check_status_code(result_post,200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, "status", "OK")

        print("Метод GET POST")
        result_get = Google_Maps_API.check_location(place_id)
        check_address = result_get.json()
        address = check_address.get("address")
        print(address)
        Checking.check_status_code(result_get,200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        # token = json.loads(result_get.text)
        # print(list(token)) -- конструкция нужна была для того, чтобы узнать все токены
        Checking.check_json_value(result_get, "address", "29, side layout, cohen 09")


        print("Метод PUT")
        result_put = Google_Maps_API.change_location(place_id)
        Checking.check_status_code(result_put,200)
        Checking.check_json_token(result_put, ["msg"])
        Checking.check_json_value(result_put, "msg", "Address successfully updated")

        print("Метод GET PUT")
        result_get = Google_Maps_API.check_location(place_id)
        check_address = result_get.json()
        address = check_address.get("address")
        print(address)
        Checking.check_status_code(result_get,200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, "address", "10 Lenina street, RU")

        print("Метод DELETE")
        result_delete = Google_Maps_API.delete_location(place_id)
        check_status = result_delete.json()
        status = check_status.get("status")
        print(status)
        Checking.check_status_code(result_delete,200)
        Checking.check_json_token(result_delete, ["status"])
        Checking.check_json_value(result_post, "status", "OK")

        print("Метод GET DELETE")
        result_get = Google_Maps_API.check_location(place_id)
        check_address = result_get.json()
        address = check_address.get("address")
        print(address)
        Checking.check_status_code(result_get,404)
        Checking.check_json_token(result_get, ["msg"])
        Checking.check_json_value(result_get, "msg", "Get operation failed, looks like place_id  doesn't exists")
        Checking.check_json_search_word_in_value(result_get, "msg", "failed")
        
        print("Тестирование создания/изменения и удаления локации успешно!")

