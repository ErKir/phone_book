def plain(tree: dict) -> str:
    def callback(item):
        id = item[0]
        data = item[1]
        result = f'{id} '
        result += f'Name: {data["last_name"]} {data["first_name"]} '
        result += f'{data["patronymic"]} '
        result += f'Organization: {data["organization"]}; '
        result += f'Work tel.: {data["work_telephone"]}; '
        result += f'Personal tel.: {data["personal_telephone"]};'
        return result

    lines = list(map(callback, tree.items()))
    return '\n'.join(lines)
