# A dictionary containing all the videos on this site
videos = {
    1: {
        "title": "The Walking Dead's Lauren Cohan", 
        "description": "The Walking Dead's Lauren Cohan at the Walking Dead 100th Issue Black-Carpet Event Powered by Hyundai and Future US. Event held at Petco Park in San Diego, CA on July 13, 2012", 
        "views": 2098, 
        "likes": 34
    },
    2: {
        "title": "Heroes of Olympus Review", 
        "description": "Reviewing the Heroes of Olympus series by Rick Riordan, spin-off series to Percy Jackson and the Olympians.", 
        "views": 49, 
        "likes": 0
    },
    3: {
        "title": "Paul Wesley - E.T.", 
        "description": "Fan made video showing scenes from The Vampire Diaries, Wolf Lake, and Fallen starring actor Paul Wesley.", 
        "views": 89030, 
        "likes": 911
    },
    4: {
        "title": "Elijah- Tear You Apart", 
        "description": "Fan made video showing scenes from The Vampire Diaries.", 
        "views": 22236, 
        "likes": 145
    },
    5: {
        "title": "The Walking Dead's Robert Kirkman & Charlie Adlard", 
        "description": "The Walking Dead's Robert Kirkman and Charlie Adlard interview at The Walking Dead 100th Issue Black-Carpet Event Powered by Hyundai and Future US. Event held at Petco Park in San Diego, CA on July 13, 2012.", 
        "views": 443, 
        "likes": 5
    }
    
}

# Shows all of the videos that you can watch.
def display_videos():
    for video_id in videos:
        video_info = videos[video_id]
        print(str(video_id) + " " + video_info['title'] + " - Views: " + str(video_info['views']) + ", Likes: " + str(video_info['likes']))


# Plays a specific video. Increases the view count.
def play_video(video_id):
    if video_id in videos:
        video_info = videos[video_id]
        print("Now Playing: " + video_info['title'])
        print("Description: " + video_info['description'])
        video_info['views'] += 1
    else:
        print("The video ID is invalid.")

# Likes a specific video. Increases the like count.
def like_video(video_id):
    if video_id in videos:
        video_info = videos[video_id]
        video_info["likes"] += 1
        print("You liked " + video_info["title"] + ".")
    else:
        print("The video ID is invalid.")

# Main loop
while True:
    print("") # For formatting
    print("Welcome to MyYouTube!")
    print("1. Display all videos")
    print("2. Play a video")
    print("3. Like a video")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        display_videos()
    elif choice == '2':
        video_id = int(input("Enter the video ID you want to play: "))
        play_video(video_id)
    elif choice == '3':
        video_id = int(input("Enter the video ID you want to like: "))
        like_video(video_id)
    elif choice == '4':
        print("Thank you for using MyYouTube!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")