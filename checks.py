import requests
import config

def check_http(url: str):  
    try:
        print("Sending GET request...")
        r = requests.get(url, timeout = 5)   
        # print(f"{r.status_code}")
        return r.status_code
    except requests.exceptions.ConnectionError:
        print("Connection failed")
        return None
    except requests.exceptions.Timeout:
        print("Connection timeout (5s reached)")
        return None


def classify_health(status_code):
    match status_code:
        case int() if 200 <= status_code <= 299:
            return "HEALTHY"
        case int() if 300 <= status_code <= 499:
            return "DEGRADED"
        case int() if 500 <= status_code <= 599:
            return "DOWN"
        case None:
            return "DOWN"




def check_services(url_list):
    checkedUrlist = []
    for i in url_list:
        result = check_http(i)
        healthResult = classify_health(result)
        service = {
           "url": i,
           "status-code": result,
           "health": healthResult
        }
        checkedUrlist.append(service)
    return checkedUrlist




if __name__ == "__main__":
    print(check_services(config.url_list))

# print(classify_health(200))
# print(classify_health(404))
# print(classify_health(502))
# print(classify_health(None))




