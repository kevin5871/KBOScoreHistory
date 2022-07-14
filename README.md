# KBOScoreHistory

KBO 점수 기록을 알리는 스크립트.

https://sports.news.naver.com/kbaseball/schedule/index 의 데이터를 크롤링하는 스크립트.

사용방법 : 
 - 단독 사용 :

  형식 : ( `'팀 이름'\n'연도'\n'월'` )
<details>
<summary>예시</summary>

`KT`

`2022`

`06`
</details>

 - 모듈 사용 :
<details>
<summary>예시</summary>

`import kboscore`

`print(kboscore.kboscorelist('KT','2022','06'))`
</details>

출력 : 
list 값 반환. (형식 : `n일 | AA AScore : BScore BB` )

<details>
<summary>예시</summary>

['1일 | KT 1:2 SSG', '2일 | KT 14:1 SSG', '3일 | KIA 2:5 KT', '4일 | KIA 3:4 KT', '5일 | KIA 2:2 KT', '6일 | 프로야구 경기가 없습니다.  ', '7일 | KT 0:3 키움', '8일 | KT 5:5 키움', '9일 | KT 7:1 키움', '10일 | KT 9:4 롯데', '11일 | KT 4:0 롯데', '12일 | KT 0:13 롯데', '13일 | 프로야구 경기가 없습니다.  ', '14일 | SSG 4:5 KT', '15일 | SSG 3:6 KT', '16일 | SSG 6:0 KT', '17일 | KT 4:2 두산', '18일 | KT 0:5 두산', '19일 | KT 7:1 두산', '20일 | 프로야구 경기가 없습니다.  ', '21일 | NC 1:8 KT', '22일 | NC 11:0 KT', '23일 | NC VS KT', '24일 | LG 6:9 KT', '25일 | LG 7:2 KT', '26일 | LG 3:1 KT', '27일 | 프로야구 경기가 없습니다.  ', '28일 | KT 14:4 삼성', '29일 | KT 2:8 삼성', '30일 | KT 13:2 삼성']
</details>
