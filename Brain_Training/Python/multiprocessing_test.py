import multiprocessing
import requests
import concurrent.futures
import time
import os


def download_files(url, name, dest_dir=r"E:\python\downloaded_image"):
    """Download an image from `url` and save it as image<name>.jpg inside dest_dir.

    This function ensures the destination directory exists and handles basic network
    errors. It returns the path to the saved file or None on failure.
    """
    print(f"downloading picture image{name}")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except Exception as exc:
        print(f"\nFailed to download image{name}: {exc}")
        return None

    # ensure destination exists
    try:
        os.makedirs(dest_dir, exist_ok=True)
    except Exception as exc:
        print(f"Failed to create directory {dest_dir}: {exc}")
        return None

    file_path = os.path.join(dest_dir, f"image{name}.jpg")
    try:
        with open(file_path, "wb") as fh:
            fh.write(response.content)
    except Exception as exc:
        print(f"Failed to write file {file_path}: {exc}")
        return None

    print(f"\nimage{name} downloaded to {file_path}")
    return file_path


url = "https://picsum.photos/3000/4000"
processes = []


if __name__ == '__main__':
    # spawn multiple processes to download images in parallel
    for i in range(1, 50):
        p = multiprocessing.Process(target=download_files, args=(url, i))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    # example using concurrent.futures (ProcessPoolExecutor)
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     urls = [url] * 5
    #     names = range(1, 6)
    #     for result in executor.map(download_files, urls, names):
    #         print(result)

