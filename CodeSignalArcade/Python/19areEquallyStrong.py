def solution(yourLeft, yourRight, friendsLeft, friendsRight):

            if max(yourLeft,yourRight) == max(friendsLeft, friendsRight) and min(yourLeft,yourRight) == min(friendsLeft, friendsRight):
                return True
            else:
                return False
