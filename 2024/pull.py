# NOTE: does not work anymore since 2023 because of cookies

import requests
import sys


def download_and_save(url, save_as):
  try:
    response = requests.get(url)
    response.raise_for_status()

    with open(save_as, "w", encoding="utf-8") as file:
      file.write(response.text)

    print(f"File downloaded and saved as {save_as}")

  except requests.exceptions.RequestException as e:
    print(f"Error downloading the file: {e}")


url = f"https://adventofcode.com/2024/day/{sys.argv[1]}/input"
save_as = f"input{sys.argv[1]:02}.txt"

download_and_save(url, save_as)
