#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex

import os
import shlex
import asyncio
from typing import Tuple


async def execute(cmnd: str) -> Tuple[str, str, int, int]:
    """
    Run a shell command asynchronously and return stdout, stderr, returncode, and pid.
    """
    cmnds = shlex.split(cmnd)
    process = await asyncio.create_subprocess_exec(
        *cmnds,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid
    )


async def clean_up(input1: str, input2: str | None = None):
    """
    Safely remove one or two files if they exist.
    """
    for path in (input1, input2):
        if path and os.path.exists(path):
            try:
                os.remove(path)
            except Exception as e:
                # optional: log instead of silently ignoring
                print(f"[clean_up] Could not remove {path}: {e}")
