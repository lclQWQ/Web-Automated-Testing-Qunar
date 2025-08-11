import json


def read_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


if __name__ == '__main__':

    file = '../datas/telephone_login.json'
    json_data = read_json(file)
    res = []

    for data in json_data.values():
        # 确保每个测试用例字典的值顺序一致
        sorted_values = tuple(value for _, value in sorted(data.items()))
        res.append(sorted_values)

    print(res)
