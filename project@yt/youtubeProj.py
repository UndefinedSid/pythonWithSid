import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)


def list_all_videos(videos):
    print("\n")
    print("-*" * 50)

    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")

    print("\n")
    print("-*" * 50)

 
  
def add_video(videos):
    name=input("Enter video name :")
    time=input("Enter video time :")
    videos.append({'name' : name,'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video no. to Update : "))

    if(1 <= index <= len(videos)):
        name=input("Enter the new video name : ")
        time=input("Enter the new video length : ")
        videos[index-1]={'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index ")



def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video no. to be deleted : "))

    if( 1 <= index <= len(videos)):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index")
        


def main():
    videos=load_data()
    while True:
        print("\n Youtube Manager Project || choose an option ")
        print("1. List all YT videos")
        print("2. Add a YT video")
        print("3. Update a YT video detail")
        print("4. Delete a YT video")
        print("5. Exit the app")
        choice=input("Enter ur choice : ")

        if choice == '1':
            list_all_videos(videos)
        elif choice == '2':
            add_video(videos)
        elif choice == '3':
            update_video(videos)
        elif choice == '4':
            delete_video(videos)
        elif choice == '5':
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

