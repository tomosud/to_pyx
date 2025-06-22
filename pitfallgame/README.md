# Pitfall Adventure

**更新条件**: ゲームの概要・基本操作方法・ゲームフローの変更時

## 概要

プレイヤーがジャングルを探検し、穴や敵を避けながらお宝を集めるサイドスクロールアクションゲームです。

**📋 開発状況**: [DEVELOPMENT_ENTRY.md](./DEVELOPMENT_ENTRY.md) | **🛠️ 開発ガイド**: [../DEVELOPMENT_GUIDE.md](../DEVELOPMENT_GUIDE.md)

## クイックスタート

### 開発環境での実行
```bash
python entry.py
```

### Web版（Windows環境）
```cmd
run.bat
```
ブラウザで http://localhost:8000 が開きます。

## 操作方法

- 左右矢印キー: プレイヤー移動
- スペースキー: ジャンプ
- R: リスタート
- Q: ゲーム終了

## ゲームの流れ

1. **開始**: ゲーム画面でスタート
2. **プレイ**: ジャングルの中を移動し、穴や敵を避けながらお宝を集める
3. **終了**: すべてのお宝を集めるか、プレイヤーが落下・敵に接触でゲームオーバー

**詳細仕様**: [CURRENT_SPECIFICATIONS.md](./CURRENT_SPECIFICATIONS.md)

## ドキュメント構成

### 📖 プレイヤー・初回利用者向け
1. **README.md** (このファイル) - このゲームの概要・操作方法・プレイ方法

### 📖 開発者向け - 読む順序
1. **[DEVELOPMENT_ENTRY.md](./DEVELOPMENT_ENTRY.md)** - 開発の入り口・現在状況
2. **[../DEVELOPMENT_GUIDE.md](../DEVELOPMENT_GUIDE.md)** - 開発方針・ルール・環境構築
3. **[CURRENT_SPECIFICATIONS.md](./CURRENT_SPECIFICATIONS.md)** - 現在の実装仕様詳細

### 📖 参考資料
- **[DEVELOPMENT_HISTORY.md](./DEVELOPMENT_HISTORY.md)** - 完了フェーズの開発履歴
- **[../CROSS_PLATFORM_PYTHON_SETUP.md](../CROSS_PLATFORM_PYTHON_SETUP.md)** - 環境構築詳細
- **[../tetgame/](../tetgame/)** - 参考実装例（ドキュメント運用・開発進行の実例）


