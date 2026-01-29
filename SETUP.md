# RVC WebUI 環境セットアップ手順

## 前提条件
- Python 3.9.x
- NVIDIA GPU + CUDA 11.8

## セットアップ手順

### 1. 仮想環境の作成
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac
```

### 2. pipを24.0に固定
```bash
python -m pip install pip==24.0
```

> **なぜpip 24.0?**
> fairseqが依存するomegaconf 2.0.6のメタデータに不正な記述（`PyYAML>=5.1.*`）があり、
> pip 24.1以降はこれをエラーとして拒否する。pip 24.0は警告のみで通す。

### 3. PyTorchのインストール（CUDA 11.8版）
```bash
pip install torch==2.7.1 torchaudio==2.7.1 torchvision==0.22.1 --index-url https://download.pytorch.org/whl/cu118
```

### 4. その他の依存関係をインストール
```bash
pip install -r requirements-no-torch.txt
```

### 5. モデルファイルのダウンロード
```bash
python tools/download_models.py
```

これにより以下のモデルが自動でダウンロードされる：
- HuBERTモデル
- 事前学習済みモデル (v1/v2)
- RMVPEモデル
- UVR5音声分離モデル

## ユーザーデータの復元（必要に応じて）

学習済みモデルやログはGitに含まれていないため、Google Driveなどから復元：
- `assets/weights/` - ユーザー学習済みモデル
- `logs/` - 学習ログとインデックス

## 起動

```bash
python infer-web.py
```

## トラブルシューティング

### PyTorchのバージョン確認
```python
import torch
print(torch.__version__)  # 2.7.1+cu118 であること
print(torch.cuda.is_available())  # True であること
```

### CUDAバージョンが合わない場合
PyTorchの公式サイトで適切なバージョンを確認：
https://pytorch.org/get-started/locally/

### numba/llvmliteのエラー
Python 3.9を使用していることを確認。3.10以降だと互換性の問題が出る場合がある。

### omegaconfのエラー
pip 24.1以降を使っている場合に発生。pip 24.0にダウングレードする：
```bash
pip install pip==24.0
```

---
最終更新: 2026-01-29
Python: 3.9.x
pip: 24.0
PyTorch: 2.7.1+cu118
