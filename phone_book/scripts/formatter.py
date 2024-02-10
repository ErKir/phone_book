def plain(tree):
    def iter(current_item, prop_names):

        def callback(obj):
            name = obj['name']
            state = obj['state']
            current_prop_name = [*prop_names, name]
            match(state):
                case 'added':
                    result = f"Property '{'.'.join(current_prop_name)}'"
                    result += f' was {state} with value: '
                    result += f'{stringify(obj["value"])}'
                    return result
                case 'removed':
                    result = f"Property '{'.'.join(current_prop_name)}'"
                    result += f" was {state}"
                    return result
                case 'updated':
                    result = f"Property '{'.'.join(current_prop_name)}'"
                    result += f' was {state}. From {stringify(obj["value1"])}'
                    result += f' to {stringify(obj["value2"])}'
                    return result
                case 'nested':
                    return iter(obj['children'], current_prop_name)
                case 'unchanged':
                    return ''

        lines = list(map(callback, current_item))
        strings = list(filter(lambda string: string != '', lines))
        return '\n'.join(strings)

    return iter(tree, [])
