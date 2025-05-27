chunk_size = 1024  # 1 KB chunks
with open('large_star_catalog.txt', 'r') as catalog:
    while True:
        chunk = catalog.read(chunk_size)
        if not chunk:
            break
        # Process the chunk here
        print(len(chunk))