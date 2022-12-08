def to_slug(str):
    valid_chars="abcdefghijklmnopqrstuvwxyz1234567890-"

    slug=""

    for char in str:
        if char in valid_chars:
            slug=slug+char
        else:
            slug=slug+'-'
    
    print(slug)

    return slug

to_slug("salut les amis")

