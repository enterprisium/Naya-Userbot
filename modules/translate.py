# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.
"""
✘ **Bantuan Untuk Translate**

๏ **Perintah:** `tr` <kode bahasa>
◉ **Keterangan:** Terjemahkan pesan.

◉ **Contoh:** `tr id` <balas ke pesan>
Ini akan menerjemahkan pesan ke Bahasa Indonesia.
"""


from contextlib import suppress

from gpytranslate import Translator

from . import ayra_cmd
from ._trans import *

BAHASA = ["en", "id", "fr", "es", "de", "it", "ja", "ko", "zh"]


@ayra_cmd(pattern=r"^[Tt][r](?: |$)(.*)", manager=False)
async def _(jink):
    match = jink.pattern_match.group(1)
    itu = match.split(" ")
    is_lang, lang = (True, itu[0]) if itu[0] in BAHASA else (False, BAHASA)
    kata = (await jink.get_reply_message()).message if jink.is_reply else match
    if is_lang:
        with suppress(BaseException):
            kata = match.split(maxsplit=1)[1]
    if not kata:
        await jink.eor("`Reply to text message or provide a text!`", time=5)
        return
    try:
        text = strip_format(strip_emoji(kata))
        translator = Translator()
        translation = await translator(text, targetlang=lang)
        tr = f"**Detected:** `{await translator.detect(translation.orig)}`\n**Translated:** `{await translator.detect(translation.text)}`\n\n```{translation.text}```"
        await jink.eor(tr)
    except Exception as err:
        await jink.eor(f"Error {err}")
