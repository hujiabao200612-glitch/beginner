status_code = int(input('响应状态码：'))
match status_code:
    case 400: description = 'Bad Request'
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 500: description = 'Internal Server Error'
    case _: description = 'Unknown Status Code'

print(f'状态码 {status_code} 的描述是：{description}')
