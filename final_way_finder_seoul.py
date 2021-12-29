# 기차에 3명의 승객이 타고 있어요.
train = ['성진', '찬경', '준영']

# 서울역: 승객 '주아'를 맨 뒷칸에 태워 주세요.
train.append('주아' )

print('서울역 도착.  // ', train)
# 대전역: 1등석 승객 '동빈'을 맨 앞에 태워 주세요.
train.insert(0,'동빈')

print('대전역 도착. // ', train)
# 동대구역: 승객 '성진'을 내려 주세요.
train.remove('성진')

print('동대구역 도착. // ', train)
# 부산역: 마지막 역이니 사전순으로 정렬해 주세요.
train.sort()

print('부산역 도착. // ', train)
print('오늘도 빠르고 편안한 기차를 이용해 주셔서 감사합니다.')


# append
#list_name.append(item)
#list_name.insert(index,element)
#"" - apostrophe 
#"주아"
#'주아'
#''