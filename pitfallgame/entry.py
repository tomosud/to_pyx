import pyxel
import random

class Game:
    def __init__(self):
        pyxel.init(240, 160, title="Pitfall Adventure")
        
        # ゲーム定数
        self.SCREEN_WIDTH = 240
        self.SCREEN_HEIGHT = 160
        self.GRAVITY = 0.5
        self.JUMP_POWER = -8
        self.PLAYER_SPEED = 2
        
        # プレイヤー
        self.player_x = 50
        self.player_y = 120
        self.player_vy = 0
        self.player_on_ground = True
        
        # ゲーム状態
        self.game_over = False
        self.game_clear = False
        self.score = 0
        self.lives = 3
        
        # マップ要素
        self.ground_y = 140
        self.init_map()
        
        pyxel.run(self.update, self.draw)
    
    def init_map(self):
        # 穴の位置（x座標）
        self.pits = [100, 150, 200, 250, 300]
        
        # 敵の位置と動き
        self.enemies = [
            {"x": 80, "y": 120, "vx": 1},
            {"x": 180, "y": 120, "vx": -1},
            {"x": 280, "y": 120, "vx": 1}
        ]
        
        # お宝の位置
        self.treasures = [
            {"x": 70, "y": 130, "collected": False},
            {"x": 120, "y": 130, "collected": False},
            {"x": 170, "y": 130, "collected": False},
            {"x": 220, "y": 130, "collected": False},
            {"x": 270, "y": 130, "collected": False},
            {"x": 320, "y": 130, "collected": False}
        ]
    
    def update(self):
        if self.game_over or self.game_clear:
            if pyxel.btnp(pyxel.KEY_R):
                self.restart_game()
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
            return
        
        # プレイヤー操作
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x -= self.PLAYER_SPEED
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x += self.PLAYER_SPEED
        
        # ジャンプ
        if pyxel.btnp(pyxel.KEY_SPACE) and self.player_on_ground:
            self.player_vy = self.JUMP_POWER
            self.player_on_ground = False
        
        # 重力
        if not self.player_on_ground:
            self.player_vy += self.GRAVITY
            self.player_y += self.player_vy
        
        # 地面との衝突判定
        if self.player_y >= self.ground_y - 10:
            # 穴にいるかチェック
            in_pit = False
            for pit_x in self.pits:
                if pit_x - 10 <= self.player_x <= pit_x + 10:
                    in_pit = True
                    break
            
            if in_pit:
                # 穴に落ちた
                self.player_died()
            else:
                # 地面に着地
                self.player_y = self.ground_y - 10
                self.player_vy = 0
                self.player_on_ground = True
        
        # 画面端での制限
        self.player_x = max(10, min(self.player_x, self.SCREEN_WIDTH - 10))
        
        # 敵の動き
        for enemy in self.enemies:
            enemy["x"] += enemy["vx"]
            if enemy["x"] <= 20 or enemy["x"] >= 220:
                enemy["vx"] *= -1
        
        # 敵との衝突判定
        for enemy in self.enemies:
            if (abs(self.player_x - enemy["x"]) < 15 and 
                abs(self.player_y - enemy["y"]) < 15):
                self.player_died()
        
        # お宝の収集
        for treasure in self.treasures:
            if (not treasure["collected"] and 
                abs(self.player_x - treasure["x"]) < 15 and 
                abs(self.player_y - treasure["y"]) < 15):
                treasure["collected"] = True
                self.score += 100
        
        # ゲームクリア判定
        if all(treasure["collected"] for treasure in self.treasures):
            self.game_clear = True
        
        # リスタート・終了
        if pyxel.btnp(pyxel.KEY_R):
            self.restart_game()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
    
    def player_died(self):
        self.lives -= 1
        if self.lives <= 0:
            self.game_over = True
        else:
            # プレイヤーをスタート位置に戻す
            self.player_x = 50
            self.player_y = 120
            self.player_vy = 0
            self.player_on_ground = True
    
    def restart_game(self):
        self.player_x = 50
        self.player_y = 120
        self.player_vy = 0
        self.player_on_ground = True
        self.game_over = False
        self.game_clear = False
        self.score = 0
        self.lives = 3
        
        # お宝をリセット
        for treasure in self.treasures:
            treasure["collected"] = False
    
    def draw(self):
        pyxel.cls(3)  # 緑の背景（ジャングル）
        
        # 地面を描画
        for x in range(0, self.SCREEN_WIDTH, 10):
            # 穴以外の地面
            is_pit = any(pit_x - 10 <= x <= pit_x + 10 for pit_x in self.pits)
            if not is_pit:
                pyxel.rect(x, self.ground_y, 10, 20, 4)  # 茶色の地面
        
        # 穴を描画
        for pit_x in self.pits:
            pyxel.rect(pit_x - 10, self.ground_y, 20, 20, 0)  # 黒い穴
        
        # 敵を描画（赤い四角）
        for enemy in self.enemies:
            pyxel.rect(enemy["x"] - 5, enemy["y"] - 5, 10, 10, 8)
        
        # お宝を描画（黄色い円）
        for treasure in self.treasures:
            if not treasure["collected"]:
                pyxel.circ(treasure["x"], treasure["y"], 4, 10)
        
        # プレイヤーを描画（青い四角）
        pyxel.rect(self.player_x - 5, self.player_y - 5, 10, 10, 12)
        
        # UI描画
        pyxel.text(5, 5, f"Score: {self.score}", 7)
        pyxel.text(5, 15, f"Lives: {self.lives}", 7)
        
        # ゲーム状態メッセージ
        if self.game_over:
            pyxel.text(80, 70, "GAME OVER", 8)
            pyxel.text(70, 85, "Press R to restart", 7)
            pyxel.text(75, 95, "Press Q to quit", 7)
        elif self.game_clear:
            pyxel.text(80, 70, "GAME CLEAR!", 10)
            pyxel.text(70, 85, "Press R to restart", 7)
            pyxel.text(75, 95, "Press Q to quit", 7)

if __name__ == "__main__":
    Game()