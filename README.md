# 2DGP
2D Game Programming Term Project

1. 게임의 간단한 소개 (카피의 경우 원작에 대한 언급)
   -
   - '고양이마리오'를 모작으로 하는 플랫포머 게임을 만드려고 한다.
   - 모작 게임인 '고양이마리오'는 전통적인 플랫포머 게임의 형태를 띄고 독특한 함정과 예측 불가능한 요소가 가득한 게임이다. 주인공인 고양이가 여러 맵을 탐방하면서 숨겨져있는 함정들을 피하고 결승점에 도달하면 되는 간단한 목표를 가진 게임이다.
   - ![image](https://github.com/user-attachments/assets/1abccb0a-e4a0-4edc-a3af-f9ee8eaa7c86)
   - 내가 만들 게임은 'TinoVenture'라는 게임으로 티노가 주인공이 되어 숨겨져있는 장애물들을 피하고 무사히 학교에 등교하는 게임이다. 간단해보이는 맵과 다르게 숨겨져있는 장애물들이 플레이어가 쉽게 결승점에 도달할 수 없게 만든다.
   - 내가 만든 게임은 '고양이 마리오'와 다르게 주인공이 티노이고 결승점인 한국공학대학교 로고 위치가 플레이어 위치에 따라 변한하는 독특한 매커니즘을 가졌다는 차이점이 있다(12월 12일 추가)
   - 11/26 게임 제목 수정
   - 핵심 메카닉
       1. 예상치 못한 함정 : 보이는 발판이 갑자기 떨어지거나 보이지않던 함정이 생기거나 안전해 보이던 것이 적으로 변신하는 등의 트릭을 숨긴다.
       2. 즉각 리스폰 : 캐릭터가 죽을 때마다 빠르게 세이브 포인트로 리스폰하여 플레이의 흐름이 끊기지 않게 설계한다.즉, 플레이어가 반복 플레이를 통해 장애물의 위치를 알고 피하는 등 공략 방법을 익힐 수 있도록 한다.
       3. 기발한 함정과 사건 : 각종 함정과 예상치 못한 사건들로 플레이어에게 유머러스한 좌절감을 주고 플레이어가 오기가 생겨 게임을 끝까지 플레이하도록 한다.
      <img width="478" alt="1 2dgp" src="https://github.com/user-attachments/assets/37580e09-c243-4c54-a228-665bcf260a64">

2. 예상 게임 실행 흐름
   -
   - 게임은 메인화면, 스테이지설정, 본게임으로 이루어져 있다
     <img width="530" alt="2 2dgp" src="https://github.com/user-attachments/assets/113fe772-4475-4f19-bc51-cda3f41bdec9">
   - 메인화면에서 게임시작을 누르면 스테이지설정에서 플레이할 스테이지를 선택한다.
     <img width="530" alt="3 2dgp" src="https://github.com/user-attachments/assets/cacbd226-85e7-422f-9eb9-d58ccc4375d9">
   - 스테이지를 선택하면 본게임에 들어가게 되고 그 스테이지의 맵과 현재 상황에 대해 설명하는 티노가 등장한다.
     <img width="530" alt="5 2dgp" src="https://github.com/user-attachments/assets/2ef3a701-2a59-4aa9-afd1-a61c991cb54d">
   - 티노를 조작해 장애물을 피하고 결승점에 도달하면 무사히 학교 도착이라는 명칭과 함께 그 스테이지를 클리어한다.
     <img width="530" alt="6 2dgp" src="https://github.com/user-attachments/assets/da054a24-7c25-4729-a401-d1dd1d2c05b4">
   - 다시 스테이지설정으로 넘어가며 플레이한 해당 스테이지는 클리어되었다는 표시가 뜨고 다음 스테이지가 열리게 된다.
     <img width="530" alt="4 2dgp" src="https://github.com/user-attachments/assets/a1c8e5b9-d2eb-42ea-b5bf-5fc7cdc61a77">
     (그림판으로 예상 게임 실행 흐름을 간단하게 그려보았다)
    
3. 개발 내용
   -
   - Scene은 위에서 말했듯이 메인화면, 스테이지설정, 본게임으로 이루어져 있다.
   - MainMenu Scene의 class
        - MainMenu : 메인 화면을 초기화하고 필요한 UI 요소인 게임 시작, 설정, 게임 종료를 표시하며, 사용자가 버튼을 클릭하면 해당 Scene으로 이동하는 기능을 수행한다
        - Button : 메인 화면의 "게임 시작", "설정", "게임 종료" 버튼을 생성하고 클릭 이벤트를 처리한다.
        - Background : 배경 이미지를 표시한다.
        - GameLogo : 게임의 로고를 표시해 게임의 제목을 시각적으로 전달한다.
   - StageSelection Scene의 class
        - StageSelection : 스테이지 설정 화면을 초기화하고, 스테이지 아이콘 클릭 이벤트를 처리한다.
        - StageIcon : 각 스테이지를 나타내는 아이콘을 표시하고, 선택된 스테이지 정보를 저장한다.
        - BackButton : 이전 화면인 메인 메뉴로 돌아가는 버튼으로 클릭하면 MainMenu Scene으로 이동한다.
   - MainGame Scene의 class
        - Game : 본게임의 핵심 클래스로, Scene의 초기화, 게임 루프 관리, 죽은 횟수 및 진행 상태 업데이트, 플레이어와 오브젝트의 상호작용을 종합적으로 처리한다.
        - Player : 플레이어가 조작하는 티노 캐릭터를 정의하며, 점프, 이동, 사망 등의 상태를 관리하고 함정이나 적과의 상호작용을 처리한다.
        - Platform : 티노가 이동하거나 점프할 수 있는 발판 역할을 한다.
        - Trap : 티노가 통과할 때 위험한 상황을 만드는 요소로, 예측 불가능한 함정, 낙하하는 가시 등 플레이어와 충돌 시 사망하는 효과를 가진다.
        - Enemy : 티노의 진행을 방해하는 적으로 플레이어와 충돌 시 사망 효과가 있다.
        - Checkpoint : 중간 저장 지점으로, 플레이어가 사망할 경우 이 지점을 지나갔다면 이 지점에서 리스폰 되도록 한다.
        - HUD : 플레이어의 진행도, 사망 횟수 등 게임의 상태를 실시간으로 표시하는 UI 요소이다.
        - Exit : 플레이어가 esc를 누르면 게임이 멈추며 "계속하기", "메인화면으로 돌아가기" 두 버튼이 뜨며 각 버튼 클릭 이벤트를 처리한다.
   - 공통 class
        - SceneManager : Scene 전환을 담당하며 Scene 간의 이동을 손쉽게 구현하고, 필요한 Scene을 호출한다.
        - AudioManager : 각 Scene과 이벤트에 맞는 배경음악과 효과음을 재생하고, 옵션 메뉴에서 사운드 설정을 제어할 수 있게 한다.
        - GameManager : 전체 게임의 진행 상태와 현재 스테이지, 잠금 해제 상태, 옵션 등 글로벌 데이터를 관리한다.
        - InputHandler : 키보드 입력을 받아서 플레이어와 상호작용할 수 있도록 하고, 움직임, 점프 등 기본적인 플레이어 조작을 처리한다.

   - MainMenu Scene의 Controller
        - AudioController : 메인화면의 설정에서 배경음악을 제어하고, 각 버튼 클릭 시 효과음을 재생한다.
   - StageSelection Scene의 Controller
        - UnlockController : 스테이지 해제 조건을 확인하고 조건이 만족되면 해당 스테이지의 잠금을 해제하는 역할을 한다.
   - MainGame Scene의 Controller
        - GameController : 게임의 전체 진행을 관리하는 핵심 컨트롤러로, Scene 초기화, 게임 루프 제어, 진행 상태 업데이트, GameObject의 생명주기를 관리한다.
        - CollisionController : 충돌 감지와 처리 로직을 담당하며 플레이어가 적이나 함정에 부딪힐 때 사망 처리를 적절히 처리한다.
        - CheckpointController : 플레이어가 체크포인트에 도착했을 때 현재 위치를 저장하고 사망 시 저장된 체크포인트에서 리스폰되도록 한다.
        - EnemyController : 적의 행동을 관리하고, 적의 움직임, 패턴, 플레이어와의 상호작용을 제어한다
        - GameOverController : 플레이어 사망 시 사망 횟수가 뜨며 마지막으로 저장된 체크포인트에서 리스폰되도록 한다.

   - 파이썬을 기반으로 한 2D 게임 프레임워크인 Pygame을 사용할 예정이다. Pygame의 Sprite는 게임 내 객체를 다루기 쉽게 해주는 클래스로 이미지, 애니메이션, 움직임, 충돌 감지 등의 기능을 갖추고 있어 GameObject를 효과적으로 관리하고 조작할 수 있게 해준다. 예를 들어 pygame.sprite.collide_rect의 함수를 통해 GameObject 간의 충돌을 손쉽게 감지할 수 있어 함정이나 적과의 충돌 처리를 간단하게 구현할 수 있다.

Pygame 장단점(11월 9일 추가)
- 장점 : 사운드, 그래픽, 텍스트 렌더링, 충돌 처리, 이벤트 관리 등 게임 개발에 필요한 다양한 기능을 포함하고 있어서 게임을 더욱 쉽게 개발할 수 있다.
- 단점 : 비교적 다른 고급 게임 엔진에 비해 객체 지향 기능이 부족하고 게임의 복잡성이 커질 수 있다. 따라서 언제든 수정하고 관리할 수 있게 구분지어서 코드를 작성할 예정이다.
      
4. 일정 (1차 발표 전까지 수정 가능)
   -
   - ~ 10월 27일 : 1차 발표를 위한 README.md 작성 및 자료조사 
   - 10월 28일 : 1차 발표 (유튜브 링크 : https://www.youtube.com/watch?v=tm51O1R8cmA&t=8s)
   - 10월 29일 ~ 11월 4일 : 게임의 기본적인 틀 제작
   - 11월 5일 ~ 11월 11일 : 각 Scene의 class 정의(Player, Enemy 등 GameObject 생성)
   - 11월 12일 ~ 11월 18일 : 각 class 구체화 및 함정 구현
   - 11월 19일 ~ 11월 25일 : 게임 내 세부적인 내용 추가
   - 11월 26일 ~ 12월 3일 : 버그 확인 및 마무리

4-1. 일정 수행 결과
   - 10월 29일 ~ 11월 4일 : 메인 캐릭터인 티노와 기본적인 게임 화면을 만들었으며 이동, 점프 등 조작 가능하게 했다.
   - 11월 5일 ~ 11월 11일 : 게임 시작 Scene과 스테이지 선택 Scene, 메인 Scene으로 나누었으며 각 Scene 내에 있는 class를 정의하였다.
   - 11월 12일 ~ 11월 18일 : 각 Scene의 배경화면과 블럭 이미지 설정하였다.
   - 11월 19일 ~ 11월 25일 : 하늘에서 떨어지는 장애물 등 장애물 설정 및 충돌처리를 구현하였다.
   - 11월 26일 ~ 12월 2일 : stage2와 stage3 기본 맵 구성하였고 각 스테이지 간 상호작용을 구현하였따. 또한, 점프 사운드를 추가하고 게임 BGM을 설정하였다.
   - 12월 3일 ~ 12월 12일 : 최종 보스를 추가하고 보스를 깨는 매커니즘을 넣었다. esc를 추가해 소리 설정을 할 수 있게 했다. 버그를 찾아 수정하고 게임의 마무리 작업을 하였다.

4-2. Commit 수 
![image](https://github.com/user-attachments/assets/7e16b2e7-4dad-417b-a1c6-3b49b3bb20ae)
![image](https://github.com/user-attachments/assets/6391bb68-ce94-424d-b21e-fd8836e14c74)
<img width="123" alt="image" src="https://github.com/user-attachments/assets/1d4677bf-a6af-43bf-b274-597d3da70dde" />
(12월 12일 추가)

5. 사용된 기술:
   -
   1. Pygame 초기화 및 설정
         -pygame.init(), pygame.mixer.init() : Pygame과 오디오 시스템 초기화
         -pygame.display.set_mode((800, 600)) : 창 크기 설정
         -pygame.display.set_caption("TinoVenture") : 창 제목 설정
   2. 오디오 관리
         -pygame.mixer.Sound("bounce.mp3") : 효과음 로딩 및 볼륨 설정
         -pygame.mixer.music.load() : 배경 음악 로딩
         -pygame.mixer.music.play() : 배경 음악 재생 및 볼륨 조절
   3. 이미지 로딩 및 변환
         -pygame.image.load() : 이미지 파일 로딩
         -.convert() 및 .convert_alpha() : 이미지 최적화 및 투명도 지원
         -pygame.transform.scale() : 이미지 크기 조정
         -pygame.transform.flip() : 이미지 뒤집기
   4. 게임 오브젝트 관리
         -오브젝트 위치와 충돌 감지:
            -pygame.Rect() : 직사각형 오브젝트 생성
            -.colliderect() : 충돌 감지
            -.subsurface() : 특정 이미지 영역 자르기
   5. 키 입력 처리
         -pygame.key.get_pressed() : 키보드 입력 확인
         -pygame.KEYDOWN, pygame.K_a, pygame.K_d, pygame.K_RETURN 등 : 특정 키 입력 이벤트 처리
   6. 마우스 입력 처리
         -pygame.MOUSEBUTTONDOWN : 마우스 버튼 클릭 감지
         -pygame.MOUSEMOTION : 마우스 이동 감지
         -pygame.mouse.get_pos() : 마우스 위치 확인
   7. 물리 및 충돌 처리
         -중력과 점프:
            -중력(gravity), 속도(velocity_y)를 사용해 물리적 움직임 구현
            -바닥과 충돌 시 위치 재설정 및 점프력 적용
         -장애물 충돌 및 낙사 감지:
            -바닥 블록과 충돌 감지 (check_falling_into_hole())
            -장애물 충돌로 위치 초기화
   8. 게임 씬 및 상태 관리
         -씬 전환:
            -scene = "stage" : 씬 이름 기반 전환
            -stage_buttons 및 stage_message_active : 스테이지 상태 관리
         -게임 초기화 및 재설정 함수들:
            -reset_instage1(), reset_outstage1() 등 스테이지 초기화
   9. 렌더링 및 UI 그리기
         -텍스트 렌더링:
            -pygame.font.SysFont() : 폰트 생성
            -.render() : 텍스트 이미지 생성
         -메시지 박스:
            -draw_message_box() : 메시지 박스 출력
            -draw_stage(), draw_game_scene() : 스테이지와 오브젝트 출력
   10. 게임 루프 관리
         -게임 루프 및 종료 조건:
            -while running: : 게임 루프 실행
            -pygame.event.get() : 이벤트 수집
            -pygame.display.flip() : 화면 업데이트
            -pygame.quit() : 게임 종료 처리
   11. 추가 기능들
         -볼륨 조절: 슬라이더로 음악 및 효과음 볼륨 조절
         -몬스터 이동: 몬스터 패턴 이동 및 충돌 감지
         -보스 전투: 보스와 충돌 시 보스 변형 (flatten_boss())
6. 참고한 것들
   -
   - 강의자료들
7. 수업내용에서 차용한 것
   -
   - 파이썬 기초
   - 2D 렌더링
   - 애니메이션
   - 입력처리
   - 직선이동
   - 게임오브젝트
   - 캐릭터컨트롤러
   - 충돌처리
   - 사운드
9. 직접 개발한 것
   -
   - 씬 관리 시스템(Scene Management): scene 변수를 사용해 게임 진행 상태를 관리하고 씬 전환 로직 구현
   - 캐릭터 움직임(Physics & Movement): 점프, 중력, 속도, 충돌 감지 등을 포함한 캐릭터 물리 시스템 개발
   - 몬스터 및 보스 패턴(Monster & Boss Logic): 몬스터 이동 및 보스 패턴 시스템 설계
   - 스테이지 관리(Stage Management): 스테이지 선택 및 상태 표시 UI 시스템 설계
   - 투명 블록 및 보상 시스템(Transparent Blocks & Rewards): 특정 조건에서 투명 블록 생성 및 보상 시스템 구현
   - 메시지 시스템(Message System): 게임 중 메시지 출력 및 상호작용 시스템 설계
   - 로딩 화면 애니메이션(Loading Animation): 로딩 화면과 캐릭터 애니메이션 시스템 개발

10. 구현하면서 어려운 부분, 수업에서 추가로 다루었으면 하는 부분에 대한 언급
   하고 싶었지만 못 한 것들
   (앱을 스토어에 판다면) 팔기 위해 보충할 것들
   결국 해결하지 못한 문제/버그
   기말 프로젝트를 하면서 겪은 어려움에 대해 소개해도 좋다
  
12. 수업 진행 방식에 대한 제안
   이번 수업에서 기대한 것, 얻은 것, 얻지 못한 것
   더 좋은 수업이 되기 위해 변화할 점

#기타
고양이 마리오 BGM 유튜브 사이트
https://www.youtube.com/playlist?list=PLOIlehl1iAoVCYB3dZ9Q6hybotCJC4Hnz
