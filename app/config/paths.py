from pathlib import Path
import os


class Paths:

    PROJECT_DIR: Path = Path(__file__).resolve().parents[2]
    MODEL_DIR: Path = os.path.join(PROJECT_DIR, "model/trained")
    ENCODERS_DIR: Path = os.path.join(PROJECT_DIR, "model/encoders")

    @classmethod
    def get_path(cls, dir_name: str) -> Path | None:
        return getattr(cls, dir_name.upper(), None)
