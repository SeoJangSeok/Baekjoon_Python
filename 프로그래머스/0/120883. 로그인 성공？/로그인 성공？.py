def solution(id_pw, db):
    _id, _pw = id_pw
    for i, p in db:
        if i == _id:
            if p == _pw:
                return 'login'
            else:
                return 'wrong pw'
    return 'fail'