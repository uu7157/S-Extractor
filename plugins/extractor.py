#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex

from pyrogram import filters
from pyrogram import Client as trojanz
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import Config
from script import Script


@trojanz.on_message(filters.private & (filters.document | filters.video))
async def confirm_dwnld(client, message):

    if message.from_user.id not in Config.AUTH_USERS:
        return

    filetype = message.document or message.video

    if filetype and filetype.mime_type and filetype.mime_type.startswith("video/"):
        await message.reply_text(
            "**What do you want me to do?**",
            quote=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("DOWNLOAD and PROCESS", callback_data="download_file")],
                    [InlineKeyboardButton("CANCEL", callback_data="close")]
                ]
            )
        )
    else:
        await message.reply_text(
            "Invalid Media",
            quote=True
        )
