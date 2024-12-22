import pyxel
import PyxelUniversalFont as puf

# 画面の状態を表す定数
STATE_TITLE = 0
STATE_GAME = 1
STATE_END = 2

class TextAdventure:
    def __init__(self):
        # Pyxel ウィンドウを初期化
        pyxel.init(160, 120)
        pyxel.caption = "Simple Text Adventure"

        # PyxelUniversalFont で使用するフォントを指定
        # 同じフォルダに misaki_gothic.ttf などを置いておく必要があります
        self.writer = puf.Writer("misaki_gothic.ttf")

        # ゲーム内部の状態を初期化
        self.reset_game()

        # メインループ開始
        pyxel.run(self.update, self.draw)

    def reset_game(self):
        """ゲーム内部の状態を初期化 (Pyxelの再initは行わない)"""
        self.state = STATE_TITLE
        self.message = ""
        self.choice = 0
        self.selected = False

    def update(self):
        """メインループ更新処理"""
        if self.state == STATE_TITLE:
            self.update_title()
        elif self.state == STATE_GAME:
            self.update_game()
        elif self.state == STATE_END:
            self.update_end()

    def draw(self):
        """メインループ描画処理"""
        pyxel.cls(0)
        if self.state == STATE_TITLE:
            self.draw_title()
        elif self.state == STATE_GAME:
            self.draw_game()
        elif self.state == STATE_END:
            self.draw_end()

    # タイトル画面の更新
    def update_title(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.state = STATE_GAME
            self.message = "森の入り口にたどり着いた。どうする？"
            self.choice = 0
            self.selected = False

    # タイトル画面の描画
    def draw_title(self):
        # draw(x, y, 文字列, フォントサイズ, 文字色, [背景色=-1])
        self.writer.draw(40, 40, "Simple Text Adventure", 8, pyxel.COLOR_WHITE)
        self.writer.draw(48, 70, "Press SPACE to Start", 8, pyxel.COLOR_YELLOW)

    # ゲーム画面の更新
    def update_game(self):
        if not self.selected:
            # 上下キーで選択肢を選ぶ
            if pyxel.btnp(pyxel.KEY_UP):
                self.choice = (self.choice - 1) % 2
            elif pyxel.btnp(pyxel.KEY_DOWN):
                self.choice = (self.choice + 1) % 2

            # エンターキーで選択を確定
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.selected = True
                if self.choice == 0:
                    self.message = (
                        "あなたは森に進んだ。するとそこには...\n"
                        "大きなドラゴンが眠っていた！"
                    )
                else:
                    self.message = (
                        "あなたは町に戻った。安全だが何も始まらない。\n"
                        "冒険はおしまい。"
                    )
        else:
            # 選択結果を見終わったらエンターキーで終了画面へ
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.state = STATE_END

    # ゲーム画面の描画
    def draw_game(self):
        x = 10
        y = 10
        for line in self.message.split("\n"):
            self.writer.draw(x, y, line, 8, pyxel.COLOR_WHITE)
            y += 12

        if not self.selected:
            option1 = "1. 森に進む"
            option2 = "2. 町に戻る"
            color_opt1 = pyxel.COLOR_YELLOW if self.choice == 0 else pyxel.COLOR_WHITE
            color_opt2 = pyxel.COLOR_YELLOW if self.choice == 1 else pyxel.COLOR_WHITE

            self.writer.draw(10, 60, option1, 8, color_opt1)
            self.writer.draw(10, 70, option2, 8, color_opt2)
            self.writer.draw(10, 90, "上下キーで選択, Enterで決定", 8, pyxel.COLOR_GRAY)
        else:
            self.writer.draw(10, 90, "Enterキーで終了画面へ", 8, pyxel.COLOR_GRAY)

    # エンド画面の更新
    def update_end(self):
        # スペースキーを押したらゲーム状態だけをリセットしてタイトルに戻る
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.reset_game()

    # エンド画面の描画
    def draw_end(self):
        self.writer.draw(50, 50, "End of Adventure", 8, pyxel.COLOR_WHITE)
        self.writer.draw(32, 70, "Press SPACE to Restart", 8, pyxel.COLOR_YELLOW)

if __name__ == "__main__":
    TextAdventure()
