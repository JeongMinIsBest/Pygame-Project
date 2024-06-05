import pygame
import sys
import random

# 초기화
pygame.init() # 파이게임 라이브러리 초기화

# 화면 설정
width, height = 800, 600 
screen = pygame.display.set_mode((width, height)) # 게임 창 크기 설정
pygame.display.set_caption("Flappy Bird") # 게임 창의 제목 설정

# 색상
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# 새의 설정
bird_image = pygame.image.load(" ") # 새의 이미지 로드 -> 위치 지정해주기!
bird_width = 50 # 새의 크기 가로
bird_height = 35 # 새의 크기 세로
bird_x = width // 3 # 새의 초기 가로 위치
bird_y = height // 2 # 새의 초기 세로 위치
bird_speed = 5 # 새가 움직이는 속도
jump_height = 10 # 새가 점프할 때 높이
gravity = 1 # 새의 중력

# 장애물 설정
obstacle_width = 70
obstacle_height = random.randint(150, 400)
obstacle_x = width # 장애물의 초기 위치
obstacle_y = height - obstacle_height # 장애물의 초기 위치
obstacle_speed = 5 # 장애물이 움직이는 속도
obstacle_gap = 150 # 장애물 간의 간격

# 폰트 설정
font = pygame.font.SysFont(None, 55) # 기본 시스템 폰트 크기를 설정

# 게임 루프
clock = pygame.time.Clock() # 시간 불러오기
score = 0 # 점수 초기화

def display_score(score): # 화면에 점수 불러오는 함수
    score_text = font.render(" Score : " + str(score), True, white)
    screen.blit(score_text, [10, 10])

while True: # 게임 루프 시작
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = -jump_height  # 스페이스바를 누르면 새가 위로 올라감

    # 새의 위치 업데이트
    bird_speed += gravity
    bird_y += bird_speed

    # 장애물 이동
    obstacle_x -= obstacle_speed

    # 충돌 확인
    if (
        bird_y < 0
        or bird_y + bird_height > height
        or (obstacle_x < bird_x + bird_width and obstacle_x + obstacle_width > bird_x and
            (bird_y < obstacle_y or bird_y + bird_height > obstacle_y + obstacle_gap))
    ):
        pygame.quit()
        sys.exit()

    # 점수 업데이트
    if obstacle_x + obstacle_width < bird_x:
        score += 1
        obstacle_x = width
        obstacle_height = random.randint(150, 400)
        obstacle_y = height - obstacle_height

    # 화면 업데이트
    screen.fill(black)
    screen.blit(bird_image, (bird_x, bird_y))
    pygame.draw.rect(screen, green, [obstacle_x, 0, obstacle_width, obstacle_y])
    pygame.draw.rect(screen, green, [obstacle_x, obstacle_y + obstacle_gap, obstacle_width, height - obstacle_y - obstacle_gap])
    display_score(score)

    pygame.display.flip()
    clock.tick(30)