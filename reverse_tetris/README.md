# Reverse Tetris

**更新条件**: ゲームの概要・基本操作方法・ゲームフローの変更時

## 概要

下から上にテトリミノが上がっていく革新的な逆テトリスゲーム。従来のテトリスとは逆方向の物理で新感覚パズル体験を提供します。

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

- **←→ 矢印キー**: テトリミノの左右移動
- **↑ 矢印キー**: テトリミノの回転（時計回り）
- **↓ 矢印キー**: 高速上昇（5倍速）
- **R キー**: ゲームオーバー時のリスタート

## ゲームの流れ

1. **開始**: ゲーム画面でスタート、テトリミノが画面下部からスポーン
2. **プレイ**: テトリミノを操作しながら上に向かって移動、ラインを完成させて消去
3. **終了**: テトリミノがスポーン位置（下部）に到達できなくなったらゲームオーバー

### 特徴
- **逆方向物理**: 従来のテトリスとは逆に、下から上にテトリミノが移動
- **7種類のテトリミノ**: I, O, T, S, Z, J, L の全種類を実装
- **レベルシステム**: 10ライン消去毎にレベルアップ、速度も上昇
- **スコアシステム**: ライン数 × 100 × レベル でスコア計算

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
- **[../pitfallgame/](../pitfallgame/)** - 参考実装例（Pyxelゲーム・ドキュメント運用・開発進行の実例）


