## Errors

## Something went wrong (1054, "Unknown column 'bank' in 'field list'")
Caused when trying to select column that doesn't exist.

## pymysql.err.InternalError: (1049, "Unknown database 'maydb'")
Caused when `connectToMySql` has the wrong database name

## raise RuntimeError("cryptography is required for sha256_password or caching_sha2_password")
###RuntimeError: cryptography is required for sha256_password or caching_sha2_password
Caused when the user id or password is incorrect. 

## pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on 'elocalhost' ([Errno 8] nodename nor servname provided, or not known)")
Caused when the host is incorrect

## AttributeError: 'NoneType' object has no attribute 'encoding'
Caused when charset is incorrect

## pymysql.err.Error: Already closed

