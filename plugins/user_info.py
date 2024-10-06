from pyrogram import Client, filters
from pyrogram.types import Message, InputMediaPhoto

@Client.on_message(filters.command("info") & filters.private)
async def user_info(client: Client, message: Message):
    user = message.from_user

    # Create a formatted message with user details
    user_info = f"""
<b>User Info:</b>
<b>First Name:</b> {user.first_name}
<b>Last Name:</b> {user.last_name if user.last_name else 'N/A'}
<b>Username:</b> @{user.username if user.username else 'N/A'}
<b>User ID:</b> {user.id}
<b>DC ID:</b> {user.dc_id}
<b>Is Bot:</b> {'Yes' if user.is_bot else 'No'}
"""

    # Fetch user's profile photo (if available)
    photos = await client.get_profile_photos(user.id)

    if photos.total_count > 0:
        # Get the file_id of the first profile photo
        photo_file_id = photos.photos[0].file_id
        # Send the user's profile photo along with the info
        await client.send_photo(
            chat_id=message.chat.id,
            photo=photo_file_id,
            caption=user_info,
            parse_mode="html"
        )
    else:
        # If no profile photo, just send the info
        await message.reply_text(user_info, parse_mode="html")
