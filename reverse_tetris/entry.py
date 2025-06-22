"""
Reverse Tetris Game
下から上にテトリミノが上がっていく逆テトリス

基本ルール：
- テトリミノは画面下部から上に向かって移動
- プレイヤーは上部でテトリミノを操作
- ライン消去は通常と同じ
- ゲームオーバーは下部に到達した時
"""

import pyxel
import random

class ReverseTetris:
    def __init__(self):
        pyxel.init(240, 320, title="Reverse Tetris")
        
        # ゲーム設定
        self.BOARD_WIDTH = 10
        self.BOARD_HEIGHT = 20
        self.CELL_SIZE = 12
        self.BOARD_X = 60
        self.BOARD_Y = 20
        
        # ゲーム状態
        self.game_over = False
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        
        # ボード（0=空、1-7=各色のブロック）
        self.board = [[0 for _ in range(self.BOARD_WIDTH)] for _ in range(self.BOARD_HEIGHT)]
        
        # テトリミノの定義（7種類）
        self.tetriminos = [
            # I字
            [[[1, 1, 1, 1]]],
            # O字
            [[[2, 2], [2, 2]]],
            # T字
            [[[0, 3, 0], [3, 3, 3]], [[3, 0], [3, 3], [3, 0]], [[3, 3, 3], [0, 3, 0]], [[0, 3], [3, 3], [0, 3]]],
            # S字
            [[[0, 4, 4], [4, 4, 0]], [[4, 0], [4, 4], [0, 4]]],
            # Z字
            [[[5, 5, 0], [0, 5, 5]], [[0, 5], [5, 5], [5, 0]]],
            # J字
            [[[6, 0, 0], [6, 6, 6]], [[6, 6], [6, 0], [6, 0]], [[6, 6, 6], [0, 0, 6]], [[0, 6], [0, 6], [6, 6]]],
            # L字
            [[[0, 0, 7], [7, 7, 7]], [[7, 0], [7, 0], [7, 7]], [[7, 7, 7], [7, 0, 0]], [[7, 7], [0, 7], [0, 7]]]
        ]
        
        # 現在のテトリミノ
        self.current_piece = None
        self.current_x = 0
        self.current_y = 0
        self.current_rotation = 0
        
        # 次のテトリミノ
        self.next_piece = random.randint(0, 6)
        
        # ゲームタイミング
        self.fall_time = 0
        self.fall_speed = 30  # 逆テトリス：下から上への移動速度
        
        self.spawn_new_piece()
        
        pyxel.run(self.update, self.draw)
    
    def spawn_new_piece(self):
        """新しいテトリミノを画面下部にスポーン"""
        self.current_piece = self.next_piece
        self.next_piece = random.randint(0, 6)
        self.current_rotation = 0
        self.current_x = self.BOARD_WIDTH // 2 - 1
        self.current_y = self.BOARD_HEIGHT - 1  # 下部からスタート
        
        # ゲームオーバーチェック
        if self.check_collision(self.current_x, self.current_y, self.current_rotation):
            self.game_over = True
    
    def get_current_tetrimino(self):
        """現在のテトリミノの形状を取得"""
        piece_rotations = self.tetriminos[self.current_piece]
        return piece_rotations[self.current_rotation % len(piece_rotations)]
    
    def check_collision(self, x, y, rotation):
        """衝突判定"""
        piece_rotations = self.tetriminos[self.current_piece]
        piece = piece_rotations[rotation % len(piece_rotations)]
        
        for py, row in enumerate(piece):
            for px, cell in enumerate(row):
                if cell:
                    nx, ny = x + px, y + py
                    if nx < 0 or nx >= self.BOARD_WIDTH or ny < 0 or ny >= self.BOARD_HEIGHT:
                        return True
                    if self.board[ny][nx]:
                        return True
        return False
    
    def place_piece(self):
        """テトリミノをボードに配置"""
        piece = self.get_current_tetrimino()
        for py, row in enumerate(piece):
            for px, cell in enumerate(row):
                if cell:
                    self.board[self.current_y + py][self.current_x + px] = cell
        
        self.clear_lines()
        self.spawn_new_piece()
    
    def clear_lines(self):
        """完成したラインを消去"""
        lines_to_clear = []
        for y in range(self.BOARD_HEIGHT):
            if all(self.board[y][x] != 0 for x in range(self.BOARD_WIDTH)):
                lines_to_clear.append(y)
        
        for y in lines_to_clear:
            del self.board[y]
            self.board.insert(0, [0] * self.BOARD_WIDTH)  # 上部に空行を追加
        
        cleared_count = len(lines_to_clear)
        if cleared_count > 0:
            self.lines_cleared += cleared_count
            self.score += cleared_count * 100 * self.level
            self.level = min(10, 1 + self.lines_cleared // 10)
            self.fall_speed = max(5, 30 - self.level * 2)
    
    def update(self):
        if self.game_over:
            if pyxel.btnp(pyxel.KEY_R):
                self.__init__()
            return
        
        # 左右移動
        if pyxel.btnp(pyxel.KEY_LEFT):
            if not self.check_collision(self.current_x - 1, self.current_y, self.current_rotation):
                self.current_x -= 1
        
        if pyxel.btnp(pyxel.KEY_RIGHT):
            if not self.check_collision(self.current_x + 1, self.current_y, self.current_rotation):
                self.current_x += 1
        
        # 回転
        if pyxel.btnp(pyxel.KEY_UP):
            new_rotation = (self.current_rotation + 1) % len(self.tetriminos[self.current_piece])
            if not self.check_collision(self.current_x, self.current_y, new_rotation):
                self.current_rotation = new_rotation
        
        # 高速落下（実際は高速上昇）
        if pyxel.btn(pyxel.KEY_DOWN):
            self.fall_time += 5
        
        # 逆方向移動（下から上へ）
        self.fall_time += 1
        if self.fall_time >= self.fall_speed:
            self.fall_time = 0
            if not self.check_collision(self.current_x, self.current_y - 1, self.current_rotation):
                self.current_y -= 1  # 上に移動
            else:
                self.place_piece()
    
    def draw(self):
        pyxel.cls(0)
        
        # ボード枠を描画
        pyxel.rectb(self.BOARD_X - 1, self.BOARD_Y - 1, 
                   self.BOARD_WIDTH * self.CELL_SIZE + 2, 
                   self.BOARD_HEIGHT * self.CELL_SIZE + 2, 7)
        
        # ボード内のブロックを描画
        for y in range(self.BOARD_HEIGHT):
            for x in range(self.BOARD_WIDTH):
                if self.board[y][x]:
                    color = self.board[y][x]
                    px = self.BOARD_X + x * self.CELL_SIZE
                    py = self.BOARD_Y + y * self.CELL_SIZE
                    pyxel.rect(px, py, self.CELL_SIZE - 1, self.CELL_SIZE - 1, color)
        
        # 現在のテトリミノを描画
        if not self.game_over:
            piece = self.get_current_tetrimino()
            for py, row in enumerate(piece):
                for px, cell in enumerate(row):
                    if cell:
                        x = self.BOARD_X + (self.current_x + px) * self.CELL_SIZE
                        y = self.BOARD_Y + (self.current_y + py) * self.CELL_SIZE
                        pyxel.rect(x, y, self.CELL_SIZE - 1, self.CELL_SIZE - 1, cell)
        
        # 次のテトリミノを描画
        next_piece = self.tetriminos[self.next_piece][0]
        pyxel.text(180, 40, "NEXT:", 7)
        for py, row in enumerate(next_piece):
            for px, cell in enumerate(row):
                if cell:
                    x = 180 + px * 8
                    y = 50 + py * 8
                    pyxel.rect(x, y, 7, 7, cell)
        
        # スコア表示
        pyxel.text(180, 80, f"SCORE:", 7)
        pyxel.text(180, 90, f"{self.score}", 7)
        pyxel.text(180, 110, f"LEVEL:", 7)
        pyxel.text(180, 120, f"{self.level}", 7)
        pyxel.text(180, 140, f"LINES:", 7)
        pyxel.text(180, 150, f"{self.lines_cleared}", 7)
        
        # 操作説明
        pyxel.text(10, 280, "← → : Move", 7)
        pyxel.text(10, 290, "↑ : Rotate", 7)
        pyxel.text(10, 300, "↓ : Fast Rise", 7)
        pyxel.text(110, 280, "R : Restart", 7)
        pyxel.text(110, 290, "REVERSE TETRIS", 10)
        
        # ゲームオーバー
        if self.game_over:
            pyxel.rect(50, 120, 140, 80, 1)
            pyxel.rectb(50, 120, 140, 80, 7)
            pyxel.text(100, 140, "GAME OVER", 7)
            pyxel.text(80, 160, f"FINAL SCORE: {self.score}", 7)
            pyxel.text(90, 180, "Press R to Restart", 7)

if __name__ == "__main__":
    ReverseTetris()