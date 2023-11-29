#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) AFK

import math, os, time, shutil


async def progress_for_pyrogram(
    current,
    total,
    ud_type,
    message,
    start
):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        # if round(current / total * 100, 0) % 5 == 0:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "[{0}{1}] \n**P:** {2}%\n".format(
            ''.join(["▪️" for i in range(math.floor(percentage / 10))]),
            ''.join(["▫️" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2))

        tmp = progress + "**Size: **{0} of {1}\n**Speed:** {2}/s\n**ETA:** {3}\n".format(
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            # elapsed_time if elapsed_time != '' else "0 s",
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(
                text="{}\n\n{}".format(
                    ud_type,
                    tmp
                )
            )
        except:
            pass


def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]

async def progress_bar(current, total, reply, start):
    if timer.can_send():
        now = time.time()
        diff = now - start
        if diff < 1:
            return
        else:
            perc = f"{current * 100 / total:.1f}%"
            elapsed_time = round(diff)
            speed = current / elapsed_time
            remaining_bytes = total - current
            if speed > 0:
                eta_seconds = remaining_bytes / speed
                eta = hrt(eta_seconds, precision=1)
            else:
                eta = "-"
            sp = str(hrb(speed)) + "/s"
            tot = hrb(total)
            cur = hrb(current)
            
            #don't even change anything till here
            # Calculate progress bar dots
            #ab mila dil ko sukun #by Kshitij
            #change from here if you want 
            bar_length = 11
            completed_length = int(current * bar_length / total)
            remaining_length = bar_length - completed_length
            progress_bar = "▰" * completed_length + "▱" * remaining_length
            
            try:
                await reply.edit(f'`╭──⌈📤 𝙐𝙥𝙡𝙤𝙖𝙙𝙞𝙣𝙜 📤⌋──╮ \n├{progress_bar}\n├ 𝙎𝙥𝙚𝙚𝙙 : {sp} \n├ 𝙋𝙧𝙤𝙜𝙧𝙚𝙨𝙨 : {perc} \n├ 𝙇𝙤𝙖𝙙𝙚𝙙 : {cur}\n├ 𝙎𝙞𝙯𝙚 :  {tot} \n├ 𝙀𝙏𝘼 : {eta} \n╰────⌈ Kshitijbots ⌋────╯`\n') 
         #       await reply.edit(f'`╭──⌈📤 𝙐𝙥𝙡𝙤𝙖𝙙𝙞𝙣𝙜 📤⌋──╮ \n├{progress_bar}\n├ 𝙎𝙥𝙚𝙚𝙙 : {sp} \n├ 𝙋𝙧𝙤𝙜𝙧𝙚𝙨𝙨 : {perc} \n├ 𝙇𝙤𝙖𝙙𝙚𝙙 : {cur}\n├ 𝙎𝙞𝙯𝙚 :  {tot} \n├ 𝙀𝙏𝘼 : {eta} \n╰─⌈ Bot Made By Kshitij ⌋─╯`\n') 
            except FloodWait as e:
                time.sleep(e.x)
