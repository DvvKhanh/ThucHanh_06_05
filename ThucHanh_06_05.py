import facebook

# Access token phải là PAGE TOKEN
access_token = "EAAS0U4pGgqABO86mUkHtiBvhefJACkB84HPHDkMHz64F8KE86ZC4j8L20CHkZC0asJZAfBU7ZCZATszd5FNVL4aVqAPkMXv3qCZBGRrFzYkzHZAZBXdJbEauuXjTfupp7wReeYVKTGMsWGB6nIYRUXnhOyoVG8d2x2OGHVF45nT4aJ69MyzKRsT1pZAC4MUBI45cKVDtTWGVBoGOZCLr7UszigBHGrqHW46ZBHbpQdRdHn1"
# Tạo đối tượng Graph API
graph = facebook.GraphAPI(access_token)

# Đăng bài lên Trang (dùng 'me' nếu access token là của Page)
graph.put_object(parent_object='me', connection_name='feed', message=' 📢 Sản phẩm mới hôm nay: Áo thun nam cao cấp - chỉ 199K! 🧥')
