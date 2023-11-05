# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ **Bantuan Untuk Blacklist**

๏ **Perintah:** `black` <kata>
◉ **Keterangan:** Daftar hitam kan kata didalam grup.

๏ **Perintah:** `white` <kata>
◉ **Keterangan:** Hapus kata dari daftar hitam.

๏ **Perintah:** `listblack`
◉ **Keterangan:** Lihat Semua Daftar Kata Terlarang .
"""


from Ayra.dB.blacklist_db import (add_blacklist, get_blacklist, list_blacklist,
                                  rem_blacklist)

from . import ayra_bot, ayra_cmd, events, get_string, udB


@ayra_cmd(pattern="^[Bb][l][a][c][k]( (.*)|$)", admins_only=True)
async def af(e):
    if xx := event.pattern_match.group(1):
        wrd = xx
    elif event.is_reply:
        wrd = await event.get_reply_message()
    chat = e.chat_id
    if not wrd:
        return await e.eor(get_string("blk_1"), time=5)
    add_blacklist(int(chat), wrd)
    ayra_bot.add_handler(blacklist, events.NewMessage(incoming=True))
    await e.eor(get_string("blk_2").format(wrd))


@ayra_cmd(pattern="^[Ww][h][i][t][e]( (.*)|$)", admins_only=True)
async def rf(e):
    if xx := event.pattern_match.group(1):
        wrd = xx
    elif event.is_reply:
        wrd = await event.get_reply_message()
    chat = e.chat_id
    if not wrd:
        return await e.eor(get_string("blk_3"), time=5)
    rem_blacklist(int(chat), wrd)
    await e.eor(get_string("blk_4").format(wrd))


@ayra_cmd(pattern="^[Ll][i][s][t][b][l][a][c][k]", admins_only=True)
async def lsnote(e):
    if x := list_blacklist(e.chat_id):
        sd = get_string("blk_5")
        return await e.eor(sd + x)
    await e.eor(get_string("blk_6"))


async def blacklist(e):
    if x := get_blacklist(e.chat_id):
        for z in e.text.lower().split():
            for zz in x:
                if z == zz:
                    try:
                        await e.delete()
                        break
                    except BaseException:
                        break


if udB.get_key("BLACKLIST_DB"):
    ayra_bot.add_handler(blacklist, events.NewMessage(incoming=True))
