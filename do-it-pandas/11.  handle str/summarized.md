# 11-4. 문자열 포매팅 알아보기
### f-문자열을 이용하여 포매팅하기
1. f-문자열은 문자열의 따옴표 기호 앞에 f를 덧붙여 만든다
```python
s = f"hello"
print(s)
```
📝 실행결과
```
hello
```

2. 문자열 안에서 {}을 사용하여 파이썬 변수를 삽입하거나 계산식을 넣을 수 있다.
```python
num = 7
s = f"I only know {num} digits od pi"
print(s)
```
📝 실행결과
```
I only know 7 digits of pi
```

3. 숫자변수 말고도 다양한 변수를 넣을 수 있다.
```python
const = "e"
value = 2.718
s = f"""Black Knight: 'Tis but a {word}.
King Authur: A {word}? Your arim's off!
"""

print(s)
```
📝 실행결과
```
Black Knight: 'Tis but a scratch.
King Authur : A scratch? Your arm's off
```

### 숫자 포매팅하기
1. 숫자 형식도 저장할 수 있다.
```python
p = 3.14159265359
print(f"Some digits of pi: {p}")
```
📝 실행결과
```
Some digits od pi: 3.14159265359
```

2. 천 단위로 쉼표를 찍어서 숫자를 표현
```python
digits = 67890
s = f"In 2005, Lu Chao of China recited {67890, :} digits of pi."
print(s)
```
📝 실행결과
```
In 2005, Lu Chao of China recited 67,890 digits of pi.
```

3. 점을 사용하여 표시할 소수 길이를 지정할 수 있으며 %로 백분율을 나타낼 수 있다.
```python
prop = 7/67890
s = f"I remember {prop:.4} or {prop:.4%} of what Lu Chao recited."
print(s)
```
📝 실행결과
```
I remember 0.0001031 or 0.0103% of what Lu chao recited.
```

4. 숫자와 d기호를 사용하면 원하는 숫자 자릿수를 지정하고 빈자리는 0으로 채울 수 있다.
```python
id = 42
print(f"My ID number is {id : 05d}")
```
📝 실행결과
```
My ID number is  00042
```
5. 중괄호 문법 대신 내장된 문자열 메서드로 형식을 지정할 수도 있다. zfill() 메서드로 미리 00042 형식의 문자열을 만들고 f-문자열에 삽입
```python
id_zfill = "42".zfill(5)
print(f"My ID number is {id_zfill}")
```
📝 실행결과
```
My ID number is  00042
```
6. 문자열을 미리 만들어 삽입하지 않고 f-문자열ㄹ의 중괄호 안에 바로 파이썬 문법을 작성 할수도 있다
```python
print(f"My ID number is {'42'.zfill(5)}")
```
📝 실행결과
```
My ID number is  00042
```

# 11-5. 정규식으로 문자열 처리에 날개 달기
### 정규식으로 패턴 찾기 
1. 10자리 비밀번호 찾는 정규식을 re모듈로 만들기
```python
import re

tele_num = '1234567890'
```
2. \d를 10개 붙인 패턴과 tele_num을 전달한 match() 함수를 호출
```python
m = re.match(pattern = '\d\d\d\d\d\d\d\d\d\d`, string = tele_num)
print(type(m)) # 함수는 match 객체를 반환한다
```
📝 실행결과
```
<class 're.Match'>
```

3. m에 어떤 값이 들었는지 출력
```python
print(m) # Match 객체는 주어진 문자열에 주어진 패턴과 일치하는 부분이 있다면 해당 부분의 처음과 끝 인덱스를 확인하고 일치하는 문자열을 추출
print(bool(m)) # 내장함수 bool()에 Match 객체를 전달하여 True 또는 False라는 값으로 확인 가능
```
📝 실행결과
```
<re.Match object; span=(0, 10), match='1234567890'>
True
```

4. 조건문에서 일치한 문자열의 존재 여부를 활용하고 싶다면 굳이 부울형으로 변환할 필요는 없다. Match 객체 그대로 조건문에 사용 가능
```python
if m:
  print('match')
else:
  print('no match')
```
📝 실행결과
```
match
```

5. start() 와 end() 메서드로 첫 번째와 마지막 인덱스를 반환.
```python
print(m.start())
print(m.end())
# span() 메서드는 찾은 패턴의 첫 번째와 마지막 인덱스를 한 번에 반환
print(m.span())
# group 메서드는 찾은 패턴을 반환
print(m.group())
```
📝 실행결과
```
0
10
(0, 10)
1234567890
```

6. 띄어쓰기를 포함한 전화번호일 경우에는 앞선 패턴을 사용할 수 없다.
```python
tele_num_spaces = '123 456 7890'

m = re.match(pattern = '\d{10}', string = tele_num_spaces)
print(m)
```
📝 실행결과
```
None
```

7. 새롭게 정의한 정규식은 다음과 같다.
```python
p = '\d{3}\s?\d{3}\s?\d{4}'
m = re.match(pattern = p, string = tele_num_spaces)
print(m)
```
📝 실행결과
```
<re.Match object; span=(0, 12), match='123 456 7890'>
```

8. 지역번호를 괄호로 감싸서 표현하거나 전화번호 사이에 하이픈 기호가 있다면?
```python
tele_num_space_paren_dash = '(123) 456-7890`
p = '\(?\d{3}\)?\s?\d{3}-?\d{4}'
m = re.match(pattern = p, string = tele_num_space_paren_dash)
print(m)
```
📝 실행결과
```
<re.Match object; span=(0, 14), match='(123) 456-7890'>
```

### 알기 쉬운 정규식 만들기
1. 파이썬에서는 긴 문자열을 여러 줄로 나누어 표현할 수 있는 기능을 제공. 이를 통해 복잡한 정규식을 보기 쉽게 정리할 수 있다.
```python
p = (
    '\+?'
    '1'
    '\s?'
    '\(?'
    '\d{3}'
    '\)?'
    '\s?'
    '\d{3}'
    '\s?'
    '-?'
    '\d{4}'
)
print(p)
```
📝 실행결과
```
\+?1\s?\(?\d{3}\)?\s?\d{3}\s?-?\d{4}
```

2. 정의한 패턴 문자열 p를 match() 함수에 전달.
```python
cnty_tele_num_space_paren_dash = '+1 (123) 456-7890'
m = re.match(pattern = p, strings = cnty_tel_num_space_paren_dash)
print(m)
```
📝 실행결과
```
<re.Match object; span=(0, 17), match='+1 (123) 456-7890'>
```

### 패턴과 일치하는 모든 문자열 찾기
1. 여러 중에 걸친 긴 문자열을 하나 선언
```python
s = (
    "14 Ncuti Gatwa,"
    "13 Jodie Whittaker, war John Hurt, 12 Peter Capaldi,"
    "11 Matt Smith, 10 David Tennant, 9 Christopher Eccleston"
)
print(s)
```
📝 실행결과
```
14 Ncuti Gatwa,13 Jodie Whittaker, war John Hurt, 12 Peter Capaldi,11 Matt Smith, 10 David Tennant, 9 Christopher Eccleston
```
2. \d와 + 기호를 사용한 패턴으로 findall()을 호출하여 문자열에서 숫자가 1개 이상 연속된 모든 부분을 찾기
```python
p = "\d+"
m = re.findall(pattern = p, string =s)
print(m)
```
📝 실행결과
```
['14', '13', '12', '11', '10', '9']
```
### 패턴과 일치하는 문자열 대체하기
1. 정규식을 사용하여 문자열에 있는 모든 인물 정보를 제거
```python
multi_str = """Guard: What? Ridden on a horse?
King Arthur: Yes!
Guard: You're using coconuts!
King Arthur: What?
Guard: You've got ... coconut[s] and you're bangin' 'em togther.
"""
p = '\w+\s?\w+:\s?'
s = re.sub(pattern=p, string=multi_str, repl='') # pattern이 p일 경우에 ''으로 바꾸기
print(s)
```
📝 실행결과
```
What? Ridden on a horse?
Yes!
You're using coconuts!
What?
You've got ... coconut[s] and you're bangin' 'em togther.
```

2. 슬라이싱 구문을 활용하여 Guard와 King Arthur가 한 말을 각각 추출
```python
guard = s.splitlines()[::2]
kinga = s.splitlines()[1::2]
print(guard)
print(kinga)
```
📝 실행결과
```
['What? Ridden on a horse?', "You're using coconuts!", "You've got ... coconut[s] and you're bangin' 'em togther."]
['Yes!', 'What?']
```

## complie() 함수
* 패턴을 반복해서 사용하는 경우에 compile() 함수로 패턴을 재사용할 수 있는 기능
1. match() 함수부터 적용
```python
p = re.complie('\d{10}')
s = '1234567890'
m = p.match(s)
print(m)
```
📝 실행결과
```
<re.Match object; span=(0, 10), match='1234567890'>
```

2. findall() 함수
```python
p = re.compile('\d+')
s = (
    "14 Ncuti Gatwa, "
    "13 Jodie Whittaker, war John Hurt, 12 Peter Capaldi,"
    "11 Matt Smith, 10 David Tennant, 9 Christopher Eccleston"
)
m = p.findall(s)
print(m)
```
📝 실행결과
```
['14', '13', '12', '11', '10', '9']
```

3. 찾은 문자열을 원하는 문자열로 바꾸는 sub() 함수
```python
p = re.complie('\w+\s?\w+:\s?')
s = "Guard: You're using coconuts!"
m = p.sub(string = s, repl='')
print(m)
```

# 11-6. regex 라이브러리 활용하기
# regex 라이브러리는 좀 더 심화된 정규식 기능을 활용한다.
```
import regex

p = regex.compile('\d+')
s = (
    "14 Ncuti Gatwa, "
    "13 Jodie Whittaker, war John Hurt, 12 Peter Capaldi,"
    "11 Matt Smith, 10 David Tennant, 9 Christopher Eccleston"
)
m = p.findall(s)
print(m)
```
📝 실행결과
```
['14', '13', '12', '11', '10', '9']
```

⭐ 핵심 포인트
* f-문자열 포매팅은 숫자 뒤에 :를 붙이고 ,나 .n, .4%와 같이 사용할 수 있다
* 정규식이란 패턴을 설정하고 그에 맞는 문자열을 찾는데 용이한 기능이다
