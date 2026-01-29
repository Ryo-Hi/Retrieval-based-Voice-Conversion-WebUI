import os
import shutil


# サブディレクトリ内の.wavファイルを探す
def move_and_rename_files(src_dir):
    counter = 0
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".wav"):
                # 新しいファイル名 (vocal_chunk_{counter}.wav)
                new_name = f"vocal_chunk_{counter}.wav"

                # 元のファイルのフルパス
                old_path = os.path.join(root, file)

                # 新しいファイルのパス（ルートディレクトリに移動）
                new_path = os.path.join(src_dir, new_name)

                # ファイルの移動とリネーム
                shutil.move(old_path, new_path)
                print(f"Moved and renamed: {old_path} -> {new_path}")

                # カウンターをインクリメント
                counter += 1

    print("ファイルの移動とリネームが完了しました。")


# ここにルートディレクトリのパスを指定（例: カレントディレクトリ）
root_dir = os.path.abspath("dataset/male1")

# 実行
move_and_rename_files(root_dir)
