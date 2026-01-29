import requests

def fetch_api():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    res=requests.get(url)
    data=res.json()

    if data["success"] and "data" in data:
        user_data=data["data"]
        country=data["location"]["country"]
        username=data['login']['username']
        return username,country
    else:
        raise Exception ('failed to fetch')
    
def main():
    try:
        username,country=fetch_api()
        print(f"user : {username} \n region : {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
 