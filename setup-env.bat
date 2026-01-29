@echo off
REM RVC WebUI 環境セットアップスクリプト
REM Python 3.9.13 + CUDA 11.8 用

echo === RVC WebUI Setup ===
echo.

REM 仮想環境作成
if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
)

REM 仮想環境有効化
call .venv\Scripts\activate.bat

REM pip 24.0に固定（omegaconf 2.0.6の壊れたメタデータ対策）
echo Installing pip 24.0...
python -m pip install pip==24.0

REM PyTorch (CUDA 11.8) インストール
echo.
echo Installing PyTorch with CUDA 11.8...
pip install torch==2.7.1 torchaudio==2.7.1 torchvision==0.22.1 --index-url https://download.pytorch.org/whl/cu118

REM その他の依存関係
echo.
echo Installing other dependencies...
pip install -r requirements-no-torch.txt

echo.
echo === Setup Complete ===
echo Run: python infer-web.py
pause
