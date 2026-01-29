# RVC WebUI 環境セットアップ手順

## 前提条件
- Python 3.10.x（推奨）または 3.9.x
- NVIDIA GPU + CUDA 11.8

## セットアップ手順

### 1. 仮想環境の作成
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac
```

### 2. PyTorchのインストール（CUDA 11.8版）
```bash
pip install torch==2.7.1 torchaudio==2.7.1 torchvision==0.22.1 --index-url https://download.pytorch.org/whl/cu118
```

### 3. その他の依存関係をインストール
```bash
pip install -r requirements-no-torch.txt
```

## 大容量ファイルの復元

モデルファイル（.pth, .index）やログデータはGitに含まれていません。
Google Driveから以下のディレクトリに復元してください：

- `assets/hubert/` - HuBERTモデル
- `assets/pretrained/` - 事前学習済みモデル (v1)
- `assets/pretrained_v2/` - 事前学習済みモデル (v2)
- `assets/rmvpe/` - RMVPEモデル
- `assets/uvr5_weights/` - UVR5音声分離モデル
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
Python 3.10を使用している場合、以下を試す：
```bash
pip install numba==0.56.4 llvmlite==0.39.0
```

---
最終更新: 2026-01-29
Python: 3.10.x
PyTorch: 2.7.1+cu118
