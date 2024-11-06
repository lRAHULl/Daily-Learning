# S3 uploads using Pre-signed urls - for public facing buckets

S3 is an object store which is commonly used for storing static assests like images, html files, and other media. It is widely for storing application users raw data directly.

However it usually has a server in front of it to authenticate users, process the media file and finally upload the file to the S3 bucket.

As you can see this becomes a bottle-neck and inefficient when it comes to cost - As there is a redundant upload happening from Server to S3, which increases our network throughput as well as the compute usage, not to mention the management of Scaling of the server.

If we can offload the upload part directly to the user after the user is authenticated (by the server) -- we can optimise our system in terms of network traffic and server compute.

This is where [S3 Presigned Urls for Upload](https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html) help us with.

1. We can have a bucket which is private
2. Have a Service which autheticates with the S3 and generates a *Presigned Url for upload*
3. A Service which runs on the client-side to use the *pre-signed url and upload the media to the S3 bucket*.

This project demonstarates exactly that.

We have 2 parts in the file `s3_presigned_url_upload.py`

1. The first part represents the authentication with the S3 (with access and secret keys) and fetching a pre-signed url for upload into S3.
2. The second part represents the client-side service using the pre-signed url to upload directly to S3 without (Access and Secret keys).

## *Learn Something new Everyday* - Rahul
