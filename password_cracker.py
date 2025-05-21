import hashlib
import argparse
import itertools
import string
import threading
from queue import Queue

# === Supported Hash Algorithms ===
HASH_FUNCTIONS = {
    'md5': hashlib.md5,
    'sha1': hashlib.sha1,
    'sha256': hashlib.sha256
}

# === Worker Thread Function ===
def worker(queue, target_hash, hash_func, found_flag):
    while not queue.empty() and not found_flag[0]:
        password = queue.get()
        hashed = hash_func(password.encode()).hexdigest()
        if hashed == target_hash:
            found_flag[0] = True
            print(f"\n[✓] Password found: {password}")
        queue.task_done()

# === Dictionary Attack Function ===
def dictionary_attack(target_hash, hash_func, wordlist_path, threads=4):
    print("[*] Starting dictionary attack...")
    found_flag = [False]
    queue = Queue()

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            for word in file:
                queue.put(word.strip())
    except FileNotFoundError:
        print(f"[!] Wordlist not found: {wordlist_path}")
        return

    for _ in range(threads):
        thread = threading.Thread(target=worker, args=(queue, target_hash, hash_func, found_flag))
        thread.start()

    queue.join()
    if not found_flag[0]:
        print("[-] Password not found in wordlist.")

# === Brute-force Attack Function ===
def brute_force_attack(target_hash, hash_func, min_len, max_len, charset, threads=4):
    print("[*] Starting brute-force attack...")
    found_flag = [False]
    queue = Queue()

    for length in range(min_len, max_len + 1):
        for combination in itertools.product(charset, repeat=length):
            queue.put(''.join(combination))

    for _ in range(threads):
        thread = threading.Thread(target=worker, args=(queue, target_hash, hash_func, found_flag))
        thread.start()

    queue.join()
    if not found_flag[0]:
        print("[-] Password not found using brute-force.")

# === Main Program Entry ===
def main():
    parser = argparse.ArgumentParser(description="Python Password Cracker - By Inlighn Tech")
    parser.add_argument("hash", help="Target hashed password")
    parser.add_argument("hash_type", choices=HASH_FUNCTIONS.keys(), help="Hash algorithm (md5, sha1, sha256)")
    parser.add_argument("--wordlist", help="Path to wordlist file (dictionary attack)")
    parser.add_argument("--min", type=int, default=1, help="Minimum password length (brute-force)")
    parser.add_argument("--max", type=int, default=4, help="Maximum password length (brute-force)")
    parser.add_argument("--charset", default=string.ascii_lowercase + string.digits, help="Characters for brute-force")
    parser.add_argument("--threads", type=int, default=4, help="Number of threads to use")

    args = parser.parse_args()
    hash_func = HASH_FUNCTIONS[args.hash_type]

    if args.wordlist:
        dictionary_attack(args.hash, hash_func, args.wordlist, args.threads)
    else:
        brute_force_attack(args.hash, hash_func, args.min, args.max, args.charset, args.threads)

if __name__ == "__main__":
    main()
