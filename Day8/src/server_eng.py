"""Launch: python3 -m src.server_eng"""
import argparse
from pathlib import Path
from .storage_eng import Storage
from .mcp_adapter_eng import build_mcp_server

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default=str(ROOT / "data/shop_eng.db"))
    parser.add_argument("--seed", default=str(ROOT / "data/seed_eng.sql"))
    args = parser.parse_args()
    storage = Storage(args.db, args.seed)
    try:
        build_mcp_server(storage).run(transport="stdio", show_banner=False)
    finally:
        storage.close()

if __name__ == "__main__":
    main()

