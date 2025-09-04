#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex

from helpers.tools import execute, clean_up
from helpers.upload import upload_audio, upload_subtitle


async def extract_audio(client, message, data):
    await message.edit_text("Extracting stream from file...")

    dwld_loc = data["location"]
    out_loc = f"{dwld_loc}.mp3"

    if data.get("name") == "mp3":
        cmd = f"ffmpeg -i '{dwld_loc}' -map 0:{data['map']} -c copy '{out_loc}' -y"
    else:
        cmd = f"ffmpeg -i '{dwld_loc}' -map 0:{data['map']} '{out_loc}' -y"

    out, err, rcode, pid = await execute(cmd)
    if rcode != 0:
        await message.edit_text("**Error Occurred. See Logs for more info.**")
        print(err)
        await clean_up(dwld_loc, out_loc)
        return

    await clean_up(dwld_loc)
    await upload_audio(client, message, out_loc)


async def extract_subtitle(client, message, data):
    await message.edit_text("Extracting stream from file...")

    dwld_loc = data["location"]
    out_loc = f"{dwld_loc}.srt"

    cmd = f"ffmpeg -i '{dwld_loc}' -map 0:{data['map']} '{out_loc}' -y"
    out, err, rcode, pid = await execute(cmd)
    if rcode != 0:
        await message.edit_text("**Error Occurred. See Logs for more info.**")
        print(err)
        await clean_up(dwld_loc, out_loc)
        return

    await clean_up(dwld_loc)
    await upload_subtitle(client, message, out_loc)
