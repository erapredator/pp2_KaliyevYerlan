import pygame

pygame.init()

size = [334, 200]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Music Player")

playlist = [r"C:\erapp\pp2_KaliyevYerlan\lab7\2\music\I Was Never There.mp3", r"C:\erapp\pp2_KaliyevYerlan\lab7\2\music\infinity.mp3", r"C:\erapp\pp2_KaliyevYerlan\lab7\2\music\Jah Khalib.mp3"]
i = 0
playlist2 = ["I was never there", "Infinity", "Твои сонные глаза"]
pygame.mixer.music.load(playlist[i])

font = pygame.font.Font(None, 36)

image = pygame.image.load(r"C:\erapp\pp2_KaliyevYerlan\lab7\2\photos\player.jpg")

paused = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
                paused = True
                if paused == True:
                    pygame.mixer.music.load(playlist[i])
                    pygame.mixer.music.play(0)
                else:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.play()
            elif event.key == pygame.K_RIGHT:
                i = (i + 1) % len(playlist)
                pygame.mixer.music.load(playlist[i])
                pygame.mixer.music.play()
                paused = False
            elif event.key == pygame.K_LEFT:
                i = (i - 1) % len(playlist)
                pygame.mixer.music.load(playlist[i])
                pygame.mixer.music.play()
                paused = False

    screen.blit(image, (0, 0))

    song_name = font.render(playlist2[i], True, (0, 0, 0))
    screen.blit(song_name, (0, 0))

    pygame.display.flip()


