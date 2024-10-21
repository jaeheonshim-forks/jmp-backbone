from __future__ import annotations

from pathlib import Path

import jmp.config as jc


def main():
    data_config = jc.MPTrjAlexOMAT24DataModuleConfig.draft()
    data_config.batch_size = 120
    data_config.num_workers = 8
    data_config.with_linear_reference_("mptrj-salex")
    data_config.subsample_val = 5_000
    data_config = data_config.finalize()


if __name__ == "__main__":
    main()