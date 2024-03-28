class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        n = len(board)
        x_count = o_count = 0
        x_score = [0] * 8
        o_score = [0] * 8

        def update_score(points, x, y):
            # antidiag
            if x + y == 2:
                points[-1] += 1
            # diag
            if x - y == 0:
                points[-2] += 1
            # row
            points[i] += 1
            # col
            points[j + 3] += 1

        for i in range(n):
            for j in range(len(board[i])):
                char = board[i][j]

                if char == 'X':
                    update_score(x_score, i, j)
                    x_count += 1
                elif char == 'O':
                    update_score(o_score, i, j)
                    o_count += 1

        # Nunca puede ser que o sea > a x 
        if o_count > x_count:
            return False

        # La diferencia entre o y x solo puede ser como maximo 1
        if x_count - o_count > 1:
            return False

        # Para que O sea = a X significa que X le dio primero Y si x ya tiene 3 en una fila entonces es invalido
        if o_count == x_count and 3 in x_score:
            return False

        # X siempre va primero lo que significa que una vez termina el turno de O va X
        # Si X le da pero O ya completó 3 entonces es invalido
        if x_count > o_count and 3 in o_score:
            return False
        
        return True
