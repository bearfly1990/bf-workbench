import json
import allure


def attach_json(json_dict, file_name_flag):
    allure.attach(json.dumps(json_dict), file_name_flag, allure.attachment_typ.JSON)
