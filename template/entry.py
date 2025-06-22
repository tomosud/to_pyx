"""
Pyxel Game Entry Point Template

このファイルはPyxelゲームのメインエントリーポイントです。
ここにゲームのメインクラスと実行コードを実装してください。

基本構造:
1. import pyxel
2. Gameクラスの定義
3. if __name__ == "__main__": Game()

このファイルは以下で実行されます:
- WSL/Linux: python entry.py
- Windows: run.bat (Webサーバー版)
- Web版: index.htmlから読み込み

詳細な実装例は ../pitfallgame/entry.py を参照してください。
"""

import pyxel

class Game:
    def __init__(self):
        # ゲームウィンドウの初期化
        pyxel.init(240, 160, title="Your Game Title")
        
        # ここにゲームの初期化処理を書く
        
        # ゲームループの開始
        pyxel.run(self.update, self.draw)
    
    def update(self):
        # ゲームロジックの更新処理
        pass
    
    def draw(self):
        # 描画処理
        pyxel.cls(0)
        pyxel.text(100, 80, "Hello, Pyxel!", 7)

if __name__ == "__main__":
    Game()