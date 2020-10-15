def decrypt_story():
    c = CiphertextMessage(get_story_string())
    return c.decrypt_message()
