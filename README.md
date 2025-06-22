# AIコーディングで作ったpyxelのゲーム集

**この文書の更新条件**: ゲームの概要・クイックスタート方法・基本ゲームフローの変更時

## 概要
AIコーディングで作ったpyxelのゲーム集です。
各フォルダに、個別のゲームを作成します。


## 開発環境

- Python 3.7以上
- Windows（`venv_win`）/ WSL・Linux（`venv`）対応

## セットアップ・実行方法

claude codeはもし、このリポジトリで環境設定ができていなかったら、以下の文書をみてsetupを行ってください。

詳細なセットアップ手順: [CROSS_PLATFORM_PYTHON_SETUP.md](./CROSS_PLATFORM_PYTHON_SETUP.md)


## 新しいゲームの開発開始手順

### 1. templateフォルダを複製
```bash
# 例：パズルゲームを作る場合
cp -r template puzzle_game
cd puzzle_game
```

**templateに含まれる実行セット**：
- **entry.py** - メインゲームファイル（テンプレートコード）
- **index.html** - Web版実行用HTML
- **run.bat** - Windows環境一括セットアップ・実行スクリプト

### 2. ゲームの実装開始
**entry.py** ファイルを編集してゲームを実装：
- テンプレートコードを参考にゲームロジックを追加
- pyxelのAPIを使用してグラフィック、サウンド、入力処理を実装
- 完成例は [pitfallgame/entry.py](./pitfallgame/entry.py) を参照

### 3. ゲームの実行テスト
**WSL/Linux環境**：
```bash
source venv/bin/activate
python entry.py
```

**Windows環境**：
- `run.bat` をダブルクリックでWeb版を起動

### 4. ドキュメントを確認・更新
開発開始時に以下の順序で読み、適宜更新してください：

1. **[DEVELOPMENT_ENTRY.md](./template/DEVELOPMENT_ENTRY.md)** - 開発状況とフェーズ管理
2. **[ゲームフォルダのREADME.md](./template/README.md)** - 個別ゲームの概要（プレイヤー向け）
3. **[CURRENT_SPECIFICATIONS.md](./template/CURRENT_SPECIFICATIONS.md)** - 詳細仕様
4. **[DEVELOPMENT_HISTORY.md](./template/DEVELOPMENT_HISTORY.md)** - 開発履歴（参考用）

### 5. 参考実装を確認
**[pitfallgame/](./pitfallgame/)** フォルダを参照して以下を確認：
- Pyxelゲームの実装例（Pitfallスタイルアクション）
- ドキュメント運用の実例
- 開発進行中の状況記録方法
- フェーズ管理の具体例

**tetgameフォルダは削除予定です。今後は[pitfallgame/](./pitfallgame/)を唯一のサンプルとして参考してください。**

**重要**: templateフォルダ自体は改変しないこと。


## 技術仕様



### ドキュメント構成

1. **README.md** (このファイル) - プロジェクト概要・クイックスタート

**詳細仕様**: [CURRENT_SPECIFICATIONS.md](./CURRENT_SPECIFICATIONS.md)

### 📖 開発者向け - 読む順序
1. **[DEVELOPMENT_ENTRY.md](./DEVELOPMENT_ENTRY.md)** - 開発の入り口・現在状況
2. **[DEVELOPMENT_GUIDE.md](./DEVELOPMENT_GUIDE.md)** - 開発方針・ルール・環境構築
3. **[CURRENT_SPECIFICATIONS.md](./CURRENT_SPECIFICATIONS.md)** - 現在の実装仕様詳細


### 📖 参考資料
- **[DEVELOPMENT_HISTORY.md](./DEVELOPMENT_HISTORY.md)** - 完了フェーズの開発履歴


### 🔧 開発ツール

- **[tools/](./tools/)** - テスト・デバッグ・分析ツール

---
