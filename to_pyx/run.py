import pyxel
import PyxelUniversalFont as puf
import json
import os

# 画面の状態を表す定数
STATE_GAME = 0
STATE_END = 1

def getpath():
    #このスクリプトのあるディレクトリのパスを取得
    r = str(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
    #print (r)
    return r

class TextAdventure:
    def __init__(self, json_file):
        # JSONからデータを読み込む
        json_file = getpath() + "/" + json_file

        self.game_data = self.load_game_data(json_file)
        
        # 開始地点を探す
        self.current_scene = self.find_start_scene()

        # Pyxel ウィンドウを初期化
        pyxel.init(240, 180)
        pyxel.caption = "Text Adventure"

        # PyxelUniversalFont で使用するフォントを指定
        self.writer = puf.Writer("misaki_gothic.ttf")

        #IPA_Gothic.ttf
        #self.writer = puf.Writer("IPA_Gothic.ttf")

        #まえの状態を保存
        self.mae = {}

        # ゲーム内部の状態を初期化
        self.state = STATE_GAME
        self.choice = 0

        # メインループ開始
        pyxel.run(self.update, self.draw)

    def load_game_data(self, json_file):
        """JSONファイルを読み込んで辞書に格納"""
        with open(json_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def find_start_scene(self):
        """開始地点（Commandがstart）を探す"""
        for key, value in self.game_data.items():
            if value.get("Command") == "start":
                return key
        raise ValueError("開始地点が見つかりません（Commandがstartのエントリが必要）")

    def update(self):
        """メインループ更新処理"""
        if self.state == STATE_GAME:
            self.update_game()
        elif self.state == STATE_END:
            self.update_end()

    def draw(self):
        """メインループ描画処理"""
        pyxel.cls(0)
        if self.state == STATE_GAME:
            self.draw_game()
        elif self.state == STATE_END:
            self.draw_end()

    def update_game(self):
        """ゲーム進行の更新処理"""
        scene = self.game_data[self.current_scene]
        
        # 上下キーで選択肢を選ぶ
        if pyxel.btnp(pyxel.KEY_UP):
            self.choice = (self.choice - 1) % 2
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.choice = (self.choice + 1) % 2

        # エンターキーで選択を確定
        if pyxel.btnp(pyxel.KEY_RETURN):
            next_scene_key = (
                scene["GoTo01"] if self.choice == 0 else scene["GoTo02"]
            )
            if next_scene_key:
                self.current_scene = next_scene_key
                self.choice = 0
            else:
                # 次のシーンが指定されていなければ終了
                self.state = STATE_END

            # コマンドがendならゲーム終了
            if self.game_data[self.current_scene].get("Command") == "end":
                self.state = STATE_END

    def draw_game(self):
        """ゲーム画面の描画"""
        scene = self.game_data[self.current_scene]
        
        #print(scene)
        if self.mae != scene:
            print('---\n')
            print(scene)
            self.mae = scene


        x, y = 10, 10
        # 場所を表示

        for line in scene["Place"].split("\n"):
            self.writer.draw(x, y, line, 8, pyxel.COLOR_DARK_BLUE)
            y += 20


        for line in scene["mainText01"].split("\n"):
            self.writer.draw(x, y, line, 8, pyxel.COLOR_WHITE)
            y += 12


        # 選択肢を表示
        #noneの場合は表示しない
        options = []

        if scene.get("SelectText01", "") != None:
            options.append(scene.get("SelectText01", ""))
        if scene.get("SelectText02", "") != None:
            options.append(scene.get("SelectText02", ""))

        '''
        options = [
            scene.get("SelectText01", ""),
            scene.get("SelectText02", ""),
        ]
        '''

        for i, option in enumerate(options):
            color = pyxel.COLOR_YELLOW if i == self.choice else pyxel.COLOR_WHITE
            self.writer.draw(10, 70 + i * 10, f"{i + 1}. {option}", 8, color)

    def update_end(self):
        """終了画面の更新処理"""
        if pyxel.btnp(pyxel.KEY_SPACE):
            # 再スタートは初期化
            self.current_scene = self.find_start_scene()
            self.state = STATE_GAME
            self.choice = 0

    def draw_end(self):
        """終了画面の描画"""
        self.writer.draw(50, 50, "The End", 8, pyxel.COLOR_WHITE)
        self.writer.draw(32, 70, "Press SPACE to Restart", 8, pyxel.COLOR_YELLOW)

if __name__ == "__main__":
    TextAdventure("exp.json")


