import sys
input = sys.stdin.readline

n = int(input())
words = []

for _ in range(n):
    words.append(input().strip())

# 1. 중복 제거 (set으로 바꿨다가 다시 list로)
words = list(set(words))

# 2. 정렬 조건 설정 (튜플 활용)
# (길이, 단어 자체) 순서로 리스트를 재구성합니다.
sort_list = []
for w in words:
    sort_list.append((len(w), w))

# 3. 정렬 실행 (길이가 짧은 순 -> 길이가 같으면 사전 순)
sort_list.sort()

# 4. 출력
for length, word in sort_list:
    sys.stdout.write(word + '\n')