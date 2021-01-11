import sys
import boto3

s3 =boto3.resource("s3")

total_size = 0
total_count = 0
for bucket in s3.buckets.all():
     print("Bucket Name " + bucket.name)
     print("Creation Date " + str(bucket.creation_date))
     for bucket in bucket.objects.all():
         total_size += bucket.size
         total_count += 1
print("Number of files " + str(total_count))
print("Total size of files " + str(total_size))
