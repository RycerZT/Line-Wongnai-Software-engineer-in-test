def fn(input):
    pair = {
        '}': '{',
        ')': '(',
        ']': '[',
        '>': '<'
    }
    start_pair = pair.values()
    end_pair = pair.keys()
    temp = []
    for i in input:
        if i in start_pair:
            temp.append(i)
        elif i in end_pair:
            if not temp or temp.pop() != pair[i]:
                return "not balanced."

    balanced = len(temp) == 0
    #ใช้นับ Count ของ Bracket แต่ยังหาวิธีแก้ของ Special Character (@#@$#$@$) ไม่ได้ครับ
    paired_count = len([i for i in input 
                       if i in pair.values() or i in pair.keys()
                         and i not in {' '}])//2

    if balanced:
        m = "balanced."
    else:
        m= "not balanced."

    return balanced, m, paired_count

# Test case
test_input = "ไก่่กกsaad{}"##Input Test Case Here

result = fn(test_input)
print(result)










