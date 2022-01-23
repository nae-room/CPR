# <center>**📡 CPR 사용자 추천 연결 서비스**</center>

<p align="center"><img src="https://mblogthumb-phinf.pstatic.net/MjAyMjAxMjNfMjgz/MDAxNjQyODY3MDI5MzY3.2-U9qIKcGv_nXkie7sLeZ8wwS2k_cR2hIUkvGJx4MQ4g.tP4mGvsroOLTC4HhY1Rfzn91MGKJWyesK-C1hI8Tc70g.PNG.pmj1010235/cpr.png?type=w800"></p>

## 🎙️ **Introduce**
코로나로 인해 제한된 활동과 비대면 수업등으로 성인이 된 이후 새로운 관계형성에 어려움을 느끼고 있는 대학생들을 위해 제작되었습니다.

기존 심폐소생술의 의미와 비슷하게 저희 팀만이 해석한 **CPR**(Connect Proxy relationship)은 '**C**onnect(연결하다.) **P**roxy(대신) **R**elationship(관계)'의 뜻을 담아 '대신해서 새로운 관계형성'에 도움을 드리고자 하는 추천 사용자 연결 서비스입니다.

## ⭐ **Key Features**
* 사용자에게 알맞는 대화상대 매칭
* 클린한 통화문화를 위한 NLP를 활용한 통화품질 제공
* 데이터분석을 통해 유의미한 데이터 

## 🗂️ **Index**
* [Front-End](https://github.com/nae-room/CPR#-front-end)
* [Back-End](https://github.com/nae-room/CPR#-back-end)

## ⚙️ **설계 및 구상**
.
.
.

## 🔨 **DB Structure**
<p align="center"><img width="593" alt="image" src="https://user-images.githubusercontent.com/54873618/150660075-625a5cfd-b4cd-4e53-885c-b78ad909d649.png"></p>


## 🔨 **Back-End**
* 구현 👉 pymysql 라이브러리를 이용하여 파이썬과 MySQL을 연결, 모든 데이터를 DB에서 가져와 연산한 후 결과를 곧바로 DB에 저장하는 식.
* 매칭 알고리즘 👉 각 사용자들끼리 매칭 점수를 관심사, MBTI 등의 독립 변수를 이용하여 Rule-based 방식으로 도출. 그 후, 모든 매칭 점수를 Priority_queue에 저장하여 greedy하게 매칭할 두 사용자를 찾는다.


## 🔨 **Front-End**
<p align="center"><img src="https://mblogthumb-phinf.pstatic.net/MjAyMjAxMjNfMjgw/MDAxNjQyODY0NjU2OTY4.Q2z-GduCayIJRZvY9mBckEHfm1JN-jmlpA5O8yQEJz8g.ZYe6qUO4B6N58dLnNgmUr7bv01TeSK9zevDVQVO6pIsg.PNG.pmj1010235/KakaoTalk_20220123_001703718.png?type=w800"/></p>
<p align="center"><img src="https://mblogthumb-phinf.pstatic.net/MjAyMjAxMjNfMjM0/MDAxNjQyODcwNjg3MTgz.GoFJOiabGadgD1l95JrtVGeMemyEJDybfi4-dWayRSQg.LqYY8-zRFFRuRXScu7w2MH6zjCW8F4rgfReipEbMsesg.PNG.pmj1010235/KakaoTalk_20220123_015703258.png?type=w800"/></p>

Front-End는 총 15개의 페이지로 구성되어 있으며 각 페이지에 대한 간단한 설명은 다음과 같습니다.

index.html - 로그인 화면 <br> 

profile.html - 개인 프로필 화면으로 사용자의 닉네임, 전공, 관심사 등 여러 항목이 표시됩니다. <br>
chats.html - 채팅방 목록 화면으로 원하는 채팅방을 선택하면 랜덤 사용자와 매칭이 성사됩니다. <br>
friends.html - 친구 목록 화면으로 친구 신청 수락 및 친구와 전화하기 등 여러 기능을 수행할 수 있습니다. <br>
notices.html - 공지사항 화면으로 공지사항 및 김앤장 팀의 소개를 볼 수 있습니다.

waiting1.html - 연결 대기 중 화면으로 연결되면 waiting2.html로 이동합니다.
waiting2.html - 연결 완료 화면으로 상대의 정보를 확인하고 '다시 매칭' 또는 '연결하기' 중 선택할 수 있습니다.
chat.html - 연결 중 화면으로 스피커폰, 음소거, 통화종료의 기능을 사용할 수 있습니다.
evaluate.html - 연결 종료 화면으로 상대에 대한 평가 및 친구신청을 할 수 있습니다.
myself.html - 자기 평가 화면으로 통화 중 자신의 언행에 대한 상세 점수를 확인할 수 있습니다.

## ✏ **Languages & IDE**
* App : PYTHON & HTML,CSS,JAVASCRIPT
* DB : MYSQL
* IDE : VSCODE, Repe.IT

## 🌐 **Environment**
* Operating System : window 11 64bit & Mac OS Monterey
* CPU : i5
* RAM : 8GB

## 👩‍💻 **Developer of Kim & Jang**
|Frontend & Algorithm|Frontend & NLP|DB & Algorithm|NLP & Algorithm|DB & Algorithm|
|--|--|--|--|--|
|<img src="https://avatars.githubusercontent.com/u/96629346?v=4"  width="150" height="150"/>|<img src="https://mblogthumb-phinf.pstatic.net/MjAyMjAxMTlfMTgx/MDAxNjQyNTY4MjcxNzc0.9FZZzG7OIT-hqtZ_7rOVEci8IeeEJ9shM_-D8-dPqugg.SwO-Bsd5H9QGQIAbDrASZEpEVthZEgh_6eIDfqiPODcg.PNG.pmj1010235/IN_duck.png?type=w800"  width="150" height="150"/>|<img src="https://mblogthumb-phinf.pstatic.net/MjAyMjAxMTlfMTMx/MDAxNjQyNTY4MDM3ODA3.LAWjWD8QCNZBVQxPsNlSkz-LoypP5lIxGiwqs-ar0fEg.bgg0nDHqkfVg3SSIf-er0zq3uDwNTSPsshkPDmjT3ykg.JPEG.pmj1010235/KakaoTalk_20220119_131657794.jpg?type=w800"  width="150" height="150"/>|<img src="https://user-images.githubusercontent.com/97957438/149934844-3d94fb3d-e29d-4550-a61d-ff9be35667de.png"  width="150" height="150">|<img src="https://mblogthumb-phinf.pstatic.net/MjAyMjAxMTlfMjgw/MDAxNjQyNTkxMTE5ODg0.j1nbRY6Uc17N4EYSNSTpvn7c-0DgVdyqbsZ7usPghrsg.u5YxXs7L1Prtr6yVFiR5NakcfzP22A_XfudxA91xDSIg.PNG.pmj1010235/KakaoTalk_20220119_195008561.png?type=w800"  width="150" height="150"/>|
|[김다연](https://github.com/nae-room)|김민섭|김성원|김예린|장찬영|
