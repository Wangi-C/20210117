#괄호 변환 #3
def balanced(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

def good(p):
    count = 0
    for i in p:
        if i == "(":
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    answer = ""
    if p == "":
        return answer
    i = balanced(p)
    u = p[:i+1]
    v = p[i+1:]

    if good(u):
        answer = u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == ")":
                u[i] = "("
            else:
                u[i] = ")"
        answer += "".join(u)
    return answer

p = input()
print(solution(p))