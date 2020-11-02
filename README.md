# fbknockknock

내 모델의 학습진행 상황을 facebook messenger로 받아볼 수 있는 패키지.

##<예제>

from fbknockknock import fbknock

myAccount = fbknock.login(id, password)

fbknock.send("message", myAccount)


### 윈도우에선 잘 작동하는데 리눅스에서 안된다 ㅠㅠ
