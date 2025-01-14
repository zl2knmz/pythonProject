import requests


def check_api_key(api_key, api_endpoint):
    """
    检查 Google API Key 是否有效。

    Args:
        api_key: Google API Key.
        api_endpoint: API 端点，例如：https://maps.googleapis.com/maps/api/geocode/json

    Returns:
        True 如果 API Key 有效，否则返回 False.
    """
    try:
        params = {'key': api_key, 'address': 'Google'}  # 使用一些测试参数
        response = requests.get(api_endpoint, params=params)
        response.raise_for_status()  # 如果状态码不是 200，则引发 HTTPError

        data = response.json()
        if data.get("status") == "OK":  # 检查 API 响应状态
            return True
        else:
            print(f"API Key 无效或配额已用完: {data.get('status', 'Unknown error')}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"API 请求失败: {e}")
        return False


if __name__ == '__main__':
    # YOUR_API_KEY
    api_key = "AIzaSyC8KZt_RKgwNeKWKhSJ_XYhHt0aE_flVHw"
    api_endpoint = "https://maps.googleapis.com/maps/api/geocode/json"  # 例如，使用 Geocoding API
    if check_api_key(api_key, api_endpoint):
        print("API Key 有效！")
    else:
        print("API Key 无效！")
