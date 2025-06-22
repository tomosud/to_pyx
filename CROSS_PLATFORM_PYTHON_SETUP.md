# WSL/Windows両環境対応Pyxelゲーム開発環境セットアップ

**更新条件**: 開発環境セットアップ手順・依存関係・プラットフォーム対応の変更時

このドキュメントは、Claude Code使用時にWSL環境とWindows環境の両方でPyxelゲームを実行できる環境を構築するための実行手順書です。


## Claude Codeへの指示

**AIコーディングエントリー時の環境確認**：

1. **WSL/Linux環境の確認**：以下をチェック
   - `venv/`フォルダが存在するか
   - `requirements.txt`にpyxelパッケージが記載されているか
   - Pyxelゲームが実行可能か

2. **未セットアップの場合**：以下の手順でWSL/Linux環境を構築してください

## 実行手順

### 1. WSL環境での仮想環境作成

Claude CodeがWSL環境で以下を実行：

```bash
python3 -m venv venv
```

### 2. requirements.txt確認・更新

現在のrequirements.txtの内容を確認し、Pyxelゲームに必要なパッケージが含まれていることを確認：

```txt
pyxel
pyxel-universal-font
```

エンコーディング問題回避のため、日本語コメントは使用禁止。

### 3. .gitignore設定

以下の内容で.gitignoreを作成または追記：

```gitignore
# Virtual Environments
venv/
venv_win/
.venv/
.env/
ENV/
env.bak/
venv.bak/
```

### 4. templateフォルダの実行セット確認

**templateフォルダには以下の実行セットが含まれています**：

#### `run.bat` - Windows用一括セットアップ・実行スクリプト
```batch
@echo off
echo Setting up and starting [Game Name]...

REM Navigate to root directory
cd ..

REM Check if venv_win exists, if not create it
if not exist "venv_win" (
    echo Creating virtual environment venv_win...
    python -m venv venv_win
)

REM Activate virtual environment
echo Activating virtual environment...
call venv_win\Scripts\activate.bat

REM Install/update requirements
echo Installing requirements...
pip install -r requirements.txt

REM Navigate back to game directory
cd [game_folder_name]

REM Start web server and open browser
echo Starting [Game Name] Web Server...
echo Opening browser at http://localhost:8000
echo.
start "" http://localhost:8000
python -m http.server 8000

pause
```

**このスクリプトの機能**：
- Windows用仮想環境(`venv_win`)がなければ自動作成
- `requirements.txt`を使用してPythonパッケージを自動インストール
- Webサーバーを起動してブラウザでゲームを起動

#### `entry.py` - メインゲームファイルテンプレート
#### `index.html` - Web版実行用HTMLファイル

### 5. 環境動作テスト

Pyxelゲームの動作テストを実行し、両環境で正常に動作することを確認。

## セットアップ完了の確認

### WSL環境での確認
```bash
source venv/bin/activate
cd [game_folder_name]
python entry.py
```

### Windows環境での確認
- `[game_folder]/run.bat` をダブルクリックで一括セットアップ・実行

両環境でゲームが正常に起動すれば、セットアップ完了です。

## 重要な注意事項

### エンコーディング問題の回避
- **requirements.txt**: 日本語コメント禁止、英語のみ使用
- **バッチファイル**: 英語メッセージ推奨
- **Pythonファイル**: UTF-8エンコーディング使用

### トラブルシューティング

**Windows環境でのエラー例**:
```
UnicodeDecodeError: 'cp932' codec can't decode
```
**解決方法**: requirements.txtから日本語文字を全て削除

**バッチファイル文字化け**:
**解決方法**: バッチファイル内のechoメッセージを英語に変更

**Pyxelライブラリエラー（WSL）**:
```
ImportError: libSDL2-2.0.so.0: cannot open shared object file
```
**解決方法**: `sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev`

## セットアップ後の開発フロー

1. **新しいゲーム開発**: `cp -r template new_game_name` でテンプレートを複製
2. **WSL環境での開発**: Claude Codeで`entry.py`を直接編集・実行
3. **Windows環境でのテスト**: 各ゲームフォルダの`run.bat`でワンクリック実行
4. **依存関係追加**: `requirements.txt`に英語コメントで追記
5. **両環境で検証**: WSLで開発、WindowsでWeb版テスト

### 新しいゲームの作成フロー
1. **テンプレート複製**: `cp -r template my_new_game`
2. **ゲーム実装**: `my_new_game/entry.py` を編集
3. **テスト実行**: WSLで `python entry.py`、Windowsで `run.bat`
4. **ドキュメント更新**: README.mdや仕様書を更新

## このセットアップの完了基準

以下がすべて達成されればセットアップ完了：

- [x] WSL環境で`venv/`仮想環境が作成される
- [x] `requirements.txt`にPyxelパッケージが記載される  
- [x] `.gitignore`に`venv_win/`が除外設定される
- [x] templateフォルダに`run.bat`、`entry.py`、`index.html`の実行セットが作成される
- [x] WSL環境でPyxelゲームが実行成功
- [ ] Windows環境でゲームの`run.bat`が実行成功（手動確認必要）

## 新しいゲーム作成時の手順

1. **テンプレート複製**: `cp -r template new_game_name`
2. **ゲーム実装**: `new_game_name/entry.py` を編集してゲームを作成
3. **環境テスト**: WSLで開発、Windowsで`run.bat`でWeb版テスト

**重要**: templateフォルダの`run.bat`は自動でWindows仮想環境を作成し、`requirements.txt`からパッケージを同期します。

**セットアップはここまでです。この後の具体的な開発内容は別途指示してください。**