class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

if __name__ == "__main__":
    user = User(input("Enter your nickname: "), input("Enter your password: "), input("Enter your age: "))


class Video:
    def __init__(self, title, time_now, adult_mode):
        self.title = title
        self.time_now = time_now
        # self.duration = duration
        self.adult_mode = False


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

        if age < 18:
            self.is_adult = False
        else:
            self.is_adult = True

        if len(nickname) < 5 or len(password) < 8:
            print("Nickname and password must be at least 5 and 8 characters long")
            return

        for user in self.users:
            if user.nickname == nickname:
                print("Nickname already exists")
                return

        if self.is_adult:
            self.nickname = nickname
            self.password = password
            self.age = age
            print("User has been registered successfully")

        if not self.is_adult:
            print("You must be 18 years old to register")

        if self.is_adult:
            print("User has been registered successfully and logged in")

    def add_user(self, user):
        self.users.append(user)
        print(f"{user.nickname} has been added")

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                print(f"Welcome, {user.nickname}!")
                return
            else:
                print("Invalid nickname or password")

    def log_out(self):
        self.current_user = None
        print("You have been logged out")

    def add(self, title, **video):
        self.title = title
        self.videos.append(video)
        print(f"{video.title} has been added")

    def get_video(self, title):
        for video in self.videos:
            if video.title == title:
                return video
            else:
                print("Video not found")

    def watch_video(self):
        if self.current_user is None:
            print("You must be logged in to watch a video")
            return

        video = self.get_video(input("Enter the title of the video you want to watch: "))

        if video is None:
            return

        if video.adult_mode and not self.current_user.is_adult:
            print("You must be 18 years old to watch this adult video")
            return

        print(f"Watching {video.title}")
        print(f"Current time: {video.time_now}/{video.duration}")
        video.time_now += 1

        if video.time_now >= video.duration:
            print(f"{video.title} has ended")



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200,False)
v2 = Video('Для чего девушкам парень программист?', 10, True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
