
# 文字テトリス

**更新条件**: ゲームの概要・基本操作方法・ゲームフローの変更時

## 概要

日本語文字（テ、ト、リ、ス）を使ったテトリス風パズルゲーム。「テトリス」の文字が隣接配置されると連鎖爆発が発生します。

**注意**: このプロジェクトは新しい開発ルールの **参考実装サンプル** です。開発進行中の状態を再現し、実際のゲーム開発時のドキュメント運用例を示しています。

**📋 開発状況**: [DEVELOPMENT_ENTRY.md](./DEVELOPMENT_ENTRY.md) | **🛠️ 開発ガイド**: [../DEVELOPMENT_GUIDE.md](../DEVELOPMENT_GUIDE.md)

## クイックスタート

### 開発環境での実行
```bash
python tet_gameB.py
```

### Web版（GitHub Pages）
[デプロイ後にURLを記入]

## 操作方法

- 矢印キー: 左右移動
- Zキー: 回転
- 下矢印: 高速落下
- R: リスタート

## ゲームの流れ

1. **文字ブロック落下**: テ・ト・リ・スの文字ブロックがランダムに落下
2. **配置**: 矢印キーで位置調整、Zキーで回転させて配置
3. **連鎖判定**: 「テトリス」の文字が隣接すると爆発連鎖が発生
4. **スコア獲得**: 連鎖でスコアを獲得し、ゲーム継続

**詳細仕様**: [CURRENT_SPECIFICATIONS.md](./CURRENT_SPECIFICATIONS.md)

## ドキュメント構成

### 📖 プレイヤー・初回利用者向け
1. **README.md** (このファイル) - プロジェクト概要・クイックスタート

### 📖 開発者向け - 読む順序
1. **[DEVELOPMENT_ENTRY.md](./DEVELOPMENT_ENTRY.md)** - 開発の入り口・現在状況
2. **[../DEVELOPMENT_GUIDE.md](../DEVELOPMENT_GUIDE.md)** - 開発方針・ルール・環境構築
3. **[CURRENT_SPECIFICATIONS.md](./CURRENT_SPECIFICATIONS.md)** - 現在の実装仕様詳細

### 📖 参考資料
- **[DEVELOPMENT_HISTORY.md](./DEVELOPMENT_HISTORY.md)** - 完了フェーズの開発履歴
- **[../CROSS_PLATFORM_PYTHON_SETUP.md](../CROSS_PLATFORM_PYTHON_SETUP.md)** - 環境構築詳細
