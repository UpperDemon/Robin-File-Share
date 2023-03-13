from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
import asyncio

from bot import Bot as bot

auth = [1930212388]
request_collection_status = False


@bot.on_message(filters.command(["start", "start@BoaHancockRobot"]))
async def start(b: Client, message: Message):
    await message.reply_animation(

        animation="https://telegra.ph/file/50c7844a766cb743597d7.mp4",

        caption=f" **✨REQUEST COLLECTOR✨**\n{Config.START_TEXT}",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("💖 Our CHANNELs 💖", url="https://t.me/Uncensored_Hanimes/4"
                                         ),
                ],
            ]
        ),
    )


@bot.on_message(filters.command(["help", "help@BoaHancockRobot"]))
async def help(bot: Client, message: Message):
    await message.reply_text(
        text=Config.HELP_TEXT,
        disable_web_page_preview=True,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("💖 Our CHANNELs 💖", url="https://t.me/Uncensored_Hanimes/4"
                                         ),
                ],
            ]
        ),
    )


@bot.on_message(filters.command(["refresh", "refresh@BoaHancockRobot"]))
def add(b: Client, message: Message):
    c = b.iter_chat_members(chat_id=-1001945047718)
    v = b.iter_chat_members(chat_id=Config.FROM, filter="administrators")
    for admin in c:
        if admin not in auth:
            auth.append(admin.user.id)
    for admin in v:
        if admin not in auth:
            auth.append(admin.user.id)
    message.reply_text(text="Admin List Updated!!")


@bot.on_message(
    filters.command(["collect_stop", "collect_stop@BoaHancockRobot"], ["/"])

    & ~filters.private
    & ~filters.edited
    & ~filters.forwarded
)
async def stop_request_collection(b: Client, message: Message):
    if message.from_user.id in auth:
        await message.reply_text("__REQUEST COLLECTION STOPPED!!!🤒__")
        global request_collection_status
        request_collection_status = False
    else:
        await message.reply_text(
            "**🤬 Oi, Who this non admin telling me to do stuff?\nWant cyber bullying? 🤬**"
        )


@bot.on_message(
    filters.command(["collect_start", "collect_start@BoaHancockRobot"], ["/"])
    & ~filters.private
    & ~filters.edited
    & ~filters.forwarded
)
async def stop_request_collection(b: Client, message: Message):
    if message.from_user.id in auth:
        await message.reply_text("__REQUEST COLLECTION STARTED!!!__")
        global request_collection_status
        request_collection_status = True
    else:
        await message.reply_text(
            "**🤬 Oi, Who this non admin telling me to do stuff?\nWant cyber bullying? 🤬**"
        )


@bot.on_message(
    filters.command(
        [
            "request",
            "request@BoaHancockRobot",
        ],
        ["/", "#"],
    )
    & ~filters.private
    & ~filters.edited
    & ~filters.forwarded
)
async def request(b: Client, message: Message):
    if request_collection_status is True:
        msg = message.text
        if message.from_user.is_bot is False:
            if message.from_user.username:
                user = f"@{message.from_user.username}"
            else:
                user = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
            x = await bot.send_message(
                chat_id=Config.TO,
                text=f"#ANIME\n\n**Requested By {user}**\n\n{msg}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "Go to message",
                                url=f"https://t.me/+HD9BkKPD1QJjNTg1/{message.message_id}",
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                "😀 Completed 😀", callback_data="completed"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                "😞 Unavailable 😞", callback_data="unavailable"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                "Wil be done by : xxxx", callback_data="done_by"
                            )
                        ],
                    ]
                ),
            )

            await message.reply_animation(

                animation="https://telegra.ph/file/b3cc1f72ed0e63bd34c1a.mp4",

                caption=f"💫Hey {user}\n{Config.REQUEST_TEXT}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                " 💖 OUR CHANNEL 💖 ", url="https://t.me/Uncensored_Hanimes/4"
                            ),
                        ],
                    ]
                ),
            )
    else:
        if message.from_user.is_bot is False:
            if message.from_user.username:
                user = f"@{message.from_user.username}"
            else:
                user = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
            await message.reply_animation(
                animation="https://telegra.ph/file/bdd82afb8415cf722e7d5.mp4",
                caption=f"🔆 Hey {user}\n{Config.NO_COLLECT}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "💖 OUR CHANNEL 💖", url="https://t.me/Uncensored_Hanimes/4"
                            ),
                        ],
                    ]
                ),
            )
@bot.on_message(
    filters.command(
        [
            "report",
            "report@BoaHancockRobot",
        ],
        ["/", "#"],
    )
    & ~filters.private
    & ~filters.edited
    & ~filters.forwarded
)
async def report(b: Client, message: Message):
    msg = message.text
    if message.from_user.is_bot is False:
        if message.from_user.username:
            user = f"@{message.from_user.username}"
        else:
            user = (
                f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
            )
        x = await bot.send_message(
            chat_id=Config.TO,
            text=f"#REPORT\n\n__Reported By {user}__ \n\n{msg}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Go to message",
                            url=f"https://t.me/+HD9BkKPD1QJjNTg1/{message.message_id}",
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "♨️ CHANNEL Reestablishing ♨️",
                            callback_data="reestablishing",
                        )
                    ],
                ]
            ),
        )

        await message.reply_text(
            text=Config.REPORT_TEXT,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "💖 Our CHANNELs 💖", url="https://t.me/Uncensored_Hanimes/4"
                        ),
                    ],
                ]
            ),
        )


@bot.on_callback_query()
async def callback(b: Client, cb: CallbackQuery):
    if "completed" in cb.data:
        if cb.from_user.id in auth:

            z = await bot.send_message(
                chat_id=Config.FROM,
                text=f"{cb.message.text}\n\nYour request is completed!\nPlease Check the CHANNEL.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "💖 Our CHANNELs 💖", url="https://t.me/Uncensored_Hanimes/4"
                            ),
                        ],
                    ]
                ),
            )
            gfh = await cb.edit_message_text(
                text=f"~~{cb.message.text}~~\n\n**COMPLETED!!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "😎 Completed 😎",
                                url=f"https://t.me/+HD9BkKPD1QJjNTg1/{z.message_id}",
                            )
                        ]
                    ]
                ),
            )
            await delete_her(gfh)
        else:
            await cb.answer(
                "This is not under your control!!! Go back!!", show_alert=True
            )

    if "unavailable" in cb.data:
        if cb.from_user.id in auth:
            p = await bot.send_message(
                chat_id=Config.FROM,
                text=f"{cb.message.text}\n\nYour request is Unavailable!\nSorry for the inconvinience.\n\n",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "💖 Our CHANNELs 💖", url="https://t.me/Uncensored_Hanimes/4"
                            ),
                        ],
                    ]
                ),
            )
            dfg = await cb.edit_message_text(
                text=f"~~{cb.message.text}~~\n\n**UNAVAilABLE!!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "📛 Unavailable 📛",
                                url=f"https://t.me/+HD9BkKPD1QJjNTg1/{p.message_id}",
                            )
                        ]
                    ]
                ),
            )
            await delete_her(dfg)
        else:
            await cb.answer(
                "This is not under your control!!! Go back!!", show_alert=True
            )

    if "reestablishing" in cb.data:

        if cb.from_user.id in auth:
            o = await bot.send_message(
                chat_id=Config.FROM,
                text=f"{cb.message.text}\n\nCHANNEL Re-established",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "💖 Our CHANNELs 💖", url="https://t.me/Uncensored_Hanimes/4"
                            ),
                        ],
                    ]
                ),
            )
            await cb.edit_message_text(
                text=f"~~{cb.message.text}~~\n\n**COMPLETED!!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "⚜️ Completed ⚜️",
                                url=f"https://t.me/+HD9BkKPD1QJjNTg1/{o.message_id}",
                            )
                        ]
                    ]
                ),
            )
        else:
            await cb.answer(
                "This is not under your control!!! Go back!!", show_alert=True
            )

    if "done_by" in cb.data:
        if cb.from_user.id in auth:
            await cb.edit_message_text(
                text=f"{cb.message.text}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "💖 .... 💖", callback_data="Hattori")],
                    ]
                ),
            )
        else:
            await cb.answer(
                "If you also want to upload anime then contact @",
                show_alert=True,
            )

    if cb.from_user.id in auth:
        if "Hattori" in cb.data:
            await cb.edit_message_text(
                text=f"{cb.message.text}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "😀 Completed 😀", callback_data="completed"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                "😞 Unavailable 😞", callback_data="unavailable"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                "Will be done by: 💖 .... 💖",
                                url="https://t.me/+HD9BkKPD1QJjNTg1",
                            )
                        ],
                    ]
                ),
            )

    else:
        await cb.answer("You are not allowed to do that!!")


async def delete_her(message):
    await asyncio.sleep(3)
    try:
        await message.delete()
    except:
        pass


