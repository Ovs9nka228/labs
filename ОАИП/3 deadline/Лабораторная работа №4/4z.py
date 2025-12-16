class Song:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        print(f"Создана песня: '{self.title}' ({self.duration} секунд)")
    def get_info(self):
        """Получить информацию о песне"""
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"'{self.title}' - {minutes}:{seconds:02d}"
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
        print(f"Создан плейлист: '{self.name}'")
    def add_song(self, song):
        """Добавить песню в плейлист"""
        self.songs.append(song)
        print(f"Песня '{song.title}' добавлена в плейлист '{self.name}'")
    def remove_song(self, song_title):
        """Удалить песню из плейлиста по названию"""
        for song in self.songs:
            if song.title == song_title:
                self.songs.remove(song)
                print(f"Песня '{song_title}' удалена из плейлиста '{self.name}'")
                return True
        print(f"Песня '{song_title}' не найдена в плейлисте '{self.name}'")
        return False
    def show_playlist(self):
        """Показать все песни в плейлисте"""
        print(f"\n=== Плейлист: '{self.name}' ===")
        if len(self.songs) == 0:
            print("Плейлист пуст")
        else:
            total_duration = 0
            for i, song in enumerate(self.songs, 1):
                song_info = song.get_info()
                print(f"{i}. {song_info}")
                total_duration += song.duration
            total_minutes = total_duration // 60
            total_seconds = total_duration % 60
            print(f"\nВсего песен: {len(self.songs)}")
            print(f"Общая длительность: {total_minutes}:{total_seconds:02d}")
    def get_total_duration(self):
        """Получить общую длительность плейлиста"""
        total = 0
        for song in self.songs:
            total += song.duration
        return total
    def find_song(self, title):
        """Найти песню по названию"""
        for song in self.songs:
            if song.title == title:
                return song
        return None
if __name__ == "__main__":
    print("=== МУЗЫКАЛЬНЫЙ ПЛЕЕР ===\n")
    print("1. Создаем песни:")
    song1 = Song("Bohemian Rhapsody", 354)
    song2 = Song("Imagine", 183)
    song3 = Song("Hotel California", 391)
    song4 = Song("Yesterday", 125)
    print("\n" + "="*50 + "\n")
    print("2. Создаем плейлист:")
    my_playlist = Playlist("Мой любимые песни")
    print("\n" + "="*50 + "\n")
    print("3. Добавляем песни в плейлист:")
    my_playlist.add_song(song1)
    my_playlist.add_song(song2)
    my_playlist.add_song(song3)
    print("\n" + "="*50 + "\n")
    print("4. Содержимое плейлиста:")
    my_playlist.show_playlist()
    print("\n" + "="*50 + "\n")
    print("5. Добавляем еще одну песню:")
    my_playlist.add_song(song4)
    print("\n" + "="*50 + "\n")
    print("6. Обновленный плейлист:")
    my_playlist.show_playlist()
    print("\n" + "="*50 + "\n")
    print("7. Ищем песню:")
    found_song = my_playlist.find_song("Imagine")
    if found_song:
        print(f"Найдена песня: {found_song.get_info()}")
    else:
        print("Песня не найдена")
    print("\n" + "="*50 + "\n")
    print("8. Удаляем песню:")
    my_playlist.remove_song("Hotel California")
    print("\n" + "="*50 + "\n")
    print("9. Итоговый плейлист:")
    my_playlist.show_playlist()
    print("\n" + "="*50 + "\n")
    print("10. Создаем второй плейлист:")
    rock_playlist = Playlist("Рок-хиты")
    song5 = Song("Stairway to Heaven", 482)
    song6 = Song("Smoke on the Water", 340)
    rock_playlist.add_song(song5)
    rock_playlist.add_song(song6)
    rock_playlist.add_song(song1) 
    print("\n" + "="*50 + "\n")
    print("11. Второй плейлист:")
    rock_playlist.show_playlist()
