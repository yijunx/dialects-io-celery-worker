# resize user profile image.. and upload image to somewhere..
# minio or s3 is needed to store user profile picture
# when user upload pic, user management takes it, and
# save to minio, and let celery know, celery go and resize it, and delete the only one (of big size)
# front end needs to restrict the photo size

# user will have a link to the pic for the front end to render
# browser go and fetch the pic without going through user-management
