def solution(park, routes):
    ops = {
        'N': [-1, 0],
        'S': [1, 0],
        'W': [0, -1],
        'E': [0, 1]
    }
    
    W = len(park[0])
    H = len(park)
    
    x, y = 0, 0
    for h in range(H):
        for w in range(W):
            if park[h][w] == 'S':
                x = h
                y = w
    
    for route in routes:
        direction, N = route.split()
        
        nx = x
        ny = y

        flag = 0

        for n in range(1, int(N)+1):
            nx += ops[direction][0]
            ny += ops[direction][1]
        
            if nx >= H or nx <= -1 or ny >= W or ny <= -1 or park[nx][ny] == 'X':
                flag = 1
                break
        
        if not flag:
            x += ops[direction][0] * int(N)
            y += ops[direction][1] * int(N)
        
        
    answer = [x, y]
    return answer

if __name__ == "__main__":
    # park = ["OOO", "OSO", "OOO", "OOO"]
    # route = ["N 2", "S 2"]
    park = ["OOOOO", "OOOOO", "OOSOO", "OOOOO", "OOOOO"]
    route = ["E 3", "W 3", "S 3", "N 3", "E 2", "E 1", "W 4", "W 1", "S 2", "S 1", "N 4", "N 1"]
    # park = ["OXO", "XSX", "OXO"]
    # route = ["S 1", "E 1", "W 1", "N 1"]
    # park = ["SOO","OXX","OOO"]
    # route = ["E 2","S 2","W 1"]
    # park =  ["OXO", "XSX", "OXO"]
    # route = ["S 1", "E 1", "W 1", "N 1"]
    answer = solution(park, route)
    print(answer)