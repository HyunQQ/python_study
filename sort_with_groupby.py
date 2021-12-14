def sort_priority(values, group):
  def helper(x):
    if x in group:
      return (0, x)
    return (1, x)
  # 정렬 진행시, 앞에 달려있는 index 기준으로 정렬을 진행한다.
  # group에 포함되어 있는 경우가 "0"으로 먼저 정렬되어 앞에 위치하게 되고,
  # 나머지는 "1"의 경우 뒤에 정렬되어 전체 정렬 구성이 이루어진다.
  values.sort(key=helper)

numbers = [8,3,1,2,5,4,7,6]
group= [2,5,3,7]

sort_priority(numbers, group)
print(numbers)
# [2,3,5,7,1,4,6,8]

