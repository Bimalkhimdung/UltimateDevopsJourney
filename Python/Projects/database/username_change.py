import hashlib

def text_to_md5(text):
    hasher = hashlib.md5()
    hasher.update(text.encode('utf-8'))  # Encoding the text to bytes
    return f"md5{hasher.hexdigest()}"

text = "realhrsoft"  
md5_hash = text_to_md5(text)
print(md5_hash)
