import sqlite3

conn=sqlite3.connect('youtube_videos.db')

cursor=conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()

    print("\n")
    print("-*" * 50)
    if not rows:  
        print("No videos found avilable ")
    else:
        for row in rows:
            print(row)
    print("-*" * 50)
    print("\n")

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    conn.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name=?,time=? WHERE id=?",(new_name,new_time,video_id))
    conn.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?",(video_id,))
    conn.commit()


def main():

    while True:
        print("\n Youtube Manager Project || choose an option ")
        print("1. List all YT videos")
        print("2. Add a YT video")
        print("3. Update a YT video detail")
        print("4. Delete a YT video")
        print("5. Exit the app")
        choice=input("Enter ur choice : ")

        if choice == '1':
            list_all_videos()
        elif choice == '2':
            name=input("Enter the video name: ")
            time=input("Enter the video time: ")
            add_video(name,time)
        elif choice == '3':
            video_id=input("Enter the video id to update: ")
            name=input("Enter the video name: ")
            time=input("Enter the video time: ")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id=input("Enter video id to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("** Invalid choice **")


    conn.close()

if __name__ == "__main__":
    main()
