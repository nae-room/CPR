# <center>**π‘ CPR μ¬μ©μ μΆμ² μ°κ²° μλΉμ€**</center>

<p align="center"><img src="https://mblogthumb-phinf.pstatic.net/MjAyMjAxMjNfMjgz/MDAxNjQyODY3MDI5MzY3.2-U9qIKcGv_nXkie7sLeZ8wwS2k_cR2hIUkvGJx4MQ4g.tP4mGvsroOLTC4HhY1Rfzn91MGKJWyesK-C1hI8Tc70g.PNG.pmj1010235/cpr.png?type=w800"></p>

## ποΈ **Introduce**
μ½λ‘λλ‘ μΈν΄ μ νλ νλκ³Ό λΉλλ©΄ μμλ±μΌλ‘ μ±μΈμ΄ λ μ΄ν μλ‘μ΄ κ΄κ³νμ±μ μ΄λ €μμ λλΌκ³  μλ λνμλ€μ μν΄ μ μλμμ΅λλ€.

κΈ°μ‘΄ μ¬νμμμ μ μλ―Έμ λΉμ·νκ² μ ν¬ νλ§μ΄ ν΄μν **CPR**(Connect Proxy Relationship)μ '**C**onnect(μ°κ²°νλ€.) **P**roxy(λμ ) **R**elationship(κ΄κ³)'μ λ»μ λ΄μ 'λμ ν΄μ μλ‘μ΄ κ΄κ³νμ±'μ λμμ λλ¦¬κ³ μ νλ μΆμ² μ¬μ©μ μ°κ²° μλΉμ€μλλ€.

## β­ **Key Features**
* μ¬μ©μμκ² μλ§λ λνμλ λ§€μΉ­
* ν΄λ¦°ν ν΅νλ¬Ένλ₯Ό μν NLPλ₯Ό νμ©ν ν΅ννμ§ μ κ³΅

## ποΈ **Index**
* [Front-End](https://github.com/nae-room/CPR#-front-end)
* [Back-End](https://github.com/nae-room/CPR#-back-end)

## βοΈ **μ€κ³ λ° κ΅¬μ**

## π¨ **DB Structure**
<p align="center"><img width="593" alt="image" src="https://user-images.githubusercontent.com/54873618/150660075-625a5cfd-b4cd-4e53-885c-b78ad909d649.png"></p>


## π¨ **Back-End**
* κ΅¬ν π pymysql λΌμ΄λΈλ¬λ¦¬λ₯Ό μ΄μ©νμ¬ νμ΄μ¬κ³Ό MySQLμ μ°κ²°, λͺ¨λ  λ°μ΄ν°λ₯Ό DBμμ κ°μ Έμ μ°μ°ν ν κ²°κ³Όλ₯Ό κ³§λ°λ‘ DBμ μ μ₯νλ μ.
* λ§€μΉ­ μκ³ λ¦¬μ¦ π κ° μ¬μ©μλ€λΌλ¦¬ λ§€μΉ­ μ μλ₯Ό κ΄μ¬μ¬, MBTI λ±μ λλ¦½ λ³μλ₯Ό μ΄μ©νμ¬ Rule-based λ°©μμΌλ‘ λμΆ. κ·Έ ν, λͺ¨λ  λ§€μΉ­ μ μλ₯Ό Priority_queueμ μ μ₯νμ¬ greedyνκ² λ§€μΉ­ν  λ μ¬μ©μλ₯Ό μ°Ύλλ€.
* κ΄μ¬μ¬ λΆμ π μ¬μ©μμ λνλ΄μ©μ νμ€νΈλ‘ λΆλ¬μμ λ, νκ΅­μ΄ ννμ λΆμκΈ°λ₯Ό μ΄μ©ν΄ λ¨μ΄λ₯Ό μΆμΆ. λΆμ©μ΄ μ²λ¦¬λ₯Ό ν΅ν΄ μ μλ―Έν κ΄μ¬μ¬ ν€μλλ₯Ό λΆμνμ¬ DBμ μλ°μ΄νΈ.
* λΉμμ΄ νν°λ§ π μμ€ λ° λΉνλ°μΈμ ν¬ν¨ν λ°μ΄ν°μμΌλ‘ λμ΄λΈλ² μ΄μ¦ λ€ν­λΆν¬ λͺ¨λΈ νμ΅. λλ¦¬λΆμ λͺ¨λΈμ νμ©νμ¬ λΉμμ΄λ₯Ό νν°λ§νλ ν¨μλ₯Ό μμ±, μ¬μ©μμ λ°ν λ΄μ©μ΄ λΉμμ΄λ₯Ό ν¬ν¨νμλμ§ νμΈν  μ μλ€.


## π¨ **Front-End**
<p align="center"><img src="https://mblogthumb-phinf.pstatic.net/MjAyMjAxMjNfMjgw/MDAxNjQyODY0NjU2OTY4.Q2z-GduCayIJRZvY9mBckEHfm1JN-jmlpA5O8yQEJz8g.ZYe6qUO4B6N58dLnNgmUr7bv01TeSK9zevDVQVO6pIsg.PNG.pmj1010235/KakaoTalk_20220123_001703718.png?type=w800"/></p>
<p align="center"><img src="https://mblogthumb-phinf.pstatic.net/MjAyMjAxMjNfNzQg/MDAxNjQyOTAyMzE1OTEw.F6Aj8Mj_tFEZDep0h7HcFTpJWKUGDACeNXpTBdMg_IEg._9NWI1uv2M4KVSX7W2MXEIZ_QSHN4I-R2uBrMn3xX9wg.PNG.pmj1010235/KakaoTalk_20220123_104324722.png?type=w800"/></p>

Front-Endλ μ΄ 15κ°μ νμ΄μ§λ‘ κ΅¬μ±λμ΄ μμΌλ©° κ° νμ΄μ§μ λν κ°λ¨ν μ€λͺμ λ€μκ³Ό κ°μ΅λλ€.

index.html - λ‘κ·ΈμΈ νλ©΄ <br> 

profile.html - κ°μΈ νλ‘ν νλ©΄μΌλ‘ μ¬μ©μμ λλ€μ, μ κ³΅, κ΄μ¬μ¬ λ± μ¬λ¬ ν­λͺ©μ΄ νμλ©λλ€. <br>
chats.html - μ±νλ°© λͺ©λ‘ νλ©΄μΌλ‘ μνλ μ±νλ°©μ μ ννλ©΄ λλ€ μ¬μ©μμ λ§€μΉ­μ΄ μ±μ¬λ©λλ€. <br>
friends.html - μΉκ΅¬ λͺ©λ‘ νλ©΄μΌλ‘ μΉκ΅¬ μ μ²­ μλ½ λ° μΉκ΅¬μ μ ννκΈ° λ± μ¬λ¬ κΈ°λ₯μ μνν  μ μμ΅λλ€. <br>
notices.html - κ³΅μ§μ¬ν­ νλ©΄μΌλ‘ κ³΅μ§μ¬ν­ λ° κΉμ€μ₯ νμ μκ°λ₯Ό λ³Ό μ μμ΅λλ€. <br>

waiting1.html - μ°κ²° λκΈ° μ€ νλ©΄μΌλ‘ μ°κ²°λλ©΄ waiting2.htmlλ‘ μ΄λν©λλ€. <br>
waiting2.html - μ°κ²° μλ£ νλ©΄μΌλ‘ μλμ μ λ³΄λ₯Ό νμΈνκ³  'λ€μ λ§€μΉ­' λλ 'μ°κ²°νκΈ°' μ€ μ νν  μ μμ΅λλ€. <br>
chat.html - μ°κ²° μ€ νλ©΄μΌλ‘ μ€νΌμ»€ν°, μμκ±°, ν΅νμ’λ£μ κΈ°λ₯μ μ¬μ©ν  μ μμ΅λλ€. <br>
evaluate.html - μ°κ²° μ’λ£ νλ©΄μΌλ‘ μλμ λν νκ° λ° μΉκ΅¬μ μ²­μ ν  μ μμ΅λλ€. <br>
myself.html - μκΈ° νκ° νλ©΄μΌλ‘ ν΅ν μ€ μμ μ μΈνμ λν μμΈ μ μλ₯Ό νμΈν  μ μμ΅λλ€. <br>

## π **Languages & IDE**
* App : PYTHON & HTML, CSS, JAVASCRIPT
* DB : MYSQL
* IDE : VSCODE, Repe.IT

## π **Environment**
* Operating System : window 11 64bit & Mac OS Monterey
* CPU : i5
* RAM : 8GB

## π©βπ» **Developer of Kim & Jang**
|Frontend & Algorithm|Frontend & NLP|DB & Algorithm|NLP & Algorithm|DB & Algorithm|
|--|--|--|--|--|
|<img src="https://avatars.githubusercontent.com/u/96629346?v=4"  width="150" height="150"/>|<img src="https://mblogthumb-phinf.pstatic.net/MjAyMjAxMTlfMTgx/MDAxNjQyNTY4MjcxNzc0.9FZZzG7OIT-hqtZ_7rOVEci8IeeEJ9shM_-D8-dPqugg.SwO-Bsd5H9QGQIAbDrASZEpEVthZEgh_6eIDfqiPODcg.PNG.pmj1010235/IN_duck.png?type=w800"  width="150" height="150"/>|<img src="https://mblogthumb-phinf.pstatic.net/MjAyMjAxMTlfMTMx/MDAxNjQyNTY4MDM3ODA3.LAWjWD8QCNZBVQxPsNlSkz-LoypP5lIxGiwqs-ar0fEg.bgg0nDHqkfVg3SSIf-er0zq3uDwNTSPsshkPDmjT3ykg.JPEG.pmj1010235/KakaoTalk_20220119_131657794.jpg?type=w800"  width="150" height="150"/>|<img src="https://user-images.githubusercontent.com/97957438/149934844-3d94fb3d-e29d-4550-a61d-ff9be35667de.png"  width="150" height="150">|<img src="https://mblogthumb-phinf.pstatic.net/MjAyMjAxMTlfMjgw/MDAxNjQyNTkxMTE5ODg0.j1nbRY6Uc17N4EYSNSTpvn7c-0DgVdyqbsZ7usPghrsg.u5YxXs7L1Prtr6yVFiR5NakcfzP22A_XfudxA91xDSIg.PNG.pmj1010235/KakaoTalk_20220119_195008561.png?type=w800"  width="150" height="150"/>|
|[κΉλ€μ°](https://github.com/nae-room)|κΉλ―Όμ­|κΉμ±μ|κΉμλ¦°|μ₯μ°¬μ|
