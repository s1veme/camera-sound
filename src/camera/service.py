def convert_camera_parameters(data):
    string = ''
    for parameter in data.values():
        string = f'{string} {parameter}'

    return string


def create_many_test_parameters(string, limit=50):
    new_string = ''
    for _ in range(limit+1):
        new_string += f'{string}\n'
    return new_string
